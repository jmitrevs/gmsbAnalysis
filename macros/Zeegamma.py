#! /usr/bin/env python

import sys
import os.path
import getopt
import math

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

import EfficiencyCalc


ELECTRON = 0
MUON = 1

GeV = 1000.0

NBINS_ETA = 26
NBINS_PHI = 10
NBINS_PT = 10

ETA_MAX = 2.6
PT_MAX = 200

minv_bins = 150
minv_low = 0
minv_high = 150

DEFAULTTTREE = 'GammaLepton'
DEFAULTWEIGHT = 1.0
DEFAULT_LEPTON = ELECTRON
DEFAULT_SUBB = False
DEFAULT_CALCULATE = False

removeCrack = True

ZMASS = 91.1876*GeV

ZWINDOW = 10.*GeV

MAXMET = 25*GeV

DELTAR = 0.0

def usage():
    print " "
    print "Usage: %s [options] inputFile.root" % sys.argv[0]    
    print "  -o | --outfile    : name of the output root file (default <inputFile>Hist.root)"
    print "  -l | --lepton     : which lepton (default: '%s') (or use -m or -e seperately)" % DEFAULT_LEPTON
    print "  -t | --ttree      : name of the TTree/TChain"
    #print "  -w | --weight     : global weight"
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"


# measureEff is simple W tag and probe; numBackground is passed for iterative improvement.

def Zeegamma(ttree, outfile, lepton):

    if not (lepton == ELECTRON):
        print "ERROR: only electron channel implemetned"
        return

    f = ROOT.TFile(outfile, 'RECREATE')


    ##########################
    # Create the histograms
    ##########################

    eee = ROOT.TH1D("eee","eee events;m_{inv} [GeV]", minv_bins, minv_low, minv_high)
    eeg = ROOT.TH1D("eeg","ee#gamma events;m_{inv} [GeV]", minv_bins, minv_low, minv_high)

    eee1bin = ROOT.TH1D("eee1bin","eee events", 1, 0, 1)
    eeg1bin = ROOT.TH1D("eeg1bin","ee#gamma events", 1, 0, 1)

    fakeRate = ROOT.TH1D("fakeRate","", 1, 0, 1)

    h_ph_eta = ROOT.TH1F("ph_eta","Psuedorapidity of the leading photons;#eta_{reco};Events", 20, -3, 3)
    h_ph_pt = ROOT.TH1F("ph_pt","Transverse momentum of the leading photons;p_{T} [GeV];Events", 20, 0, 100)

    h_el_eta = ROOT.TH1F("el_eta","Psuedorapidity of the leading photons;#eta_{reco};Events", 20, -3, 3)
    h_el_pt = ROOT.TH1F("el_pt","Transverse momentum of the leading photons;p_{T} [GeV];Events", 20, 0, 100)

    eee.Sumw2()
    eeg.Sumw2()
    eee1bin.Sumw2()
    eeg1bin.Sumw2()

    for ev in ttree:
        # lets apply the cuts
        # double-check quality
        if ev.numEl <  2:
            continue

        met = math.hypot(ev.Metx, ev.Mety)
        if met > MAXMET:
            continue

        #weight = glWeight * ev.Weight
        weight = 1.0  # don't currently support weights

        if removeCrack and (1.37 < abs(ev.ElectronEta2[0]) < 1.52 or 1.37 < abs(ev.ElectronEta2[1]) < 1.52):
            continue

        el0 = ROOT.TLorentzVector()
        el0.SetPtEtaPhiM(ev.ElectronPt[0], ev.ElectronEta[0], ev.ElectronPhi[0], 0.0)
        el1 = ROOT.TLorentzVector()
        el1.SetPtEtaPhiM(ev.ElectronPt[1], ev.ElectronEta[1], ev.ElectronPhi[1], 0.0)
        
        if el0.DeltaR(el1) < DELTAR:
            continue

        if ev.numEl > 2 and not (1.37 < abs(ev.ElectronEta2[2]) < 1.52):
            el2 = ROOT.TLorentzVector()
            el2.SetPtEtaPhiM(ev.ElectronPt[2], ev.ElectronEta[2], ev.ElectronPhi[2], 0.0)
            
            if el2.DeltaR(el0) > DELTAR and el2.DeltaR(el1) > DELTAR:
                total = el0 + el1 + el2

                mass = total.M()
                eee.Fill(mass/GeV, weight)
                
                if abs(ZMASS - mass) < ZWINDOW:
                    eee1bin.Fill(0, weight)
                    h_el_eta.Fill(ev.ElectronEta[2], weight)
                    h_el_pt.Fill(ev.ElectronPt[2]/GeV, weight)

        if ev.numPh > 0:
            ph = ROOT.TLorentzVector()
            ph.SetPtEtaPhiM(ev.PhotonPt[0], ev.PhotonEta[0], ev.PhotonPhi[0], 0.0)

            if ph.DeltaR(el0) > DELTAR and ph.DeltaR(el1) > DELTAR:
           
                total = el0 + el1 + ph
                
                mass = total.M()
                eeg.Fill(mass/GeV, weight)
                if abs(ZMASS - mass) < ZWINDOW:
                    eeg1bin.Fill(0, weight)
                    h_ph_eta.Fill(ev.PhotonEta[0], weight)
                    h_ph_pt.Fill(ev.PhotonPt[0]/GeV, weight)
                    

    fakeRate.Divide(eee1bin, eeg1bin, 1, 1, "B")
    print "***** Overal fake rate =", fakeRate.GetBinContent(1),"+-", fakeRate.GetBinError(1)
    f.Write()


# This function calls the LepPhotonAnalysis function 
def main():
    
    try:
        # retrive command line options
        shortopts  = "o:l:t:s:vmeh?"
        longopts   = ["outfile=", "lepton=", "ttree=", "help", "usage"]
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
    print "infile =",infile
    inFileNoPath = os.path.split(infile)[1]
    print "infileNoPath =",inFileNoPath
    outfile = os.path.splitext(inFileNoPath)[0] + "_gtoe_Hist.root"
    ttreeName = DEFAULTTTREE
    #weight = DEFAULTWEIGHT
    lepton = DEFAULT_LEPTON
    subBackground = DEFAULT_SUBB
    calculate = DEFAULT_CALCULATE

    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-o", "--outfile"):
            outfile = a
        elif o in ("-t", "--ttree"):
            ttreeName = a
        # elif o in ("-w", "--weight"):
        #     weight = float(a)
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

    print "outfile =", outfile
    Zeegamma(ttree, outfile, lepton)

if __name__ == "__main__":
    main()
