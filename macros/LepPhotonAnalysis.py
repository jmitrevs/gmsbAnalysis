#! /usr/bin/env python

# code to make all the plots in a file

import sys
import os.path
import getopt
import math

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

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

printAccepted = False

# if the following is set to true, then no selections are made
ONLY_PRESEL = True

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

EL_WCR_MET_MIN = 25*GeV
EL_WCR_MET_MAX = 80*GeV
EL_WCR_MT_MIN = 40*GeV
EL_WCR_MT_MAX = 80*GeV

EL_TCR_MET_MIN = 55*GeV
EL_TCR_MET_MAX = 90*GeV
EL_TCR_MT_MIN =  100*GeV

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

MU_WCR_MET_MIN = 25*GeV
MU_WCR_MET_MAX = 80*GeV
MU_WCR_MT_MIN = 40*GeV
MU_WCR_MT_MAX = 80*GeV

MU_TCR_MET_MIN = 55*GeV
MU_TCR_MET_MAX = 90*GeV
MU_TCR_MT_MIN =  100*GeV

MU_QCD_MET_MAX = 20*GeV
MU_QCD_MT_MAX = 20*GeV

DELTAR_MU_PH = 0.7

VETO_SECOND_LEPTON = False
VETO_SECOND_SFLEPTON_MINV = False
VETO_TRTSA_PHOTON_E_BLAYER = True

def usage():
    print " "
    print "Usage: %s [options] inputFile.root" % sys.argv[0]    
    print "  -o | --outfile    : name of the output root file (default <inputFile>Hist.root)"
    print "  -l | --lepton     : which lepton (default: '%s')" % DEFAULT_LEPTON
    print "  -t | --ttree      : name of the TTree/TChain"
    print "  -w | --weight     : global weight"
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"


# measureEff is simple W tag and probe; numBackground is passed for iterative improvement.

def LepPhotonAnalysis(ttree, outfile, lepton, glWeight, filterPhotons = False, 
                      onlyStrong = False, 
                      measureFakeAndEff = False, 
                      numBkgTight = 0, scaleQCD = False,
                      applySF = NONE, applyTrigWeight = NONE,
                      onlyPreselection = ONLY_PRESEL):

    if not (lepton == ELECTRON or lepton == MUON):
        print "ERROR: The lepton must be ELECTRON or MUON"
        return

    f = ROOT.TFile(outfile, 'RECREATE')

    #print "glWeight = ", glWeight

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

    h_ph_eta1 = ROOT.TH1F("ph_eta1","Psuedorapidity of the leading photons;#eta_{reco}", 100, -3,3)
    h_ph_pt1 = ROOT.TH1F("ph_pt1","Transverse momentum of the leading photons;p_{T} [GeV]", 100, 0, 500)
    h_ph_eta2 = ROOT.TH1F("ph_eta2","Psuedorapidity of the second photons;#eta_{reco}", 100, -3,3)
    h_ph_pt2 = ROOT.TH1F("ph_pt2","Transverse momentum of the second photons;p_{T} [GeV]", 100, 0, 500)

    # h_ph_ptB_unconv = ROOT.TH1F("ph_ptB_unconv","Transverse momentum of the unconverted Barrel photons;p_{T} [GeV]", 500, 0, 500)
    # h_ph_ptEC_unconv = ROOT.TH1F("ph_ptEC_unconv","Transverse momentum of the unconverted EC photons;p_{T} [GeV]", 500, 0, 500)

    # h_ph_ptB_conv = ROOT.TH1F("ph_ptB_conv","Transverse momentum of the converted Barrel photons;p_{T} [GeV]", 500, 0, 500)
    # h_ph_ptEC_conv = ROOT.TH1F("ph_ptEC_conv","Transverse momentum of the converted EC photons;p_{T} [GeV]", 500, 0, 500)
    h_ph_el_minv = ROOT.TH1F("ph_el_minv", "The invariant mass of the leading photon and electron;M_{inv} [GeV]", 250, 0, 500)
    h_ph_mu_minv = ROOT.TH1F("ph_mu_minv", "The invariant mass of the leading photon and muon;M_{inv} [GeV]", 250, 0, 500)
    h_numPh = ROOT.TH1F("numPh", "The number of photons that pass cuts;N_{photons}", 9, -0.5, 8.5)

    h_ph_lep_deltaR = ROOT.TH1F("ph_lep_deltaR", "The delta-R beteween the lepton and the photon", 100, 0, 10)

    h_ph_ConvType = ROOT.TH1F("ph_ConvType", "The number of conversion tracks;N_{tracks}", 3, -0.5, 2.5)
    h_ph_numSi0 = ROOT.TH1F("ph_numSi0", "The number of Si hits in conversion track 0;N_{hits}", 30, -9.5, 20.5)
    h_ph_numSi1 = ROOT.TH1F("ph_numSi1", "The number of Si hits in conversion track 1;N_{hits}", 30, -9.5, 20.5)
    h_ph_numPix0 = ROOT.TH1F("ph_numPix0", "The number of PIX hits in conversion track 0;N_{hits}", 30, -9.5, 20.5)
    h_ph_numPix1 = ROOT.TH1F("ph_numPix1", "The number of PIX hits in conversion track 1;N_{hits}", 30, -9.5, 20.5)
    h_ph_numSiEl = ROOT.TH1F("ph_numSiEl", "The number of Si hits in electron track;N_{hits}", 30, -9.5, 20.5)
    h_ph_numPixEl = ROOT.TH1F("ph_numPixEl", "The number of PIX hits in electron track;N_{hits}", 30, -9.5, 20.5)
    h_ph_numBEl = ROOT.TH1F("ph_numBEl", "The number of PIX hits in electron track;N_{hits}", 30, -9.5, 20.5)
    h_ph_rejectStudies = ROOT.TH1F("ph_rejectStudies", "1 = Fail with BL, 2 = Fail with PIX", 30, -9.5, 20.5)


    ######## mudir
    mudir.cd()
    h_mu_eta1 = ROOT.TH1F("mu_eta1","Psuedorapidity of the leading muons;#eta_{reco}", 100, -3,3)
    h_mu_pt1 = ROOT.TH1F("mu_pt1","Transverse momentum of the leading muons;p_{T} [GeV]", 100, 0, 500)
    h_mu_eta2 = ROOT.TH1F("mu_eta2","Psuedorapidity of the second muons;#eta_{reco}", 100, -3,3)
    h_mu_pt2 = ROOT.TH1F("mu_pt2","Transverse momentum of the second muons;p_{T} [GeV]", 100, 0, 500)
    h_numMu = ROOT.TH1F("numMu", "The number of muons that pass cuts;N_{muons}", 9, -0.5, 8.5)
    h_mu_mInv = ROOT.TH1F("mu_mInv", "The invariant mass of leading muons;m_{inv} [GeV]", 120, 0, 120)

    ######## eldir
    eldir.cd()
    h_el_eta1 = ROOT.TH1F("el_eta1","Psuedorapidity of the leading electrons;#eta_{reco}", 100, -3,3)
    h_el_pt1 = ROOT.TH1F("el_pt1","Transverse momentum of the leading electrons;p_{T} [GeV]", 100, 0, 500)
    h_el_eta2 = ROOT.TH1F("el_eta2","Psuedorapidity of the second electrons;#eta_{reco}", 100, -3,3)
    h_el_pt2 = ROOT.TH1F("el_pt2","Transverse momentum of the second electrons;p_{T} [GeV]", 100, 0, 500)
    h_numEl = ROOT.TH1F("numEl", "The number of electrons that pass cuts;N_{electrons}", 9, -0.5, 8.5)
    h_el_mInv = ROOT.TH1F("el_mInv", "The invariant mass of leading electrons;m_{inv} [GeV]", 120, 0, 120)

    ######## jdir
    jdir.cd()
    h_numJets = ROOT.TH1F("numJets", "The number of jets that pass cuts;N_{jets}", 9, -0.5, 8.5)

    ######## MET
    mdir.cd()
    h_met = ROOT.TH1F("met", "The MET distribution;Etmiss [GeV]", 100, 0, 500)
    # h_met0J = ROOT.TH1F("met0J", "The MET distribution of events with zero jets;Etmiss [GeV]", 500, 0, 500)
    # h_met1J = ROOT.TH1F("met1J", "The MET distribution of events with one jet;Etmiss [GeV]", 500, 0, 500)
    # h_met2J = ROOT.TH1F("met2J", "The MET distribution of events with two jets;Etmiss [GeV]", 500, 0, 500)
    # h_met3J = ROOT.TH1F("met3J", "The MET distribution of events with three jets;Etmiss [GeV]", 500, 0, 500)
    # h_met4J = ROOT.TH1F("met4J", "The MET distribution of events with four jets;Etmiss [GeV]", 500, 0, 500)

    # h_metExtended = ROOT.TH1F("metExtended", "The MET distribution;Etmiss [GeV]", 250, 0, 1250)

    h_deltaPhiPhMETvsMET = ROOT.TH2F("deltaPhiPhMETvsMET", 
						  "The DeltaPhi(Photon,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  50, 0, math.pi, 20, 100, 300)

    h_deltaPhiElMETvsMET = ROOT.TH2F("deltaPhiElMETvsMET", 
						  "The DeltaPhi(Electron,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  50, 0, math.pi, 20, 100, 300)

    h_deltaPhiMuMETvsMET = ROOT.TH2F("deltaPhiMuMETvsMET", 
						  "The DeltaPhi(Muon,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  50, 0, math.pi, 20, 100, 300)
    ############ gldir
    gldir.cd()
    h_HT = ROOT.TH1F("HT", "The H_{T} distribution;H_{T} [GeV]", 300, 0, 1500)
    h_mTel = ROOT.TH1F("mTel", "The m_{T} distribution;m_{T} [GeV]", 100, 0, 500)
    h_mTmu = ROOT.TH1F("mTmu", "The m_{T} distribution;m_{T} [GeV]", 100, 0, 500)
    h_meff = ROOT.TH1F("meff", "The m_{eff} distribution;m_{eff} [GeV]", 300, 0, 1500)

    h_mTelvsMET = ROOT.TH2F("mTelvsMET", "m_{T} vs. MET;Etmiss [GeV];m_{T} [GeV]",
                            50, 0, 500, 50, 0, 500)
    h_mTmuvsMET = ROOT.TH2F("mTmuvsMET", "m_{T} vs. MET;Etmiss [GeV];m_{T} [GeV]",
                            50, 0, 500, 50, 0, 500)

    h_eventType = ROOT.TH1F("eventType", "The event type, based on truth;event type", 
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
            print "ERROR: event is malformed:", ev.numPh, ev.numEl, ev.numMu, lepton
            sys.exit(1)

        if filterPhotons and ev.numTruthPh > 0:
            continue

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

        if onlyStrong and not ev.isStrong:
            continue

        if not onlyPreselection:

            # first the basic lepton and photon selection (but not MET and mT):
            if ((lepton == ELECTRON and
                 (ev.PhotonPt[0] < EL_PHPTCUT or abs(ev.PhotonEta[0]) > EL_PHETACUT or
                  ev.ElectronPt[0] < EL_ELPTCUT or abs(ev.ElectronEta[0]) > EL_ELETACUT)) or
                (lepton == MUON and
                 (ev.PhotonPt[0] < MU_PHPTCUT or abs(ev.PhotonEta[0]) > MU_PHETACUT or
                  ev.MuonPt[0] < MU_MUPTCUT or abs(ev.MuonEta[0]) > MU_MUETACUT))):
                continue

            # veto second lepton or Z window cut
            if lepton == ELECTRON and EL_MINV_WINDOW != 0:
                if ZMASS - EL_MINV_WINDOW < ev.PhElMinv < ZMASS + EL_QCD_MINV_WINDOW:
                    continue

            if VETO_SECOND_LEPTON and ev.numMu + ev.numEl > 1:
                continue
            elif (lepton == ELECTRON and ev.numMu > 0 or
                  lepton == MUON and ev.numEl > 0):
                continue

            if (VETO_SECOND_SFLEPTON_MINV and
                (lepton == ELECTRON and ZMASS - EL_MINV_WINDOW < ev.ElMinv < ZMASS + EL_QCD_MINV_WINDOW) or
                (lepton == MUON and ZMASS - EL_MINV_WINDOW < ev.MuMinv < ZMASS + EL_QCD_MINV_WINDOW)):
                continue

            if (VETO_TRTSA_PHOTON_E_BLAYER and ev.numPh == 1 and
                ev.PhotonConvType[0] == 1 and ev.PhotonNumSi0[0] == 0 and
                ev.PhotonNumBEl[0]):
                continue

        photon = ROOT.TVector3()
        photon.SetPtEtaPhi(ev.PhotonPt[0], ev.PhotonEta[0], ev.PhotonPhi[0])
        if lepton == ELECTRON:
            electron = ROOT.TVector3()
            electron.SetPtEtaPhi(ev.ElectronPt[0], ev.ElectronEta[0], ev.ElectronPhi[0])
            el_ph_deltaR = photon.DeltaR(electron)
            if not onlyPreselection and el_ph_deltaR < DELTAR_EL_PH:
                continue
        else:
            muon = ROOT.TVector3()
            muon.SetPtEtaPhi(ev.MuonPt[0], ev.MuonEta[0], ev.MuonPhi[0])
            mu_ph_deltaR = photon.DeltaR(muon)
            if not onlyPreselection and mu_ph_deltaR < DELTAR_MU_PH:
                continue

        # scale the gj sampe to represent QCD
        if scaleQCD:
            if lepton == ELECTRON:
                weight *= Nqcd(1, ev.ElectronTight[0])
            else:
                weight *= Nqcd(1, ev.MuonTight[0])


        # now plots that should be made before MET and mT cuts
        h_mTelvsMET.Fill(met/GeV, ev.mTel/GeV, weight)
        h_mTmuvsMET.Fill(met/GeV, ev.mTmu/GeV, weight)

        # then make MET cut after mT and visa versa

        if not onlyPreselection:
            if ((lepton == ELECTRON and met > EL_MET) or
                (lepton == MUON and met > MU_MET)):
                h_mTel.Fill(ev.mTel/GeV, weight)
                h_mTmu.Fill(ev.mTmu/GeV, weight)

            if ((lepton == ELECTRON and ev.mTel > EL_MT) or
                (lepton == MUON and ev.mTmu > MU_MT)):
                h_met.Fill(met/GeV, weight)
        else:
            h_mTel.Fill(ev.mTel/GeV, weight)
            h_mTmu.Fill(ev.mTmu/GeV, weight)
            h_met.Fill(met/GeV, weight)
                

        inTCR = False
            
        # do CR counts
        if lepton == ELECTRON:
            if met < EL_QCD_MET_MAX and ev.mTel < EL_QCD_MT_MAX:
                if (ev.PhElMinv < ZMASS - EL_QCD_MINV_WINDOW or
                    ev.PhElMinv > ZMASS + EL_QCD_MINV_WINDOW):
                    # in QCD CR
                    nQCD.Fill(0, weight)
                    if measureFakeAndEff and ev.ElectronTight[0]:
                        nQCDTight.Fill(0, weight)

            elif (EL_WCR_MET_MIN < met < EL_WCR_MET_MAX and
                  EL_WCR_MT_MIN < ev.mTel < EL_WCR_MT_MAX):
                nWCR.Fill(0, weight)
                if measureFakeAndEff and ev.ElectronTight[0]:
                    nWCRTight.Fill(0, weight)
            elif (EL_TCR_MET_MIN < met < EL_TCR_MET_MAX and
                  EL_TCR_MT_MIN < ev.mTel):
                nTCR.Fill(0, weight)
                inTCR = True
        else:
            if met < MU_QCD_MET_MAX and ev.mTmu < MU_QCD_MT_MAX:
                if (ev.PhElMinv < ZMASS - MU_QCD_MINV_WINDOW or
                    ev.PhElMinv > ZMASS + MU_QCD_MINV_WINDOW):
                    nQCD.Fill(0, weight)
                    if measureFakeAndEff and ev.MuonTight[0]:
                        nQCDTight.Fill(0, weight)
            elif (MU_WCR_MET_MIN < met < MU_WCR_MET_MAX and
                  MU_WCR_MT_MIN < ev.mTmu < MU_WCR_MT_MAX):
                nWCR.Fill(0, weight)
                if measureFakeAndEff and ev.MuonTight[0]:
                    nWCRTight.Fill(0, weight)
            elif (MU_TCR_MET_MIN < met < MU_TCR_MET_MAX and
                  MU_TCR_MT_MIN < ev.mTmu):
                nTCR.Fill(0, weight)
                inTCR = True

        # do the XR
        if lepton == ELECTRON:
            if (EL_WCR_MET_MAX < met and
                EL_WCR_MT_MIN < ev.mTel < EL_WCR_MT_MAX):
                nXR2.Fill(0, weight)
            if (EL_WCR_MT_MAX < ev.mTel and
                EL_WCR_MET_MIN < met < EL_WCR_MET_MAX and
                not inTCR):
                nXR1.Fill(0, weight)
        else:
            if (MU_WCR_MET_MAX < met and
                MU_WCR_MT_MIN < ev.mTmu < MU_WCR_MT_MAX):
                nXR2.Fill(0, weight)
            if (MU_WCR_MT_MAX < ev.mTmu and
                MU_WCR_MET_MIN < met < MU_WCR_MET_MAX and
                not inTCR):
                nXR1.Fill(0, weight)


        ## our selection
        if not onlyPreselection:
            if ((lepton == ELECTRON and
                 (met < EL_MET or ev.mTel < EL_MT)) or
                (lepton == MUON and
                 (met < MU_MET or ev.mTmu < MU_MT))):
                continue

        # Accepted avent
        if printAccepted:
            print "Accepted event with Run =", ev.Run, ", Event =", ev.Event 
        nSIG.Fill(0, weight)
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
        if ev.PhotonConvType[0] == 0:
            # unconverted
            if ev.PhotonNumBEl[0] > 0:
                rejectStudies = 0
            elif ev.PhotonNumPixEl[0] > 0:
                rejectStudies = 1
            elif ev.PhotonNumSiEl[0] > 0:
                rejectStudies = 2
        elif ev.PhotonConvType[0] == 1 and ev.PhotonNumSi0[0] == 0:
            # TRTSA single-track
            isSame = (ev.PhotonNumSiEl[0] == ev.PhotonNumSi0[0] or
                      ev.PhotonNumPixEl[0] == ev.PhotonNumPix0[0])
            if ev.PhotonNumBEl[0] > 0:
                rejectStudies = 3
            elif not isSame:
                if ev.PhotonNumPixEl[0] > 0:
                    rejectStudies = 4
                elif ev.PhotonNumSiEl[0] > 0:
                    rejectStudies = 5
                else:
                    rejectStudies = 6
        elif ev.PhotonConvType[0] == 1:
            # Si single-track
            isSame = (ev.PhotonNumSiEl[0] == ev.PhotonNumSi0[0] or
                      ev.PhotonNumPixEl[0] == ev.PhotonNumPix0[0])
            if ev.PhotonNumBEl[0] > 0:
                rejectStudies = 7
            elif not isSame:
                if ev.PhotonNumPixEl[0] > 0:
                    rejectStudies = 8
                elif ev.PhotonNumSiEl[0] > 0:
                    rejectStudies = 9
                else:
                    rejectStudies = 10

        h_ph_rejectStudies.Fill(rejectStudies, weight)
        #h_ph_ConvType.Fill(ev.PhotonConvType[0], weight)
        h_ph_ConvType.Fill(ev.PhotonConvType[0], weight)
        h_ph_numSi0.Fill(ev.PhotonNumSi0[0], weight)
        h_ph_numSi1.Fill(ev.PhotonNumSi1[0], weight)
        h_ph_numPix0.Fill(ev.PhotonNumPix0[0], weight)
        h_ph_numPix1.Fill(ev.PhotonNumPix1[0], weight)
        h_ph_numSiEl.Fill(ev.PhotonNumSiEl[0], weight)
        h_ph_numPixEl.Fill(ev.PhotonNumPixEl[0], weight)
        h_ph_numBEl.Fill(ev.PhotonNumBEl[0], weight)

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
            h_ph_eta2.Fill(ev.PhotonEta[1]/GeV, weight)
        h_ph_pt1.Fill(ev.PhotonPt[0]/GeV, weight)
        h_ph_eta1.Fill(ev.PhotonEta[0]/GeV, weight)
        if ev.numEl >= 2:
            h_el_pt2.Fill(ev.ElectronPt[1]/GeV, weight)
            h_el_eta2.Fill(ev.ElectronEta[1], weight)
        if ev.numEl >= 1:
            h_el_pt1.Fill(ev.ElectronPt[0]/GeV, weight)
            h_el_eta1.Fill(ev.ElectronEta[0], weight)
        if ev.numMu >= 2:
            h_mu_pt2.Fill(ev.MuonPt[1]/GeV, weight)
            h_mu_eta2.Fill(ev.MuonEta[1], weight)
        if ev.numMu >= 1:
            h_mu_pt1.Fill(ev.MuonPt[0]/GeV, weight)
            h_mu_eta1.Fill(ev.MuonEta[0], weight)
        

    f.Write()
    print "**************************************"
    print "*****          YIELDS            *****"
    print "**************************************"
    print "  Signal Yield =",nSIG.GetBinContent(1),"+-", nSIG.GetBinError(1)
    print "  W+jets CR Yield =",nWCR.GetBinContent(1),"+-", nWCR.GetBinError(1)
    if measureFakeAndEff:
        print "  W+jets CR Yield (making tight req) =",nWCRTight.GetBinContent(1),"+-", nQCD.GetBinError(1)
    print "  ttbar CR Yield =",nTCR.GetBinContent(1),"+-", nTCR.GetBinError(1)
    print "  QCD CR Yield =",nQCD.GetBinContent(1),"+-", nQCD.GetBinError(1)
    if measureFakeAndEff:
        print "  QCD CR Yield (making tight req) =",nQCDTight.GetBinContent(1),"+-", nQCD.GetBinError(1)
        
    print "  XR1 Yield =",nXR1.GetBinContent(1),"+-", nXR1.GetBinError(1)
    print "  XR2 Yield =",nXR2.GetBinContent(1),"+-", nXR2.GetBinError(1)



    if measureFakeAndEff:
        fakeRate = nQCDTight.Clone()
        fakeRate.Divide(nQCDTight, nQCD, 1.0, 1.0, "B")
        print "**************************************"
        print "  jet to lepton fake rate =",fakeRate.GetBinContent(1),"+-",fakeRate.GetBinError(1)
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


#def Nqcd(nLoose, nTight, eps_sig = 0.93, eps_qcd = 0.23): # for electrons
def Nqcd(nLoose, nTight, eps_sig = 0.973, eps_qcd = 0.62): # for muons
    if eps_sig != eps_qcd:
        return eps_qcd*(1.0*eps_sig*nLoose - nTight)/(eps_sig - eps_qcd)
    else:
        raise ValueError("eps_sig = %f and eps_qcd = %f must be different" % (eps_sig,eps_qcd))
        return -1
    
if __name__ == "__main__":
    main()

