#! /usr/bin/env python

# code to make all the plots in a file

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

import os.path
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

def makeOutputName(infileName):
    inFileNoPath = os.path.split(infileName)[1]
    outfile = os.path.splitext(inFileNoPath)[0] + "Hist.root"
    return outfile

def RunAnalysis(lepton):


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
                                        True)

    print
    print "Wlepnu_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np1),
                                        lepton,
                                        DataManager.Wlepnu_Np1_scale,
                                        True)

    print
    print "Wlepnu_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np2),
                                        lepton,
                                        DataManager.Wlepnu_Np2_scale,
                                        True)

    print
    print "Wlepnu_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np3),
                                        lepton,
                                        DataManager.Wlepnu_Np3_scale,
                                        True)

    print
    print "Wlepnu_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np4),
                                        lepton,
                                        DataManager.Wlepnu_Np4_scale,
                                        True)

    print
    print "Wlepnu_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WlepnuFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.WlepnuFileName_Np5),
                                        lepton,
                                        DataManager.Wlepnu_Np5_scale,
                                        True)
    print
    print "Wtaunu_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np0),
                                        lepton,
                                        DataManager.Wtaunu_Np0_scale,
                                        True)

    print
    print "Wtaunu_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np1),
                                        lepton,
                                        DataManager.Wtaunu_Np1_scale,
                                        True)

    print
    print "Wtaunu_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np2),
                                        lepton,
                                        DataManager.Wtaunu_Np2_scale,
                                        True)

    print
    print "Wtaunu_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np3),
                                        lepton,
                                        DataManager.Wtaunu_Np3_scale,
                                        True)

    print
    print "Wtaunu_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np4),
                                        lepton,
                                        DataManager.Wtaunu_Np4_scale,
                                        True)

    print
    print "Wtaunu_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WtaunuFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.WtaunuFileName_Np5),
                                        lepton,
                                        DataManager.Wtaunu_Np5_scale,
                                        True)
    print
    print "Wgamma_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np0),
                                        lepton,
                                        DataManager.Wgamma_Np0_scale)

    print
    print "Wgamma_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np1),
                                        lepton,
                                        DataManager.Wgamma_Np1_scale)

    print
    print "Wgamma_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np2),
                                        lepton,
                                        DataManager.Wgamma_Np2_scale)

    print
    print "Wgamma_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np3),
                                        lepton,
                                        DataManager.Wgamma_Np3_scale)

    print
    print "Wgamma_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np4),
                                        lepton,
                                        DataManager.Wgamma_Np4_scale)

    print
    print "Wgamma_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WgammaFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.WgammaFileName_Np5),
                                        lepton,
                                        DataManager.Wgamma_Np5_scale)
    print

    print "ttbar:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ttbarFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ttbarFileName),
                                        lepton,
                                        DataManager.ttbar_scale)

    print
    print "ttbargamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ttbargammaFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ttbargammaFileName),
                                        lepton,
                                        DataManager.ttbargamma_scale)

    print
    print "st_tchan_lepnu:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.st_tchan_lepnuFile.Get(ttreeName), 
                                        makeOutputName(DataManager.st_tchan_lepnuFileName),
                                        lepton,
                                        DataManager.st_tchan_lepnu_scale)

    print
    print "st_tchan_taunu:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.st_tchan_taunuFile.Get(ttreeName), 
                                        makeOutputName(DataManager.st_tchan_taunuFileName),
                                        lepton,
                                        DataManager.st_tchan_taunu_scale)

    print
    print "st_Wt:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.st_WtFile.Get(ttreeName), 
                                        makeOutputName(DataManager.st_WtFileName),
                                        lepton,
                                        DataManager.st_Wt_scale)

    print

    print "WW:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WWFile.Get(ttreeName), 
                                        makeOutputName(DataManager.WWFileName),
                                        lepton,
                                        DataManager.WW_scale)

    print
    print "WZ:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.WZFile.Get(ttreeName), 
                                        makeOutputName(DataManager.WZFileName),
                                        lepton,
                                        DataManager.WZ_scale)

    print
    print "ZZ:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZZFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ZZFileName),
                                        lepton,
                                        DataManager.ZZ_scale)

    print


    print "Zleplepgamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepgammaFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepgammaFileName),
                                        lepton,
                                        DataManager.Zleplepgamma_scale)

    print

    print "Ztautaugamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautaugammaFile.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautaugammaFileName),
                                        lepton,
                                        DataManager.Ztautaugamma_scale)

    print


    print "Zleplep_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np0),
                                        lepton,
                                        DataManager.Zleplep_Np0_scale,
                                        True)

    print
    print "Zleplep_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np1),
                                        lepton,
                                        DataManager.Zleplep_Np1_scale,
                                        True)

    print
    print "Zleplep_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np2),
                                        lepton,
                                        DataManager.Zleplep_Np2_scale,
                                        True)

    print
    print "Zleplep_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np3),
                                        lepton,
                                        DataManager.Zleplep_Np3_scale,
                                        True)

    print
    print "Zleplep_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np4),
                                        lepton,
                                        DataManager.Zleplep_Np4_scale,
                                        True)

    print
    print "Zleplep_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZleplepFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.ZleplepFileName_Np5),
                                        lepton,
                                        DataManager.Zleplep_Np5_scale,
                                        True)
    print
    print "Ztautau_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np0.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np0),
                                        lepton,
                                        DataManager.Ztautau_Np0_scale,
                                        True)

    print
    print "Ztautau_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np1),
                                        lepton,
                                        DataManager.Ztautau_Np1_scale,
                                        True)

    print
    print "Ztautau_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np2),
                                        lepton,
                                        DataManager.Ztautau_Np2_scale,
                                        True)

    print
    print "Ztautau_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np3),
                                        lepton,
                                        DataManager.Ztautau_Np3_scale,
                                        True)

    print
    print "Ztautau_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np4),
                                        lepton,
                                        DataManager.Ztautau_Np4_scale,
                                        True)

    print
    print "Ztautau_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.ZtautauFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.ZtautauFileName_Np5),
                                        lepton,
                                        DataManager.Ztautau_Np5_scale,
                                        True)
    print

    print "gamma_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np1.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np1),
                                        lepton,
                                        DataManager.gamma_Np1_scale)

    print
    print "gamma_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np2.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np2),
                                        lepton,
                                        DataManager.gamma_Np2_scale)

    print
    print "gamma_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np3.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np3),
                                        lepton,
                                        DataManager.gamma_Np3_scale)

    print
    print "gamma_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np4.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np4),
                                        lepton,
                                        DataManager.gamma_Np4_scale)

    print
    print "gamma_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gammaFile_Np5.Get(ttreeName), 
                                        makeOutputName(DataManager.gammaFileName_Np5),
                                        lepton,
                                        DataManager.gamma_Np5_scale)
    print

    print "wino:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.winoFile.Get(ttreeName), 
                                        makeOutputName(DataManager.winoFileName),
                                        lepton,
                                        DataManager.wino_scale)
    print

    print "data:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.dataFile.Get(ttreeName), 
                                        makeOutputName(DataManager.dataFileName),
                                        lepton,
                                        1.0)
    print

    print "gj:"
    LepPhotonAnalysis.LepPhotonAnalysis(DataManager.gjFile.Get(ttreeName), 
                                        makeOutputName(DataManager.gjFileName),
                                        lepton,
                                        1.0)
    print
    
if __name__ == "__main__":
    RunAnalysis(DEFAULTLEPTON)
