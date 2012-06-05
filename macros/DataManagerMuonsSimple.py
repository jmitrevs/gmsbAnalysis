#! /usr/bin/env python

'''
Module to store all the source files, yields, etc, for electron channel.
'''

import ROOT
#ROOT.gROOT.LoadMacro("AtlasStyle.C") 
#ROOT.SetAtlasStyle()

PRINT_YIELDS = True

Lumi = 4708.61 # really electron only

print "Lepton is MUON."
path = "/data3/jmitrevs/lepPhotonResults/plots_120603/muon/PRESEL_SIGMADOWN/"

winoFileName = path + "wino_600_200_muHist.root"

WlepnuFileName_Np0 = path + "Wmunu_Np0Hist.root"
WlepnuFileName_Np1 = path + "Wmunu_Np1Hist.root"
WlepnuFileName_Np2 = path + "Wmunu_Np2Hist.root"
WlepnuFileName_Np3 = path + "Wmunu_Np3Hist.root"
WlepnuFileName_Np4 = path + "Wmunu_Np4Hist.root"
WlepnuFileName_Np5 = path + "Wmunu_Np5Hist.root"

ZleplepFileName_Np0 = path + "Zmumu_Np0Hist.root"
ZleplepFileName_Np1 = path + "Zmumu_Np1Hist.root"
ZleplepFileName_Np2 = path + "Zmumu_Np2Hist.root"
ZleplepFileName_Np3 = path + "Zmumu_Np3Hist.root"
ZleplepFileName_Np4 = path + "Zmumu_Np4Hist.root"
ZleplepFileName_Np5 = path + "Zmumu_Np5Hist.root"

st_tchan_lepnuFileName   = path + "st_tchan_munuHist.root"
ZleplepgammaFileName = path + "ZmumugammaHist.root"

WtaunuFileName_Np0 = path + "Wtaunu_Np0Hist.root"
WtaunuFileName_Np1 = path + "Wtaunu_Np1Hist.root"
WtaunuFileName_Np2 = path + "Wtaunu_Np2Hist.root"
WtaunuFileName_Np3 = path + "Wtaunu_Np3Hist.root"
WtaunuFileName_Np4 = path + "Wtaunu_Np4Hist.root"
WtaunuFileName_Np5 = path + "Wtaunu_Np5Hist.root"

ZtautauFileName_Np0 = path + "Ztautau_Np0Hist.root"
ZtautauFileName_Np1 = path + "Ztautau_Np1Hist.root"
ZtautauFileName_Np2 = path + "Ztautau_Np2Hist.root"
ZtautauFileName_Np3 = path + "Ztautau_Np3Hist.root"
ZtautauFileName_Np4 = path + "Ztautau_Np4Hist.root"
ZtautauFileName_Np5 = path + "Ztautau_Np5Hist.root"

st_tchan_taunuFileName = path + "st_tchan_taunuHist.root"    
st_WtFileName   = path + "st_WtHist.root"    
    
WgammaFileName_Np0 = path + "Wgamma_Np0Hist.root"
WgammaFileName_Np1 = path + "Wgamma_Np1Hist.root"
WgammaFileName_Np2 = path + "Wgamma_Np2Hist.root"
WgammaFileName_Np3 = path + "Wgamma_Np3Hist.root"
WgammaFileName_Np4 = path + "Wgamma_Np4Hist.root"
WgammaFileName_Np5 = path + "Wgamma_Np5Hist.root"

ttbarFileName = path + "ttbarHist.root"
ttbargammaFileName = path + "ttbargammaHist.root"

WWFileName = path + "WWHist.root"
WZFileName = path + "WZHist.root"
ZZFileName = path + "ZZHist.root"

ZtautaugammaFileName = path + "ZtautaugammaHist.root"
# ZnunugammagammaFileName = path + "ZnunugammagammaHist.root"

gammaFileName_Np1 = path + "gamma_Np1Hist.root"
gammaFileName_Np2 = path + "gamma_Np2Hist.root"
gammaFileName_Np3 = path + "gamma_Np3Hist.root"
gammaFileName_Np4 = path + "gamma_Np4Hist.root"
gammaFileName_Np5 = path + "gamma_Np5Hist.root"

# diphotonsFileName = path + "diphotonsHist.root"

dataFileName = path + "mugHist.root"
gjFileName = path + "gjHist.root"
    
###########################################

    
winoFile = ROOT.TFile(winoFileName)

WlepnuFile_Np0 = ROOT.TFile(WlepnuFileName_Np0)
WlepnuFile_Np1 = ROOT.TFile(WlepnuFileName_Np1)
WlepnuFile_Np2 = ROOT.TFile(WlepnuFileName_Np2)
WlepnuFile_Np3 = ROOT.TFile(WlepnuFileName_Np3)
WlepnuFile_Np4 = ROOT.TFile(WlepnuFileName_Np4)
WlepnuFile_Np5 = ROOT.TFile(WlepnuFileName_Np5)

WtaunuFile_Np0 = ROOT.TFile(WtaunuFileName_Np0)
WtaunuFile_Np1 = ROOT.TFile(WtaunuFileName_Np1)
WtaunuFile_Np2 = ROOT.TFile(WtaunuFileName_Np2)
WtaunuFile_Np3 = ROOT.TFile(WtaunuFileName_Np3)
WtaunuFile_Np4 = ROOT.TFile(WtaunuFileName_Np4)
WtaunuFile_Np5 = ROOT.TFile(WtaunuFileName_Np5)

ZleplepFile_Np0 = ROOT.TFile(ZleplepFileName_Np0)
ZleplepFile_Np1 = ROOT.TFile(ZleplepFileName_Np1)
ZleplepFile_Np2 = ROOT.TFile(ZleplepFileName_Np2)
ZleplepFile_Np3 = ROOT.TFile(ZleplepFileName_Np3)
ZleplepFile_Np4 = ROOT.TFile(ZleplepFileName_Np4)
ZleplepFile_Np5 = ROOT.TFile(ZleplepFileName_Np5)

ZtautauFile_Np0 = ROOT.TFile(ZtautauFileName_Np0)
ZtautauFile_Np1 = ROOT.TFile(ZtautauFileName_Np1)
ZtautauFile_Np2 = ROOT.TFile(ZtautauFileName_Np2)
ZtautauFile_Np3 = ROOT.TFile(ZtautauFileName_Np3)
ZtautauFile_Np4 = ROOT.TFile(ZtautauFileName_Np4)
ZtautauFile_Np5 = ROOT.TFile(ZtautauFileName_Np5)

WgammaFile_Np0 = ROOT.TFile(WgammaFileName_Np0)
WgammaFile_Np1 = ROOT.TFile(WgammaFileName_Np1)
WgammaFile_Np2 = ROOT.TFile(WgammaFileName_Np2)
WgammaFile_Np3 = ROOT.TFile(WgammaFileName_Np3)
WgammaFile_Np4 = ROOT.TFile(WgammaFileName_Np4)
WgammaFile_Np5 = ROOT.TFile(WgammaFileName_Np5)

ttbarFile = ROOT.TFile(ttbarFileName)
ttbargammaFile = ROOT.TFile(ttbargammaFileName)

st_tchan_lepnuFile   = ROOT.TFile(st_tchan_lepnuFileName)
st_tchan_taunuFile = ROOT.TFile(st_tchan_taunuFileName)

st_WtFile   = ROOT.TFile(st_WtFileName)

WWFile = ROOT.TFile(WWFileName)
WZFile = ROOT.TFile(WZFileName)
ZZFile = ROOT.TFile(ZZFileName)

ZleplepgammaFile = ROOT.TFile(ZleplepgammaFileName)
ZtautaugammaFile = ROOT.TFile(ZtautaugammaFileName)
# ZnunugammagammaFile = ROOT.TFile(ZnunugammagammaFileName)

gammaFile_Np1 = ROOT.TFile(gammaFileName_Np1)
gammaFile_Np2 = ROOT.TFile(gammaFileName_Np2)
gammaFile_Np3 = ROOT.TFile(gammaFileName_Np3)
gammaFile_Np4 = ROOT.TFile(gammaFileName_Np4)
gammaFile_Np5 = ROOT.TFile(gammaFileName_Np5)

#diphotonsFile = ROOT.TFile(diphotonsFileName)

dataFile = ROOT.TFile(dataFileName)
gjFile = ROOT.TFile(gjFileName)

##############################

