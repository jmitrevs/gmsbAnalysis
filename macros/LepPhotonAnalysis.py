#! /usr/bin/env python

# code to make all the plots in a file

import sys
import os.path
import getopt
import math

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

DEFAULTTTREE = 'GammaLepton'
DEFAULTWEIGHT = 1

GeV = 1000

def usage():
    print " "
    print "Usage: %s [options] inputFile.root" % sys.argv[0]    
    print "  -o | --outfile    : name of the output root file (default <inputFile>Hist.root)"
    print "  -t | --ttree      : name of the TTree/TChain"
    print "  -w | --weight     : global weight"
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"


def LepPhotonAnalysis(ttree, outfile, glWeight):

    f = ROOT.TFile(outfile, 'RECREATE')

    ##########################
    # Create the histograms
    ##########################

    h_ph_numConv = ROOT.TH1F("ph_numConv","Number of converted photons;number converted photons", 4, -0.5, 3.5)

    h_ph_eta1 = ROOT.TH1F("ph_eta1","Psuedorapidity of the leading photons;#eta_{reco}", 100, -3,3)
    h_ph_pt1 = ROOT.TH1F("ph_pt1","Transverse momentum of the leading photons;p_{T} [GeV]", 500, 0, 500)
    h_ph_eta2 = ROOT.TH1F("ph_eta2","Psuedorapidity of the second photons;#eta_{reco}", 100, -3,3)
    h_ph_pt2 = ROOT.TH1F("ph_pt2","Transverse momentum of the second photons;p_{T} [GeV]", 500, 0, 500)

    h_ph_ptB_unconv = ROOT.TH1F("ph_ptB_unconv","Transverse momentum of the unconverted Barrel photons;p_{T} [GeV]", 500, 0, 500)
    h_ph_ptEC_unconv = ROOT.TH1F("ph_ptEC_unconv","Transverse momentum of the unconverted EC photons;p_{T} [GeV]", 500, 0, 500)

    h_ph_ptB_conv = ROOT.TH1F("ph_ptB_conv","Transverse momentum of the converted Barrel photons;p_{T} [GeV]", 500, 0, 500)
    h_ph_ptEC_conv = ROOT.TH1F("ph_ptEC_conv","Transverse momentum of the converted EC photons;p_{T} [GeV]", 500, 0, 500)


    h_mu_eta1 = ROOT.TH1F("mu_eta1","Psuedorapidity of the leading muons;#eta_{reco}", 100, -3,3)
    h_mu_pt1 = ROOT.TH1F("mu_pt1","Transverse momentum of the leading muons;p_{T} [GeV]", 100, 0, 500)

    h_el_eta1 = ROOT.TH1F("el_eta1","Psuedorapidity of the leading electrons;#eta_{reco}", 100, -3,3)
    h_el_pt1 = ROOT.TH1F("el_pt1","Transverse momentum of the leading electrons;p_{T} [GeV]", 100, 0, 500)
    h_el_eta2 = ROOT.TH1F("el_eta2","Psuedorapidity of the second electrons;#eta_{reco}", 100, -3,3)
    h_el_pt2 = ROOT.TH1F("el_pt2","Transverse momentum of the second electrons;p_{T} [GeV]", 100, 0, 500)

    h_ph_el_minv = ROOT.TH1F("ph_el_minv", "The invariant mass of the leading photon and electron;M_{inv} [GeV]", 120, 0, 120)
    h_ph_mu_minv = ROOT.TH1F("ph_mu_minv", "The invariant mass of the leading photon and muon;M_{inv} [GeV]", 120, 0, 120)

    h_numPh = ROOT.TH1F("numPh", "The number of photons that pass cuts;N_{photons}", 9, -0.5, 8.5)
    h_numEl = ROOT.TH1F("numEl", "The number of electrons that pass cuts;N_{electrons}", 9, -0.5, 8.5)
    h_numMu = ROOT.TH1F("numMu", "The number of muons that pass cuts;N_{muons}", 9, -0.5, 8.5)
    h_numJets = ROOT.TH1F("numJets", "The number of jets that pass cuts;N_{jets}", 9, -0.5, 8.5)

    # MET
    h_met = ROOT.TH1F("met", "The MET distribution;Etmiss [GeV]", 500, 0, 500)
    h_met0J = ROOT.TH1F("met0J", "The MET distribution of events with zero jets;Etmiss [GeV]", 500, 0, 500)
    h_met1J = ROOT.TH1F("met1J", "The MET distribution of events with one jet;Etmiss [GeV]", 500, 0, 500)
    h_met2J = ROOT.TH1F("met2J", "The MET distribution of events with two jets;Etmiss [GeV]", 500, 0, 500)
    h_met3J = ROOT.TH1F("met3J", "The MET distribution of events with three jets;Etmiss [GeV]", 500, 0, 500)
    h_met4J = ROOT.TH1F("met4J", "The MET distribution of events with four jets;Etmiss [GeV]", 500, 0, 500)

    h_metExtended = ROOT.TH1F("metExtended", "The MET distribution;Etmiss [GeV]", 250, 0, 1250)

    h_deltaPhiPhMETvsMET = ROOT.TH2F("deltaPhiPhMETvsMET", 
						  "The DeltaPhi(Photon,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  100, 0, math.pi, 250, 0, 250)

    h_deltaPhiElMETvsMET = ROOT.TH2F("deltaPhiElMETvsMET", 
						  "The DeltaPhi(Electron,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  100, 0, math.pi, 250, 0, 250)

    h_deltaPhiMuMETvsMET = ROOT.TH2F("deltaPhiMuMETvsMET", 
						  "The DeltaPhi(Muon,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  100, 0, math.pi, 250, 0, 250)

    h_HT = ROOT.TH1F("HT", "The H_{T} distribution;H_{T} [GeV]", 300, 0, 1500)
    h_mTel = ROOT.TH1F("mTel", "The m_{T} distribution;m_{T} [GeV]", 500, 0, 500)
    h_mTmu = ROOT.TH1F("mTmu", "The m_{T} distribution;m_{T} [GeV]", 500, 0, 500)
    h_meff = ROOT.TH1F("meff", "The m_{eff} distribution;m_{eff} [GeV]", 300, 0, 1500)

    count = 0
    for ev in ttree:
        count += 1
        met = math.hypot(ev.Metx, ev.Mety)/GeV
        print count, met, ev.Weight, glWeight
        h_met.Fill(met, ev.Weight * glWeight)

    f.Write()


# This function calls the LepPhotonAnalysis function 
def main():
    
    try:
        # retrive command line options
        shortopts  = "o:t:w:vh?"
        longopts   = ["outfile=", "ttree=", "weight=", "help", "usage"]
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

    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-o", "--outfile"):
            outfile = a
        elif o in ("-t", "--ttree"):
            ttreeName = a
        elif o in ("-2", "--weight"):
            weight = a

    # let's get the TFile and outfile and call a new function

    f = ROOT.TFile(infile)
    ttree=f.Get(ttreeName)

    LepPhotonAnalysis(ttree, outfile, weight)

    
if __name__ == "__main__":
    main()
