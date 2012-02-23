#! /usr/bin/env python

# code to make all the plots in a file

import sys
import os.path
import getopt
import math

import ROOT
#ROOT.gROOT.LoadMacro("AtlasStyle.C") 
#ROOT.SetAtlasStyle()

ELECTRON = 0
MUON = 1

GeV = 1000

DEFAULTTTREE = 'GammaLepton'
DEFAULTWEIGHT = 1
DEFAULT_LEPTON = ELECTRON

DEFAULT_PATH = 

#Cuts
# - electron channel
EL_PHPTCUT = 85*GeV
EL_PHETACUT = 2.37
EL_ELPTCUT = 25*GeV
EL_ELETACUT = 2.47
EL_MET = 100*GeV
EL_MT = 100*GeV

# - muon channel
MU_PHPTCUT = 85*GeV
MU_PHETACUT = 2.37
MU_MUPTCUT = 25*GeV
MU_MUETACUT = 2.4
MU_MET = 100*GeV
MU_MT = 100*GeV

def usage():
    print " "
    print "Usage: %s [options] [inputFile.root]" % sys.argv[0]
    print " No input files means use default hardcoded inputs"
    print "  -o | --outfile    : name of the output root file (default <inputFile>Hist.root)"
    print "  -l | --lepton     : which lepton (default: '%s')" % DEFAULT_LEPTON
    print "  -t | --ttree      : name of the TTree/TChain"
    print "  -w | --weight     : global weight"
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"


def LepPhotonAnalysis(ttree, outfile, lepton, glWeight):

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
    h_ph_numConv = ROOT.TH1F("ph_numConv","Number of converted photons;number converted photons", 4, -0.5, 3.5)

    h_ph_eta1 = ROOT.TH1F("ph_eta1","Psuedorapidity of the leading photons;#eta_{reco}", 100, -3,3)
    h_ph_pt1 = ROOT.TH1F("ph_pt1","Transverse momentum of the leading photons;p_{T} [GeV]", 500, 0, 500)
    h_ph_eta2 = ROOT.TH1F("ph_eta2","Psuedorapidity of the second photons;#eta_{reco}", 100, -3,3)
    h_ph_pt2 = ROOT.TH1F("ph_pt2","Transverse momentum of the second photons;p_{T} [GeV]", 500, 0, 500)

    h_ph_ptB_unconv = ROOT.TH1F("ph_ptB_unconv","Transverse momentum of the unconverted Barrel photons;p_{T} [GeV]", 500, 0, 500)
    h_ph_ptEC_unconv = ROOT.TH1F("ph_ptEC_unconv","Transverse momentum of the unconverted EC photons;p_{T} [GeV]", 500, 0, 500)

    h_ph_ptB_conv = ROOT.TH1F("ph_ptB_conv","Transverse momentum of the converted Barrel photons;p_{T} [GeV]", 500, 0, 500)
    h_ph_ptEC_conv = ROOT.TH1F("ph_ptEC_conv","Transverse momentum of the converted EC photons;p_{T} [GeV]", 500, 0, 500)
    h_ph_el_minv = ROOT.TH1F("ph_el_minv", "The invariant mass of the leading photon and electron;M_{inv} [GeV]", 120, 0, 120)
    h_ph_mu_minv = ROOT.TH1F("ph_mu_minv", "The invariant mass of the leading photon and muon;M_{inv} [GeV]", 120, 0, 120)
    h_numPh = ROOT.TH1F("numPh", "The number of photons that pass cuts;N_{photons}", 9, -0.5, 8.5)

    ######## mudir
    mudir.cd()
    h_mu_eta1 = ROOT.TH1F("mu_eta1","Psuedorapidity of the leading muons;#eta_{reco}", 100, -3,3)
    h_mu_pt1 = ROOT.TH1F("mu_pt1","Transverse momentum of the leading muons;p_{T} [GeV]", 100, 0, 500)
    h_numMu = ROOT.TH1F("numMu", "The number of muons that pass cuts;N_{muons}", 9, -0.5, 8.5)

    ######## eldir
    eldir.cd()
    h_el_eta1 = ROOT.TH1F("el_eta1","Psuedorapidity of the leading electrons;#eta_{reco}", 100, -3,3)
    h_el_pt1 = ROOT.TH1F("el_pt1","Transverse momentum of the leading electrons;p_{T} [GeV]", 100, 0, 500)
    h_el_eta2 = ROOT.TH1F("el_eta2","Psuedorapidity of the second electrons;#eta_{reco}", 100, -3,3)
    h_el_pt2 = ROOT.TH1F("el_pt2","Transverse momentum of the second electrons;p_{T} [GeV]", 100, 0, 500)
    h_numEl = ROOT.TH1F("numEl", "The number of electrons that pass cuts;N_{electrons}", 9, -0.5, 8.5)

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
						  100, 0, math.pi, 250, 0, 250)

    h_deltaPhiElMETvsMET = ROOT.TH2F("deltaPhiElMETvsMET", 
						  "The DeltaPhi(Electron,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  100, 0, math.pi, 250, 0, 250)

    h_deltaPhiMuMETvsMET = ROOT.TH2F("deltaPhiMuMETvsMET", 
						  "The DeltaPhi(Muon,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  100, 0, math.pi, 250, 0, 250)
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

    ######## go back to root
    f.cd()


    for ev in ttree:
        # lets apply the cuts
        # double-check quality
        if ev.numPh == 0 or (ev.numEl == 0 and lepton == ELECTRON) or (ev.numMu == 0 and lepton == MUON):
            print "ERROR: event is malformed"
            sys.exit(1)

        met = math.hypot(ev.Metx, ev.Mety)
        #print "MET =", met, "lepton =", lepton, "ev.PhotonPt[0] = ", ev.PhotonPt[0]
        #print "weight =", ev.Weight * glWeight

        # first the basic lepton and photon selection (but not MET and mT):
        if ((lepton == ELECTRON and
             (ev.PhotonPt[0] < EL_PHPTCUT or abs(ev.PhotonEta[0]) > EL_PHETACUT or
              ev.ElectronPt[0] < EL_ELPTCUT or abs(ev.ElectronEta[0]) > EL_ELETACUT)) or
            (lepton == MUON and
             (ev.PhotonPt[0] < MU_PHPTCUT or abs(ev.PhotonEta[0]) > MU_PHETACUT or
              ev.MuonPt[0] < MU_MUPTCUT or abs(ev.MuonEta[0]) > MU_MUETACUT))):
            continue

        # now plots that should be made before MET and mT cuts
        h_mTelvsMET.Fill(met/GeV, ev.mTel/GeV, ev.Weight * glWeight)
        h_mTmuvsMET.Fill(met/GeV, ev.mTmu/GeV, ev.Weight * glWeight)

        # then make MET cut after mT and visa versa

        if ((lepton == ELECTRON and met > EL_MET) or
            (lepton == MUON and met > MU_MET)):
            h_mTel.Fill(ev.mTel/GeV, ev.Weight * glWeight)
            h_mTmu.Fill(ev.mTmu/GeV, ev.Weight * glWeight)

        if ((lepton == ELECTRON and ev.mTel > EL_MT) or
            (lepton == MUON and ev.mTmu > MU_MT)):
            h_met.Fill(met/GeV, ev.Weight * glWeight)
            

        ## our selection
        if ((lepton == ELECTRON and
             (met < EL_MET or ev.mTel < EL_MT)) or
            (lepton == MUON and
             (met < MU_MET or ev.mTmu < MU_MT))):
            continue


    f.Write()


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
        # use the default inputs
        outfile = "Hist.root"
    elif len(args) == 1:
        # use the input file
        infile = args[0]
        inFileNoPath = os.path.split(infile)[1]
        outfile = os.path.splitext(inFileNoPath)[0] + "Hist.root"
    elif len(args) > 1:
        print "ERROR: only one input file is used"
        usage()
        sys.exit(1)
        
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
        elif o in ("-2", "--weight"):
            weight = a
        elif o in ("-l", "--lepton"):
            if a == "electron":
                lepton = ELECTRON
            elif a == "muon":
                lepton = MUON
            else:
                print "*** Lepton must be 'electron' or 'muon ****"
                sys.exit(1)

    # let's get the TFile and outfile and call a new function
    if len(args) == 0:

    else:
        # use the input file
        f = ROOT.TFile(infile)
        ttree=f.Get(ttreeName)

    LepPhotonAnalysis(ttree, outfile, lepton, weight)

    
if __name__ == "__main__":
    main()
