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

# TTType (note all should be LEPJETS or DILEP):
ALL = 0
LEPJETS = 1
DILEP = 2

# ONLY STRONG
# use same ALL as for TTType
WEAK = 1
STRONG = 2

#Cuts
# - electron channel
EL_PHPTCUT = 100*GeV
EL_PHETACUT = 2.37
EL_ELPTCUT = 25*GeV
EL_ELETACUT = 2.47
EL_MET = 100*GeV
EL_MT = 100*GeV

EL_QCD_MINV_WINDOW = 30*GeV
EL_MINV_WINDOW = 15*GeV

# tight (default)
# EL_WCR_MET_MIN = 35*GeV
# EL_WCR_MET_MAX = 80*GeV
# EL_WCR_MT_MIN = 35*GeV
# EL_WCR_MT_MAX = 90*GeV

# loose
EL_WCR_MET_MIN = 25*GeV
EL_WCR_MET_MAX = 80*GeV
EL_WCR_MT_MIN = 25*GeV
EL_WCR_MT_MAX = 90*GeV

EL_TCR_MET_MIN = 35*GeV
EL_TCR_MET_MAX = 80*GeV
EL_TCR_MT_MIN =  90*GeV

EL_QCD_MET_MAX = 20*GeV
EL_QCD_MT_MAX = 20*GeV

DELTAR_EL_PH = 0.7

# - muon channel
MU_PHPTCUT = 85*GeV
MU_PHETACUT = 2.37
MU_MUPTCUT = 25*GeV
MU_MUETACUT = 2.4
MU_MET = 100*GeV
MU_MT = 100*GeV

MU_QCD_MINV_WINDOW = 0*GeV
MU_MINV_WINDOW = 15*GeV

# tight (default)
MU_WCR_MET_MIN = 35*GeV
MU_WCR_MET_MAX = 80*GeV
MU_WCR_MT_MIN = 35*GeV
MU_WCR_MT_MAX = 90*GeV

# loose
# MU_WCR_MET_MIN = 25*GeV
# MU_WCR_MET_MAX = 80*GeV
# MU_WCR_MT_MIN = 25*GeV
# MU_WCR_MT_MAX = 90*GeV

MU_TCR_MET_MIN = 35*GeV
MU_TCR_MET_MAX = 80*GeV
MU_TCR_MT_MIN =  90*GeV

MU_QCD_MET_MAX = 25*GeV
MU_QCD_MT_MAX = 25*GeV

DELTAR_MU_PH = 0.7

VETO_SECOND_LEPTON = False
VETO_SECOND_SFLEPTON_MINV = False
VETO_TRTSA_PHOTON_E_BLAYER = True

#loose = 0xc5fc01
##loose = 0xf7fc01 # this is OK
##loose = 0xeffc01
#loose = 0xc5cc01
loose = 0xc5fc01
tight = 0xfffc01

#bits = [0x020000, 0x080000, 0x100000, 0x200000] 
bits = [0x20000] 

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

def LepPhotonAnalysis(ttree, outfile, lepton, glWeight, filterPhotons = False, 
                      onlyStrong = ALL, 
                      measureFakeAndEff = False, 
                      numBkgTight = 0, scaleQCD = False,
                      applySF = NONE, applyTrigWeight = NONE,
                      plotsRegion = DEFAULT_PLOTS,
                      doABCD = NoABCD,
                      doAltABCD = False,
                      blind = False,
                      tttype = ALL,
                      qcdOtherRoot = "",
                      qcdOtherRootSimulate = "",
                      reweighAlpgen = False,
                      debug = False,
                      doTruth = False):

    if not (lepton == ELECTRON or lepton == MUON):
        print "ERROR: The lepton must be ELECTRON or MUON"
        return

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

    nWCR = ROOT.TH1F("nWCR", "Number of events in the WCR", 1, 0, 1);
    nTCR = ROOT.TH1F("nTCR", "Number of events in the TCR", 1, 0, 1);
    nQCD = ROOT.TH1F("nQCD", "Number of events in the QCD", 1, 0, 1);
    nSIG = ROOT.TH1F("nSIG", "Number of events in the SR", 1, 0, 1);
    nXR1 = ROOT.TH1F("nXR1", "Number of events in the XR1", 1, 0, 1);
    nXR2 = ROOT.TH1F("nXR2", "Number of events in the XR2", 1, 0, 1);


    nWCR.Sumw2()
    nTCR.Sumw2()
    nQCD.Sumw2()
    nSIG.Sumw2()
    nXR1.Sumw2()
    nXR2.Sumw2()

    if measureFakeAndEff:
        nWCRTight = ROOT.TH1F("nWCRTight", "Number of tight events in the WCR", 1, 0, 1);
        nQCDTight = ROOT.TH1F("nQCDTight", "Number of tight events in the QCD", 1, 0, 1);
        nWCRTight.Sumw2()
        nQCDTight.Sumw2()    


    for ev in ttree:
        # lets apply the cuts
        # double-check quality
        if ev.numPh == 0 or (ev.numEl == 0 and lepton == ELECTRON) or (ev.numMu == 0 and lepton == MUON):
            # print "ERROR: event is malformed:", ev.numPh, ev.numEl, ev.numMu, lepton
            # sys.exit(1)
            continue

        if debug: print "Analizing event with Run =", ev.Run, ", Event =", ev.Event

        if filterPhotons and ev.numTruthPh > 0:
            continue

        if debug: print "  pass filterPhotons"

        met = math.hypot(ev.Metx, ev.Mety)
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

        lepIndex = 0

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

        if debug: print "  pass onlyStrong"

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
            indexLL = -1
            indexTL = -1
            indexLT = -1
            indexTT = -1
            for i in range(ev.numPh):
                if not doAltABCD:
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
                    if isTight(isem) and isIsolated(iso):
                        foundTT = True
                        if indexTT < 0:
                            indexTT = i
                    if isAntiTight(isem) and isIsolated(iso):
                        foundLT = True
                        if indexLT < 0:
                            indexLT = i
                    if isTight(isem) and isNotIsolated(iso):
                        foundTL = True
                        if indexTL < 0:
                            indexTL = i
                    if isAntiTight(isem) and isNotIsolated(iso):
                        foundLL = True
                        if indexLL < 0:
                            indexLL = i

            if debug: print "  foundTT=", foundTT, "foundTL=", foundTL, "foundLT=", foundLT, "foundLL=", foundLL

            #print "doABCD=", doABCD, "foundTT=", foundTT

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

        if debug: print "  passed ABCD, photonIndex =", photonIndex

        photon = ROOT.TLorentzVector()
        photon.SetPtEtaPhiM(ev.PhotonPt[photonIndex], ev.PhotonEta[photonIndex], ev.PhotonPhi[photonIndex], 0.0)
        if lepton == ELECTRON:
            electron = ROOT.TLorentzVector()
            electron.SetPtEtaPhiM(ev.ElectronPt[lepIndex], ev.ElectronEta[lepIndex], ev.ElectronPhi[lepIndex], 0.0)

        if plotsRegion != NO_SEL:

            # first the basic lepton and photon selection (but not MET and mT):
            if ((lepton == ELECTRON and
                 (ev.PhotonPt[photonIndex] < EL_PHPTCUT or abs(ev.PhotonEta[photonIndex]) > EL_PHETACUT or
                  ev.ElectronPt[lepIndex] < EL_ELPTCUT or abs(ev.ElectronEta[lepIndex]) > EL_ELETACUT)) or
                (lepton == MUON and
                 (ev.PhotonPt[photonIndex] < MU_PHPTCUT or abs(ev.PhotonEta[photonIndex]) > MU_PHETACUT or
                  ev.MuonPt[lepIndex] < MU_MUPTCUT or abs(ev.MuonEta[lepIndex]) > MU_MUETACUT))):
                continue

            # veto second lepton or Z window cut
            if lepton == ELECTRON and EL_MINV_WINDOW != 0:
                if photonIndex == 0 and lepIndex == 0:
                    minv = ev.PhElMinv
                else:
                    elph = electron + photon
                    minv = elph.M()
                    # print "**minv =", minv
                if ZMASS - EL_MINV_WINDOW < minv < ZMASS + EL_QCD_MINV_WINDOW:
                    continue

            if VETO_SECOND_LEPTON and ev.numMu + ev.numEl > 1:
                continue
            elif (lepton == ELECTRON and ev.numMu > 0 or
                  lepton == MUON and ev.numEl > 0):
                continue

            if (VETO_SECOND_SFLEPTON_MINV and
                (lepton == ELECTRON and ZMASS - EL_MINV_WINDOW < ev.ElMinv < ZMASS + EL_MINV_WINDOW) or
                (lepton == MUON and ZMASS - MU_MINV_WINDOW < ev.MuMinv < ZMASS + MU_MINV_WINDOW)):
                continue

            if (VETO_TRTSA_PHOTON_E_BLAYER and ev.numPh == 1 and
                ev.PhotonConvType[photonIndex] == 1 and ev.PhotonNumSi0[photonIndex] == 0 and
                ev.PhotonNumBEl[photonIndex]):
                continue

        if debug: print "  passed some presel"

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

        # scale the gj sampe to represent QCD
        if scaleQCD:
            if lepton == ELECTRON:
                weight *= Nqcd(1, ev.ElectronTight[lepIndex], ev.ElectronEta[lepIndex], lepton)
            else:
                weight *= Nqcd(1, ev.MuonTight[lepIndex], ev.MuonEta[lepIndex], lepton)


        if lepton == ELECTRON:
            if lepIndex != 0:
                mt = mT(ev.ElectronPt[lepIndex], ev.ElectronPhi[lepIndex], ev.Metx, ev.Mety)
            else:
                mt = ev.mTel
        else:
            mt = ev.mTmu

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

        # do CR counts
        if lepton == ELECTRON:
            if met < EL_QCD_MET_MAX and mt < EL_QCD_MT_MAX:
                if (ev.PhElMinv < ZMASS - EL_QCD_MINV_WINDOW or
                    ev.PhElMinv > ZMASS + EL_QCD_MINV_WINDOW):
                    # in QCD CR
                    inQCD = True
                    nQCD.Fill(0, weight)
                    if measureFakeAndEff and ev.ElectronTight[lepIndex]:
                        nQCDTight.Fill(0, weight)

            elif (EL_WCR_MET_MIN < met < EL_WCR_MET_MAX and
                  EL_WCR_MT_MIN < mt < EL_WCR_MT_MAX):
                inWCR = True
                nWCR.Fill(0, weight)
                if measureFakeAndEff and ev.ElectronTight[lepIndex]:
                    nWCRTight.Fill(0, weight)
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
                    if measureFakeAndEff and ev.MuonTight[lepIndex]:
                        nQCDTight.Fill(0, weight)
            elif (MU_WCR_MET_MIN < met < MU_WCR_MET_MAX and
                  MU_WCR_MT_MIN < mt < MU_WCR_MT_MAX):
                inWCR = True
                nWCR.Fill(0, weight)
                if measureFakeAndEff and ev.MuonTight[lepIndex]:
                    nWCRTight.Fill(0, weight)
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

            if plotsRegion != SR:  # think this is a bug, if statement not needed
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

            h_el_mInv.Fill(ev.ElMinv/GeV, weight)
            h_mu_mInv.Fill(ev.MuMinv/GeV, weight)

            h_meff.Fill(ev.meff/GeV, weight)
            h_HT.Fill(ev.HT/GeV, weight)

            if lepton == ELECTRON:
                h_ph_lep_deltaR.Fill(el_ph_deltaR, weight)
            else:
                h_ph_lep_deltaR.Fill(mu_ph_deltaR, weight)

            if ev.numPh >= 2:
                h_ph_pt2.Fill(ev.PhotonPt[1]/GeV, weight)
                h_ph_eta2.Fill(ev.PhotonEta[1], weight)
            h_ph_pt1.Fill(ev.PhotonPt[photonIndex]/GeV, weight)
            h_ph_eta1.Fill(ev.PhotonEta[photonIndex], weight)
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
    if measureFakeAndEff:
        print "  W+jets CR Yield (making tight req) =",nWCRTight.GetBinContent(1),"+-", nWCRTight.GetBinError(1)
    print "  ttbar CR Yield =",nTCR.GetBinContent(1),"+-", nTCR.GetBinError(1)
    print "  QCD CR Yield =",nQCD.GetBinContent(1),"+-", nQCD.GetBinError(1)
    if measureFakeAndEff:
        print "  QCD CR Yield (making tight req) =",nQCDTight.GetBinContent(1),"+-", nQCDTight.GetBinError(1)
        
    print "  XR1 Yield =",nXR1.GetBinContent(1),"+-", nXR1.GetBinError(1)
    print "  XR2 Yield =",nXR2.GetBinContent(1),"+-", nXR2.GetBinError(1)



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

    LepPhotonAnalysis(ttree, outfile, lepton, weight)


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

if __name__ == "__main__":
    main()

