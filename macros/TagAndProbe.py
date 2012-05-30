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

def usage():
    print " "
    print "Usage: %s [options] inputFile.root" % sys.argv[0]    
    print "  -o | --outfile    : name of the output root file (default <inputFile>Hist.root)"
    print "  -l | --lepton     : which lepton (default: '%s') (or use -m or -e seperately)" % DEFAULT_LEPTON
    print "  -t | --ttree      : name of the TTree/TChain"
    #print "  -w | --weight     : global weight"
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"
    print "  -s | --subBackground : set to true or false"


# measureEff is simple W tag and probe; numBackground is passed for iterative improvement.

def TagAndProbe(ttree, outfile, lepton, calculate = True, subBack = True):

    if not (lepton == ELECTRON or lepton == MUON):
        print "ERROR: The lepton must be ELECTRON or MUON"
        return

    f = ROOT.TFile(outfile, 'RECREATE')

    ##########################
    # Create the histograms
    ##########################

    eff_num = ROOT.TH1F("eff_num","Numerator;m_{inv} [GeV]", minv_bins, minv_low, minv_high)
    eff_eta_num = ROOT.TH2F("eff_eta_num","Numerator vs. #eta;m_{inv} [GeV];#eta", minv_bins, minv_low, minv_high, NBINS_ETA, - ETA_MAX, ETA_MAX)
    eff_pt_num = ROOT.TH2F("eff_pt_num","Numerator vs. p_{T};m_{inv} [GeV];p_{T} [GeV]", minv_bins, minv_low, minv_high, NBINS_PT, 0, PT_MAX)
    eff_phi_num = ROOT.TH2F("eff_phi_num","Numerator vs. #phi;m_{inv} [GeV];#phi", minv_bins, minv_low, minv_high, NBINS_PHI, - math.pi, math.pi)

    eff_den = ROOT.TH1F("eff_den","Denominator;m_{inv} [GeV]", minv_bins, minv_low, minv_high)
    eff_eta_den = ROOT.TH2F("eff_eta_den","Denominator vs. #eta;m_{inv} [GeV];#eta", minv_bins, minv_low, minv_high, NBINS_ETA, - ETA_MAX, ETA_MAX)
    eff_pt_den = ROOT.TH2F("eff_pt_den","Denominator vs. p_{T};m_{inv} [GeV];p_{T} [GeV]", minv_bins, minv_low, minv_high, NBINS_PT, 0, PT_MAX)
    eff_phi_den = ROOT.TH2F("eff_phi_den","Denominator vs. #phi;m_{inv} [GeV];#phi", minv_bins, minv_low, minv_high, NBINS_PHI, - math.pi, math.pi)

    eff_eta_num.Sumw2()
    eff_pt_num.Sumw2()
    eff_phi_num.Sumw2()

    eff_eta_den.Sumw2()
    eff_pt_den.Sumw2()
    eff_phi_den.Sumw2()

    for ev in ttree:
        # lets apply the cuts
        # double-check quality
        if (ev.numEl <  2 and lepton == ELECTRON) or (ev.numMu < 2 and lepton == MUON):
            print "ERROR: event is malformed:", ev.numPh, ev.numEl, ev.numMu, lepton, doPhoton
            sys.exit(1)


        #weight = glWeight * ev.Weight
        weight = 1.0  # don't currently support weights

        if lepton == ELECTRON:
            for tag, probe in ((0, 1), (1, 0)):
                #print "tag, probe =",tag,",",probe
                if ev.ElectronTight[tag]:
                    eff_den.Fill(ev.ElMinv/GeV, weight)
                    eff_eta_den.Fill(ev.ElMinv/GeV, ev.ElectronEta[probe], weight)
                    eff_phi_den.Fill(ev.ElMinv/GeV, ev.ElectronPhi[probe], weight)
                    eff_pt_den.Fill(ev.ElMinv/GeV, ev.ElectronPt[probe]/GeV, weight)
                    if ev.ElectronTight[probe]:
                        eff_num.Fill(ev.ElMinv/GeV, weight)
                        eff_eta_num.Fill(ev.ElMinv/GeV, ev.ElectronEta[probe], weight)
                        eff_phi_num.Fill(ev.ElMinv/GeV, ev.ElectronPhi[probe], weight)
                        eff_pt_num.Fill(ev.ElMinv/GeV, ev.ElectronPt[probe]/GeV, weight)
        else:
            for tag, probe in ((0, 1), (1, 0)):
                #print "tag, probe =",tag,",",probe
                if ev.MuonTight[tag]:
                    eff_den.Fill(ev.MuMinv/GeV, weight)
                    eff_eta_den.Fill(ev.MuMinv/GeV, ev.MuonEta[probe], weight)
                    eff_phi_den.Fill(ev.MuMinv/GeV, ev.MuonPhi[probe], weight)
                    eff_pt_den.Fill(ev.MuMinv/GeV, ev.MuonPt[probe]/GeV, weight)
                    if ev.MuonTight[probe]:
                        eff_num.Fill(ev.MuMinv/GeV, weight)
                        eff_eta_num.Fill(ev.MuMinv/GeV, ev.MuonEta[probe], weight)
                        eff_phi_num.Fill(ev.MuMinv/GeV, ev.MuonPhi[probe], weight)
                        eff_pt_num.Fill(ev.MuMinv/GeV, ev.MuonPt[probe]/GeV, weight)


    if calculate:
        eff = ROOT.TH1F("eff","Efficiency", 1, 0, 1)
        eff_eta = ROOT.TH1F("eff_eta","Efficiency vs. #eta;#eta", NBINS_ETA, - ETA_MAX, ETA_MAX)
        eff_pt = ROOT.TH1F("eff_pt","Efficiency vs. p_{T};p_{T} [GeV]", NBINS_PT, 0, PT_MAX)
        eff_phi = ROOT.TH1F("eff_phi","Efficiency vs. #phi;#phi", NBINS_PHI, - math.pi, math.pi)

        eff_eta.Sumw2()
        eff_pt.Sumw2()
        eff_phi.Sumw2()

        intdir = f.mkdir("Internal")
        intdir.cd()
        EfficiencyCalc.calcEff(eff, eff_num, eff_den, subBack)
        EfficiencyCalc.calcEff(eff_eta, eff_eta_num, eff_eta_den, subBack)
        EfficiencyCalc.calcEff(eff_pt, eff_pt_num, eff_pt_den, subBack)
        EfficiencyCalc.calcEff(eff_phi, eff_phi_num, eff_phi_den, subBack)
        f.cd()

    f.Write()
    if calculate:
        print "***** Overal Eficiency =", eff.GetBinContent(1),"+-", eff.GetBinError(1)

# This function calls the LepPhotonAnalysis function 
def main():
    
    try:
        # retrive command line options
        shortopts  = "o:l:t:s:c:vmeh?"
        longopts   = ["outfile=", "lepton=", "ttree=", "help", "usage", "subBackground=", "calculate="]
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
        elif o in ("-s", "--subBackground"):
            if a == "0" or a == "false" or a == "False" or a == "FALSE":
                subBackground = False
            else:
                subBackground = True
        elif o in ("-c", "--calculate"):
            if a == "0" or a == "false" or a == "False" or a == "FALSE":
                calculate = False
            else:
                calculate = True
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

    TagAndProbe(ttree, outfile, lepton, calculate=calculate, subBack=subBackground)

if __name__ == "__main__":
    main()
