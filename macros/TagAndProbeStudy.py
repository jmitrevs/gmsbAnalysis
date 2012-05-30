#! /usr/bin/env python

import sys
import os.path
import getopt
import math

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

import EfficiencyCalc

NBINS_ETA = 26
NBINS_PHI = 10
NBINS_PT = 10

ETA_MAX = 2.6
PT_MAX = 200

DEFAULT_SUBB = False

def usage():
    print " "
    print "Usage: %s [options] inputFile.root" % sys.argv[0]    
    print "  -o | --outfile    : name of the output root file (default <inputFile>Hist.root)"
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"
    print "  -s | --subBackground : set to true or false"


# measureEff is simple W tag and probe; numBackground is passed for iterative improvement.

def TagAndProbeStudy(infile, outfile, subBack = True):

    fin = ROOT.TFile(infile)
    f = ROOT.TFile(outfile, 'RECREATE')

    ##########################
    # Create the histograms
    ##########################

    eff_num = fin.Get("eff_num")
    eff_eta_num = fin.Get("eff_eta_num")
    eff_pt_num = fin.Get("eff_pt_num")
    eff_phi_num = fin.Get("eff_phi_num")

    eff_den = fin.Get("eff_den")
    eff_eta_den = fin.Get("eff_eta_den")
    eff_pt_den = fin.Get("eff_pt_den")
    eff_phi_den = fin.Get("eff_phi_den")

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
    print "***** Overal Eficiency =", eff.GetBinContent(1),"+-", eff.GetBinError(1)

# This function calls the LepPhotonAnalysis function 
def main():
    
    try:
        # retrive command line options
        shortopts  = "o:s:vmeh?"
        longopts   = ["outfile=", "help", "usage", "subBackground="]
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
    outfile = os.path.splitext(inFileNoPath)[0] + "HistOut.root"
    subBackground = DEFAULT_SUBB

    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-o", "--outfile"):
            outfile = a
        elif o in ("-s", "--subBackground"):
            if a == "0" or a == "false" or a == "False" or a == "FALSE":
                subBackground = False
            else:
                subBackground = True

    TagAndProbeStudy(infile, outfile, subBack=subBackground)

if __name__ == "__main__":
    main()
