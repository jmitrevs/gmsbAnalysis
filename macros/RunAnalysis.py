#! /usr/bin/env python

# code to make all the plots in a file
import sys
import getopt

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

import os.path
import LepPhotonAnalysis

removeOverlap = True
removeOverlapTtbar = True
onlyStrong = False

ELECTRON = 0
MUON = 1

DEFAULTLEPTON = ELECTRON
DEFAULTABCD = LepPhotonAnalysis.NoABCD

REWEIGHW = False
REWEIGHZ = False

DO_TTBAR_SYST = False

APPLY_WEIGHTS = True
#APPLY_WEIGHTS = False

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

def RunAnalysis(lepton, plots = LepPhotonAnalysis.DEFAULT_PLOTS, 
                abcd = DEFAULTABCD, metType = LepPhotonAnalysis.MET_DEFAULT, 
                applySF=LepPhotonAnalysis.NOMINAL, extraName="",
                doStandard = True, doSyst = False):

    SRs = {}

    if lepton == ELECTRON:
        import DataManagerElectrons as DataManager
    elif lepton == MUON:
        import DataManagerMuons as DataManager
    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")


    ttreeName = LepPhotonAnalysis.DEFAULTTTREE
  
    if doStandard:
        for nameEnt in  DataManager.names:
            name = nameEnt[0]
            value = DataManager.values[name]
            if APPLY_WEIGHTS:
                scale = value[1]
            else:
                scale = 1.0
            print name + ": (scale = " + str(value[1]) +")" 
            sr = LepPhotonAnalysis.LepPhotonAnalysis(value[0].Get(ttreeName), 
                                                     makeOutputName(name, extraName),
                                                     lepton,
                                                     scale, plotsRegion = plots,
                                                     metType = metType,
                                                     applySF = applySF,
                                                     useWeights = APPLY_WEIGHTS,
                                                     debug = False)
            SRs[name] = sr
    if doSyst:
        for nameEnt in  DataManager.namesSyst:
            name = nameEnt[0]
            value = DataManager.values[name]
            if APPLY_WEIGHTS:
                scale = value[1]
            else:
                scale = 1.0
            print name + ": (scale = " + str(value[1]) +")" 
            sr = LepPhotonAnalysis.LepPhotonAnalysis(value[0].Get(ttreeName), 
                                                     makeOutputName(name, extraName),
                                                     lepton,
                                                     scale, plotsRegion = plots,
                                                     metType = metType,
                                                     useWeights = APPLY_WEIGHTS,
                                                     useJetAsPhoton = True,
                                                     debug = False)
            SRs[name] = sr

    return SRs

    
if __name__ == "__main__":
    try:
        # retrive command line options
        shortopts  = "eml:p:a:"
        longopts   = ["lepton=", "plots=", "abcd=", "met=", "applySF="]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )
    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        sys.exit(1)

    lepton = DEFAULTLEPTON
    plots = LepPhotonAnalysis.DEFAULT_PLOTS
    abcd = DEFAULTABCD
    metType = LepPhotonAnalysis.MET_DEFAULT
    applySF=LepPhotonAnalysis.NOMINAL #for scale factors
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
            elif a == "SRW":
                plots = LepPhotonAnalysis.SRW
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
        elif o in ("-a", "--abcd"):
            if a == "TT":
                abcd = LepPhotonAnalysis.TT
            elif a == "TL":
                abcd = LepPhotonAnalysis.TL
            elif a == "LT":
                abcd = LepPhotonAnalysis.LT
            elif a == "LL":
                abcd = LepPhotonAnalysis.LL
            else:
                print "*** abcd unknown ****"
                sys.exit(1)
        elif o in ("--met"):
            if a == "nominal":
                metType = LepPhotonAnalysis.MET_DEFAULT
            elif a == "plus":
                metType = LepPhotonAnalysis.MET_PLUS
            elif a == "minus":
                metType = LepPhotonAnalysis.MET_MINUS
            elif a == "muon":
                metType = LepPhotonAnalysis.MET_MUON
            elif a == "full":
                metType = LepPhotonAnalysis.MET_FULL
            elif a == "orig":
                metType = LepPhotonAnalysis.MET_ORIG
            else:
                print "*** met unknown ****"
                sys.exit(1)
        elif o in ("--applySF"):
            if a == "nominal":
                applySF = LepPhotonAnalysis.NOMINAL
            elif a == "high":
                applySF = LepPhotonAnalysis.HIGH
            elif a == "low":
                applySF = LepPhotonAnalysis.LOW
            elif a == "phohigh":
                applySF = LepPhotonAnalysis.PHOHIGH
            elif a == "pholow":
                applySF = LepPhotonAnalysis.PHOLOW
            else:
                print "*** applySF unknown ****"
                sys.exit(1)


    RunAnalysis(lepton, plots, abcd, metType, applySF)
