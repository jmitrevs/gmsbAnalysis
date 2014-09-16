#! /usr/bin/env python
'''
Module to run the analysis over all the grid ponts
'''
from __future__ import division

GeV = 1000

from glob import glob
import os, sys, getopt
import ROOT
# ROOT.gROOT.LoadMacro("AtlasStyle.C") 
# ROOT.SetAtlasStyle()

import signalOrigEvents
import signalXsecsStrong
import LepPhotonAnalysis
import math

Lumi = 20300.0

ELECTRON = 0
MUON = 1

DEFAULTLEPTON = ELECTRON


def GetHistNames(inFile):
    
    histNames = []

    for key in inFile.GetListOfKeys():
        h = key.ReadObj()
        #dirItem = [key.ReadObj().ClassName(), key.GetName(), key.GetTitle()]
        #print dirItem
        if h.InheritsFrom("TDirectory"):
            newList = [key.GetName() + "/" + x for x in GetHistNames(key.ReadObj())]
            #print newList
            histNames.extend(newList)
        elif h.InheritsFrom("TH1"):
            histNames.append(key.GetName())

    return histNames

def makeOutputName(infileName, extra = ""):
    inFileNoPath = os.path.split(infileName)[1]
    outfile = os.path.splitext(inFileNoPath)[0] + extra + "Hist.root"
    return outfile

def RunAnalysis(lepton = DEFAULTLEPTON, 
                plots = LepPhotonAnalysis.DEFAULT_PLOTS, 
                metType = LepPhotonAnalysis.MET_DEFAULT, 
                printRes=False):

    SRs = {}

    if lepton == ELECTRON:
        print "Lepton is ELECTRON."
        path = "/data/jmitrevs/output/elphoton_grid/v140912/"
    elif lepton == MUON:
        print "Lepton is Muon."
        #path = "/data3/jmitrevs/lepphoton/muphoton_grid2/mergedFiles/"
        #path = "/data3/jmitrevs/lepphoton/muphoton_gridMetSyst/mergedFiles/"
        path = "/data3/jmitrevs/lepphoton/muphoton_grid_purw/mergedFiles/"
    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")

    xsecs = signalXsecsStrong.signalXsecsStrong()
  
    
    for key, eff in signalXsecsStrong.filterEff.iteritems():
        filelist = glob(path + '*GGM_gl_wino_%s_egfilter*/*.root' % key)
        if len(filelist) > 1:
            print >> sys.stderr, "Something wrong: filelist has size", len(filelist)  
            sys.exit(1)
        if len(filelist) == 1:
            winoFileName = filelist[0]
            winoFile = ROOT.TFile(winoFileName)
            #nOrig = signalOrigEvents.getNEvents(mgl, mC1, strong)
            cutFlow = winoFile.Get("Global/CutFlow")
            nOrig = cutFlow.GetBinContent(1)
            xsec = xsecs.getXsecK(key)
            scale = Lumi * xsec * eff / nOrig
            ttreeName = LepPhotonAnalysis.DEFAULTTTREE

            #print "nOrig =", nOrig, "xsec =", xsec, "eff =", eff, "scale =", scale 

            print "wino_%s" % key
            sr = LepPhotonAnalysis.LepPhotonAnalysis(winoFile.Get(ttreeName), 
                                                     makeOutputName(winoFileName),
                                                     lepton,
                                                     scale,
                                                     applySF=LepPhotonAnalysis.NOMINAL, 
                                                     plotsRegion=plots,
                                                     metType = metType)

            #print "sr =", sr
            SRs[key] = sr

    return SRs

if __name__ == "__main__":
    try:
        # retrive command line options
        shortopts  = "eml:p:"
        longopts   = ["lepton=", "plots=", "doMetSyst"]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )
    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        sys.exit(1)

    lepton = DEFAULTLEPTON
    plots = LepPhotonAnalysis.DEFAULT_PLOTS
    metType = 0

    doMetSyst = False

    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-m"):
            lepton = MUON
        elif o in ("-e"):
            lepton = ELECTRON
        elif o in ("-l", "--lepton"):
            if a == "electron":
                lepton = ELECTRON
            elif a == "muon":
                lepton = MUON
            else:
                print "*** Lepton must be 'electron' or 'muon ****"
                sys.exit(1)
        elif o in ("--doMetSyst"):
            doMetSyst = True
        elif o in ("-p", "--plots"):
            if a == "NO_SEL":
                plots = LepPhotonAnalysis.NO_SEL
            elif a == "PRESEL":
                plots = LepPhotonAnalysis.PRESEL
            elif a == "SR":
                plots = LepPhotonAnalysis.SR
            elif a == "WCR":
                plots = LepPhotonAnalysis.WCR
            elif a == "TCR" or a == "HMT":
                plots = LepPhotonAnalysis.TCR
            elif a == "QCD":
                plots = LepPhotonAnalysis.QCD
            elif a == "XR1":
                plots = LepPhotonAnalysis.XR1
            elif a == "XR2" or a == "HMET":
                plots = LepPhotonAnalysis.XR2
            else:
                print "*** plots type unknown ****"
                sys.exit(1)

    if doMetSyst:
        default = RunAnalysis(lepton, plots, LepPhotonAnalysis.MET_DEFAULT)
        plus = RunAnalysis(lepton, plots, LepPhotonAnalysis.MET_PLUS)
        minus = RunAnalysis(lepton, plots, LepPhotonAnalysis.MET_MINUS)
        muon = RunAnalysis(lepton, plots, LepPhotonAnalysis.MET_MUON)

        for i in range(len(default)):
            errPlus = (plus[i][0] - default[i][0])/default[i][0] * 100
            errMinus = (minus[i][0] - default[i][0])/default[i][0] * 100
            errMuon = abs(muon[i][0] - default[i][0])/default[i][0] * 100

            print "%s & $%+.1f\,\%%$ & $%+.1f\,\%%$ & $%.1f\,\%%$ \\\\" % (default[i][3], errPlus, errMinus, errMuon)

    else:
        RunAnalysis(lepton, plots, metType, True)

