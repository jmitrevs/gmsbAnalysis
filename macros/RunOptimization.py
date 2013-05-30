#! /usr/bin/env python

from __future__ import division

# code to make all the plots in a file

import sys
import os.path
import getopt
import math

import ROOT
ROOT.gROOT.SetBatch()
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

from LepPhotonAnalysisOptimization import LepPhotonAnalysisOptimization, ELECTRON, MUON, GeV, DEFAULTTTREE


DEFAULT_LEPTON = ELECTRON
DEFAULT_SIGNAL = "800_500"

# optimization range
pts = [100, 110, 120, 125, 130, 140]
mts = [-100, 105, 110, 115, 120] 
mets = [100, 110, 120, 130, 140, 150, 160, 180, 200]
mt2s = [-100, 80, 90, 100, 110, 120]
hts = [-100, 200, 400, 600, 800, 1000] 
meffs = [-100, 200, 400, 600, 800, 1000] 

sigxsec = {}
# strong
sigxsec["800_500"] = 0.157
# weak
sigxsec["1500_100"] = 18.72
sigxsec["1500_200"] = 1.192
sigxsec["1500_300"] = 0.205
sigxsec["1500_350"] = 0.0992
sigxsec["1500_400"] = 0.0507


# Main routine
def main():

    try:
        # retrive command line options
        shortopts  = "l:s:vh?"
        longopts   = ["lepton=", "signal=", "verbose", "help", "usage"]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )

    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        usage()
        sys.exit(1)

    ttreeName = DEFAULTTTREE
    lepton = DEFAULT_LEPTON
    verbose     = False
    signal      = DEFAULT_SIGNAL
    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-s", "--signal"):
            signal = a
        elif o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-l", "--lepton"):
            if a == "electron":
                lepton = ELECTRON
            elif a == "muon":
                lepton = MUON
            else:
                print "*** Lepton must be 'electron' or 'muon ****"
                sys.exit(1)


 
   
    # let's open the input files
    if lepton == ELECTRON:

        print "Lepton is ELECTRON."
        sigpath = "/data3/jmitrevs/lepphoton_optimize/elphoton_grid/mergedFiles/"
        backpath = "/data3/jmitrevs/lepphoton_optimize/elphoton_ntuple/mergedFiles/"

        winoFileName = sigpath + "wino_" + signal + ".root"
        
        WgammaFileName = backpath + "Wgamma_enu_sherpa.root"
        ttbarFileName = backpath + "ttbar.root"
        ttbargammaFileName = backpath + "ttbargamma.root"


    elif lepton == MUON:

        raise ValueError("Muon not yet implemented.")


    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")

        
    ###########################################

    
    winoFile = ROOT.TFile(winoFileName)

    WgammaFile = ROOT.TFile(WgammaFileName)
    ttbarFile = ROOT.TFile(ttbarFileName)
    ttbargammaFile = ROOT.TFile(ttbargammaFileName)
    

    ###########################################

    
    cutFlowwino = winoFile.Get("Global/CutFlow")
    cutFlowWgamma = WgammaFile.Get("Global/CutFlow")
    cutFlowttbar = ttbarFile.Get("Global/CutFlow")
    cutFlowttbargamma = ttbargammaFile.Get("Global/CutFlow")

    nOrigwino = cutFlowwino.GetBinContent(1)
    nOrigWgamma = cutFlowWgamma.GetBinContent(1)
    nOrigttbar = cutFlowttbar.GetBinContent(1)
    nOrigttbargamma = cutFlowttbargamma.GetBinContent(1)

    ##############################

    winoTree = winoFile.Get("GammaLepton")
    WgammaTree = WgammaFile.Get("GammaLepton")
    ttbarTree = ttbarFile.Get("GammaLepton")
    ttbargammaTree = ttbargammaFile.Get("GammaLepton")

    ##############################################
    #   scale is lumi * xsec * kfact * filter / numEvents

    Lumi = 21000.0

    #wino_scale = Lumi * 18.72 * 0.23765 / nOrigwino # 100 weak
    #wino_scale = Lumi * 1.192 * 0.23765 / nOrigwino # 200 weak
    #wino_scale = Lumi * 0.205 * 0.23765 / nOrigwino # 300 weak
    #wino_scale = Lumi * 0.0992 * 0.23765 / nOrigwino # 350 weak
    #wino_scale = Lumi * 0.0507 * 0.23765 / nOrigwino # 400 weak
    #wino_scale = Lumi * 0.157 * 0.23765 / nOrigwino # 800_500 strong
    wino_scale = Lumi * sigxsec[signal] * 0.23765 / nOrigwino

    Wgamma_scale = Lumi * 5.5810E-01 * 1.43 / nOrigWgamma
    ttbar_scale          =  Lumi  *  79.01 * 1.146 * 1.43 / nOrigttbar
    ttbargamma_scale     =  Lumi  *  0.84 * 2.55 * 1.43 / nOrigttbargamma

    print " Optimization for", signal
    print
    print " pt   mt   met  mt2  ht  meff |  wino  Wgamma ttgamma  tt   sign"
    print "---- ---- ---- ---- ---- ----   ------ ------ ------ ------ ----"

    sys.stdout.flush()

    for mt2 in mt2s:
        for ht in hts:
            for meff in meffs:
                for pt in pts:
                    for mt in mts:
                        for met in mets:

                            wino = LepPhotonAnalysisOptimization(winoFile.Get(ttreeName), 
                                                                makeOutputName(winoFileName),
                                                                lepton,
                                                                wino_scale,
                                                                phPtCut = pt*GeV,
                                                                metCut = met*GeV,
                                                                mtCut = mt*GeV,
                                                                mt2Cut = mt2*GeV,
                                                                HTCut = ht*GeV,
                                                                meffCut = meff*GeV)[0]

                            Wgamma = LepPhotonAnalysisOptimization(WgammaFile.Get(ttreeName), 
                                                                makeOutputName(WgammaFileName, "_"+signal),
                                                                lepton,
                                                                Wgamma_scale,
                                                                phPtCut = pt*GeV,
                                                                metCut = met*GeV,
                                                                mtCut = mt*GeV,
                                                                mt2Cut = mt2*GeV,
                                                                HTCut = ht*GeV,
                                                                meffCut = meff*GeV)[0]

                            ttbar = LepPhotonAnalysisOptimization(ttbarFile.Get(ttreeName), 
                                                                makeOutputName(ttbarFileName, "_"+signal),
                                                                lepton,
                                                                ttbar_scale,
                                                                phPtCut = pt*GeV,
                                                                metCut = met*GeV,
                                                                mtCut = mt*GeV,
                                                                mt2Cut = mt2*GeV,
                                                                HTCut = ht*GeV,
                                                                meffCut = meff*GeV)[0]

                            ttbargamma = LepPhotonAnalysisOptimization(ttbargammaFile.Get(ttreeName), 
                                                                makeOutputName(ttbargammaFileName, "_"+signal),
                                                                lepton,
                                                                ttbargamma_scale,
                                                                phPtCut = pt*GeV,
                                                                metCut = met*GeV,
                                                                mtCut = mt*GeV,
                                                                mt2Cut = mt2*GeV,
                                                                HTCut = ht*GeV,
                                                                meffCut = meff*GeV)[0]

                            back = Wgamma + ttbar + ttbargamma

                            if back <= 0.0:
                                back = 0.01
                                
                            if wino <= 0.0:
                                signif = 0
                            else:
                                signif = math.sqrt(2 * ((wino + back) * math.log(1 + wino / back) - wino))
                                    
                            print "{0:>4} {1:>4} {2:>4} {3:>4} {4:>4} {5:>4}   {6:>6.1f} {7:>6.1f} {8:>6.1f} {9:>6.1f} {10:>4.1f}".format(pt, mt, met, mt2, ht, meff, wino, Wgamma, ttbargamma, ttbar, signif)

                            sys.stdout.flush()




def makeOutputName(infileName, extra = ""):
    inFileNoPath = os.path.split(infileName)[1]
    outfile = os.path.splitext(inFileNoPath)[0] + extra + "Hist.root"
    return outfile

if __name__ == "__main__":
    main()
