#! /usr/bin/env python

'''
Module to store all the source files, yields, etc, for electron channel.
'''

import math
import ROOT
# ROOT.gROOT.LoadMacro("AtlasStyle.C") 
# ROOT.SetAtlasStyle()

GeV = 1000.0
Lumi = 4812.34 # really electron only
DEFAULTTTREE = 'GammaLepton'
numEventTypes = 46

path = "/data3/jmitrevs/lepphoton/e_ntuple/mergedFiles/"

diphotonsSherpaFileName = path + "diphoton_Sherpa.root"
diphotonsSherpaFile = ROOT.TFile(diphotonsSherpaFileName)
cutFlowdiphotonsSherpa = diphotonsSherpaFile.Get("Global/CutFlow");
nOrigdiphotonsSherpa = cutFlowdiphotonsSherpa.GetBinContent(1)
print "\tnOrigdiphotonsSherpa =", nOrigdiphotonsSherpa

diphotonsPythiaFileName = path + "diphoton_Pythia.root"
diphotonsPythiaFile = ROOT.TFile(diphotonsPythiaFileName)
cutFlowdiphotonsPythia = diphotonsPythiaFile.Get("Global/CutFlow");
nOrigdiphotonsPythia = cutFlowdiphotonsPythia.GetBinContent(1)
print "\tnOrigdiphotonsPythia =", nOrigdiphotonsPythia

### k-factor of 1.2 is from diphoton group, but 1.4 with Higgs cuts?
diphotons_kfact = 1.2
# this is for the diphotons50
#diphotons50_scale = Lumi * 6.1162 * 8.7509E-01 * diphotons_kfact / nOrigdiphotons
# this is the pythia with radiative photons, too
diphotonsPythia_scale = Lumi * 1.3709E+05 * 6.0277E-04 * diphotons_kfact / nOrigdiphotonsPythia
# and the sherpa with radiative phtons
diphotonsSherpa_scale = Lumi * 4.5566E+02 * 1.7217E-01 * diphotons_kfact / nOrigdiphotonsSherpa

print "diphotonsScale =",diphotonsSherpa_scale

#########################################################
# let's print the yield before any cuts
#########################################################

binToLookAt = 12 #1 more than last Fill value because this count starts at 1

nAfterPreselectdiphotonsSherpa = cutFlowdiphotonsSherpa.GetBinContent(binToLookAt)
print "Yield diphotonsSherpa =", nAfterPreselectdiphotonsSherpa
nAfterPreselectdiphotonsPythia = cutFlowdiphotonsPythia.GetBinContent(binToLookAt)
print "Yield diphotonsPythia =", nAfterPreselectdiphotonsPythia

print "difference in yield =", (nAfterPreselectdiphotonsSherpa - nAfterPreselectdiphotonsPythia)/nAfterPreselectdiphotonsSherpa

DIPHOTON = 0
ASYMDIPHOTON = 1
PHOTONELECTRON = 2
ASYMPHOTONELECTRON = 3

def MakeName(filein, selection):
    if selection == DIPHOTON:
        return filein+"_dipho.root"
    if selection == ASYMDIPHOTON:
        return filein+"_asymdipho.root"
    if selection == PHOTONELECTRON:
        return filein+"_phoel.root"
    if selection == ASYMPHOTONELECTRON:
        return filein+"_asymphoel.root"

def DiphotonStudy(ttree, outfile, glWeight, selection):
    f = ROOT.TFile(outfile, 'RECREATE')

    nBinsEta = 30
    nBinsPt = 50
    nBinsHT = 75

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

    nSIG = ROOT.TH1F("nSIG", "Number of events in the SR", 1, 0, 1);

    for ev in ttree:
        if selection == DIPHOTON and ev.numPh < 2:
            continue
        elif selection == ASYMDIPHOTON and (ev.numPh < 2 or ev.PhotonPt[0] < 100*GeV):
            continue
        elif selection == PHOTONELECTRON and (ev.numPh < 1 or ev.numEl < 1):
            continue
        elif selection == ASYMPHOTONELECTRON and (ev.numPh < 1 or ev.numEl < 1 or ev.PhotonPt[0] < 100*GeV):
            continue
        
        weight = ev.Weight * glWeight

        photonIndex = 0
        lepIndex = 0
        if selection == PHOTONELECTRON or selection == ASYMPHOTONELECTRON:
            for i in range(ev.numEl):
                if not (1.37 < abs(ev.ElectronEta2[i]) < 1.52):
                    lepIndex = i
                    break
            else:
                # print "*** electron only in crack ***"
                continue

        photon = ROOT.TLorentzVector()
        photon.SetPtEtaPhiM(ev.PhotonPt[photonIndex], ev.PhotonEta[photonIndex], ev.PhotonPhi[photonIndex], 0.0)
        el_ph_deltaR = -1.0

        if selection == PHOTONELECTRON or selection == ASYMPHOTONELECTRON:
            electron = ROOT.TLorentzVector()
            electron.SetPtEtaPhiM(ev.ElectronPt[lepIndex], ev.ElectronEta[lepIndex], ev.ElectronPhi[lepIndex], 0.0)
            el_ph_deltaR = photon.DeltaR(electron)

        met = math.hypot(ev.Metx, ev.Mety)
        if lepIndex != 0:
            mt = mT(ev.ElectronPt[lepIndex], ev.ElectronPhi[lepIndex], ev.Metx, ev.Mety)
        else:
            mt = ev.mTel

        h_mTelvsMET.Fill(met/GeV, mt/GeV, weight)
        h_mTmuvsMET.Fill(met/GeV, mt/GeV, weight)

        nSIG.Fill(0, weight)

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

        h_el_mInv.Fill(ev.ElMinv/GeV, weight)
        h_mu_mInv.Fill(ev.MuMinv/GeV, weight)

        h_meff.Fill(ev.meff/GeV, weight)
        h_HT.Fill(ev.HT/GeV, weight)

        h_ph_lep_deltaR.Fill(el_ph_deltaR, weight)

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

    print "  Signal Yield =",nSIG.GetBinContent(1),"+-", nSIG.GetBinError(1)
    f.Write()


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
    for selection in range(4):
        print "***** Sherpa, selection =", selection,"*****"
        DiphotonStudy(diphotonsSherpaFile.Get(DEFAULTTTREE), 
                      MakeName(diphotonsSherpaFileName,selection), 
                      diphotonsSherpa_scale, selection)
        print
        print "***** Pythia, selection =", selection,"*****"
        DiphotonStudy(diphotonsPythiaFile.Get(DEFAULTTTREE), 
                      MakeName(diphotonsPythiaFileName,selection), 
                      diphotonsPythia_scale, selection)
        print
