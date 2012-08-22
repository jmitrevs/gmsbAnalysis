#! /usr/bin/env python
'''
Module to run the analysis over all the grid ponts
'''

from glob import glob
import os, sys, getopt
import ROOT
# ROOT.gROOT.LoadMacro("AtlasStyle.C") 
# ROOT.SetAtlasStyle()

import signalOrigEvents
from signalXsecs import signalXsecs
import LepPhotonAnalysis

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

def makeOutputName(infileName, strong):
    inFileNoPath = os.path.split(infileName)[1]
    outfile = os.path.splitext(inFileNoPath)[0] + "_" + str(strong) + "_Hist.root"
    return outfile

def RunAnalysis(lepton, plots, metType):


    if lepton == ELECTRON:
        print "Lepton is ELECTRON."
        #path = "/data3/jmitrevs/lepphoton/elphoton_grid2/mergedFiles/"
        path = "/data3/jmitrevs/lepphoton/elphoton_gridMetSys/mergedFiles/"
        Lumi = 4812.34
    elif lepton == MUON:
        print "Lepton is Muon."
        path = "/data3/jmitrevs/lepphoton/muphoton_grid2/mergedFiles/"
        Lumi = 4708.61
    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")

    f = ROOT.TFile("output_gl_wino.root")
    ttree = f.Get("SignalUncertainties")
    xsecs = signalXsecs(ttree)

    ttreeName = LepPhotonAnalysis.DEFAULTTTREE
  
    for mgl in range(0, 1600, 100):
        for mC1 in range(0, mgl, 50) + [mgl-20]:
            filelist = glob(path + 'wino_%d_%d.root' % (mgl, mC1))
            if len(filelist) > 1:
                print >> sys.stderr, "Something wrong: filelist has size", len(filelist)  
                sys.exit(1)
            if len(filelist) == 1:
                winoFileName = filelist[0]
                winoFile = ROOT.TFile(winoFileName)

                for strong in (0, 1):
                    nOrig = signalOrigEvents.getNEvents(mgl, mC1, strong)
                    xsec = xsecs.getXsec(mgl, mC1, strong)
                    feff = signalOrigEvents.getFilterEff(mgl, mC1, strong)
                    scale = Lumi * xsec * feff / nOrig

                    print "nOrig =", nOrig, "xsec =", xsec, "feff =", feff, "scale =", scale 

                    print "wino_%d_%d_%d:" % (mgl, mC1, strong)
                    LepPhotonAnalysis.LepPhotonAnalysis(winoFile.Get(ttreeName), 
                                                        makeOutputName(winoFileName, strong),
                                                        lepton,
                                                        scale,
                                                        onlyStrong=(strong+1), 
                                                        applySF=LepPhotonAnalysis.NOMINAL, 
                                                        applyTrigWeight=LepPhotonAnalysis.NOMINAL,
                                                        plotsRegion=plots,
                                                        metType = metType)
                    print


if __name__ == "__main__":
    try:
        # retrive command line options
        shortopts  = "eml:p:"
        longopts   = ["lepton=", "plots="]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )
    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        sys.exit(1)

    lepton = DEFAULTLEPTON
    plots = LepPhotonAnalysis.DEFAULT_PLOTS
    metType = 0
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

    RunAnalysis(lepton, plots, metType)
