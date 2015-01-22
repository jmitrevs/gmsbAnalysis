#! /usr/bin/env python

from __future__ import division

# code to make all the plots in a file

import sys
import os.path
import getopt
import math

import ROOT
ROOT.gROOT.SetBatch()
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

FILENAME_ELEFF = 'eeNoCrackHistHistOut.root'
#FILENAME_ELEFF = 'eeHistHistOut.root'

ELECTRON = 0
MUON = 1

# for SFs
NONE = 0
NOMINAL = 1
LOW = 2
HIGH = 3

GeV = 1000.0

ZMASS = 91.1876*GeV

numEventTypes = 46

DEFAULTTTREE = 'GammaLepton'
DEFAULTWEIGHT = 1.0
DEFAULT_LEPTON = ELECTRON

removeCrack = True
DELTAR_EL_PH = 0.7
DELTAR_MU_PH = 0.7
EL_MINV_WINDOW = 15*GeV

# removeCrack = False
# DELTAR_EL_PH = 0
# DELTAR_MU_PH = 0
# EL_MINV_WINDOW = 0*GeV

printAccepted = False

printSummary = True

# What plots should be made
NO_SEL = 0
PRESEL = 1
SRW = 2
WCR = 3
HMT = 4
QCD = 5
XR1 = 6  #obsolete
HMET = 7
WCR1 = 8
WCR2 = 9
HMTW = 10
HMETW = 11
HMTS = 12
HMETS = 13
SRS = 14

#DEFAULT_PLOTS = NO_SEL
DEFAULT_PLOTS = PRESEL

# For the ABCD method
NoABCD = 0
LL = 1
LT = 2
TL = 3
TT = 4
lT = 5  #loose, not necessarily anti-tight, and isolated
Tl = 6

# TTType (note all should be LEPJETS or DILEP):
ALL = 0
LEPJETS = 1
DILEP = 2

# ONLY STRONG
# use same ALL as for TTType
WEAK = 1
STRONG = 2

#uncertainty types
SYM_HESS = 0
ASYM_HESS = 1
ENS = 2

#Cuts

# - electron channel

EL_PHPTCUT = 125*GeV
EL_ELPTCUT = 20*GeV
EL_MT = 120*GeV

#SRS
EL_SRS_MET = 220*GeV
EL_SRS_HT = 0*GeV
EL_SRS_MEFF = 1000*GeV

#SRW
EL_SRW_MET = 120*GeV
EL_SRW_HTjet_MAX = 100*GeV
EL_SRW_BVETO = -1.0
#EL_SRW_BVETO = 0.3511 #80%
#EL_SRW_BVETO = 0.7892 #70%
#EL_SRW_BVETO = 0.9827 #60%

EL_QCD_MINV_WINDOW = 15*GeV

# tight (default)
EL_WCR_MET_MIN = 45*GeV
EL_WCR_MET_MAX = 100*GeV
EL_WCR_MT_MIN = 35*GeV
EL_WCR_MT_MAX = 90*GeV

EL_WCR1_HTjet_MAX = 100*GeV
EL_WCR2_HTjet_MIN = 100*GeV

# # loose
#EL_WCR_MET_MIN = 0*GeV
#EL_WCR_MET_MAX = 10000000*GeV
#EL_WCR_MT_MIN = 0*GeV
#EL_WCR_MT_MAX = 1000000*GeV
#EL_HMT_MET_MIN = 25*GeV

# # Wgamma selection
# EL_WCR_MET_MIN = 25*GeV
# EL_WCR_MET_MAX = 1000000*GeV
# EL_WCR_MT_MIN = 40*GeV
# EL_WCR_MT_MAX = 90000000*GeV
# EL_HMT_MET_MIN = 25*GeV

#This is also known as the HMT
EL_HMT_MET_MIN = 45*GeV
EL_HMT_MET_MAX = 100*GeV
EL_HMT_MT_MIN =  120*GeV

EL_HMTW_HTjet_MAX = 100*GeV
EL_HMTS_MEFF = 1000*GeV

EL_HMET_MT_MIN = 35*GeV
EL_HMET_MT_MAX = 90*GeV
EL_HMET_MET_MIN =  100*GeV

EL_HMETW_HTjet_MAX = 100*GeV
EL_HMETS_MEFF = 1000*GeV

EL_QCD_MET_MAX = 20*GeV
EL_QCD_MT_MAX = 20*GeV

# - muon channel

MU_PHPTCUT = 125*GeV
MU_MUPTCUT = 20*GeV
MU_MT = 120*GeV

MU_QCD_MINV_WINDOW = 0*GeV
MU_MINV_WINDOW = 15*GeV

#SRS
MU_SRS_MET = 220*GeV
MU_SRS_HT = 0*GeV
MU_SRS_MEFF = 1000*GeV

#SRW
MU_SRW_MET = 120*GeV
MU_SRW_HTjet_MAX = 100*GeV
MU_SRW_BVETO = -1.0
#MU_SRW_BVETO = 0.3511 #80%
#MU_SRW_BVETO = 0.7892 #70%
#MU_SRW_BVETO = 0.9827 #60%

# tight (default)
MU_WCR_MET_MIN = 45*GeV
MU_WCR_MET_MAX = 100*GeV
MU_WCR_MT_MIN = 35*GeV
MU_WCR_MT_MAX = 90*GeV

MU_WCR1_HTjet_MAX = 100*GeV
MU_WCR2_HTjet_MIN = 100*GeV

# # loose
# MU_WCR_MET_MIN = 25*GeV
# MU_WCR_MET_MAX = 80*GeV
# MU_WCR_MT_MIN = 25*GeV
# MU_WCR_MT_MAX = 90*GeV
#MU_HMT_MET_MIN = 25*GeV

# Wgamma
# MU_WCR_MET_MIN = 25*GeV
# MU_WCR_MET_MAX = 80000000*GeV
# MU_WCR_MT_MIN = 40*GeV
# MU_WCR_MT_MAX = 900000000*GeV
# MU_HMT_MET_MIN = 25*GeV

# # test for events
# MU_WCR_MET_MIN = 50*GeV
# MU_WCR_MET_MAX = 100*GeV
# MU_WCR_MT_MIN = 100*GeV
# MU_WCR_MT_MAX = 90000*GeV
# MU_HMT_MET_MIN = 25*GeV


MU_HMT_MET_MIN = 45*GeV
MU_HMT_MET_MAX = 100*GeV
MU_HMT_MT_MIN =  120*GeV

MU_HMTW_HTjet_MAX = 100*GeV
MU_HMTS_MEFF = 1000*GeV

MU_HMET_MT_MIN = 35*GeV
MU_HMET_MT_MAX = 90*GeV
MU_HMET_MET_MIN =  100*GeV

MU_HMETW_HTjet_MAX = 100*GeV
MU_HMETS_MEFF = 1000*GeV

MU_QCD_MET_MAX = 25*GeV
MU_QCD_MT_MAX = 25*GeV


VETO_SECOND_LEPTON = False
VETO_SECOND_SFLEPTON_MINV = False
VETO_TRTSA_PHOTON_E_BLAYER = False

MET_DEFAULT = 0
MET_PLUS = 1
MET_MINUS = 2
MET_MUON = 3
MET_FULL = 4
MET_ORIG = 5

#loose = 0xc5fc01
##loose = 0xf7fc01 # this is OK
##loose = 0xeffc01
#loose = 0xc5cc01
loose = 0xc5fc01
tight = 0xfffc01

bits = [0x020000, 0x080000, 0x100000] 
#bits = [0x20000] 

def isLoose(isEM):
    return (isEM & loose) == 0

def isTight(isEM): 
    return (isEM & tight) == 0

def isAntiTight(isEM):
    isL = isLoose(isEM)

    # if not isL:
    #     return False
    # fail = 0
    # for i in bits:
    #     if isEM & i:
    #         fail += 1
    # return fail > 0

    isT = isTight(isEM)
    return isL and not isT

def isIsolated(iso):
    return iso < 5*GeV

def isNotIsolated(iso):
    return iso > 5*GeV



def usage():
    print " "
    print "Usage: %s [options] inputFile.root" % sys.argv[0]    
    print "  -o | --outfile    : name of the output root file (default <inputFile>Hist.root)"
    print "  -l | --lepton     : which lepton (default: '%s') (or use -m or -e seperately)" % DEFAULT_LEPTON
    print "  -t | --ttree      : name of the TTree/TChain"
    print "  -w | --weight     : global weight"
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"


# measureEff is simple W tag and probe; numBackground is passed for iterative improvement.

def LepPhotonAnalysis(ttree, outfile, lepton, glWeight, filterPhotons = True, 
                      onlyStrong = ALL, 
                      measureFakeAndEff = False, 
                      numBkgTight = 0, scaleQCD = False,
                      applySF = NOMINAL,
                      plotsRegion = DEFAULT_PLOTS,
                      doABCD = NoABCD,
                      doAltABCD = False,
                      blind = False,
                      tttype = ALL,
                      qcdOtherRoot = "",
                      qcdOtherRootSimulate = "",
                      reweighAlpgen = False,
                      debug = False,
                      doTruth = False,
                      onlyOrigin = -1,
                      metType = MET_DEFAULT,
                      useWeights = True,
                      doPDFUnc = False,
                      PDFUncType = SYM_HESS,
                      nPDF = 25):

    if not (lepton == ELECTRON or lepton == MUON):
        print "ERROR: The lepton must be ELECTRON or MUON"
        return

    if metType != MET_DEFAULT:
        print "Using metType =",metType

    f = ROOT.TFile(outfile, 'RECREATE')


    mtBinMin = 0
    metBinMin = 0
    mtBinMax = 250
    metBinMax = 250
    mtBinExtMax = 500
    metBinExtMax = 500

    nBinsEta = 30
    nBinsPt = 50
    nBinsHT = 75
    nBinsmT = 50
    nBinsMET = 50

    binSizeExtMET = "10 GeV"
    binSizeExtmt = "10 GeV"
    binSizeMET = "5 GeV"
    binSizemt = "5 GeV"

    if plotsRegion == WCR:
        nBinsEta = 15
        nBinsPt = 25
        nBinsHT = 50
        nBinsMET = 12
        nBinsmT = 16
        mtBinMin = 20
        mtBinMax = 100
        metBinMin = 30
        metBinMax = 90
        mtBinExtMax = 320
        metBinExtMax = 300
        binSizeExtMET = "10 GeV"
        binSizeExtmt = "10 GeV"
        binSizeMET = "5 GeV"
        binSizemt = "5 GeV"
    elif plotsRegion == HMT:
        nBinsEta = 15
        nBinsPt = 25
        nBinsHT = 30
        nBinsMET = 18
        nBinsmT = 16
        mtBinMin = 40
        mtBinExtMax = 360
        metBinExtMax = 360
        binSizeExtMET = "20 GeV"
        binSizeExtmt = "20 GeV"
        mtBinMax = 200
        metBinMax = 180
        binSizeMET = "10 GeV"
        binSizemt = "10 GeV"
    elif plotsRegion == HMET:
        nBinsEta = 15
        nBinsPt = 25
        nBinsHT = 30
        nBinsMET = 18
        nBinsmT = 20
        metBinMin = 40
        mtBinExtMax = 400
        metBinExtMax = 400
        binSizeExtMET = "20 GeV"
        binSizeExtmt = "20 GeV"
        mtBinMax = 200
        metBinMax = 220
        binSizeMET = "10 GeV"
        binSizemt = "10 GeV"
    elif plotsRegion == SRW:
        nBinsEta = 10
        nBinsPt = 10
        nBinsHT = 10
        nBinsmT = 22
        nBinsMET = 22
        mtBinMin = 60
        metBinMin = 60
        binSizeExtMET = "20 GeV"
        binSizeExtmt = "20 GeV"
        mtBinMax = 280
        metBinMax = 280
        binSizeMET = "10 GeV"
        binSizemt = "10 GeV"


    ##########################
    # Create the histograms
    ##########################

    ROOT.TH1.SetDefaultSumw2()

    # First create the directories
    phdir = f.mkdir("Photon")
    eldir = f.mkdir("Electron")
    gldir = f.mkdir("Global")
    mudir = f.mkdir("Muon")
    jdir = f.mkdir("Jets")
    mdir = f.mkdir("MET")

    ######## phdir
    phdir.cd()

    h_ph_phi1 = ROOT.TH1F("ph_phi1","#phi of the leading photons;#phi_{reco};Events", 16, -math.pi, math.pi)
    h_ph_eta1 = ROOT.TH1F("ph_eta1","Psuedorapidity of the leading photons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_ph_pt1 = ROOT.TH1F("ph_pt1","Transverse momentum of the leading photons;p_{T} [GeV];Events", nBinsPt, 50, 300)
    h_ph_eta2 = ROOT.TH1F("ph_eta2","Psuedorapidity of the second photons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_ph_pt2 = ROOT.TH1F("ph_pt2","Transverse momentum of the second photons;p_{T} [GeV];Events", nBinsPt, 50, 300)

    h_ph_iso = ROOT.TH1F("ph_iso","The isolation energy of photons;Iso [GeV];Events", 25, -5.0, 20.0)

    # h_ph_ptB_unconv = ROOT.TH1F("ph_ptB_unconv","Transverse momentum of the unconverted Barrel photons;p_{T} [GeV];Events", 500, 0, 500)
    # h_ph_ptEC_unconv = ROOT.TH1F("ph_ptEC_unconv","Transverse momentum of the unconverted EC photons;p_{T} [GeV];Events", 500, 0, 500)

    # h_ph_ptB_conv = ROOT.TH1F("ph_ptB_conv","Transverse momentum of the converted Barrel photons;p_{T} [GeV];Events", 500, 0, 500)
    # h_ph_ptEC_conv = ROOT.TH1F("ph_ptEC_conv","Transverse momentum of the converted EC photons;p_{T} [GeV];Events", 500, 0, 500)
    h_ph_el_minv = ROOT.TH1F("ph_el_minv", "The invariant mass of the leading photon and electron;M_{inv} [GeV];Events", 100, 0, 500)
    h_ph_mu_minv = ROOT.TH1F("ph_mu_minv", "The invariant mass of the leading photon and muon;M_{inv} [GeV];Events", 100, 0, 500)
    h_numPh = ROOT.TH1F("numPh", "The number of photons that pass cuts;N_{photons};Events", 9, -0.5, 8.5)

    h_ph_lep_deltaR = ROOT.TH1F("ph_lep_deltaR", "The delta-R beteween the lepton and the photon;#DeltaR(l,#gamma);Events", 25, 0, 5)
    h_ph_lep_deltaPhi = ROOT.TH1F("ph_lep_deltaPhi", "The delta-Phi beteween the lepton and the photon;#Delta#phi(l,#gamma);Events", 30, -math.pi, math.pi)

    h_ph_ConvType = ROOT.TH1F("ph_ConvType", "The number of conversion tracks;N_{tracks};Events", 3, -0.5, 2.5)
    h_ph_numSi0 = ROOT.TH1F("ph_numSi0", "The number of Si hits in conversion track 0;N_{hits};Events", 30, -9.5, 20.5)
    h_ph_numSi1 = ROOT.TH1F("ph_numSi1", "The number of Si hits in conversion track 1;N_{hits};Events", 30, -9.5, 20.5)
    h_ph_numPix0 = ROOT.TH1F("ph_numPix0", "The number of PIX hits in conversion track 0;N_{hits};Events", 30, -9.5, 20.5)
    h_ph_numPix1 = ROOT.TH1F("ph_numPix1", "The number of PIX hits in conversion track 1;N_{hits};Events", 30, -9.5, 20.5)
    h_ph_numSiEl = ROOT.TH1F("ph_numSiEl", "The number of Si hits in electron track;N_{hits};Events", 30, -9.5, 20.5)
    h_ph_numPixEl = ROOT.TH1F("ph_numPixEl", "The number of PIX hits in electron track;N_{hits};Events", 30, -9.5, 20.5)
    h_ph_numBEl = ROOT.TH1F("ph_numBEl", "The number of PIX hits in electron track;N_{hits};Events", 30, -9.5, 20.5)
    h_ph_rejectStudies = ROOT.TH1F("ph_rejectStudies", "1 = Fail with BL, 2 = Fail with PIX;Events", 30, -9.5, 20.5)

    h_ph_truth = ROOT.TH1F("ph_truth", "The truth classication", 25, 0, 25);
    h_ph_origin = ROOT.TH1F("ph_origin", "The truth origin", 50, 0, 50);

    ######## mudir
    mudir.cd()
    h_mu_eta1_phi1 = ROOT.TH2F("mu_eta1_phi1","#eta vs. #phi of the leading muons;#eta_{reco};#phi_{reco};Events", 20, -3, 3, 16, -math.pi, math.pi)
    h_mu_phi1 = ROOT.TH1F("mu_phi1","#phi of the leading muons;#phi_{reco};Events", 16, -math.pi, math.pi)
    h_mu_eta1 = ROOT.TH1F("mu_eta1","Psuedorapidity of the leading muons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_mu_pt1 = ROOT.TH1F("mu_pt1","Transverse momentum of the leading muons;p_{T} [GeV];Events", nBinsPt, 0, 250)
    h_mu_eta2 = ROOT.TH1F("mu_eta2","Psuedorapidity of the second muons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_mu_pt2 = ROOT.TH1F("mu_pt2","Transverse momentum of the second muons;p_{T} [GeV];Events", nBinsPt, 0, 250)
    h_numMu = ROOT.TH1F("numMu", "The number of muons that pass cuts;N_{muons};Events", 9, -0.5, 8.5)
    h_mu_mInv = ROOT.TH1F("mu_mInv", "The invariant mass of leading muons;m_{inv} [GeV];Events", 120, 0, 120)

    ######## eldir
    eldir.cd()
    h_el_phi1 = ROOT.TH1F("el_phi1","#phi of the leading electrons;#phi_{reco};Events", 16, -math.pi, math.pi)
    h_el_eta1 = ROOT.TH1F("el_eta1","Psuedorapidity of the leading electrons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_el_pt1 = ROOT.TH1F("el_pt1","Transverse momentum of the leading electrons;p_{T} [GeV];Events", nBinsPt, 0, 250)
    h_el_eta2 = ROOT.TH1F("el_eta2","Psuedorapidity of the second electrons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_el_pt2 = ROOT.TH1F("el_pt2","Transverse momentum of the second electrons;p_{T} [GeV];Events", nBinsPt, 0, 250)
    h_numEl = ROOT.TH1F("numEl", "The number of electrons that pass cuts;N_{electrons};Events", 9, -0.5, 8.5)
    h_el_mInv = ROOT.TH1F("el_mInv", "The invariant mass of leading electrons;m_{inv} [GeV];Events", 120, 0, 120)

    ######## jdir
    jdir.cd()
    h_numJets = ROOT.TH1F("numJets", "The number of jets that pass cuts;N_{jets};Events", 9, -0.5, 8.5)

    ######## MET
    mdir.cd()
    h_met = ROOT.TH1F("met", "The MET distribution;E_{T}^{miss} [GeV];Events / " + binSizeMET, nBinsMET, metBinMin, metBinMax)
    # h_met0J = ROOT.TH1F("met0J", "The MET distribution of events with zero jets;E_{T}^{miss} [GeV];Events", 500, 0, 500)
    # h_met1J = ROOT.TH1F("met1J", "The MET distribution of events with one jet;E_{T}^{miss} [GeV];Events", 500, 0, 500)
    # h_met2J = ROOT.TH1F("met2J", "The MET distribution of events with two jets;E_{T}^{miss} [GeV];Events", 500, 0, 500)
    # h_met3J = ROOT.TH1F("met3J", "The MET distribution of events with three jets;E_{T}^{miss} [GeV];Events", 500, 0, 500)
    # h_met4J = ROOT.TH1F("met4J", "The MET distribution of events with four jets;E_{T}^{miss} [GeV];Events", 500, 0, 500)

    h_metExtended = ROOT.TH1F("metExtended", "The MET distribution;E_{T}^{miss} [GeV];Events / " + binSizeExtMET, nBinsMET, metBinMin, metBinExtMax)
    h_metShort = ROOT.TH1F("metShort", "The MET distribution;E_{T}^{miss} [GeV];Events", 20, 0, 100)

    h_deltaPhiPhMETvsMET = ROOT.TH2F("deltaPhiPhMETvsMET", 
						  "The DeltaPhi(Photon,MET) distribution vs. MET;#Delta#phi;E_{T}^{miss} [GeV]",
						  50, 0, math.pi, 16, 0, 300)

    h_deltaPhiElMETvsMET = ROOT.TH2F("deltaPhiElMETvsMET", 
						  "The DeltaPhi(Electron,MET) distribution vs. MET;#Delta#phi;E_{T}^{miss} [GeV]",
						  50, 0, math.pi, 16, 0, 300)

    h_deltaPhiMuMETvsMET = ROOT.TH2F("deltaPhiMuMETvsMET", 
						  "The DeltaPhi(Muon,MET) distribution vs. MET;#Delta#phi;E_{T}^{miss} [GeV]",
						  50, 0, math.pi, 16, 0, 300)

    h_deltaPhiMuMET = ROOT.TH1F("deltaPhiMuMET", 
                                "The DeltaPhi(Muon,MET) distribution;#Delta#phi(l,MET);Events", 30, -math.pi, math.pi)
    ############ gldir
    gldir.cd()
    h_HT = ROOT.TH1F("HT", "The H_{T} distribution;H_{T} [GeV];Events", nBinsHT, 0, 1500)
    h_mTel = ROOT.TH1F("mTel", "The m_{T} distribution;m_{T} [GeV];Events / " + binSizemt, nBinsmT, mtBinMin, mtBinMax)
    h_mTmu = ROOT.TH1F("mTmu", "The m_{T} distribution;m_{T} [GeV];Events / " + binSizemt, nBinsmT, mtBinMin, mtBinMax)
    h_mTelShort = ROOT.TH1F("mTelShort", "The m_{T} distribution;m_{T} [GeV];Events", 20, 0, 100)
    h_mTmuShort = ROOT.TH1F("mTmuShort", "The m_{T} distribution;m_{T} [GeV];Events", 20, 0, 100)
    h_mTelExtended = ROOT.TH1F("mTelExtended", "The m_{T} distribution;m_{T} [GeV];Events / " + binSizeExtmt, nBinsmT, mtBinMin, mtBinExtMax)
    h_mTmuExtended = ROOT.TH1F("mTmuExtended", "The m_{T} distribution;m_{T} [GeV];Events / " + binSizeExtmt, nBinsmT, mtBinMin, mtBinExtMax)
    h_meff = ROOT.TH1F("meff", "The m_{eff} distribution;m_{eff} [GeV];Events", nBinsHT, 0, 1500)

    h_mTelvsMET = ROOT.TH2F("mTelvsMET", "m_{T} vs. MET;E_{T}^{miss} [GeV];m_{T} [GeV]",
                            50, 0, 500, 50, 0, 500)
    h_mTmuvsMET = ROOT.TH2F("mTmuvsMET", "m_{T} vs. MET;E_{T}^{miss} [GeV];m_{T} [GeV]",
                            50, 0, 500, 50, 0, 500)

    h_eventType = ROOT.TH1F("eventType", "The event type, based on truth;event type;Events", 
					 numEventTypes, 0, numEventTypes);

    # These are reco values
    h_Wpt = ROOT.TH1F("Wpt","Transverse momentum of the leading electron + E_{T}^{miss};p_{T} [GeV];Events", nBinsPt, 0, 350)
    h_WptAlt = ROOT.TH1F("WptAlt","Transverse momentum of the leading electron + photon + E_{T}^{miss};p_{T} [GeV];Events", nBinsPt, 0, 350)

    ######## go back to root
    f.cd()

    ######## initialize counts

    nPRESEL = ROOT.TH1F("nPRESEL", "Number of events in the PRESEL", 1, 0, 1);
    nWCR = ROOT.TH1F("nWCR", "Number of events in the WCR", 1, 0, 1);
    nWCR1 = ROOT.TH1F("nWCR1", "Number of events in the WCR1", 1, 0, 1);
    nWCR2 = ROOT.TH1F("nWCR2", "Number of events in the WCR2", 1, 0, 1);
    nHMT = ROOT.TH1F("nHMT", "Number of events in the HMT", 1, 0, 1);
    nHMTW = ROOT.TH1F("nHMTW", "Number of events in the HMTW", 1, 0, 1);
    nHMTS = ROOT.TH1F("nHMTS", "Number of events in the HMTS", 1, 0, 1);
    nQCD = ROOT.TH1F("nQCD", "Number of events in the QCD", 1, 0, 1);
    nSRS = ROOT.TH1F("nSRS", "Number of events in the SRS", 1, 0, 1);
    nSRW = ROOT.TH1F("nSRW", "Number of events in the SRW", 1, 0, 1);
    nHMET = ROOT.TH1F("nHMET", "Number of events in the HMET", 1, 0, 1);
    nHMETW = ROOT.TH1F("nHMETW", "Number of events in the HMETW", 1, 0, 1);
    nHMETS = ROOT.TH1F("nHMETS", "Number of events in the HMETS", 1, 0, 1);

    if doPDFUnc:
        nWCRp = ROOT.TH1F("nWCRp", "Number of events in the WCR", nPDF, 0, nPDF);
        nWCR1p = ROOT.TH1F("nWCR1p", "Number of events in the WCR1", nPDF, 0, nPDF);
        nWCR2p = ROOT.TH1F("nWCR2p", "Number of events in the WCR2", nPDF, 0, nPDF);
        nHMTp = ROOT.TH1F("nHMTp", "Number of events in the HMT", nPDF, 0, nPDF);
        nHMTWp = ROOT.TH1F("nHMTWp", "Number of events in the HMTW", nPDF, 0, nPDF);
        nHMTSp = ROOT.TH1F("nHMTSp", "Number of events in the HMTS", nPDF, 0, nPDF);
        nSRSp = ROOT.TH1F("nSRSp", "Number of events in the SRS", nPDF, 0, nPDF);
        nSRWp = ROOT.TH1F("nSRWp", "Number of events in the SRW", nPDF, 0, nPDF);
        nHMETp = ROOT.TH1F("nHMETp", "Number of events in the HMET", nPDF, 0, nPDF);
        nHMETWp = ROOT.TH1F("nHMETWp", "Number of events in the HMETW", nPDF, 0, nPDF);
        nHMETSp = ROOT.TH1F("nHMETSp", "Number of events in the HMETS", nPDF, 0, nPDF);

        nWCRm = ROOT.TH1F("nWCRm", "Number of events in the WCR", nPDF, 0, nPDF);
        nWCR1m = ROOT.TH1F("nWCR1m", "Number of events in the WCR1", nPDF, 0, nPDF);
        nWCR2m = ROOT.TH1F("nWCR2m", "Number of events in the WCR2", nPDF, 0, nPDF);
        nHMTm = ROOT.TH1F("nHMTm", "Number of events in the HMT", nPDF, 0, nPDF);
        nHMTWm = ROOT.TH1F("nHMTWm", "Number of events in the HMTW", nPDF, 0, nPDF);
        nHMTSm = ROOT.TH1F("nHMTSm", "Number of events in the HMTS", nPDF, 0, nPDF);
        nSRSm = ROOT.TH1F("nSRSm", "Number of events in the SRS", nPDF, 0, nPDF);
        nSRWm = ROOT.TH1F("nSRWm", "Number of events in the SRW", nPDF, 0, nPDF);
        nHMETm = ROOT.TH1F("nHMETm", "Number of events in the HMET", nPDF, 0, nPDF);
        nHMETWm = ROOT.TH1F("nHMETWm", "Number of events in the HMETW", nPDF, 0, nPDF);
        nHMETSm = ROOT.TH1F("nHMETSm", "Number of events in the HMETS", nPDF, 0, nPDF);
        

    if measureFakeAndEff:
        nWCRTight = ROOT.TH1F("nWCRTight", "Number of tight events in the WCR", 1, 0, 1);
        nQCDTight = ROOT.TH1F("nQCDTight", "Number of tight events in the QCD", 1, 0, 1);

    for ev in ttree:
        # lets apply the cuts
        # double-check quality
        if ev.numPh == 0 or (ev.numEl == 0 and lepton == ELECTRON) or (ev.numMu == 0 and lepton == MUON):
            print "ERROR: event is malformed:", ev.numPh, ev.numEl, ev.numMu, lepton
            sys.exit(1)
            #continue

        if debug: print "Analizing event with Run =", ev.Run, ", Event =", ev.Event


        if filterPhotons and ev.numTruthPh > 0:
            if debug: print "fail truth photon"
            continue

        if debug: print "  pass filterPhotons"

        if metType == MET_DEFAULT:
            metx = ev.Metx
            mety = ev.Mety
            # metx = ev.Metx_noMuon + ev.Metx_MuonBoy - ev.Metx_RefTrack 
            # mety = ev.Mety_noMuon + ev.Mety_MuonBoy - ev.Mety_RefTrack 
        elif metType == MET_PLUS:
            metx = ev.MetxPlus_noMuon + ev.Metx_MuonBoy - ev.Metx_RefTrack 
            mety = ev.MetyPlus_noMuon + ev.Mety_MuonBoy - ev.Mety_RefTrack 
        elif metType == MET_MINUS:
            metx = ev.MetxMinus_noMuon + ev.Metx_MuonBoy - ev.Metx_RefTrack 
            mety = ev.MetyMinus_noMuon + ev.Mety_MuonBoy - ev.Mety_RefTrack 
        elif metType == MET_MUON:
            metx = ev.Metx_noMuon + ev.Metx_muon_smear - ev.Metx_RefTrack 
            mety = ev.Mety_noMuon + ev.Mety_muon_smear - ev.Mety_RefTrack 
        elif metType == MET_FULL:
            metx = ev.Metx_full_noMuon + ev.Metx_MuonBoy - ev.Metx_RefTrack 
            mety = ev.Mety_full_noMuon + ev.Mety_MuonBoy - ev.Mety_RefTrack
        elif metType == MET_ORIG:
            metx = ev.MetxOrig
            mety = ev.MetyOrig
        else:
            print >> sys.stderr, "Have an invalid metType =", metType
            sys.exit(1)


        met = math.hypot(metx, mety)

        met4vec = ROOT.TLorentzVector(metx,mety,0,0)

        #print "MET =", met, "lepton =", lepton, "ev.PhotonPt[0] = ", ev.PhotonPt[0]
        #print "weight =", ev.Weight * glWeight

        weight = ev.Weight * glWeight


        weight *= ev.PileupWeight
        #try:
        #    weight *= ev.PileupWeight
        #except AttributeError:
        #    pass


        if applySF == NOMINAL:
            if lepton == ELECTRON:
                weight *= ev.PhotonSF * ev.ElectronSF
            else:
                weight *= ev.PhotonSF * ev.MuonSF
        elif applySF == LOW:
            if lepton == ELECTRON:
                weight *= ev.PhotonSF * (ev.ElectronSF - ev.ElectronSFUnc)
            else:
                weight *= ev.PhotonSF * (ev.MuonSF - ev.MuonSFUnc)
        elif applySF == HIGH:
            if lepton == ELECTRON:
                weight *= ev.PhotonSF * (ev.ElectronSF + ev.ElectronSFUnc)
            else:
                weight *= ev.PhotonSF * (ev.MuonSF + ev.MuonSFUnc)


        if reweighAlpgen:
            if ev.Wpt < -9999999.0:
                print >> sys.stderr, "Have an invalid Wpt"
            elif ev.Wpt < 10*GeV:
                weight *= 0.90
            elif ev.Wpt < 20*GeV:
                weight *= 1.05
            elif ev.Wpt < 30*GeV:
                weight *= 1.13
            elif ev.Wpt < 40*GeV:
                weight *= 1.15
            elif ev.Wpt < 250*GeV:
                weight *= math.exp(0.2165 - 0.0000022075*ev.Wpt)
            else:
                weight *= 0.72

        if onlyStrong == STRONG and not ev.isStrong:
            print "fail only strong"
            continue

        if onlyStrong == WEAK and ev.isStrong:
            print "fail only weak"
            continue
        if debug: print "  pass onlyStrong"


        lepIndex = 0

        if removeCrack and lepton == ELECTRON:
            for i in range(ev.numEl):
                if not (1.37 < abs(ev.ElectronEta2[i]) < 1.52):
                    lepIndex = i
                    break
            else:
                #print "*** electron only in crack ***"
                continue

        # if lepIndex != 0:
        #     print "***WARNING***"


        if tttype != ALL:
            if lepton == MUON:
                if tttype == LEPJETS and ev.eventType not in (11, 13, 9):
                    continue
                elif tttype == DILEP and ev.eventType in (11, 13, 9):
                    continue
            else:
                if tttype == LEPJETS and ev.eventType not in (8, 13):
                    continue
                elif tttype == DILEP and ev.eventType in (8, 13):
                    continue

        if debug: print "  pass tttype"

        photonIndex = 0
        if doABCD:
            #print "doABCD =",doABCD
            foundLL = False
            foundTL = False
            foundLT = False
            foundTT = False
            foundlT = False
            foundTl = False
            indexLL = -1
            indexTL = -1
            indexLT = -1
            indexTT = -1
            indexlT = -1
            indexTl = -1
            for i in range(ev.numPh):
                if ev.PhotonTight[i]:
                    foundTl = True
                    if indexTl < 0:
                        indexTl = i
                if not doAltABCD:
                    if ev.PhotonAlt[i]:
                        foundlT = True
                        if indexlT < 0:
                            indexlT = i
                    if ev.PhotonTight[i] and ev.PhotonAlt[i]:
                        foundTT = True
                        if indexTT < 0:
                            indexTT = i
                    if not ev.PhotonTight[i] and ev.PhotonAlt[i]:
                        foundLT = True
                        if indexLT < 0:
                            indexLT = i
                    if ev.PhotonTight[i] and not ev.PhotonAlt[i]:
                        foundTL = True
                        if indexTL < 0:
                            indexTL = i
                    if not ev.PhotonTight[i] and not ev.PhotonAlt[i]:
                        foundLL = True
                        if indexLL < 0:
                            indexLL = i
                else:
                    isem = ev.PhotonIsEM[i] & 0x0FFFFFFF
                    iso = ev.PhotonEtcone20[i]
                    if isIsolated(iso):
                        foundlT = True
                        if indexlT < 0:
                            indexlT = i
                    if ev.PhotonTight[i] and isIsolated(iso):
                        foundTT = True
                        if indexTT < 0:
                            indexTT = i
                    if isAntiTight(isem) and isIsolated(iso):
                        foundLT = True
                        if indexLT < 0:
                            indexLT = i
                    if ev.PhotonTight[i] and isNotIsolated(iso):
                        foundTL = True
                        if indexTL < 0:
                            indexTL = i
                    if isAntiTight(isem) and isNotIsolated(iso):
                        foundLL = True
                        if indexLL < 0:
                            indexLL = i

            if debug: print "  foundTT=", foundTT, "foundTL=", foundTL, "foundLT=", foundLT, "foundLL=", foundLL

            #print "doABCD=", doABCD, "foundTT=", foundTT

            # if foundLL and foundLT:
            #     print "Found both LL and LT"
            #     continue
            # if foundLL and foundTL:
            #     print "Found both LL and TL"
            #     continue
            # if foundLL and foundTT:
            #     print "Found both LL and TT"
            #     continue
            # if foundLT and foundTL:
            #     print "Found both LT and TL"
            #     continue
            # if foundLT and foundTT:
            #     print "Found both LT and TT"
            #     continue
            # if foundTL and foundTT:
            #     print "Found both TL and TT"
            #     continue

            # precedence
            if foundTT:
                foundTL = False
                foundLT = False
                foundLL = False
            elif foundTL:
                foundLT = False
                foundLL = False
            elif foundLT:
                foundLL = False

            if doABCD == TT:
                if not foundTT:
                    continue
                else:
                    photonIndex = indexTT
            if doABCD == TL:
                if not foundTL:
                    continue
                else:
                    photonIndex = indexTL
            if doABCD == LT:
                if not foundLT:
                    continue
                else:
                    photonIndex = indexLT
            if doABCD == LL:
                if not foundLL:
                    continue
                else:
                    photonIndex = indexLL

            if doABCD == lT:
                if not foundlT:
                    continue
                else:
                    photonIndex = indexlT

            if doABCD == Tl:
                if not foundTl:
                    continue
                else:
                    photonIndex = indexTl

        if debug: print "  passed ABCD, photonIndex =", photonIndex

        if onlyOrigin >= 0:
            if ev.PhotonOrigin[photonIndex] != onlyOrigin:
                print '** fail onlyOrigin **'
                continue


        photon = ROOT.TLorentzVector()
        photon.SetPtEtaPhiM(ev.PhotonPt[photonIndex], ev.PhotonEta[photonIndex], ev.PhotonPhi[photonIndex], 0.0)
        if lepton == ELECTRON:
            electron = ROOT.TLorentzVector()
            electron.SetPtEtaPhiM(ev.ElectronPt[lepIndex], ev.ElectronEta[lepIndex], ev.ElectronPhi[lepIndex], 0.0)


        iso = -999.0
        try:
            iso = ev.PhotonEtcone20[photonIndex]
        except AttributeError:
            pass



        if plotsRegion != NO_SEL:

            # first the basic lepton and photon selection (but not MET and mT):
            if ((lepton == ELECTRON and
                 (ev.PhotonPt[photonIndex] < EL_PHPTCUT or #abs(ev.PhotonEta[photonIndex]) > EL_PHETACUT or
                  ev.ElectronPt[lepIndex] < EL_ELPTCUT)) or #abs(ev.ElectronEta[lepIndex]) > EL_ELETACUT)) or
                (lepton == MUON and
                 (ev.PhotonPt[photonIndex] < MU_PHPTCUT or #abs(ev.PhotonEta[photonIndex]) > MU_PHETACUT or
                  ev.MuonPt[lepIndex] < MU_MUPTCUT))): # or abs(ev.MuonEta[lepIndex]) > MU_MUETACUT))):
                print '** fail basic selection **', lepton, ev.PhotonPt[photonIndex], ev.PhotonEta[photonIndex], ev.ElectronPt[lepIndex], ev.ElectronEta[lepIndex]
                continue

            # veto second lepton or Z window cut
            if lepton == ELECTRON and EL_MINV_WINDOW != 0:
                if photonIndex == 0 and lepIndex == 0:
                    minv = ev.PhElMinv
                else:
                    elph = electron + photon
                    minv = elph.M()
                    #print "**minv =", minv
                if ZMASS - EL_MINV_WINDOW < minv < ZMASS + EL_MINV_WINDOW:
                    #print '** fail electron z **'
                    continue

            if VETO_SECOND_LEPTON and ev.numMu + ev.numEl > 1:
                print '** fail veto second electron **'
                continue
            # elif (lepton == ELECTRON and ev.numMu > 0 or
            #       lepton == MUON and ev.numEl > 0):
            #     print '** fail simple orthogonal channels **'
            #     continue

            if (VETO_SECOND_SFLEPTON_MINV and
                ((lepton == ELECTRON and ZMASS - EL_MINV_WINDOW < ev.ElMinv < ZMASS + EL_MINV_WINDOW) or
                 (lepton == MUON and ZMASS - MU_MINV_WINDOW < ev.MuMinv < ZMASS + MU_MINV_WINDOW))):
                print '** fail second sflepon veto **'
                continue

            if (VETO_TRTSA_PHOTON_E_BLAYER and # ev.numPh == 1 and
                ev.PhotonConvType[photonIndex] == 1 and ev.PhotonNumSi0[photonIndex] == 0 and
                ev.PhotonNumBEl[photonIndex]):
                print '** fail trtsa photon veto **'
                continue

        if debug: print "  passed some presel"

        if lepton == ELECTRON:
            el_ph_deltaR = photon.DeltaR(electron)
            el_ph_deltaPhi = photon.DeltaPhi(electron)
            if plotsRegion != NO_SEL and el_ph_deltaR < DELTAR_EL_PH:
                #print '** fail deltar photon lepton veto **'
                continue
        else:
            muon = ROOT.TLorentzVector()
            muon.SetPtEtaPhiM(ev.MuonPt[lepIndex], ev.MuonEta[lepIndex], ev.MuonPhi[lepIndex], 105.65836668)
            mu_ph_deltaR = photon.DeltaR(muon)
            mu_ph_deltaPhi = photon.DeltaPhi(muon)
            if plotsRegion != NO_SEL and mu_ph_deltaR < DELTAR_MU_PH:
                #print '** fail deltar photon lepton veto **'
                continue

            # if abs(mu_ph_deltaPhi) < 2.93:
            #     continue

        if debug: print "  passed lep-ph deltaR"

        # scale the gj sampe to represent QCD
        if scaleQCD:
            if lepton == ELECTRON:
                weight *= Nqcd(1, ev.ElectronTight[lepIndex], ev.ElectronEta[lepIndex], lepton)
            else:
                weight *= Nqcd(1, ev.MuonTight[lepIndex], ev.MuonEta[lepIndex], lepton)


        if metType == MET_DEFAULT:
            if lepton == ELECTRON:
                if lepIndex != 0:
                    mt = mT(ev.ElectronPt[lepIndex], ev.ElectronPhi[lepIndex], ev.Metx, ev.Mety)
                else:
                    mt = ev.mTel
            else:
                mt = ev.mTmu
        else:
            if lepton == ELECTRON:
                mt = mT(ev.ElectronPt[lepIndex], ev.ElectronPhi[lepIndex], metx, mety)
            else:
                mt = mT(ev.MuonPt[lepIndex], ev.MuonPhi[lepIndex], metx, mety)


        #these are reco values
        if lepton == ELECTRON:
            W = met4vec + electron
        else:
            W = met4vec + muon
        Walt = W+photon


        # for debugging
        if useWeights != True:
            weight = 1



            
        # if lepton == MUON and abs(ev.deltaPhiMuMET) > 2.9:
        #     continue
        #     pass

        # now plots that should be made before MET and mT cuts
        h_mTelvsMET.Fill(met/GeV, mt/GeV, weight)
        h_mTmuvsMET.Fill(met/GeV, mt/GeV, weight)

        inQCD = False
        inWCR = False
        inWCR1 = False
        inWCR2 = False
        inHMT = False
        inHMTW = False
        inHMTS = False
        inHMET = False
        inHMETW = False
        inHMETS = False
        inSRS = False
        inSRW = False
            
        if debug: print "  met =", met, "mTmu =", mt, "mTel =", mt

        #nPRESEL.Fill(0)
        nPRESEL.Fill(0, weight)

        # do CR counts

        # if not passBVeto:
        #     continue

        if lepton == ELECTRON:
            if met < EL_QCD_MET_MAX and mt < EL_QCD_MT_MAX:
                if (ev.PhElMinv < ZMASS - EL_QCD_MINV_WINDOW or
                    ev.PhElMinv > ZMASS + EL_QCD_MINV_WINDOW):
                    # in QCD CR
                    inQCD = True
                    nQCD.Fill(0, weight)
                    if measureFakeAndEff and ev.ElectronTight[lepIndex]:
                        nQCDTight.Fill(0, weight)

            if (EL_WCR_MET_MIN < met < EL_WCR_MET_MAX and
                  EL_WCR_MT_MIN < mt < EL_WCR_MT_MAX):
                inWCR = True
                nWCR.Fill(0, weight)

                if doPDFUnc and PDFUncType == SYM_HESS:
                    SymHess(nWCRp, nWCRm, weight, ev.PDFWeights, nPDF)

                if measureFakeAndEff and ev.ElectronTight[lepIndex]:
                    nWCRTight.Fill(0, weight)

                if ev.HTjet < EL_WCR1_HTjet_MAX:
                    inWCR1 = True
                    nWCR1.Fill(0, weight)
                    if doPDFUnc and PDFUncType == SYM_HESS:
                        SymHess(nWCR1p, nWCR1m, weight, ev.PDFWeights, nPDF)
                   
                if ev.HTjet > EL_WCR2_HTjet_MIN:
                    inWCR2 = True
                    nWCR2.Fill(0, weight)
                    if doPDFUnc and PDFUncType == SYM_HESS:
                        SymHess(nWCR2p, nWCR2m, weight, ev.PDFWeights, nPDF)

            if (EL_HMT_MET_MIN < met < EL_HMT_MET_MAX and
                  EL_HMT_MT_MIN < mt):
                nHMT.Fill(0, weight)
                inHMT = True
                if ev.HTjet < EL_HMTW_HTjet_MAX:
                    inHMTW = True
                    nHMTW.Fill(0, weight)
                    
                if ev.meff > EL_HMTS_MEFF:
                    inHMTS = True
                    nHMTS.Fill(0, weight)

            if (EL_HMET_MET_MIN < met and
                EL_HMET_MT_MIN < mt < EL_HMET_MT_MAX):
                inHMET = True
                nHMET.Fill(0, weight)
                if ev.HTjet < EL_HMETW_HTjet_MAX:
                    inHMETW = True
                    nHMETW.Fill(0, weight)
                    
                if ev.meff > EL_HMETS_MEFF:
                    inHMETS = True
                    nHMETS.Fill(0, weight)

            if mt > EL_MT and met > EL_SRW_MET and (EL_SRW_HTjet_MAX < 0 or ev.HTjet < EL_SRW_HTjet_MAX):
                passBVeto = True
                if EL_SRW_BVETO > 0.0:
                    for i in range(ev.numJets):
                        if ev.JetMV1[i] > BVETO:
                            passBVeto = False
                if passBVeto:
                    inSRW = True
                    nSRW.Fill(0, weight)

                    if doPDFUnc and PDFUncType == SYM_HESS:
                        SymHess(nSRWp, nSRWm, weight, ev.PDFWeights, nPDF)
                
            if mt > EL_MT and met > EL_SRS_MET and ev.HT > EL_SRS_HT and ev.meff > EL_SRS_MEFF:
                inSRS = True
                nSRS.Fill(0, weight)

                if doPDFUnc and PDFUncType == SYM_HESS:
                    SymHess(nSRSp, nSRSm, weight, ev.PDFWeights, nPDF)

        else:
            if met < MU_QCD_MET_MAX and mt < MU_QCD_MT_MAX:
                if (ev.PhElMinv < ZMASS - MU_QCD_MINV_WINDOW or
                    ev.PhElMinv > ZMASS + MU_QCD_MINV_WINDOW):
                    inQCD = True
                    nQCD.Fill(0, weight)
                    if measureFakeAndEff and ev.MuonTight[lepIndex]:
                        nQCDTight.Fill(0, weight)
            if (MU_WCR_MET_MIN < met < MU_WCR_MET_MAX and
                  MU_WCR_MT_MIN < mt < MU_WCR_MT_MAX):
                inWCR = True
                nWCR.Fill(0, weight)
                if measureFakeAndEff and ev.MuonTight[lepIndex]:
                    nWCRTight.Fill(0, weight)
                if ev.HTjet < MU_WCR1_HTjet_MAX:
                    inWCR1 = True
                    nWCR1.Fill(0, weight)
                    
                if ev.HTjet > MU_WCR2_HTjet_MIN:
                    inWCR2 = True
                    nWCR2.Fill(0, weight)

            if (MU_HMT_MET_MIN < met < MU_HMT_MET_MAX and
                  MU_HMT_MT_MIN < mt):
                nHMT.Fill(0, weight)
                inHMT = True
                if ev.HTjet < MU_HMTW_HTjet_MAX:
                    inHMTW = True
                    nHMTW.Fill(0, weight)
                    
                if ev.meff > MU_HMTS_MEFF:
                    inHMTS = True
                    nHMTS.Fill(0, weight)
            if (MU_HMET_MET_MIN < met and
                MU_HMET_MT_MIN < mt < MU_HMET_MT_MAX):
                inHMET = True
                nHMET.Fill(0, weight)
                if ev.HTjet < MU_HMETW_HTjet_MAX:
                    inHMETW = True
                    nHMETW.Fill(0, weight)
                    
                if ev.meff > MU_HMETS_MEFF:
                    inHMETS = True
                    nHMETS.Fill(0, weight)

            if mt > MU_MT and met > MU_SRW_MET and (MU_SRW_HTjet_MAX < 0 or ev.HTjet < MU_SRW_HTjet_MAX):
                passBVeto = True
                if MU_SRW_BVETO > 0.0:
                    for i in range(ev.numJets):
                        if ev.JetMV1[i] > BVETO:
                            passBVeto = False
                if passBVeto:
                    inSRW = True
                    nSRW.Fill(0, weight)
                
            if mt > MU_MT and met > MU_SRS_MET and ev.HT > MU_SRS_HT and ev.meff > MU_SRS_MEFF:
                inSRS = True
                nSRS.Fill(0, weight)


        # if not (blind and inSR):
        #     if plotsRegion == SR:
        #         if ((lepton == ELECTRON and met > EL_MET) or
        #             (lepton == MUON and met > MU_MET)):
        #             h_mTel.Fill(mt/GeV, weight)
        #             h_mTmu.Fill(mt/GeV, weight)
        #             h_mTelShort.Fill(mt/GeV, weight)
        #             h_mTmuShort.Fill(mt/GeV, weight)
                    
        #         if ((lepton == ELECTRON and mt > EL_MT) or
        #             (lepton == MUON and mt > MU_MT)):
        #             h_met.Fill(met/GeV, weight)
        #             h_metShort.Fill(met/GeV, weight)
                
        if (plotsRegion == NO_SEL or plotsRegion == PRESEL or
            plotsRegion == SRS and inSRS and not blind or
            plotsRegion == SRW and inSRW and not blind or
            plotsRegion == WCR and inWCR or
            plotsRegion == HMT and inHMT or
            plotsRegion == HMET and inHMET):

            # Accepted avent
            if printAccepted:
                print "Accepted event with Run =", ev.Run, "Event =", ev.Event, "met =", met, "mT =", mt, "meff =", ev.meff

            # if plotsRegion != SR:  # think this is a bug, if statement not needed
            #     pass

            h_mTel.Fill(mt/GeV, weight)
            h_mTmu.Fill(mt/GeV, weight)
            h_mTelShort.Fill(mt/GeV, weight)
            h_mTmuShort.Fill(mt/GeV, weight)
            h_met.Fill(met/GeV, weight)
            h_metShort.Fill(met/GeV, weight)

            h_mTelExtended.Fill(mt/GeV, weight)
            h_mTmuExtended.Fill(mt/GeV, weight)
            h_metExtended.Fill(met/GeV, weight)

            h_ph_el_minv.Fill(ev.PhElMinv/GeV, weight)
            h_ph_mu_minv.Fill(ev.PhMuMinv/GeV, weight)
            h_numEl.Fill(ev.numEl, weight)
            h_numMu.Fill(ev.numMu, weight)
            h_numPh.Fill(ev.numPh, weight)
            h_numJets.Fill(ev.numJets, weight)
            h_deltaPhiPhMETvsMET.Fill(abs(ev.deltaPhiPhMET), met/GeV, weight)
            h_deltaPhiElMETvsMET.Fill(abs(ev.deltaPhiElMET), met/GeV, weight)
            h_eventType.Fill(ev.eventType, weight)

            rejectStudies = -9
            if ev.PhotonConvType[photonIndex] == 0:
                # unconverted
                if ev.PhotonNumBEl[photonIndex] > 0:
                    rejectStudies = 0
                elif ev.PhotonNumPixEl[photonIndex] > 0:
                    rejectStudies = 1
                elif ev.PhotonNumSiEl[photonIndex] > 0:
                    rejectStudies = 2
            elif ev.PhotonConvType[photonIndex] == 1 and ev.PhotonNumSi0[photonIndex] == 0:
                # TRTSA single-track
                isSame = (ev.PhotonNumSiEl[photonIndex] == ev.PhotonNumSi0[photonIndex] or
                          ev.PhotonNumPixEl[photonIndex] == ev.PhotonNumPix0[photonIndex])
                if ev.PhotonNumBEl[photonIndex] > 0:
                    rejectStudies = 3
                elif not isSame:
                    if ev.PhotonNumPixEl[photonIndex] > 0:
                        rejectStudies = 4
                    elif ev.PhotonNumSiEl[photonIndex] > 0:
                        rejectStudies = 5
                    else:
                        rejectStudies = 6
            elif ev.PhotonConvType[photonIndex] == 1:
                # Si single-track
                isSame = (ev.PhotonNumSiEl[photonIndex] == ev.PhotonNumSi0[photonIndex] or
                          ev.PhotonNumPixEl[photonIndex] == ev.PhotonNumPix0[photonIndex])
                if ev.PhotonNumBEl[photonIndex] > 0:
                    rejectStudies = 7
                elif not isSame:
                    if ev.PhotonNumPixEl[photonIndex] > 0:
                        rejectStudies = 8
                    elif ev.PhotonNumSiEl[photonIndex] > 0:
                        rejectStudies = 9
                    else:
                        rejectStudies = 10

            h_ph_rejectStudies.Fill(rejectStudies, weight)
            #h_ph_ConvType.Fill(ev.PhotonConvType[photonIndex], weight)
            h_ph_ConvType.Fill(ev.PhotonConvType[photonIndex], weight)
            h_ph_numSi0.Fill(ev.PhotonNumSi0[photonIndex], weight)
            h_ph_numSi1.Fill(ev.PhotonNumSi1[photonIndex], weight)
            h_ph_numPix0.Fill(ev.PhotonNumPix0[photonIndex], weight)
            h_ph_numPix1.Fill(ev.PhotonNumPix1[photonIndex], weight)
            h_ph_numSiEl.Fill(ev.PhotonNumSiEl[photonIndex], weight)
            h_ph_numPixEl.Fill(ev.PhotonNumPixEl[photonIndex], weight)
            h_ph_numBEl.Fill(ev.PhotonNumBEl[photonIndex], weight)
            h_ph_iso.Fill(iso/GeV, weight)
            h_Wpt.Fill(W.Pt()/GeV, weight)
            h_WptAlt.Fill(Walt.Pt()/GeV, weight)

            if doTruth:
                h_ph_truth.Fill(ev.PhotonTruth[photonIndex], weight)
                h_ph_origin.Fill(ev.PhotonOrigin[photonIndex], weight)

            h_el_mInv.Fill(ev.ElMinv/GeV, weight)
            h_mu_mInv.Fill(ev.MuMinv/GeV, weight)

            h_meff.Fill(ev.meff/GeV, weight)
            h_HT.Fill(ev.HT/GeV, weight)

            if lepton == ELECTRON:
                h_ph_lep_deltaR.Fill(el_ph_deltaR, weight)
                h_ph_lep_deltaPhi.Fill(el_ph_deltaPhi, weight)                
            else:
                h_ph_lep_deltaR.Fill(mu_ph_deltaR, weight)
                h_ph_lep_deltaPhi.Fill(mu_ph_deltaPhi, weight)

            if ev.numPh >= 2:
                h_ph_pt2.Fill(ev.PhotonPt[1]/GeV, weight)
                h_ph_eta2.Fill(ev.PhotonEta[1], weight)
            h_ph_pt1.Fill(ev.PhotonPt[photonIndex]/GeV, weight)
            h_ph_eta1.Fill(ev.PhotonEta[photonIndex], weight)
            h_ph_phi1.Fill(ev.PhotonPhi[photonIndex], weight)
            if ev.numEl >= 2:
                h_el_pt2.Fill(ev.ElectronPt[1]/GeV, weight)
                h_el_eta2.Fill(ev.ElectronEta[1], weight)
            if ev.numEl >= 1:
                h_el_pt1.Fill(ev.ElectronPt[lepIndex]/GeV, weight)
                h_el_eta1.Fill(ev.ElectronEta[lepIndex], weight)
                h_el_phi1.Fill(ev.ElectronPhi[lepIndex], weight)
            if ev.numMu >= 2:
                h_mu_pt2.Fill(ev.MuonPt[1]/GeV, weight)
                h_mu_eta2.Fill(ev.MuonEta[1], weight)
            if ev.numMu >= 1:
                h_mu_pt1.Fill(ev.MuonPt[0]/GeV, weight)
                h_mu_eta1.Fill(ev.MuonEta[0], weight)
                h_mu_phi1.Fill(ev.MuonPhi[0], weight)
                h_mu_eta1_phi1.Fill(ev.MuonEta[0], ev.MuonPhi[0], weight)
                # print "ev.deltaPhiMuMET =",ev.deltaPhiMuMET
                h_deltaPhiMuMETvsMET.Fill(ev.deltaPhiMuMET, met/GeV, weight)
                h_deltaPhiMuMET.Fill(ev.deltaPhiMuMET, weight)
        

    f.Write()
    if printSummary:
        print "**************************************"
        print "*****          YIELDS            *****"
        print "**************************************"
        if not blind:
            print "  SRS Yield =",nSRS.GetBinContent(1),"+-", nSRS.GetBinError(1)
            print "  SRW Yield =",nSRW.GetBinContent(1),"+-", nSRW.GetBinError(1)
        print "  WCR Yield =",nWCR.GetBinContent(1),"+-", nWCR.GetBinError(1)
        print "  WCR1 Yield =",nWCR1.GetBinContent(1),"+-", nWCR1.GetBinError(1)
        print "  WCR2 Yield =",nWCR2.GetBinContent(1),"+-", nWCR2.GetBinError(1)
        if measureFakeAndEff:
            print "  W+jets CR Yield (making tight req) =",nWCRTight.GetBinContent(1),"+-", nWCRTight.GetBinError(1)
        print "  HMT Yield =",nHMT.GetBinContent(1),"+-", nHMT.GetBinError(1)
        print "  HMTW Yield =",nHMTW.GetBinContent(1),"+-", nHMTW.GetBinError(1)
        print "  HMTS Yield =",nHMTS.GetBinContent(1),"+-", nHMTS.GetBinError(1)
        print "  HMET Yield =",nHMET.GetBinContent(1),"+-", nHMET.GetBinError(1)
        print "  HMETW Yield =",nHMETW.GetBinContent(1),"+-", nHMETW.GetBinError(1)
        print "  HMETS Yield =",nHMETS.GetBinContent(1),"+-", nHMETS.GetBinError(1)
        print "  QCD CR Yield =",nQCD.GetBinContent(1),"+-", nQCD.GetBinError(1)
        if measureFakeAndEff:
            print "  QCD CR Yield (making tight req) =",nQCDTight.GetBinContent(1),"+-", nQCDTight.GetBinError(1)
        
        print "  PRESEL Yield =",nPRESEL.GetBinContent(1),"+-", nPRESEL.GetBinError(1)


    if measureFakeAndEff:
        fakeRate = ROOT.TH1F("fakeRate", "The j->lepton fake rate", 1, 0, 1);
        fakeRateNum = nQCDTight.Clone()        
        fakeRateDen = nQCD.Clone()
        if qcdOtherRoot:
            backgroundFile = ROOT.TFile(qcdOtherRoot)
            qcdBackNum = backgroundFile.Get("nQCDTight")
            qcdBackDen = backgroundFile.Get("nQCD")
            fakeRateNum.Add(qcdBackNum, -1)
            fakeRateDen.Add(qcdBackDen, -1)

        if qcdOtherRootSimulate:
            backgroundFileSimulate = ROOT.TFile(qcdOtherRootSimulate)
            print "fakeRateNum =",fakeRateNum.GetBinContent(1), "fakeRateDen=",fakeRateDen.GetBinContent(1) 
            qcdBackNumSim = backgroundFileSimulate.Get("nQCD")
            print "qcdBackNumSim =",qcdBackNumSim.GetBinContent(1) 
            fakeRateNum.Add(qcdBackNumSim, -1)
            #fakeRateDen.Add(qcdBackNumSim, -1.016)
            fakeRateDen.Add(qcdBackNumSim, -1.07)

        fakeRate.Divide(fakeRateNum, fakeRateDen, 1.0, 1.0, "B")

        print "**************************************"
        print "  jet to lepton fake rate =",fakeRate.GetBinContent(1),"+-",fakeRate.GetBinError(1)
        if fakeRate.GetBinError(1):
            backGroundTight = ROOT.TH1F("backGroundTight", "Number of background events in WCR (tight selection)", 1, 0, 1);
            backGroundLoose = ROOT.TH1F("backGroundLoose", "Number of background events in WCR (loose selection)", 1, 0, 1);
            backGroundTight.Fill(0, numBkgTight);
            backGroundLoose.Fill(0, numBkgTight/fakeRate.GetBinContent(1));
            eff = nWCRTight.Clone()
            effDen = nWCR.Clone()
            eff.Add(backGroundTight, -1)
            effDen.Add(backGroundLoose, -1)
            eff.Divide(eff, effDen, 1.0, 1.0, "B")
            print "  lepton incremental eff =",eff.GetBinContent(1),"+-",eff.GetBinError(1)
            print "**************************************"
        

    # nTF = nSIG.Clone()
    # nTF.Divide(nWCR)

    # nXF2 = nHMET.Clone()
    # nXF2.Divide(nCR)

    # print "  SR/CR =",nTF.GetBinContent(1),"+-", nTF.GetBinError(1)
    # print "  HMET/CR =",nXF2.GetBinContent(1),"+-", nXF2.GetBinError(1)

    return (nSRW.GetBinContent(1), nSRW.GetBinError(1), nSRS.GetBinContent(1), nSRS.GetBinError(1))
    #return (nPRESEL.GetBinContent(1), nPRESEL.GetBinError(1))

# This function calls the LepPhotonAnalysis function 
def main():
    
    try:
        # retrive command line options
        shortopts  = "o:l:t:w:vh?"
        longopts   = ["outfile=", "lepton=", "ttree=", "weight=", "help", "usage"]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )

    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        usage()
        sys.exit(1)

    if len(args) == 0:
        print "ERROR: need an input file"
        usage()
        sys.exit(1)
    elif len(args) > 1:
        print "ERROR: only one input file is used"
        usage()
        sys.exit(1)
        
    infile = args[0]
    inFileNoPath = os.path.split(infile)[1]
    outfile = os.path.splitext(inFileNoPath)[0] + "Hist.root"
    ttreeName = DEFAULTTTREE
    weight = DEFAULTWEIGHT
    lepton = DEFAULT_LEPTON

    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-o", "--outfile"):
            outfile = a
        elif o in ("-t", "--ttree"):
            ttreeName = a
        elif o in ("-w", "--weight"):
            weight = float(a)
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

    # let's get the TFile and outfile and call a new function

    f = ROOT.TFile(infile)
    ttree=f.Get(ttreeName)

    LepPhotonAnalysis(ttree, outfile, lepton, weight, useWeights = False, debug = True)


def Nqcd(nLoose, nTight, eta, lepton):
    if lepton == MUON:
        #eps_sig = 1.0
        eps_sig = 0.984
        #eps_qcd = 0.62
        #eps_qcd = 0.50
        #eps_qcd = 0.45
        #eps_qcd = 0.40
        #eps_qcd = 0.35
        eps_qcd = 0.32
        #eps_qcd = 0.30
    else:
        #eps_qcd = 0.24
        #eps_qcd = 0.23
        #eps_qcd = 0.22
        eps_qcd = 0.21
        #eps_qcd = 0.20
        #eps_qcd = 0.19
        #eps_qcd = 0.18
        #eps_qcd = 0.17
        #eps_qcd = 0.20
        eps_sig = ElEffPar.GetEfficiency(eta)
    #print "eta =", eta, "eps_qcd =", eps_qcd, "eps_sig =", eps_sig
    if eps_sig != eps_qcd:
        return eps_qcd*(1.0*eps_sig*nLoose - nTight)/(eps_sig - eps_qcd)
    else:
        raise ValueError("eps_sig = %f and eps_qcd = %f must be different" % (eps_sig,eps_qcd))
        return -1

class EffParametrization:
    '''A 1D parametrization of an efficiency'''
    def __init__(self, h):
        self.hist = h

    def GetEfficiency(self, par):
        b = self.hist.FindBin(par)
        return self.hist.GetBinContent(b)

fpar = ROOT.TFile(FILENAME_ELEFF)
ElEffPar = EffParametrization(fpar.Get("eff_eta"))


def deltaPhi(phiA, phiB):
    diff = (phiB - phiA) % (2.0 * math.pi)
    if diff >= math.pi:
        diff = (2.0 * math.pi) - diff
    return diff

def mT(pt, phi, metx, mety):
    if metx == 0.0 and mety == 0.0:
        return 0.0
    else:
        metphi = math.atan2(mety, metx)
        phidiff = deltaPhi(phi, metphi)
        return math.sqrt(2 * pt * math.hypot(metx, mety) * (1 - math.cos(phidiff)))

def SymHess(histp, histm, weight, pdfWeights, nPDFs, scale=0.6079):
    for i in range(nPDFs):
        deltaX = 0.5 * (pdfWeights[2*i] - pdfWeights[2*i + 1]) * scale
        histp.Fill(i, weight*(1+deltaX))
        histm.Fill(i, weight*(1-deltaX))


if __name__ == "__main__":
    main()

