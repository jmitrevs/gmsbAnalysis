#! /usr/bin/env python

from __future__ import division

import sys
import os.path
import getopt
import math

import ROOT

ELECTRON = 0
MUON = 1

GeV = 1000.0

PT_MIN = 20*GeV
#ZMASS = 91.1876*GeV
ZMASS = 90*GeV
ZMASS_WINDOW = 10*GeV

DEFAULTTTREE = 'susy'
DEFAULT_LEPTON = ELECTRON

def usage():
    print " "
    print "Usage: %s [options] inputFile.root" % sys.argv[0]    
    print "  -l | --lepton     : which lepton (default: '%s') (or use -m or -e seperately)" % DEFAULT_LEPTON
    print "  -t | --ttree      : name of the TTree/TChain"
    #print "  -w | --weight     : global weight"
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"


# measureEff is simple W tag and probe; numBackground is passed for iterative improvement.

def TagAndProbe(ttree, lepton):

    if not (lepton == ELECTRON or lepton == MUON):
        print "ERROR: The lepton must be ELECTRON or MUON"
        return

    numProbes = 0
    numProbesPass = 0

    numEvents = 0
    numEventsWithTwo = 0
    numEventsWithTwoAndMinv = 0

    for ev in ttree:
        # take the two leading leptons that pass at least probe criteria
        # (can simplify if you skim on events that pass probe criteria and
        # that are also pT sorted)

        #[0] is leading, [1] is second

        lepIndices = [-1, -1]
        lepPts = [-1.0, -1.0]

        numEvents+=1

        if lepton == ELECTRON:

            for i in range(ev.el_n):
                if passProbeElectron(ev, i):
                    pt = ev.el_pt[i]
                    if pt > lepPts[0]:
                        lepIndices[1] = lepIndices[0]
                        lepPts[1] = lepPts[0]
                        lepIndices[0] = i
                        lepPts[0] = pt
                    elif pt > lepPts[1]:
                        lepIndices[1] = i
                        lepPts[1] = pt
            
            if lepIndices[1] != -1:

                numEventsWithTwo+=1

                # if lepIndices[1] < lepIndices[0]:
                #     print '**** unsorted ****', lepPts

                # have at least two electrons
                electrons = [ROOT.TLorentzVector(ev.el_px[lepIndices[0]], ev.el_py[lepIndices[0]], 
                                                 ev.el_pz[lepIndices[0]], ev.el_E[lepIndices[0]]),
                             ROOT.TLorentzVector(ev.el_px[lepIndices[1]], ev.el_py[lepIndices[1]], 
                                                 ev.el_pz[lepIndices[1]], ev.el_E[lepIndices[1]])]
                
                # calculate the inv mass
                sum = electrons[0] + electrons[1]
                minv = sum.M()

                if abs(minv-ZMASS) < ZMASS_WINDOW:

                    numEventsWithTwoAndMinv+=1

                    for tag, probe in ((0, 1), (1, 0)):
                        if passTagElectron(ev, lepIndices[tag]):
                            numProbes += 1
                            if  passTestCutElectron(ev, lepIndices[probe]):
                                numProbesPass += 1

        else:
            print "Only implemented for electrons so far"
            sys.exit(1)


    eff = numProbesPass/numProbes # note I am using the float division, not int division (because from future)
    print "Number Events:", numEvents
    print "Number Events with two or more loose electorns:", numEventsWithTwo
    print "Number Events that pass mInv:", numEventsWithTwoAndMinv
    print "Number Probes:", numProbes
    print "Number Passing Probes:", numProbesPass
    print "***** Overal Eficiency =", eff

def passProbeElectron(ev, i):
    return ev.el_loosePP[i] and ev.el_pt[i] > PT_MIN and not (1.37 < abs(ev.el_etas2[i]) < 1.52)

# note, NOT THE FULL "official" definition 
def passTestCutElectron(ev, i):
    return ev.el_mediumPP[i] and ev.el_ptcone30[i] <  0.16 * ev.el_pt[i]

# this should also have trigger
def passTagElectron(ev, i):
    return ev.el_mediumPP[i] and ev.el_ptcone30[i] <  0.16 * ev.el_pt[i]


# This function calls the LepPhotonAnalysis function 
def main():
    
    try:
        # retrive command line options
        shortopts  = "l:t:vmeh?"
        longopts   = ["lepton=", "ttree=", "help", "usage"]
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
    ttreeName = DEFAULTTTREE
    #weight = DEFAULTWEIGHT
    lepton = DEFAULT_LEPTON

    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
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

    TagAndProbe(ttree, lepton)

if __name__ == "__main__":
    main()
