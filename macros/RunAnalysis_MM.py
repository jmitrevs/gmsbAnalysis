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

REWEIGHW = True

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

def RunAnalysis(lepton):


    if lepton == ELECTRON:
        import DataManagerElectrons as DataManager
    elif lepton == MUON:
        import DataManagerMuons as DataManager
    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")


    ttreeName = LepPhotonAnalysis.DEFAULTTTREE
  

    print "Wgamma_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np0),
                                        lepton,
                                        DataManager.Wgamma_Np0_scale, applySF=LepPhotonAnalysis.NOMINAL, 
                                        applyTrigWeight=LepPhotonAnalysis.NOMINAL, 
                                        reweighAlpgen=REWEIGHW, measureFakeAndEff=True)

    print
    print "Wgamma_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np1),
                                        lepton,
                                        DataManager.Wgamma_Np1_scale, applySF=LepPhotonAnalysis.NOMINAL, 
                                        applyTrigWeight=LepPhotonAnalysis.NOMINAL, 
                                        reweighAlpgen=REWEIGHW, measureFakeAndEff=True)

    print
    print "Wgamma_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np2),
                                        lepton,
                                        DataManager.Wgamma_Np2_scale, applySF=LepPhotonAnalysis.NOMINAL, 
                                        applyTrigWeight=LepPhotonAnalysis.NOMINAL, 
                                        reweighAlpgen=REWEIGHW, measureFakeAndEff=True)

    print
    print "Wgamma_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np3),
                                        lepton,
                                        DataManager.Wgamma_Np3_scale, applySF=LepPhotonAnalysis.NOMINAL, 
                                        applyTrigWeight=LepPhotonAnalysis.NOMINAL, 
                                        reweighAlpgen=REWEIGHW, measureFakeAndEff=True)

    print
    print "Wgamma_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np4),
                                        lepton,
                                        DataManager.Wgamma_Np4_scale, applySF=LepPhotonAnalysis.NOMINAL, 
                                        applyTrigWeight=LepPhotonAnalysis.NOMINAL, 
                                        reweighAlpgen=REWEIGHW, measureFakeAndEff=True)

    print
    print "Wgamma_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np5),
                                        lepton,
                                        DataManager.Wgamma_Np5_scale, applySF=LepPhotonAnalysis.NOMINAL,
                                        applyTrigWeight=LepPhotonAnalysis.NOMINAL, 
                                        reweighAlpgen=REWEIGHW, measureFakeAndEff=True)
    print

    print "Zleplepgamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepgammaFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepgammaFileName),
                                        lepton,
                                        DataManager.Zleplepgamma_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print

    print "Ztautaugamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautaugammaFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautaugammaFileName),
                                        lepton,
                                        DataManager.Ztautaugamma_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print


    print "Zleplep_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np0),
                                        lepton,
                                        DataManager.Zleplep_Np0_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Zleplep_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np1),
                                        lepton,
                                        DataManager.Zleplep_Np1_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Zleplep_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np2),
                                        lepton,
                                        DataManager.Zleplep_Np2_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Zleplep_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np3),
                                        lepton,
                                        DataManager.Zleplep_Np3_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Zleplep_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np4),
                                        lepton,
                                        DataManager.Zleplep_Np4_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Zleplep_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np5),
                                        lepton,
                                        DataManager.Zleplep_Np5_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)
    print
    print "Ztautau_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np0),
                                        lepton,
                                        DataManager.Ztautau_Np0_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Ztautau_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np1),
                                        lepton,
                                        DataManager.Ztautau_Np1_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Ztautau_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np2),
                                        lepton,
                                        DataManager.Ztautau_Np2_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Ztautau_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np3),
                                        lepton,
                                        DataManager.Ztautau_Np3_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Ztautau_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np4),
                                        lepton,
                                        DataManager.Ztautau_Np4_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)

    print
    print "Ztautau_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np5),
                                        lepton,
                                        DataManager.Ztautau_Np5_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)
    print

    if lepton == ELECTRON:
        print "diphotons:"
        LepPhotonAnalysis.LepPhotonAnalysis(DataManager.diphotonsFile.Get(ttreeName), 
                                            makeOutputName(DataManager.diphotonsFileName),
                                            lepton,
                                            DataManager.diphotons_scale, applySF=LepPhotonAnalysis.NONE, applyTrigWeight=LepPhotonAnalysis.NOMINAL, measureFakeAndEff=True)
        print

    print "data:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.dataFile.Get(ttreeName), 
                                        makeOutputName(DataManager.dataFileName),
                                        lepton,
                                        1.0)
    print

    print "gj:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gjFile.Get(ttreeName), 
                                        makeOutputName(DataManager.gjFileName, "_meas"),
                                        lepton,
                                        1.0,
                                        measureFakeAndEff=True,
                                        numBkgTight=34.5,
                                        qcdOtherRoot = "total.root")
    print "gj:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gjFile.Get(ttreeName), 
                                        makeOutputName(DataManager.gjFileName),
                                        lepton,
                                        1.0,
                                        scaleQCD=True)
    print
    
if __name__ == "__main__":
    try:
        # retrive command line options
        shortopts  = "eml:"
        longopts   = ["lepton="]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )
    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        sys.exit(1)

    lepton = DEFAULTLEPTON
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
    RunAnalysis(lepton)
