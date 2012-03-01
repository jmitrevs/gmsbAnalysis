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

        Lumi = 4812.34 # really electron only


        print "Lepton is ELECTRON."
        path = "/data3/jmitrevs/lepphoton/elphoton_ntuple3/mergedFiles/"
        datapath = "/data3/jmitrevs/lepphoton/elphoton_data2/mergedFiles/"

        winoFileName = path + "wino_600_200_el.root"
        
        WlepnuFileName_Np0 = path + "Wenu_Np0.root"
        WlepnuFileName_Np1 = path + "Wenu_Np1.root"
        WlepnuFileName_Np2 = path + "Wenu_Np2.root"
        WlepnuFileName_Np3 = path + "Wenu_Np3.root"
        WlepnuFileName_Np4 = path + "Wenu_Np4.root"
        WlepnuFileName_Np5 = path + "Wenu_Np5.root"

        ZleplepFileName_Np0 = path + "Zee_Np0.root"
        ZleplepFileName_Np1 = path + "Zee_Np1.root"
        ZleplepFileName_Np2 = path + "Zee_Np2.root"
        ZleplepFileName_Np3 = path + "Zee_Np3.root"
        ZleplepFileName_Np4 = path + "Zee_Np4.root"
        ZleplepFileName_Np5 = path + "Zee_Np5.root"

        st_tchan_lepnuFileName   = path + "st_tchan_enu.root"
        #st_schan_lepnuFileName   = path + "st_schan_enu.root"
        ZleplepgammaFileName = path + "Zeegamma.root"

    elif lepton == MUON:

        Lumi = 4812.34 # really electron only


        print "Lepton is MUON."
        path = "/data3/jmitrevs/lepphoton/muphoton2/mergedFiles/"
        datapath = "/data3/jmitrevs/lepphoton/muphoton_data/mergedFiles/"

        winoFileName = path + "wino_600_200_mu.root"

        WlepnuFileName_Np0 = path + "Wmunu_Np0.root"
        WlepnuFileName_Np1 = path + "Wmunu_Np1.root"
        WlepnuFileName_Np2 = path + "Wmunu_Np2.root"
        WlepnuFileName_Np3 = path + "Wmunu_Np3.root"
        WlepnuFileName_Np4 = path + "Wmunu_Np4.root"
        WlepnuFileName_Np5 = path + "Wmunu_Np5.root"

        ZleplepFileName_Np0 = path + "Zmumu_Np0.root"
        ZleplepFileName_Np1 = path + "Zmumu_Np1.root"
        ZleplepFileName_Np2 = path + "Zmumu_Np2.root"
        ZleplepFileName_Np3 = path + "Zmumu_Np3.root"
        ZleplepFileName_Np4 = path + "Zmumu_Np4.root"
        ZleplepFileName_Np5 = path + "Zmumu_Np5.root"

        st_tchan_lepnuFileName   = path + "st_tchan_munu.root"
        #st_schan_lepnuFileName   = path + "st_schan_munu.root"
        ZleplepgammaFileName = path + "Zeegamma.root"

    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")

    
    WtaunuFileName_Np0 = path + "Wtaunu_Np0.root"
    WtaunuFileName_Np1 = path + "Wtaunu_Np1.root"
    WtaunuFileName_Np2 = path + "Wtaunu_Np2.root"
    WtaunuFileName_Np3 = path + "Wtaunu_Np3.root"
    WtaunuFileName_Np4 = path + "Wtaunu_Np4.root"
    WtaunuFileName_Np5 = path + "Wtaunu_Np5.root"

    ZtautauFileName_Np0 = path + "Ztautau_Np0.root"
    ZtautauFileName_Np1 = path + "Ztautau_Np1.root"
    ZtautauFileName_Np2 = path + "Ztautau_Np2.root"
    ZtautauFileName_Np3 = path + "Ztautau_Np3.root"
    ZtautauFileName_Np4 = path + "Ztautau_Np4.root"
    ZtautauFileName_Np5 = path + "Ztautau_Np5.root"

    st_tchan_taunuFileName = path + "st_tchan_taunu.root"    
    #st_schan_taunuFileName = path + "st_schan_taunu.root"
    st_WtFileName   = path + "st_Wt.root"    
    
    WgammaFileName_Np0 = path + "Wgamma_Np0.root"
    WgammaFileName_Np1 = path + "Wgamma_Np1.root"
    WgammaFileName_Np2 = path + "Wgamma_Np2.root"
    WgammaFileName_Np3 = path + "Wgamma_Np3.root"
    WgammaFileName_Np4 = path + "Wgamma_Np4.root"
    WgammaFileName_Np5 = path + "Wgamma_Np5.root"
    
    ttbarFileName = path + "ttbar.root"

    WWFileName = path + "WW.root"
    WZFileName = path + "WZ.root"
    ZZFileName = path + "ZZ.root"

    ZtautaugammaFileName = path + "Ztautaugamma.root"

    gammaFileName_Np1 = path + "gamma_Np1.root"
    gammaFileName_Np2 = path + "gamma_Np2.root"
    gammaFileName_Np3 = path + "gamma_Np3.root"
    gammaFileName_Np4 = path + "gamma_Np4.root"
    gammaFileName_Np5 = path + "gamma_Np5.root"

    dataFileName = datapath + "eg.root"
    gjFileName = datapath + "gj.root"
    
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
    
    st_tchan_lepnuFile   = ROOT.TFile(st_tchan_lepnuFileName)
    st_tchan_taunuFile = ROOT.TFile(st_tchan_taunuFileName)
    
    #st_schan_lepnuFile   = ROOT.TFile(st_schan_lepnuFileName)
    #st_schan_taunuFile = ROOT.TFile(st_schan_taunuFileName)
    
    st_WtFile   = ROOT.TFile(st_WtFileName)

    WWFile = ROOT.TFile(WWFileName)
    WZFile = ROOT.TFile(WZFileName)
    ZZFile = ROOT.TFile(ZZFileName)
    
    ZleplepgammaFile = ROOT.TFile(ZleplepgammaFileName)
    ZtautaugammaFile = ROOT.TFile(ZtautaugammaFileName)
    
    gammaFile_Np1 = ROOT.TFile(gammaFileName_Np1)
    gammaFile_Np2 = ROOT.TFile(gammaFileName_Np2)
    gammaFile_Np3 = ROOT.TFile(gammaFileName_Np3)
    gammaFile_Np4 = ROOT.TFile(gammaFileName_Np4)
    gammaFile_Np5 = ROOT.TFile(gammaFileName_Np5)

    dataFile = ROOT.TFile(dataFileName)
    gjFile = ROOT.TFile(gjFileName)

    ##############################

    cutFlowwino = winoFile.Get("Global/CutFlow")

    cutFlowWlepnu_Np0 = WlepnuFile_Np0.Get("Global/CutFlow")
    cutFlowWlepnu_Np1 = WlepnuFile_Np1.Get("Global/CutFlow")
    cutFlowWlepnu_Np2 = WlepnuFile_Np2.Get("Global/CutFlow")
    cutFlowWlepnu_Np3 = WlepnuFile_Np3.Get("Global/CutFlow")
    cutFlowWlepnu_Np4 = WlepnuFile_Np4.Get("Global/CutFlow")
    cutFlowWlepnu_Np5 = WlepnuFile_Np5.Get("Global/CutFlow")

    cutFlowWtaunu_Np0 = WtaunuFile_Np0.Get("Global/CutFlow")
    cutFlowWtaunu_Np1 = WtaunuFile_Np1.Get("Global/CutFlow")
    cutFlowWtaunu_Np2 = WtaunuFile_Np2.Get("Global/CutFlow")
    cutFlowWtaunu_Np3 = WtaunuFile_Np3.Get("Global/CutFlow")
    cutFlowWtaunu_Np4 = WtaunuFile_Np4.Get("Global/CutFlow")
    cutFlowWtaunu_Np5 = WtaunuFile_Np5.Get("Global/CutFlow")

    cutFlowZleplep_Np0 = ZleplepFile_Np0.Get("Global/CutFlow")
    cutFlowZleplep_Np1 = ZleplepFile_Np1.Get("Global/CutFlow")
    cutFlowZleplep_Np2 = ZleplepFile_Np2.Get("Global/CutFlow")
    cutFlowZleplep_Np3 = ZleplepFile_Np3.Get("Global/CutFlow")
    cutFlowZleplep_Np4 = ZleplepFile_Np4.Get("Global/CutFlow")
    cutFlowZleplep_Np5 = ZleplepFile_Np5.Get("Global/CutFlow")

    cutFlowZtautau_Np0 = ZtautauFile_Np0.Get("Global/CutFlow")
    cutFlowZtautau_Np1 = ZtautauFile_Np1.Get("Global/CutFlow")
    cutFlowZtautau_Np2 = ZtautauFile_Np2.Get("Global/CutFlow")
    cutFlowZtautau_Np3 = ZtautauFile_Np3.Get("Global/CutFlow")
    cutFlowZtautau_Np4 = ZtautauFile_Np4.Get("Global/CutFlow")
    cutFlowZtautau_Np5 = ZtautauFile_Np5.Get("Global/CutFlow")

    cutFlowWgamma_Np0 = WgammaFile_Np0.Get("Global/CutFlow")
    cutFlowWgamma_Np1 = WgammaFile_Np1.Get("Global/CutFlow")
    cutFlowWgamma_Np2 = WgammaFile_Np2.Get("Global/CutFlow")
    cutFlowWgamma_Np3 = WgammaFile_Np3.Get("Global/CutFlow")
    cutFlowWgamma_Np4 = WgammaFile_Np4.Get("Global/CutFlow")
    cutFlowWgamma_Np5 = WgammaFile_Np5.Get("Global/CutFlow")

    cutFlowttbar = ttbarFile.Get("Global/CutFlow")

    cutFlowst_tchan_lepnu = st_tchan_lepnuFile.Get("Global/CutFlow")
    cutFlowst_tchan_taunu = st_tchan_taunuFile.Get("Global/CutFlow")

    #cutFlowst_schan_lepnu = st_schan_lepnuFile.Get("Global/CutFlow")
    #cutFlowst_schan_taunu = st_schan_taunuFile.Get("Global/CutFlow")

    cutFlowst_Wt   = st_WtFile.Get("Global/CutFlow")

    cutFlowWW   = WWFile.Get("Global/CutFlow")
    cutFlowWZ   = WZFile.Get("Global/CutFlow")
    cutFlowZZ   = ZZFile.Get("Global/CutFlow")

    cutFlowZleplepgamma = ZleplepgammaFile.Get("Global/CutFlow")
    cutFlowZtautaugamma = ZtautaugammaFile.Get("Global/CutFlow")

    cutFlowgamma_Np1 = gammaFile_Np1.Get("Global/CutFlow")
    cutFlowgamma_Np2 = gammaFile_Np2.Get("Global/CutFlow")
    cutFlowgamma_Np3 = gammaFile_Np3.Get("Global/CutFlow")
    cutFlowgamma_Np4 = gammaFile_Np4.Get("Global/CutFlow")
    cutFlowgamma_Np5 = gammaFile_Np5.Get("Global/CutFlow")

    cutFlowdata = dataFile.Get("Global/CutFlow");
    cutFlowgj = gjFile.Get("Global/CutFlow");

    #########################################################

    nOrigwino = cutFlowwino.GetBinContent(1)

    nOrigWlepnu_Np0 = cutFlowWlepnu_Np0.GetBinContent(1)
    nOrigWlepnu_Np1 = cutFlowWlepnu_Np1.GetBinContent(1)
    nOrigWlepnu_Np2 = cutFlowWlepnu_Np2.GetBinContent(1)
    nOrigWlepnu_Np3 = cutFlowWlepnu_Np3.GetBinContent(1)
    nOrigWlepnu_Np4 = cutFlowWlepnu_Np4.GetBinContent(1)
    nOrigWlepnu_Np5 = cutFlowWlepnu_Np5.GetBinContent(1)
    
    nOrigWtaunu_Np0 = cutFlowWtaunu_Np0.GetBinContent(1)
    nOrigWtaunu_Np1 = cutFlowWtaunu_Np1.GetBinContent(1)
    nOrigWtaunu_Np2 = cutFlowWtaunu_Np2.GetBinContent(1)
    nOrigWtaunu_Np3 = cutFlowWtaunu_Np3.GetBinContent(1)
    nOrigWtaunu_Np4 = cutFlowWtaunu_Np4.GetBinContent(1)
    nOrigWtaunu_Np5 = cutFlowWtaunu_Np5.GetBinContent(1)

    nOrigZleplep_Np0 = cutFlowZleplep_Np0.GetBinContent(1)
    nOrigZleplep_Np1 = cutFlowZleplep_Np1.GetBinContent(1)
    nOrigZleplep_Np2 = cutFlowZleplep_Np2.GetBinContent(1)
    nOrigZleplep_Np3 = cutFlowZleplep_Np3.GetBinContent(1)
    nOrigZleplep_Np4 = cutFlowZleplep_Np4.GetBinContent(1)
    nOrigZleplep_Np5 = cutFlowZleplep_Np5.GetBinContent(1)
    
    nOrigZtautau_Np0 = cutFlowZtautau_Np0.GetBinContent(1)
    nOrigZtautau_Np1 = cutFlowZtautau_Np1.GetBinContent(1)
    nOrigZtautau_Np2 = cutFlowZtautau_Np2.GetBinContent(1)
    nOrigZtautau_Np3 = cutFlowZtautau_Np3.GetBinContent(1)
    nOrigZtautau_Np4 = cutFlowZtautau_Np4.GetBinContent(1)
    nOrigZtautau_Np5 = cutFlowZtautau_Np5.GetBinContent(1)
    
    nOrigWgamma_Np0 = cutFlowWgamma_Np0.GetBinContent(1)
    nOrigWgamma_Np1 = cutFlowWgamma_Np1.GetBinContent(1)
    nOrigWgamma_Np2 = cutFlowWgamma_Np2.GetBinContent(1)
    nOrigWgamma_Np3 = cutFlowWgamma_Np3.GetBinContent(1)
    nOrigWgamma_Np4 = cutFlowWgamma_Np4.GetBinContent(1)
    nOrigWgamma_Np5 = cutFlowWgamma_Np5.GetBinContent(1)
    
    nOrigttbar = cutFlowttbar.GetBinContent(1)
    
    nOrigst_tchan_lepnu = cutFlowst_tchan_lepnu.GetBinContent(1)
    nOrigst_tchan_taunu = cutFlowst_tchan_taunu.GetBinContent(1)
    
    #nOrigst_schan_lepnu = cutFlowst_schan_lepnu.GetBinContent(1)
    #nOrigst_schan_taunu = cutFlowst_schan_taunu.GetBinContent(1)
    
    nOrigst_Wt = cutFlowst_Wt.GetBinContent(1)

    nOrigWW = cutFlowWW.GetBinContent(1)
    nOrigWZ = cutFlowWZ.GetBinContent(1)
    nOrigZZ = cutFlowZZ.GetBinContent(1)
    
    nOrigZleplepgamma = cutFlowZleplepgamma.GetBinContent(1)
    nOrigZtautaugamma = cutFlowZtautaugamma.GetBinContent(1)

    nOriggamma_Np1 = cutFlowgamma_Np1.GetBinContent(1)
    nOriggamma_Np2 = cutFlowgamma_Np2.GetBinContent(1)
    nOriggamma_Np3 = cutFlowgamma_Np3.GetBinContent(1)
    nOriggamma_Np4 = cutFlowgamma_Np4.GetBinContent(1)
    nOriggamma_Np5 = cutFlowgamma_Np5.GetBinContent(1)

    nOrigdata = cutFlowdata.GetBinContent(1)
    nOriggj = cutFlowgj.GetBinContent(1)

    ######################################################

    # let's print out the number of events for debugging
    print "Number of input events:"

    print "\tnOrigwino =", nOrigwino

    print "\tnOrigWlepnu_Np0 =", nOrigWlepnu_Np0
    print "\tnOrigWlepnu_Np1 =", nOrigWlepnu_Np1
    print "\tnOrigWlepnu_Np2 =", nOrigWlepnu_Np2
    print "\tnOrigWlepnu_Np3 =", nOrigWlepnu_Np3
    print "\tnOrigWlepnu_Np4 =", nOrigWlepnu_Np4
    print "\tnOrigWlepnu_Np5 =", nOrigWlepnu_Np5
    
    print "\tnOrigWtaunu_Np0 =", nOrigWtaunu_Np0
    print "\tnOrigWtaunu_Np1 =", nOrigWtaunu_Np1
    print "\tnOrigWtaunu_Np2 =", nOrigWtaunu_Np2
    print "\tnOrigWtaunu_Np3 =", nOrigWtaunu_Np3
    print "\tnOrigWtaunu_Np4 =", nOrigWtaunu_Np4
    print "\tnOrigWtaunu_Np5 =", nOrigWtaunu_Np5

    print "\tnOrigZleplep_Np0 =", nOrigZleplep_Np0
    print "\tnOrigZleplep_Np1 =", nOrigZleplep_Np1
    print "\tnOrigZleplep_Np2 =", nOrigZleplep_Np2
    print "\tnOrigZleplep_Np3 =", nOrigZleplep_Np3
    print "\tnOrigZleplep_Np4 =", nOrigZleplep_Np4
    print "\tnOrigZleplep_Np5 =", nOrigZleplep_Np5
    
    print "\tnOrigZtautau_Np0 =", nOrigZtautau_Np0
    print "\tnOrigZtautau_Np1 =", nOrigZtautau_Np1
    print "\tnOrigZtautau_Np2 =", nOrigZtautau_Np2
    print "\tnOrigZtautau_Np3 =", nOrigZtautau_Np3
    print "\tnOrigZtautau_Np4 =", nOrigZtautau_Np4
    print "\tnOrigZtautau_Np5 =", nOrigZtautau_Np5
    
    print "\tnOrigWgamma_Np0 =", nOrigWgamma_Np0
    print "\tnOrigWgamma_Np1 =", nOrigWgamma_Np1
    print "\tnOrigWgamma_Np2 =", nOrigWgamma_Np2
    print "\tnOrigWgamma_Np3 =", nOrigWgamma_Np3
    print "\tnOrigWgamma_Np4 =", nOrigWgamma_Np4
    print "\tnOrigWgamma_Np5 =", nOrigWgamma_Np5
    
    print "\tnOrigttbar =", nOrigttbar
    
    print "\tnOrigst_tchan_lepnu =", nOrigst_tchan_lepnu
    print "\tnOrigst_tchan_taunu =", nOrigst_tchan_taunu
    
    #print "\tnOrigst_schan_lepnu =", nOrigst_schan_lepnu
    #print "\tnOrigst_schan_taunu =", nOrigst_schan_taunu
    
    print "\tnOrigst_Wt =", nOrigst_Wt

    print "\tnOrigWW =", nOrigWW
    print "\tnOrigWZ =", nOrigWZ
    print "\tnOrigZZ =", nOrigZZ

    print "\tnOrigZleplepgamma =", nOrigZleplepgamma
    print "\tnOrigZtautaugamma =", nOrigZtautaugamma

    print "\tnOriggamma_Np1 =", nOriggamma_Np1
    print "\tnOriggamma_Np2 =", nOriggamma_Np2
    print "\tnOriggamma_Np3 =", nOriggamma_Np3
    print "\tnOriggamma_Np4 =", nOriggamma_Np4
    print "\tnOriggamma_Np5 =", nOriggamma_Np5
    print
    print "\tnOrigdata =", nOrigdata
    print "\tnOriggj (before subtraction) =", nOriggj
    print

    ##############################################
    #   scale is lumi * xsec * kfact * filter / numEvents

    wino_scale = Lumi * 1.1675 * 1 / nOrigwino


    if lepton == ELECTRON:

        Wlepnu_Np0_scale     =  Lumi  *  6921.60 * 1.20   / nOrigWlepnu_Np0
        Wlepnu_Np1_scale     =  Lumi  *  1304.30 * 1.20   / nOrigWlepnu_Np1
        Wlepnu_Np2_scale     =  Lumi  *   378.29 * 1.20   / nOrigWlepnu_Np2
        Wlepnu_Np3_scale     =  Lumi  *   101.43 * 1.20   / nOrigWlepnu_Np3
        Wlepnu_Np4_scale     =  Lumi  *    25.87 * 1.20   / nOrigWlepnu_Np4
        Wlepnu_Np5_scale     =  Lumi  *     7.00 * 1.20   / nOrigWlepnu_Np5

        Zleplep_Np0_scale     =  Lumi  *  668.32 * 1.25   / nOrigZleplep_Np0
        Zleplep_Np1_scale     =  Lumi  *  134.36 * 1.25   / nOrigZleplep_Np1
        Zleplep_Np2_scale     =  Lumi  *   40.54 * 1.25   / nOrigZleplep_Np2
        Zleplep_Np3_scale     =  Lumi  *   11.16 * 1.25   / nOrigZleplep_Np3
        Zleplep_Np4_scale     =  Lumi  *    2.88 * 1.25   / nOrigZleplep_Np4
        Zleplep_Np5_scale     =  Lumi  *    0.83 * 1.25   / nOrigZleplep_Np5

    else:  # muon
        
        Wlepnu_Np0_scale     =  Lumi  *  6919.60 * 1.20   / nOrigWlepnu_Np0
        Wlepnu_Np1_scale     =  Lumi  *  1304.20 * 1.20   / nOrigWlepnu_Np1
        Wlepnu_Np2_scale     =  Lumi  *   377.83 * 1.20   / nOrigWlepnu_Np2
        Wlepnu_Np3_scale     =  Lumi  *   101.88 * 1.20   / nOrigWlepnu_Np3
        Wlepnu_Np4_scale     =  Lumi  *    25.75 * 1.20   / nOrigWlepnu_Np4
        Wlepnu_Np5_scale     =  Lumi  *     6.92 * 1.20   / nOrigWlepnu_Np5

        Zleplep_Np0_scale     =  Lumi  *  668.68 * 1.25   / nOrigZleplep_Np0
        Zleplep_Np1_scale     =  Lumi  *  134.14 * 1.25   / nOrigZleplep_Np1
        Zleplep_Np2_scale     =  Lumi  *   40.33 * 1.25   / nOrigZleplep_Np2
        Zleplep_Np3_scale     =  Lumi  *   11.19 * 1.25   / nOrigZleplep_Np3
        Zleplep_Np4_scale     =  Lumi  *    2.75 * 1.25   / nOrigZleplep_Np4
        Zleplep_Np5_scale     =  Lumi  *    0.77 * 1.25   / nOrigZleplep_Np5


    Wtaunu_Np0_scale   =  Lumi  *  6919.60 * 1.20   / nOrigWtaunu_Np0
    Wtaunu_Np1_scale   =  Lumi  *  1303.20 * 1.20   / nOrigWtaunu_Np1
    Wtaunu_Np2_scale   =  Lumi  *   378.18 * 1.20   / nOrigWtaunu_Np2
    Wtaunu_Np3_scale   =  Lumi  *   101.43 * 1.20   / nOrigWtaunu_Np3
    Wtaunu_Np4_scale   =  Lumi  *    25.87 * 1.20   / nOrigWtaunu_Np4
    Wtaunu_Np5_scale   =  Lumi  *     6.92 * 1.20   / nOrigWtaunu_Np5

    Ztautau_Np0_scale   =  Lumi  *  668.40 * 1.25   / nOrigZtautau_Np0
    Ztautau_Np1_scale   =  Lumi  *  134.81 * 1.25   / nOrigZtautau_Np1
    Ztautau_Np2_scale   =  Lumi  *   40.36 * 1.25   / nOrigZtautau_Np2
    Ztautau_Np3_scale   =  Lumi  *   11.25 * 1.25   / nOrigZtautau_Np3
    Ztautau_Np4_scale   =  Lumi  *    2.79 * 1.25   / nOrigZtautau_Np4
    Ztautau_Np5_scale   =  Lumi  *    0.77 * 1.25   / nOrigZtautau_Np5

    ttbar_scale          =  Lumi  *  89.02311 / nOrigttbar

    # if using gamma pt > 10 GeV samples
    # Wgamma_Np0_scale     =  Lumi  *  213.270 * 1.488   / nOrigWgamma_Np0
    # Wgamma_Np1_scale     =  Lumi  *   52.238 * 1.488   / nOrigWgamma_Np1
    # Wgamma_Np2_scale     =  Lumi  *   17.259 * 1.488   / nOrigWgamma_Np2
    # Wgamma_Np3_scale     =  Lumi  *    5.3339 * 1.488   / nOrigWgamma_Np3
    # Wgamma_Np4_scale     =  Lumi  *    1.3762 * 1.488   / nOrigWgamma_Np4
    # Wgamma_Np5_scale     =  Lumi  *    0.34445 * 1.488   / nOrigWgamma_Np5
    
    # if using gamma pt > 40 GeV sample
    Wgamma_Np0_scale     =  Lumi  *  1.7837 * 1.488   / nOrigWgamma_Np0
    Wgamma_Np1_scale     =  Lumi  *  4.3796 * 1.488   / nOrigWgamma_Np1
    Wgamma_Np2_scale     =  Lumi  *  2.1381 * 1.488   / nOrigWgamma_Np2
    Wgamma_Np3_scale     =  Lumi  *  0.87283 * 1.488   / nOrigWgamma_Np3
    Wgamma_Np4_scale     =  Lumi  *  0.27846 * 1.488   / nOrigWgamma_Np4
    Wgamma_Np5_scale     =  Lumi  *  0.08504 * 1.488   / nOrigWgamma_Np5

    Zleplepgamma_scale   =  Lumi  *  9.63   / nOrigZleplepgamma
    Ztautaugamma_scale   =  Lumi  *  9.41   / nOrigZtautaugamma

    st_tchan_lepnu_scale = Lumi * 7.12 / nOrigst_tchan_lepnu
    #st_schan_lepnu_scale = Lumi * 0.47 / nOrigst_schan_lepnu
    st_tchan_taunu_scale = Lumi * 7.10 / nOrigst_tchan_taunu
    #st_schan_taunu_scale = Lumi * 0.47 / nOrigst_schan_taunu
    st_Wt_scale = Lumi * 14.59 / nOrigst_Wt

    WW_scale = Lumi * 11.5003 * 1.48 / nOrigWW
    WZ_scale = Lumi *  3.4641 * 1.60 / nOrigWZ
    ZZ_scale = Lumi *  0.9722 * 1.30 / nOrigZZ

    gamma_Np1_scale     =  Lumi  *  74235 * 1.0933E-01 / nOriggamma_Np1
    gamma_Np2_scale     =  Lumi  *  21574 * 3.1052E-01 / nOriggamma_Np2
    gamma_Np3_scale     =  Lumi  *  5861.9 * 4.6724E-01 / nOriggamma_Np3
    gamma_Np4_scale     =  Lumi  *  1355.9 * 6.2450E-01 / nOriggamma_Np4
    gamma_Np5_scale     =  Lumi  *  351.86 * 7.6173E-01 / nOriggamma_Np5

    ##########################################################
    # let's print out the scales

    print "Scale (weight) for each sample:"

    print "\twino_scale =", wino_scale

    print "\tWlepnu_Np0_scale =", Wlepnu_Np0_scale
    print "\tWlepnu_Np1_scale =", Wlepnu_Np1_scale
    print "\tWlepnu_Np2_scale =", Wlepnu_Np2_scale
    print "\tWlepnu_Np3_scale =", Wlepnu_Np3_scale
    print "\tWlepnu_Np4_scale =", Wlepnu_Np4_scale
    print "\tWlepnu_Np5_scale =", Wlepnu_Np5_scale
    
    print "\tWtaunu_Np0_scale =", Wtaunu_Np0_scale
    print "\tWtaunu_Np1_scale =", Wtaunu_Np1_scale
    print "\tWtaunu_Np2_scale =", Wtaunu_Np2_scale
    print "\tWtaunu_Np3_scale =", Wtaunu_Np3_scale
    print "\tWtaunu_Np4_scale =", Wtaunu_Np4_scale
    print "\tWtaunu_Np5_scale =", Wtaunu_Np5_scale

    print "\tZleplep_Np0_scale =", Zleplep_Np0_scale
    print "\tZleplep_Np1_scale =", Zleplep_Np1_scale
    print "\tZleplep_Np2_scale =", Zleplep_Np2_scale
    print "\tZleplep_Np3_scale =", Zleplep_Np3_scale
    print "\tZleplep_Np4_scale =", Zleplep_Np4_scale
    print "\tZleplep_Np5_scale =", Zleplep_Np5_scale
    
    print "\tZtautau_Np0_scale =", Ztautau_Np0_scale
    print "\tZtautau_Np1_scale =", Ztautau_Np1_scale
    print "\tZtautau_Np2_scale =", Ztautau_Np2_scale
    print "\tZtautau_Np3_scale =", Ztautau_Np3_scale
    print "\tZtautau_Np4_scale =", Ztautau_Np4_scale
    print "\tZtautau_Np5_scale =", Ztautau_Np5_scale
    
    print "\tWgamma_Np0_scale =", Wgamma_Np0_scale
    print "\tWgamma_Np1_scale =", Wgamma_Np1_scale
    print "\tWgamma_Np2_scale =", Wgamma_Np2_scale
    print "\tWgamma_Np3_scale =", Wgamma_Np3_scale
    print "\tWgamma_Np4_scale =", Wgamma_Np4_scale
    print "\tWgamma_Np5_scale =", Wgamma_Np5_scale
    
    print "\tttbar_scale =", ttbar_scale
    
    print "\tst_tchan_lepnu_scale =", st_tchan_lepnu_scale
    print "\tst_tchan_taunu_scale =", st_tchan_taunu_scale
    
    #print "\tst_schan_lepnu_scale =", st_schan_lepnu_scale
    #print "\tst_schan_taunu_scale =", st_schan_taunu_scale
    
    print "\tst_Wt_scale =", st_Wt_scale

    print "\tWW_scale =", WW_scale
    print "\tWZ_scale =", WZ_scale
    print "\tZZ_scale =", ZZ_scale

    print "\tZleplepgamma_scale =", Zleplepgamma_scale
    print "\tZtautaugamma_scale =", Ztautaugamma_scale

    print "\tgamma_Np1_scale =", gamma_Np1_scale
    print "\tgamma_Np2_scale =", gamma_Np2_scale
    print "\tgamma_Np3_scale =", gamma_Np3_scale
    print "\tgamma_Np4_scale =", gamma_Np4_scale
    print "\tgamma_Np5_scale =", gamma_Np5_scale
    print

    #########################################################
    # let's print the yield before any cuts

    #########################################################

    binToLookAt = 10

    nAfterPreselectwino = cutFlowwino.GetBinContent(binToLookAt)

    nAfterPreselectWlepnu_Np0 = cutFlowWlepnu_Np0.GetBinContent(binToLookAt)
    nAfterPreselectWlepnu_Np1 = cutFlowWlepnu_Np1.GetBinContent(binToLookAt)
    nAfterPreselectWlepnu_Np2 = cutFlowWlepnu_Np2.GetBinContent(binToLookAt)
    nAfterPreselectWlepnu_Np3 = cutFlowWlepnu_Np3.GetBinContent(binToLookAt)
    nAfterPreselectWlepnu_Np4 = cutFlowWlepnu_Np4.GetBinContent(binToLookAt)
    nAfterPreselectWlepnu_Np5 = cutFlowWlepnu_Np5.GetBinContent(binToLookAt)
    
    nAfterPreselectWtaunu_Np0 = cutFlowWtaunu_Np0.GetBinContent(binToLookAt)
    nAfterPreselectWtaunu_Np1 = cutFlowWtaunu_Np1.GetBinContent(binToLookAt)
    nAfterPreselectWtaunu_Np2 = cutFlowWtaunu_Np2.GetBinContent(binToLookAt)
    nAfterPreselectWtaunu_Np3 = cutFlowWtaunu_Np3.GetBinContent(binToLookAt)
    nAfterPreselectWtaunu_Np4 = cutFlowWtaunu_Np4.GetBinContent(binToLookAt)
    nAfterPreselectWtaunu_Np5 = cutFlowWtaunu_Np5.GetBinContent(binToLookAt)

    nAfterPreselectZleplep_Np0 = cutFlowZleplep_Np0.GetBinContent(binToLookAt)
    nAfterPreselectZleplep_Np1 = cutFlowZleplep_Np1.GetBinContent(binToLookAt)
    nAfterPreselectZleplep_Np2 = cutFlowZleplep_Np2.GetBinContent(binToLookAt)
    nAfterPreselectZleplep_Np3 = cutFlowZleplep_Np3.GetBinContent(binToLookAt)
    nAfterPreselectZleplep_Np4 = cutFlowZleplep_Np4.GetBinContent(binToLookAt)
    nAfterPreselectZleplep_Np5 = cutFlowZleplep_Np5.GetBinContent(binToLookAt)
    
    nAfterPreselectZtautau_Np0 = cutFlowZtautau_Np0.GetBinContent(binToLookAt)
    nAfterPreselectZtautau_Np1 = cutFlowZtautau_Np1.GetBinContent(binToLookAt)
    nAfterPreselectZtautau_Np2 = cutFlowZtautau_Np2.GetBinContent(binToLookAt)
    nAfterPreselectZtautau_Np3 = cutFlowZtautau_Np3.GetBinContent(binToLookAt)
    nAfterPreselectZtautau_Np4 = cutFlowZtautau_Np4.GetBinContent(binToLookAt)
    nAfterPreselectZtautau_Np5 = cutFlowZtautau_Np5.GetBinContent(binToLookAt)
    
    nAfterPreselectWgamma_Np0 = cutFlowWgamma_Np0.GetBinContent(binToLookAt)
    nAfterPreselectWgamma_Np1 = cutFlowWgamma_Np1.GetBinContent(binToLookAt)
    nAfterPreselectWgamma_Np2 = cutFlowWgamma_Np2.GetBinContent(binToLookAt)
    nAfterPreselectWgamma_Np3 = cutFlowWgamma_Np3.GetBinContent(binToLookAt)
    nAfterPreselectWgamma_Np4 = cutFlowWgamma_Np4.GetBinContent(binToLookAt)
    nAfterPreselectWgamma_Np5 = cutFlowWgamma_Np5.GetBinContent(binToLookAt)
    
    nAfterPreselectttbar = cutFlowttbar.GetBinContent(binToLookAt)
    
    nAfterPreselectst_tchan_lepnu = cutFlowst_tchan_lepnu.GetBinContent(binToLookAt)
    nAfterPreselectst_tchan_taunu = cutFlowst_tchan_taunu.GetBinContent(binToLookAt)
    
    #nAfterPreselectst_schan_lepnu = cutFlowst_schan_lepnu.GetBinContent(binToLookAt)
    #nAfterPreselectst_schan_taunu = cutFlowst_schan_taunu.GetBinContent(binToLookAt)
    
    nAfterPreselectst_Wt = cutFlowst_Wt.GetBinContent(binToLookAt)

    nAfterPreselectWW = cutFlowWW.GetBinContent(binToLookAt)
    nAfterPreselectWZ = cutFlowWZ.GetBinContent(binToLookAt)
    nAfterPreselectZZ = cutFlowZZ.GetBinContent(binToLookAt)
    
    nAfterPreselectZleplepgamma = cutFlowZleplepgamma.GetBinContent(binToLookAt)
    nAfterPreselectZtautaugamma = cutFlowZtautaugamma.GetBinContent(binToLookAt)

    nAfterPreselectgamma_Np1 = cutFlowgamma_Np1.GetBinContent(binToLookAt)
    nAfterPreselectgamma_Np2 = cutFlowgamma_Np2.GetBinContent(binToLookAt)
    nAfterPreselectgamma_Np3 = cutFlowgamma_Np3.GetBinContent(binToLookAt)
    nAfterPreselectgamma_Np4 = cutFlowgamma_Np4.GetBinContent(binToLookAt)
    nAfterPreselectgamma_Np5 = cutFlowgamma_Np5.GetBinContent(binToLookAt)

    nAfterPreselectdata = cutFlowdata.GetBinContent(binToLookAt)
    nAfterPreselectgj = cutFlowgj.GetBinContent(binToLookAt)

    #############################################################
    # let's print out the yield after preselection
    print "Yield after Preselection:"

    print "Yield wino =", nAfterPreselectwino * wino_scale

    print "Yield Wlepnu_Np0 =", nAfterPreselectWlepnu_Np0 * Wlepnu_Np0_scale
    print "Yield Wlepnu_Np1 =", nAfterPreselectWlepnu_Np1 * Wlepnu_Np1_scale
    print "Yield Wlepnu_Np2 =", nAfterPreselectWlepnu_Np2 * Wlepnu_Np2_scale
    print "Yield Wlepnu_Np3 =", nAfterPreselectWlepnu_Np3 * Wlepnu_Np3_scale
    print "Yield Wlepnu_Np4 =", nAfterPreselectWlepnu_Np4 * Wlepnu_Np4_scale
    print "Yield Wlepnu_Np5 =", nAfterPreselectWlepnu_Np5 * Wlepnu_Np5_scale
    
    print "Yield Wtaunu_Np0 =", nAfterPreselectWtaunu_Np0 * Wtaunu_Np0_scale
    print "Yield Wtaunu_Np1 =", nAfterPreselectWtaunu_Np1 * Wtaunu_Np1_scale
    print "Yield Wtaunu_Np2 =", nAfterPreselectWtaunu_Np2 * Wtaunu_Np2_scale
    print "Yield Wtaunu_Np3 =", nAfterPreselectWtaunu_Np3 * Wtaunu_Np3_scale
    print "Yield Wtaunu_Np4 =", nAfterPreselectWtaunu_Np4 * Wtaunu_Np4_scale
    print "Yield Wtaunu_Np5 =", nAfterPreselectWtaunu_Np5 * Wtaunu_Np5_scale

    print "Yield Zleplep_Np0 =", nAfterPreselectZleplep_Np0 * Zleplep_Np0_scale
    print "Yield Zleplep_Np1 =", nAfterPreselectZleplep_Np1 * Zleplep_Np1_scale
    print "Yield Zleplep_Np2 =", nAfterPreselectZleplep_Np2 * Zleplep_Np2_scale
    print "Yield Zleplep_Np3 =", nAfterPreselectZleplep_Np3 * Zleplep_Np3_scale
    print "Yield Zleplep_Np4 =", nAfterPreselectZleplep_Np4 * Zleplep_Np4_scale
    print "Yield Zleplep_Np5 =", nAfterPreselectZleplep_Np5 * Zleplep_Np5_scale
    
    print "Yield Ztautau_Np0 =", nAfterPreselectZtautau_Np0 * Ztautau_Np0_scale
    print "Yield Ztautau_Np1 =", nAfterPreselectZtautau_Np1 * Ztautau_Np1_scale
    print "Yield Ztautau_Np2 =", nAfterPreselectZtautau_Np2 * Ztautau_Np2_scale
    print "Yield Ztautau_Np3 =", nAfterPreselectZtautau_Np3 * Ztautau_Np3_scale
    print "Yield Ztautau_Np4 =", nAfterPreselectZtautau_Np4 * Ztautau_Np4_scale
    print "Yield Ztautau_Np5 =", nAfterPreselectZtautau_Np5 * Ztautau_Np5_scale
    
    print "Yield Wgamma_Np0 =", nAfterPreselectWgamma_Np0 * Wgamma_Np0_scale
    print "Yield Wgamma_Np1 =", nAfterPreselectWgamma_Np1 * Wgamma_Np1_scale
    print "Yield Wgamma_Np2 =", nAfterPreselectWgamma_Np2 * Wgamma_Np2_scale
    print "Yield Wgamma_Np3 =", nAfterPreselectWgamma_Np3 * Wgamma_Np3_scale
    print "Yield Wgamma_Np4 =", nAfterPreselectWgamma_Np4 * Wgamma_Np4_scale
    print "Yield Wgamma_Np5 =", nAfterPreselectWgamma_Np5 * Wgamma_Np5_scale
    
    print "Yield ttbar =", nAfterPreselectttbar * ttbar_scale
    
    print "Yield st_tchan_lepnu =", nAfterPreselectst_tchan_lepnu * st_tchan_lepnu_scale
    print "Yield st_tchan_taunu =", nAfterPreselectst_tchan_taunu * st_tchan_taunu_scale
    
    #print "Yield st_schan_lepnu =", nAfterPreselectst_schan_lepnu * st_schan_lepnu_scale
    #print "Yield st_schan_taunu =", nAfterPreselectst_schan_taunu * st_schan_taunu_scale
    
    print "Yield st_Wt =", nAfterPreselectst_Wt * st_Wt_scale

    print "Yield WW =", nAfterPreselectWW * WW_scale
    print "Yield WZ =", nAfterPreselectWZ * WZ_scale
    print "Yield ZZ =", nAfterPreselectZZ * ZZ_scale

    print "Yield Zleplepgamma =", nAfterPreselectZleplepgamma * Zleplepgamma_scale
    print "Yield Ztautaugamma =", nAfterPreselectZtautaugamma * Ztautaugamma_scale

    print "Yield gamma_Np1 =", nAfterPreselectgamma_Np1 * gamma_Np1_scale
    print "Yield gamma_Np2 =", nAfterPreselectgamma_Np2 * gamma_Np2_scale
    print "Yield gamma_Np3 =", nAfterPreselectgamma_Np3 * gamma_Np3_scale
    print "Yield gamma_Np4 =", nAfterPreselectgamma_Np4 * gamma_Np4_scale
    print "Yield gamma_Np5 =", nAfterPreselectgamma_Np5 * gamma_Np5_scale

    print "Yield data (not correct if blinded) =", nAfterPreselectdata
    print "Yield gj before tight subtraction (not correct if blinded) =", nAfterPreselectgj

    ttreeName = LepPhotonAnalysis.DEFAULTTTREE
  

    print "Wlepnu_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(WlepnuFile_Np0.Get(ttreeName), 
                                        makeOutputName(WlepnuFileName_Np0),
                                        lepton,
                                        Wlepnu_Np0_scale)

    print
    print "Wlepnu_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(WlepnuFile_Np1.Get(ttreeName), 
                                        makeOutputName(WlepnuFileName_Np1),
                                        lepton,
                                        Wlepnu_Np1_scale)

    print
    print "Wlepnu_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(WlepnuFile_Np2.Get(ttreeName), 
                                        makeOutputName(WlepnuFileName_Np2),
                                        lepton,
                                        Wlepnu_Np2_scale)

    print
    print "Wlepnu_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(WlepnuFile_Np3.Get(ttreeName), 
                                        makeOutputName(WlepnuFileName_Np3),
                                        lepton,
                                        Wlepnu_Np3_scale)

    print
    print "Wlepnu_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(WlepnuFile_Np4.Get(ttreeName), 
                                        makeOutputName(WlepnuFileName_Np4),
                                        lepton,
                                        Wlepnu_Np4_scale)

    print
    print "Wlepnu_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(WlepnuFile_Np5.Get(ttreeName), 
                                        makeOutputName(WlepnuFileName_Np5),
                                        lepton,
                                        Wlepnu_Np5_scale)
    print
    print "Wtaunu_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(WtaunuFile_Np0.Get(ttreeName), 
                                        makeOutputName(WtaunuFileName_Np0),
                                        lepton,
                                        Wtaunu_Np0_scale)

    print
    print "Wtaunu_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(WtaunuFile_Np1.Get(ttreeName), 
                                        makeOutputName(WtaunuFileName_Np1),
                                        lepton,
                                        Wtaunu_Np1_scale)

    print
    print "Wtaunu_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(WtaunuFile_Np2.Get(ttreeName), 
                                        makeOutputName(WtaunuFileName_Np2),
                                        lepton,
                                        Wtaunu_Np2_scale)

    print
    print "Wtaunu_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(WtaunuFile_Np3.Get(ttreeName), 
                                        makeOutputName(WtaunuFileName_Np3),
                                        lepton,
                                        Wtaunu_Np3_scale)

    print
    print "Wtaunu_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(WtaunuFile_Np4.Get(ttreeName), 
                                        makeOutputName(WtaunuFileName_Np4),
                                        lepton,
                                        Wtaunu_Np4_scale)

    print
    print "Wtaunu_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(WtaunuFile_Np5.Get(ttreeName), 
                                        makeOutputName(WtaunuFileName_Np5),
                                        lepton,
                                        Wtaunu_Np5_scale)
    print
    print "Wgamma_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(WgammaFile_Np0.Get(ttreeName), 
                                        makeOutputName(WgammaFileName_Np0),
                                        lepton,
                                        Wgamma_Np0_scale)

    print
    print "Wgamma_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(WgammaFile_Np1.Get(ttreeName), 
                                        makeOutputName(WgammaFileName_Np1),
                                        lepton,
                                        Wgamma_Np1_scale)

    print
    print "Wgamma_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(WgammaFile_Np2.Get(ttreeName), 
                                        makeOutputName(WgammaFileName_Np2),
                                        lepton,
                                        Wgamma_Np2_scale)

    print
    print "Wgamma_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(WgammaFile_Np3.Get(ttreeName), 
                                        makeOutputName(WgammaFileName_Np3),
                                        lepton,
                                        Wgamma_Np3_scale)

    print
    print "Wgamma_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(WgammaFile_Np4.Get(ttreeName), 
                                        makeOutputName(WgammaFileName_Np4),
                                        lepton,
                                        Wgamma_Np4_scale)

    print
    print "Wgamma_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(WgammaFile_Np5.Get(ttreeName), 
                                        makeOutputName(WgammaFileName_Np5),
                                        lepton,
                                        Wgamma_Np5_scale)
    print

    print "ttbar:"
    LepPhotonAnalysis.LepPhotonAnalysis(ttbarFile.Get(ttreeName), 
                                        makeOutputName(ttbarFileName),
                                        lepton,
                                        ttbar_scale)

    print
    print "st_tchan_lepnu:"
    LepPhotonAnalysis.LepPhotonAnalysis(st_tchan_lepnuFile.Get(ttreeName), 
                                        makeOutputName(st_tchan_lepnuFileName),
                                        lepton,
                                        st_tchan_lepnu_scale)

    print
    print "st_tchan_taunu:"
    LepPhotonAnalysis.LepPhotonAnalysis(st_tchan_taunuFile.Get(ttreeName), 
                                        makeOutputName(st_tchan_taunuFileName),
                                        lepton,
                                        st_tchan_taunu_scale)

    print
    print "st_Wt:"
    LepPhotonAnalysis.LepPhotonAnalysis(st_WtFile.Get(ttreeName), 
                                        makeOutputName(st_WtFileName),
                                        lepton,
                                        st_Wt_scale)

    print

    print "WW:"
    LepPhotonAnalysis.LepPhotonAnalysis(WWFile.Get(ttreeName), 
                                        makeOutputName(WWFileName),
                                        lepton,
                                        WW_scale)

    print
    print "WZ:"
    LepPhotonAnalysis.LepPhotonAnalysis(WZFile.Get(ttreeName), 
                                        makeOutputName(WZFileName),
                                        lepton,
                                        WZ_scale)

    print
    print "ZZ:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZZFile.Get(ttreeName), 
                                        makeOutputName(ZZFileName),
                                        lepton,
                                        ZZ_scale)

    print


    print "Zleplepgamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZleplepgammaFile.Get(ttreeName), 
                                        makeOutputName(ZleplepgammaFileName),
                                        lepton,
                                        Zleplepgamma_scale)

    print

    print "Ztautaugamma:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZtautaugammaFile.Get(ttreeName), 
                                        makeOutputName(ZtautaugammaFileName),
                                        lepton,
                                        Ztautaugamma_scale)

    print


    print "Zleplep_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZleplepFile_Np0.Get(ttreeName), 
                                        makeOutputName(ZleplepFileName_Np0),
                                        lepton,
                                        Zleplep_Np0_scale)

    print
    print "Zleplep_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZleplepFile_Np1.Get(ttreeName), 
                                        makeOutputName(ZleplepFileName_Np1),
                                        lepton,
                                        Zleplep_Np1_scale)

    print
    print "Zleplep_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZleplepFile_Np2.Get(ttreeName), 
                                        makeOutputName(ZleplepFileName_Np2),
                                        lepton,
                                        Zleplep_Np2_scale)

    print
    print "Zleplep_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZleplepFile_Np3.Get(ttreeName), 
                                        makeOutputName(ZleplepFileName_Np3),
                                        lepton,
                                        Zleplep_Np3_scale)

    print
    print "Zleplep_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZleplepFile_Np4.Get(ttreeName), 
                                        makeOutputName(ZleplepFileName_Np4),
                                        lepton,
                                        Zleplep_Np4_scale)

    print
    print "Zleplep_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZleplepFile_Np5.Get(ttreeName), 
                                        makeOutputName(ZleplepFileName_Np5),
                                        lepton,
                                        Zleplep_Np5_scale)
    print
    print "Ztautau_Np0:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZtautauFile_Np0.Get(ttreeName), 
                                        makeOutputName(ZtautauFileName_Np0),
                                        lepton,
                                        Ztautau_Np0_scale)

    print
    print "Ztautau_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZtautauFile_Np1.Get(ttreeName), 
                                        makeOutputName(ZtautauFileName_Np1),
                                        lepton,
                                        Ztautau_Np1_scale)

    print
    print "Ztautau_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZtautauFile_Np2.Get(ttreeName), 
                                        makeOutputName(ZtautauFileName_Np2),
                                        lepton,
                                        Ztautau_Np2_scale)

    print
    print "Ztautau_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZtautauFile_Np3.Get(ttreeName), 
                                        makeOutputName(ZtautauFileName_Np3),
                                        lepton,
                                        Ztautau_Np3_scale)

    print
    print "Ztautau_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZtautauFile_Np4.Get(ttreeName), 
                                        makeOutputName(ZtautauFileName_Np4),
                                        lepton,
                                        Ztautau_Np4_scale)

    print
    print "Ztautau_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(ZtautauFile_Np5.Get(ttreeName), 
                                        makeOutputName(ZtautauFileName_Np5),
                                        lepton,
                                        Ztautau_Np5_scale)
    print

    print "gamma_Np1:"
    LepPhotonAnalysis.LepPhotonAnalysis(gammaFile_Np1.Get(ttreeName), 
                                        makeOutputName(gammaFileName_Np1),
                                        lepton,
                                        gamma_Np1_scale)

    print
    print "gamma_Np2:"
    LepPhotonAnalysis.LepPhotonAnalysis(gammaFile_Np2.Get(ttreeName), 
                                        makeOutputName(gammaFileName_Np2),
                                        lepton,
                                        gamma_Np2_scale)

    print
    print "gamma_Np3:"
    LepPhotonAnalysis.LepPhotonAnalysis(gammaFile_Np3.Get(ttreeName), 
                                        makeOutputName(gammaFileName_Np3),
                                        lepton,
                                        gamma_Np3_scale)

    print
    print "gamma_Np4:"
    LepPhotonAnalysis.LepPhotonAnalysis(gammaFile_Np4.Get(ttreeName), 
                                        makeOutputName(gammaFileName_Np4),
                                        lepton,
                                        gamma_Np4_scale)

    print
    print "gamma_Np5:"
    LepPhotonAnalysis.LepPhotonAnalysis(gammaFile_Np5.Get(ttreeName), 
                                        makeOutputName(gammaFileName_Np5),
                                        lepton,
                                        gamma_Np5_scale)
    print

    print "wino:"
    LepPhotonAnalysis.LepPhotonAnalysis(winoFile.Get(ttreeName), 
                                        makeOutputName(winoFileName),
                                        lepton,
                                        wino_scale)
    print

    print "data:"
    LepPhotonAnalysis.LepPhotonAnalysis(dataFile.Get(ttreeName), 
                                        makeOutputName(dataFileName),
                                        lepton,
                                        1.0)
    print

    print "gj:"
    LepPhotonAnalysis.LepPhotonAnalysis(gjFile.Get(ttreeName), 
                                        makeOutputName(gjFileName),
                                        lepton,
                                        1.0)
    print
    
if __name__ == "__main__":
    RunAnalysis(DEFAULTLEPTON)