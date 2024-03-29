#! /usr/bin/env python

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

printAccepted = False

# What plots should be made
NO_SEL = 0
PRESEL = 1
SR = 2
WCR = 3
TCR = 4
QCD = 5
XR1 = 6
XR2 = 7

DEFAULT_PLOTS = PRESEL

# For the ABCD method
NoABCD = 0
LL = 1
LT = 2
TL = 3
TT = 4
lT = 5  #loose, not necessarily anti-tight, and isolated

# TTType (note all should be LEPJETS or DILEP):
ALL = 0
LEPJETS = 1
DILEP = 2

# ONLY STRONG
# use same ALL as for TTType
WEAK = 1
STRONG = 2

# ttbar systematics
# use NONE for no syst
TTBAR_NOPHOTON = 1
TTBAR_ELASPHOTON = 2

#Cuts
# - electron channel
EL_PHPTCUT = 30*GeV
EL_PHETACUT = 2.37
EL_ELPTCUT = 25*GeV
EL_ELETACUT = 2.47
EL_MET = 50*GeV
EL_MT = 50*GeV

EL_QCD_MINV_WINDOW = 15*GeV
EL_MINV_WINDOW = 15*GeV

# tight (default)
EL_WCR_MET_MIN = 35*GeV
EL_WCR_MET_MAX = 80*GeV
EL_WCR_MT_MIN = 35*GeV
EL_WCR_MT_MAX = 90*GeV
EL_TCR_MET_MIN = 35*GeV

# # loose
# EL_WCR_MET_MIN = 25*GeV
# EL_WCR_MET_MAX = 80*GeV
# EL_WCR_MT_MIN = 25*GeV
# EL_WCR_MT_MAX = 90*GeV
# EL_TCR_MET_MIN = 25*GeV

# # Wgamma selection
# EL_WCR_MET_MIN = 25*GeV
# EL_WCR_MET_MAX = 1000000*GeV
# EL_WCR_MT_MIN = 40*GeV
# EL_WCR_MT_MAX = 90000000*GeV
# EL_TCR_MET_MIN = 25*GeV


EL_TCR_MET_MAX = 80*GeV
EL_TCR_MT_MIN =  90*GeV

EL_QCD_MET_MAX = 20*GeV
EL_QCD_MT_MAX = 20*GeV

DELTAR_EL_PH = 0.7

# - muon channel
MU_PHPTCUT = 30*GeV
#MU_PHPTCUT = 100*GeV
MU_PHETACUT = 2.37
MU_MUPTCUT = 25*GeV
MU_MUETACUT = 2.4
MU_MET = 50*GeV
MU_MT = 50*GeV

MU_QCD_MINV_WINDOW = 0*GeV
MU_MINV_WINDOW = 15*GeV

# tight (default)
MU_WCR_MET_MIN = 35*GeV
MU_WCR_MET_MAX = 80*GeV
MU_WCR_MT_MIN = 35*GeV
MU_WCR_MT_MAX = 90*GeV
MU_TCR_MET_MIN = 35*GeV

# # loose
# MU_WCR_MET_MIN = 25*GeV
# MU_WCR_MET_MAX = 80*GeV
# MU_WCR_MT_MIN = 25*GeV
# MU_WCR_MT_MAX = 90*GeV
#MU_TCR_MET_MIN = 25*GeV

# Wgamma
# MU_WCR_MET_MIN = 25*GeV
# MU_WCR_MET_MAX = 80000000*GeV
# MU_WCR_MT_MIN = 40*GeV
# MU_WCR_MT_MAX = 900000000*GeV
# MU_TCR_MET_MIN = 25*GeV

# # test for events
# MU_WCR_MET_MIN = 50*GeV
# MU_WCR_MET_MAX = 100*GeV
# MU_WCR_MT_MIN = 0*GeV
# MU_WCR_MT_MAX = 90000*GeV
# MU_TCR_MET_MIN = 25*GeV


MU_TCR_MET_MAX = 80*GeV
MU_TCR_MT_MIN =  90*GeV

MU_QCD_MET_MAX = 25*GeV
MU_QCD_MT_MAX = 25*GeV

DELTAR_MU_PH = 0.7

VETO_SECOND_LEPTON = False
#VETO_SECOND_SFLEPTON_MINV = False  # not supported in this
VETO_TRTSA_PHOTON_E_BLAYER = True

MET_DEFAULT = 0
MET_PLUS = 1
MET_MINUS = 2
MET_MUON = 3
MET_FULL = 4

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

def TtbarSystAnalysis(ttree, outfile, lepton, glWeight, filterPhotons = False, 
                      onlyStrong = ALL, 
                      applySF = NONE, applyTrigWeight = NONE,
                      plotsRegion = DEFAULT_PLOTS,
                      blind = False,
                      tttype = ALL,
                      qcdOtherRoot = "",
                      qcdOtherRootSimulate = "",
                      reweighAlpgen = False,
                      debug = False,
                      doTruth = False,
                      onlyOrigin = -1,
                      metType = MET_DEFAULT,
                      ttbarSyst = NONE):

    if not (lepton == ELECTRON or lepton == MUON):
        print "ERROR: The lepton must be ELECTRON or MUON"
        return

    if metType != MET_DEFAULT:
        print "Using metType =",metType

    if ttbarSyst != NONE:
        print "Doing ttbarSyst =",ttbarSyst

    f = ROOT.TFile(outfile, 'RECREATE')


    nBinsEta = 30
    nBinsPt = 50
    nBinsHT = 75
    if plotsRegion == WCR:
        nBinsEta = 15
        nBinsPt = 25
        nBinsHT = 50
    elif plotsRegion == TCR or plotsRegion == XR2:
        nBinsEta = 15
        nBinsPt = 25
        nBinsHT = 30
    elif plotsRegion == SR:
        nBinsEta = 15
        nBinsPt = 25
        nBinsHT = 30

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

    h_ph_eta1 = ROOT.TH1F("ph_eta1","Psuedorapidity of the leading photons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_ph_pt1 = ROOT.TH1F("ph_pt1","Transverse momentum of the leading photons;p_{T} [GeV];Events", nBinsPt, 50, 300)
    h_ph_eta2 = ROOT.TH1F("ph_eta2","Psuedorapidity of the second photons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_ph_pt2 = ROOT.TH1F("ph_pt2","Transverse momentum of the second photons;p_{T} [GeV];Events", nBinsPt, 50, 300)

    # h_ph_ptB_unconv = ROOT.TH1F("ph_ptB_unconv","Transverse momentum of the unconverted Barrel photons;p_{T} [GeV];Events", 500, 0, 500)
    # h_ph_ptEC_unconv = ROOT.TH1F("ph_ptEC_unconv","Transverse momentum of the unconverted EC photons;p_{T} [GeV];Events", 500, 0, 500)

    # h_ph_ptB_conv = ROOT.TH1F("ph_ptB_conv","Transverse momentum of the converted Barrel photons;p_{T} [GeV];Events", 500, 0, 500)
    # h_ph_ptEC_conv = ROOT.TH1F("ph_ptEC_conv","Transverse momentum of the converted EC photons;p_{T} [GeV];Events", 500, 0, 500)
    h_ph_el_minv = ROOT.TH1F("ph_el_minv", "The invariant mass of the leading photon and electron;M_{inv} [GeV];Events", 100, 0, 500)
    h_ph_mu_minv = ROOT.TH1F("ph_mu_minv", "The invariant mass of the leading photon and muon;M_{inv} [GeV];Events", 100, 0, 500)
    h_numPh = ROOT.TH1F("numPh", "The number of photons that pass cuts;N_{photons};Events", 9, -0.5, 8.5)

    h_ph_lep_deltaR = ROOT.TH1F("ph_lep_deltaR", "The delta-R beteween the lepton and the photon;#DeltaR(l,#gamma);Events", 50, 0, 5)

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
    h_mu_eta1 = ROOT.TH1F("mu_eta1","Psuedorapidity of the leading muons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_mu_pt1 = ROOT.TH1F("mu_pt1","Transverse momentum of the leading muons;p_{T} [GeV];Events", nBinsPt, 0, 250)
    h_mu_eta2 = ROOT.TH1F("mu_eta2","Psuedorapidity of the second muons;#eta_{reco};Events", nBinsEta, -3, 3)
    h_mu_pt2 = ROOT.TH1F("mu_pt2","Transverse momentum of the second muons;p_{T} [GeV];Events", nBinsPt, 0, 250)
    h_numMu = ROOT.TH1F("numMu", "The number of muons that pass cuts;N_{muons};Events", 9, -0.5, 8.5)
    h_mu_mInv = ROOT.TH1F("mu_mInv", "The invariant mass of leading muons;m_{inv} [GeV];Events", 120, 0, 120)

    ######## eldir
    eldir.cd()
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
    h_met = ROOT.TH1F("met", "The MET distribution;E_{T}^{miss} [GeV];Events", 50, 0, 250)
    # h_met0J = ROOT.TH1F("met0J", "The MET distribution of events with zero jets;E_{T}^{miss} [GeV];Events", 500, 0, 500)
    # h_met1J = ROOT.TH1F("met1J", "The MET distribution of events with one jet;E_{T}^{miss} [GeV];Events", 500, 0, 500)
    # h_met2J = ROOT.TH1F("met2J", "The MET distribution of events with two jets;E_{T}^{miss} [GeV];Events", 500, 0, 500)
    # h_met3J = ROOT.TH1F("met3J", "The MET distribution of events with three jets;E_{T}^{miss} [GeV];Events", 500, 0, 500)
    # h_met4J = ROOT.TH1F("met4J", "The MET distribution of events with four jets;E_{T}^{miss} [GeV];Events", 500, 0, 500)

    h_metExtended = ROOT.TH1F("metExtended", "The MET distribution;E_{T}^{miss} [GeV];Events", 100, 0, 500)
    h_metShort = ROOT.TH1F("metShort", "The MET distribution;E_{T}^{miss} [GeV];Events", 20, 0, 100)

    h_deltaPhiPhMETvsMET = ROOT.TH2F("deltaPhiPhMETvsMET", 
						  "The DeltaPhi(Photon,MET) distribution vs. MET;#Delta#phi;E_{T}^{miss} [GeV]",
						  50, 0, math.pi, 20, 100, 300)

    h_deltaPhiElMETvsMET = ROOT.TH2F("deltaPhiElMETvsMET", 
						  "The DeltaPhi(Electron,MET) distribution vs. MET;#Delta#phi;E_{T}^{miss} [GeV]",
						  50, 0, math.pi, 20, 100, 300)

    h_deltaPhiMuMETvsMET = ROOT.TH2F("deltaPhiMuMETvsMET", 
						  "The DeltaPhi(Muon,MET) distribution vs. MET;#Delta#phi;E_{T}^{miss} [GeV]",
						  50, 0, math.pi, 20, 100, 300)
    ############ gldir
    gldir.cd()
    h_HT = ROOT.TH1F("HT", "The H_{T} distribution;H_{T} [GeV];Events", nBinsHT, 0, 1500)
    h_mTel = ROOT.TH1F("mTel", "The m_{T} distribution;m_{T} [GeV];Events", 50, 0, 250)
    h_mTmu = ROOT.TH1F("mTmu", "The m_{T} distribution;m_{T} [GeV];Events", 50, 0, 250)
    h_mTelShort = ROOT.TH1F("mTelShort", "The m_{T} distribution;m_{T} [GeV];Events", 20, 0, 100)
    h_mTmuShort = ROOT.TH1F("mTmuShort", "The m_{T} distribution;m_{T} [GeV];Events", 20, 0, 100)
    h_mTelExtended = ROOT.TH1F("mTelExtended", "The m_{T} distribution;m_{T} [GeV];Events", 100, 0, 500)
    h_mTmuExtended = ROOT.TH1F("mTmuExtended", "The m_{T} distribution;m_{T} [GeV];Events", 100, 0, 500)
    h_meff = ROOT.TH1F("meff", "The m_{eff} distribution;m_{eff} [GeV];Events", nBinsHT, 0, 1500)

    h_mTelvsMET = ROOT.TH2F("mTelvsMET", "m_{T} vs. MET;E_{T}^{miss} [GeV];m_{T} [GeV]",
                            50, 0, 500, 50, 0, 500)
    h_mTmuvsMET = ROOT.TH2F("mTmuvsMET", "m_{T} vs. MET;E_{T}^{miss} [GeV];m_{T} [GeV]",
                            50, 0, 500, 50, 0, 500)

    h_eventType = ROOT.TH1F("eventType", "The event type, based on truth;event type;Events", 
					 numEventTypes, 0, numEventTypes);

    ######## go back to root
    f.cd()

    ######## initialize counts

    nPRESEL = ROOT.TH1F("nPRESEL", "Number of events in the PRESEL", 1, 0, 1);
    nWCR = ROOT.TH1F("nWCR", "Number of events in the WCR", 1, 0, 1);
    nTCR = ROOT.TH1F("nTCR", "Number of events in the TCR", 1, 0, 1);
    nQCD = ROOT.TH1F("nQCD", "Number of events in the QCD", 1, 0, 1);
    nSIG = ROOT.TH1F("nSIG", "Number of events in the SR", 1, 0, 1);
    nXR1 = ROOT.TH1F("nXR1", "Number of events in the XR1", 1, 0, 1);
    nXR2 = ROOT.TH1F("nXR2", "Number of events in the XR2", 1, 0, 1);

    nPRESEL.Sumw2()
    nWCR.Sumw2()
    nTCR.Sumw2()
    nQCD.Sumw2()
    nSIG.Sumw2()
    nXR1.Sumw2()
    nXR2.Sumw2()

    for ev in ttree:
        # lets apply the cuts
        # double-check quality
        if ttbarSyst == NONE and (ev.numPh == 0 or (ev.numEl == 0 and lepton == ELECTRON) or (ev.numMu == 0 and lepton == MUON)):
            # print "ERROR: event is malformed:", ev.numPh, ev.numEl, ev.numMu, lepton
            # sys.exit(1)
            continue

        if debug: print "Analizing event with Run =", ev.Run, ", Event =", ev.Event

        if filterPhotons and ev.numTruthPh > 0:
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
        else:
            print >> sys.stderr, "Have an invalid metType =", metType
            sys.exit(1)


        met = math.hypot(metx, mety)
            
        #print "MET =", met, "lepton =", lepton, "ev.PhotonPt[0] = ", ev.PhotonPt[0]
        #print "weight =", ev.Weight * glWeight

        weight = ev.Weight * glWeight

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


        if lepton == MUON:
            if applyTrigWeight == NOMINAL:
                weight *= ev.MuonTrigWeight
            elif applyTrigWeight == LOW:
                weight *= (ev.MuonTrigWeight - ev.MuonTrigWeightUnc)
            elif applyTrigWeight == HIGH:
                weight *= (ev.MuonTrigWeight + ev.MuonTrigWeightUnc)

        if reweighAlpgen:
            if ev.Wpt < -990.0:
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
            continue

        if onlyStrong == WEAK and ev.isStrong:
            continue
        if debug: print "  pass onlyStrong"


        lepIndex = 0

        elAsPhotonIndex = -1
        if ttbarSyst == TTBAR_ELASPHOTON:
            if lepton == MUON:
                for i in range(ev.numEl):
                    if ev.ElectronPt[i] > MU_PHPTCUT and (removeCrack and not (1.37 < abs(ev.ElectronEta2[i]) < 1.52) or
                                                          not removeCrack):
                        elAsPhotonIndex = i
                        break
            else:
                lepIndex = -1
                for i in range(ev.numEl):
                    if removeCrack and not (1.37 < abs(ev.ElectronEta2[i]) < 1.52) or not removeCrack:
                        if elAsPhotonIndex < 0 and ev.ElectronPt[i] > EL_PHPTCUT: # this assumes phptcut is bigger than elptcut
                            elAsPhotonIndex = i
                        elif lepIndex < 0 and ev.ElectronPt[i] > EL_ELPTCUT:
                            lepIndex = i

            if lepIndex < 0 or elAsPhotonIndex < 0:
                continue
           
        else:

            if removeCrack and lepton == ELECTRON:
                for i in range(ev.numEl):
                    if not (1.37 < abs(ev.ElectronEta2[i]) < 1.52):
                        lepIndex = i
                        break
                else:
                    # print "*** electron only in crack ***"
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

        if ttbarSyst == NONE:
            if onlyOrigin >= 0:
                if ev.PhotonOrigin[photonIndex] != onlyOrigin:
                    continue
            photon = ROOT.TLorentzVector()
            photon.SetPtEtaPhiM(ev.PhotonPt[photonIndex], ev.PhotonEta[photonIndex], ev.PhotonPhi[photonIndex], 0.0)
        elif ttbarSyst == TTBAR_ELASPHOTON:
            photon = ROOT.TLorentzVector()
            photon.SetPtEtaPhiM(ev.ElectronPt[elAsPhotonIndex], ev.ElectronEta[elAsPhotonIndex], ev.ElectronPhi[elAsPhotonIndex], 0.0)
           
        if lepton == ELECTRON:
            electron = ROOT.TLorentzVector()
            electron.SetPtEtaPhiM(ev.ElectronPt[lepIndex], ev.ElectronEta[lepIndex], ev.ElectronPhi[lepIndex], 0.0)

        if plotsRegion != NO_SEL:

            # first the basic lepton and photon selection (but not MET and mT):
            if ((lepton == ELECTRON and
                 (ev.ElectronPt[lepIndex] < EL_ELPTCUT or abs(ev.ElectronEta[lepIndex]) > EL_ELETACUT)) or
                (lepton == MUON and
                 (ev.MuonPt[lepIndex] < MU_MUPTCUT or abs(ev.MuonEta[lepIndex]) > MU_MUETACUT))):
                continue
            
            if ttbarSyst != TTBAR_NOPHOTON:
                if ((lepton == ELECTRON and 
                     (photon.Pt() < EL_PHPTCUT or abs(photon.Eta()) > EL_PHETACUT)) or
                    (lepton == MUON and
                     (photon.Pt() < MU_PHPTCUT or abs(photon.Eta()) > MU_PHETACUT))):
                    continue


            # veto second lepton or Z window cut
            if lepton == ELECTRON and EL_MINV_WINDOW != 0 and ttbarSyst != TTBAR_NOPHOTON:
                elph = electron + photon
                minv = elph.M()
                # print "**minv =", minv
                if ZMASS - EL_MINV_WINDOW < minv < ZMASS + EL_MINV_WINDOW:
                    continue

            numEl = ev.numEl
            if ttbarSyst == TTBAR_ELASPHOTON:
                numEl -= 1

            if VETO_SECOND_LEPTON and ev.numMu + numEl > 1:
                continue
            elif (lepton == ELECTRON and ev.numMu > 0 or
                  lepton == MUON and numEl > 0):
                continue

            # if (VETO_SECOND_SFLEPTON_MINV and
            #     (lepton == ELECTRON and ZMASS - EL_MINV_WINDOW < ev.ElMinv < ZMASS + EL_MINV_WINDOW) or
            #     (lepton == MUON and ZMASS - MU_MINV_WINDOW < ev.MuMinv < ZMASS + MU_MINV_WINDOW)):
            #     continue

            if (VETO_TRTSA_PHOTON_E_BLAYER and ttbarSyst == NONE and
                ev.PhotonConvType[photonIndex] == 1 and ev.PhotonNumSi0[photonIndex] == 0 and
                ev.PhotonNumBEl[photonIndex]):
                continue

        if debug: print "  passed some presel"
        el_ph_deltaR = -1.0
        mu_ph_deltaR = -1.0
        if ttbarSyst != TTBAR_NOPHOTON:
            if lepton == ELECTRON:
                el_ph_deltaR = photon.DeltaR(electron)
                if plotsRegion != NO_SEL and el_ph_deltaR < DELTAR_EL_PH:
                    continue
            else:
                muon = ROOT.TLorentzVector()
                muon.SetPtEtaPhiM(ev.MuonPt[lepIndex], ev.MuonEta[lepIndex], ev.MuonPhi[lepIndex], 105.65836668)
                mu_ph_deltaR = photon.DeltaR(muon)
                if plotsRegion != NO_SEL and mu_ph_deltaR < DELTAR_MU_PH:
                    continue

            if debug: print "  passed lep-ph deltaR"

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
                 

        # now plots that should be made before MET and mT cuts
        h_mTelvsMET.Fill(met/GeV, mt/GeV, weight)
        h_mTmuvsMET.Fill(met/GeV, mt/GeV, weight)

        inQCD = False
        inTCR = False
        inWCR = False
        inXR1 = False
        inXR2 = False
        inSR = False
            
        if debug: print "  met =", met, "mTmu =", mt, "mTel =", mt

        nPRESEL.Fill(0, weight)

        # do CR counts
        if lepton == ELECTRON:
            if met < EL_QCD_MET_MAX and mt < EL_QCD_MT_MAX:
                if (ev.PhElMinv < ZMASS - EL_QCD_MINV_WINDOW or
                    ev.PhElMinv > ZMASS + EL_QCD_MINV_WINDOW):
                    # in QCD CR
                    inQCD = True
                    nQCD.Fill(0, weight)

            elif (EL_WCR_MET_MIN < met < EL_WCR_MET_MAX and
                  EL_WCR_MT_MIN < mt < EL_WCR_MT_MAX):
                inWCR = True
                nWCR.Fill(0, weight)
            elif (EL_TCR_MET_MIN < met < EL_TCR_MET_MAX and
                  EL_TCR_MT_MIN < mt):
                nTCR.Fill(0, weight)
                inTCR = True
        else:
            if met < MU_QCD_MET_MAX and mt < MU_QCD_MT_MAX:
                if (ev.PhElMinv < ZMASS - MU_QCD_MINV_WINDOW or
                    ev.PhElMinv > ZMASS + MU_QCD_MINV_WINDOW):
                    inQCD = True
                    nQCD.Fill(0, weight)
            elif (MU_WCR_MET_MIN < met < MU_WCR_MET_MAX and
                  MU_WCR_MT_MIN < mt < MU_WCR_MT_MAX):
                inWCR = True
                nWCR.Fill(0, weight)
            elif (MU_TCR_MET_MIN < met < MU_TCR_MET_MAX and
                  MU_TCR_MT_MIN < mt):
                nTCR.Fill(0, weight)
                inTCR = True

        # do the XR
        if lepton == ELECTRON:
            if (EL_WCR_MET_MAX < met and
                EL_WCR_MT_MIN < mt < EL_WCR_MT_MAX):
                inXR2 = True
                nXR2.Fill(0, weight)
            if (EL_WCR_MT_MAX < mt and
                EL_WCR_MET_MIN < met < EL_WCR_MET_MAX and
                not inTCR):
                inXR1 = True
                nXR1.Fill(0, weight)
        else:
            if (MU_WCR_MET_MAX < met and
                MU_WCR_MT_MIN < mt < MU_WCR_MT_MAX):
                inXR2 = True
                nXR2.Fill(0, weight)
            if (MU_WCR_MT_MAX < mt and
                MU_WCR_MET_MIN < met < MU_WCR_MET_MAX and
                not inTCR):
                inXR1 = True
                nXR1.Fill(0, weight)


        ## our selection
        if ((lepton == ELECTRON and
             (met > EL_MET and mt > EL_MT)) or
            (lepton == MUON and
             (met > MU_MET and mt > MU_MT))):
            inSR = True
            nSIG.Fill(0, weight)


        if not (blind and inSR):
            if plotsRegion == SR:
                if ((lepton == ELECTRON and met > EL_MET) or
                    (lepton == MUON and met > MU_MET)):
                    h_mTel.Fill(mt/GeV, weight)
                    h_mTmu.Fill(mt/GeV, weight)
                    h_mTelShort.Fill(mt/GeV, weight)
                    h_mTmuShort.Fill(mt/GeV, weight)
                    h_mTelExtended.Fill(mt/GeV, weight)
                    h_mTmuExtended.Fill(mt/GeV, weight)
                    
                if ((lepton == ELECTRON and mt > EL_MT) or
                    (lepton == MUON and mt > MU_MT)):
                    h_met.Fill(met/GeV, weight)
                    h_metShort.Fill(met/GeV, weight)
                    h_metExtended.Fill(met/GeV, weight)
                
        if (plotsRegion == NO_SEL or plotsRegion == PRESEL or
            plotsRegion == SR and inSR and not blind or
            plotsRegion == WCR and inWCR or
            plotsRegion == TCR and inTCR or
            plotsRegion == XR1 and inXR1 or
            plotsRegion == XR2 and inXR2):

            # Accepted avent
            if printAccepted:
                print "Accepted event with Run =", ev.Run, ", Event =", ev.Event

            if plotsRegion != SR:  # think this is a bug, if statement not needed -- no; need if
                h_mTel.Fill(mt/GeV, weight)
                h_mTmu.Fill(mt/GeV, weight)
                h_mTelShort.Fill(mt/GeV, weight)
                h_mTmuShort.Fill(mt/GeV, weight)
                h_mTelExtended.Fill(mt/GeV, weight)
                h_mTmuExtended.Fill(mt/GeV, weight)
                h_met.Fill(met/GeV, weight)
                h_metShort.Fill(met/GeV, weight)
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
            if ttbarSyst == NONE:
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

                if doTruth:
                    h_ph_truth.Fill(ev.PhotonTruth[photonIndex], weight)
                    h_ph_origin.Fill(ev.PhotonOrigin[photonIndex], weight)

                if ev.numPh >= 2:
                    h_ph_pt2.Fill(ev.PhotonPt[1]/GeV, weight)
                    h_ph_eta2.Fill(ev.PhotonEta[1], weight)
                h_ph_pt1.Fill(ev.PhotonPt[photonIndex]/GeV, weight)
                h_ph_eta1.Fill(ev.PhotonEta[photonIndex], weight)

            h_el_mInv.Fill(ev.ElMinv/GeV, weight)
            h_mu_mInv.Fill(ev.MuMinv/GeV, weight)

            h_meff.Fill(ev.meff/GeV, weight)
            h_HT.Fill(ev.HT/GeV, weight)

            if lepton == ELECTRON:
                h_ph_lep_deltaR.Fill(el_ph_deltaR, weight)
            else:
                h_ph_lep_deltaR.Fill(mu_ph_deltaR, weight)

            if ev.numEl >= 2:
                h_el_pt2.Fill(ev.ElectronPt[1]/GeV, weight)
                h_el_eta2.Fill(ev.ElectronEta[1], weight)
            if ev.numEl >= 1:
                h_el_pt1.Fill(ev.ElectronPt[lepIndex]/GeV, weight)
                h_el_eta1.Fill(ev.ElectronEta[lepIndex], weight)
            if ev.numMu >= 2:
                h_mu_pt2.Fill(ev.MuonPt[1]/GeV, weight)
                h_mu_eta2.Fill(ev.MuonEta[1], weight)
            if ev.numMu >= 1:
                h_mu_pt1.Fill(ev.MuonPt[lepIndex]/GeV, weight)
                h_mu_eta1.Fill(ev.MuonEta[lepIndex], weight)
        

    f.Write()
    print "**************************************"
    print "*****          YIELDS            *****"
    print "**************************************"
    if not blind:
        print "  Signal Yield =",nSIG.GetBinContent(1),"+-", nSIG.GetBinError(1)
    print "  W+jets CR Yield =",nWCR.GetBinContent(1),"+-", nWCR.GetBinError(1)
    print "  ttbar CR Yield =",nTCR.GetBinContent(1),"+-", nTCR.GetBinError(1)
    print "  QCD CR Yield =",nQCD.GetBinContent(1),"+-", nQCD.GetBinError(1)
        
    print "  XR1 Yield =",nXR1.GetBinContent(1),"+-", nXR1.GetBinError(1)
    print "  XR2 Yield =",nXR2.GetBinContent(1),"+-", nXR2.GetBinError(1)
    print "  PRESEL Yield =",nPRESEL.GetBinContent(1),"+-", nPRESEL.GetBinError(1)


    # nTF = nSIG.Clone()
    # nTF.Divide(nWCR)

    # nXF1 = nXR1.Clone()
    # nXF1.Divide(nCR)

    # nXF2 = nXR2.Clone()
    # nXF2.Divide(nCR)

    # print "  SR/CR =",nTF.GetBinContent(1),"+-", nTF.GetBinError(1)
    # print "  XR1/CR =",nXF1.GetBinContent(1),"+-", nXF1.GetBinError(1)
    # print "  XR2/CR =",nXF2.GetBinContent(1),"+-", nXF2.GetBinError(1)

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

    TtbarSystAnalysis(ttree, outfile, lepton, weight)


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

if __name__ == "__main__":
    main()

