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

def RunAnalysis(lepton, plots, abcd):


    if lepton == ELECTRON:
        import DataManagerElectrons as DataManager
    elif lepton == MUON:
        import DataManagerMuons as DataManager
    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")


    ttreeName = LepPhotonAnalysis.DEFAULTTTREE
  

    print "Wlepnu_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np0),
                                        lepton,
                                        DataManager.Wlepnu_Np0_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion = plots)

    print
    print "Wlepnu_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np1),
                                        lepton,
                                        DataManager.Wlepnu_Np1_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wlepnu_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np2),
                                        lepton,
                                        DataManager.Wlepnu_Np2_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wlepnu_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np3),
                                        lepton,
                                        DataManager.Wlepnu_Np3_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wlepnu_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np4),
                                        lepton,
                                        DataManager.Wlepnu_Np4_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wlepnu_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np5),
                                        lepton,
                                        DataManager.Wlepnu_Np5_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)
    print
    print "Wtaunu_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np0),
                                        lepton,
                                        DataManager.Wtaunu_Np0_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wtaunu_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np1),
                                        lepton,
                                        DataManager.Wtaunu_Np1_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wtaunu_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np2),
                                        lepton,
                                        DataManager.Wtaunu_Np2_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wtaunu_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np3),
                                        lepton,
                                        DataManager.Wtaunu_Np3_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wtaunu_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np4),
                                        lepton,
                                        DataManager.Wtaunu_Np4_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wtaunu_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np5),
                                        lepton,
                                        DataManager.Wtaunu_Np5_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)
    print
    print "Wgamma_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np0),
                                        lepton,
                                        DataManager.Wgamma_Np0_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wgamma_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np1),
                                        lepton,
                                        DataManager.Wgamma_Np1_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wgamma_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np2),
                                        lepton,
                                        DataManager.Wgamma_Np2_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wgamma_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np3),
                                        lepton,
                                        DataManager.Wgamma_Np3_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wgamma_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np4),
                                        lepton,
                                        DataManager.Wgamma_Np4_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Wgamma_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np5),
                                        lepton,
                                        DataManager.Wgamma_Np5_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)
    print

    # print "ttbar:"
    # LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ttbarFile.Get(ttreeName), 
    #                                     makeOutputName(DataManager.ttbarFileName),
    #                                     lepton,
    #                                     DataManager.ttbar_scale,
    #                                     removeOverlapTtbar,
    #                                     applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print "ttbar (lepjets):"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ttbarFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ttbarFileName, "Lepjets"),
                                        lepton,
                                        DataManager.ttbarLepjets_scale,
                                        removeOverlapTtbar,
                                        applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots,
                                        tttype = LepPhotonAnalysis.LEPJETS)

    print

    print "ttbar (dilep):"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ttbarFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ttbarFileName, "Dilep"),
                                        lepton,
                                        DataManager.ttbar_scale,
                                        removeOverlapTtbar,
                                        applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots,
                                        tttype = LepPhotonAnalysis.DILEP)

    print
    print "ttbargamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ttbargammaFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ttbargammaFileName),
                                        lepton,
                                        DataManager.ttbargamma_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "st_tchan_lepnu:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.st_tchan_lepnuFile.Get(ttreeName), 
                                        makeOutputName(DataManager.st_tchan_lepnuFileName),
                                        lepton,
                                        DataManager.st_tchan_lepnu_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "st_tchan_taunu:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.st_tchan_taunuFile.Get(ttreeName), 
                                        makeOutputName(DataManager.st_tchan_taunuFileName),
                                        lepton,
                                        DataManager.st_tchan_taunu_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "st_Wt:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.st_WtFile.Get(ttreeName), 
                                        makeOutputName(DataManager.st_WtFileName),
                                        lepton,
                                        DataManager.st_Wt_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print

    print "WW:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WWFile.Get(ttreeName), 
                                        makeOutputName(DataManager.WWFileName),
                                        lepton,
                                        DataManager.WW_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "WZ:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WZFile.Get(ttreeName), 
                                        makeOutputName(DataManager.WZFileName),
                                        lepton,
                                        DataManager.WZ_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "ZZ:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZZFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ZZFileName),
                                        lepton,
                                        DataManager.ZZ_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print


    print "Zleplepgamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepgammaFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepgammaFileName),
                                        lepton,
                                        DataManager.Zleplepgamma_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print

    print "Ztautaugamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautaugammaFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautaugammaFileName),
                                        lepton,
                                        DataManager.Ztautaugamma_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print


    print "Zleplep_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np0),
                                        lepton,
                                        DataManager.Zleplep_Np0_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Zleplep_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np1),
                                        lepton,
                                        DataManager.Zleplep_Np1_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Zleplep_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np2),
                                        lepton,
                                        DataManager.Zleplep_Np2_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Zleplep_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np3),
                                        lepton,
                                        DataManager.Zleplep_Np3_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Zleplep_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np4),
                                        lepton,
                                        DataManager.Zleplep_Np4_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Zleplep_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np5),
                                        lepton,
                                        DataManager.Zleplep_Np5_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)
    print
    if lepton == ELECTRON:
        print "Zee_alt:"
        LepPhotonAnalysis.LepPhotonAnalysis(DataManager.Zee_altFile.Get(ttreeName), 
                                            makeOutputName(DataManager.Zee_altFileName),
                                            lepton,
                                            DataManager.Zee_alt_scale,
                                            removeOverlap, applySF=LepPhotonAnalysis.NONE, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)
        print
    print "Ztautau_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np0),
                                        lepton,
                                        DataManager.Ztautau_Np0_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Ztautau_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np1),
                                        lepton,
                                        DataManager.Ztautau_Np1_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Ztautau_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np2),
                                        lepton,
                                        DataManager.Ztautau_Np2_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Ztautau_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np3),
                                        lepton,
                                        DataManager.Ztautau_Np3_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Ztautau_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np4),
                                        lepton,
                                        DataManager.Ztautau_Np4_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "Ztautau_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np5),
                                        lepton,
                                        DataManager.Ztautau_Np5_scale,
                                        removeOverlap, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)
    print

    print "gamma_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np1),
                                        lepton,
                                        DataManager.gamma_Np1_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "gamma_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np2),
                                        lepton,
                                        DataManager.gamma_Np2_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "gamma_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np3),
                                        lepton,
                                        DataManager.gamma_Np3_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "gamma_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np4),
                                        lepton,
                                        DataManager.gamma_Np4_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)

    print
    print "gamma_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np5),
                                        lepton,
                                        DataManager.gamma_Np5_scale, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)
    print
    if lepton == ELECTRON:
        print "diphotons:"
        LepPhotonAnalysis.LepPhotonAnalysis(DataManager.diphotonsFile.Get(ttreeName), 
                                            makeOutputName(DataManager.diphotonsFileName),
                                            lepton,
                                            DataManager.diphotons_scale, applySF=LepPhotonAnalysis.NONE, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)
        print

    print "wino:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.winoFile.Get(ttreeName), 
                                        makeOutputName(DataManager.winoFileName),
                                        lepton,
                                        DataManager.wino_scale,
                                        onlyStrong=onlyStrong, applySF=LepPhotonAnalysis.NOMINAL, applyTrigWeight=LepPhotonAnalysis.NOMINAL, plotsRegion=plots)
    print

    print "data:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.dataFile.Get(ttreeName), 
                                        makeOutputName(DataManager.dataFileName),
                                        lepton,
                                        1.0, plotsRegion=plots, doABCD=abcd, blind=True)
    print

    # print "gj:"
    # LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gjFile.Get(ttreeName), 
    #                                     makeOutputName(DataManager.gjFileName),
    #                                     lepton,
    #                                     1.0,
    #                                     measureFakeAndEff=True,
    #                                     numBkgTight=0, plotsRegion=plots)
    print "gj:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gjFile.Get(ttreeName), 
                                        makeOutputName(DataManager.gjFileName),
                                        lepton,
                                        1.0,
                                        scaleQCD=True, plotsRegion=plots)
    print
    
if __name__ == "__main__":
    try:
        # retrive command line options
        shortopts  = "eml:p:a:"
        longopts   = ["lepton=", "plots=", "abcd="]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )
    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        sys.exit(1)

    lepton = DEFAULTLEPTON
    plots = LepPhotonAnalysis.DEFAULT_PLOTS
    abcd = DEFAULTABCD
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
            elif a == "TCR":
                plots = LepPhotonAnalysis.TCR
            elif a == "QCD":
                plots = LepPhotonAnalysis.QCD
            elif a == "XR1":
                plots = LepPhotonAnalysis.XR1
            elif a == "XR2":
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
    RunAnalysis(lepton, plots, abcd)
