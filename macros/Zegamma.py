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

def Zegamma(ttree, outfile, lepton):

    if not (lepton == ELECTRON):
        print "ERROR: only electron channel implemetned"
        return

    f = ROOT.TFile(outfile, 'RECREATE')


    ##########################
    # Create the histograms
    ##########################

    ee = ROOT.TH1D("ee","ee events;m_{inv} [GeV]", minv_bins, minv_low, minv_high)
    eg = ROOT.TH1D("eg","e#gamma events;m_{inv} [GeV]", minv_bins, minv_low, minv_high)

    ee1bin = ROOT.TH1D("ee1bin","eee events", 1, 0, 1)
    eg1bin = ROOT.TH1D("eg1bin","ee#gamma events", 1, 0, 1)

    fakeRate = ROOT.TH1D("fakeRate","", 1, 0, 1)

    h_ph_eta = ROOT.TH1F("ph_eta","Psuedorapidity of the leading photons;#eta_{reco};Events", 20, -3, 3)
    h_ph_pt = ROOT.TH1F("ph_pt","Transverse momentum of the leading photons;p_{T} [GeV];Events", 20, 0, 100)

    h_el_eta = ROOT.TH1F("el_eta","Psuedorapidity of the leading photons;#eta_{reco};Events", 20, -3, 3)
    h_el_pt = ROOT.TH1F("el_pt","Transverse momentum of the leading photons;p_{T} [GeV];Events", 20, 0, 100)

    ee.Sumw2()
    eg.Sumw2()
    ee1bin.Sumw2()
    eg1bin.Sumw2()

    for ev in ttree:
        # lets apply the cuts
        # double-check quality
        if ev.numEl <  1:
            continue

        #weight = glWeight * ev.Weight
        weight = 1.0  # don't currently support weights

        if removeCrack and (1.37 < abs(ev.ElectronEta2[0]) < 1.52):
            continue

        if ev.numEl > 1 and not (1.37 < abs(ev.ElectronEta2[1]) < 1.52):
            mass = ev.ElMinv
            ee.Fill(mass/GeV, weight)
            if abs(ZMASS - mass) < ZWINDOW:
                ee1bin.Fill(0, weight)
                h_el_eta.Fill(ev.ElectronEta[1], weight)
                h_el_pt.Fill(ev.ElectronPt[1]/GeV, weight)

        if ev.numPh > 0:
            mass = ev.PhElMinv
            eg.Fill(mass/GeV, weight)
            if abs(ZMASS - mass) < ZWINDOW:
                eg1bin.Fill(0, weight)
                h_ph_eta.Fill(ev.PhotonEta[0], weight)
                h_ph_pt.Fill(ev.PhotonPt[0]/GeV, weight)
                    

    fakeRate.Divide(eg1bin, ee1bin, 1.0, 2.0, "B")
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
    outfile = os.path.splitext(inFileNoPath)[0] + "_etog_Hist.root"
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
    Zegamma(ttree, outfile, lepton)

if __name__ == "__main__":
    main()
