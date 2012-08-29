#! /usr/bin/env python

# code to make all the plots in a file
import sys
import getopt

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

import os.path
import TtbarSystAnalysis

removeOverlapTtbar = False
onlyStrong = False

ELECTRON = 0
MUON = 1

DEFAULTLEPTON = ELECTRON

def GetHistNames(inFile):
    
    histNames = []

    for key in inFile.GetListOfKeys():
        h = key.ReadObj()
        #dirItem = [key.ReadObj().ClassName(), key.GetName(), key.GetTitle()]
        #print dirItem
        if h.InheritsFrom("TDirectory"):
            newList = [key.GetName() + "/" + x for x in GetHistNames(key.ReadObj())]
            #print newList
            histNames.extend(newList)
        elif h.InheritsFrom("TH1"):
            histNames.append(key.GetName())

    return histNames

def makeOutputName(infileName, extra = ""):
    inFileNoPath = os.path.split(infileName)[1]
    outfile = os.path.splitext(inFileNoPath)[0] + extra + "Hist.root"
    return outfile

def RunAnalysis(lepton, plots, metType, ttbarSystType, doSeperate):

    print "ttbarSystType =",ttbarSystType


    if lepton == ELECTRON:
        import DataManagerElectrons_ttbarSyst as DataManager
    elif lepton == MUON:
        import DataManagerMuons_ttbarSyst as DataManager
    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")


    ttreeName = TtbarSystAnalysis.DEFAULTTTREE

    # print "ttbar:"
    # TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbarFile.Get(ttreeName), 
    #                                     makeOutputName(DataManager.ttbarFileName),
    #                                     lepton,
    #                                     DataManager.ttbar_scale,
    #                                     removeOverlapTtbar,
    #                                     applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots, ttbarSystType =  ttbarSystType)

    if doSeperate:
        print "ttbar (dilep):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbarFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbarFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.DILEP, metType = metType, ttbarSyst = ttbarSystType)

        print

        print "ttbar (lepjets):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbarFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbarFileName, "Lepjets"),
                                            lepton,
                                            DataManager.ttbarLepjets_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.LEPJETS, metType = metType, ttbarSyst = ttbarSystType)

        print

        print "ttbar_ph_jm (dilep):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ph_jmFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ph_jmFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_ph_jm_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.DILEP, ttbarSyst = ttbarSystType)

        print
        print "ttbar_ph_jm (lepjets):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ph_jmFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ph_jmFileName, "Lepjets"),
                                            lepton,
                                            DataManager.ttbar_ph_jmLepjets_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.LEPJETS, ttbarSyst = ttbarSystType)

        print

        print "ttbar_ph_py (dilep):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ph_pyFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ph_pyFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_ph_py_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.DILEP, ttbarSyst = ttbarSystType)

        print
        print "ttbar_ph_py (lepjets):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ph_pyFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ph_pyFileName, "Lepjets"),
                                            lepton,
                                            DataManager.ttbar_ph_pyLepjets_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.LEPJETS, ttbarSyst = ttbarSystType)

        print

        print "ttbar_ac_mps (dilep):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ac_mpsFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ac_mpsFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_ac_mps_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.DILEP, ttbarSyst = ttbarSystType)

        print
        print "ttbar_ac_mps (lepjets):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ac_mpsFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ac_mpsFileName, "Lepjets"),
                                            lepton,
                                            DataManager.ttbar_ac_mpsLepjets_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.LEPJETS, ttbarSyst = ttbarSystType)

        print

        print "ttbar_ac_lps (dilep):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ac_lpsFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ac_lpsFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_ac_lps_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.DILEP, ttbarSyst = ttbarSystType)

        print
        print "ttbar_ac_lps (lepjets):"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ac_lpsFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ac_lpsFileName, "Lepjets"),
                                            lepton,
                                            DataManager.ttbar_ac_lpsLepjets_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            tttype = TtbarSystAnalysis.LEPJETS, ttbarSyst = ttbarSystType)

        print
    else:
        print "ttbar:"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbarFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbarFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            metType = metType, ttbarSyst = ttbarSystType)

        print

        print "ttbar_ph_jm:"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ph_jmFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ph_jmFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_ph_jm_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            ttbarSyst = ttbarSystType)

        print
        print "ttbar_ph_py:"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ph_pyFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ph_pyFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_ph_py_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            ttbarSyst = ttbarSystType)

        print
        print "ttbar_ac_mps:"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ac_mpsFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ac_mpsFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_ac_mps_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            ttbarSyst = ttbarSystType)

        print
        print "ttbar_ac_lps:"
        TtbarSystAnalysis.TtbarSystAnalysis(DataManager.ttbar_ac_lpsFile.Get(ttreeName), 
                                            makeOutputName(DataManager.ttbar_ac_lpsFileName, "Dilep"),
                                            lepton,
                                            DataManager.ttbar_ac_lps_scale,
                                            removeOverlapTtbar,
                                            applySF=TtbarSystAnalysis.NOMINAL, applyTrigWeight=TtbarSystAnalysis.NOMINAL, plotsRegion=plots,
                                            ttbarSyst = ttbarSystType)

        print

if __name__ == "__main__":
    try:
        # retrive command line options
        shortopts  = "emlsp:a:"
        longopts   = ["lepton=", "plots=", "abcd=", "met=", "syst="]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )
    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        sys.exit(1)

    lepton = DEFAULTLEPTON
    plots = TtbarSystAnalysis.DEFAULT_PLOTS
    metType = TtbarSystAnalysis.MET_DEFAULT
    ttbarSystType = TtbarSystAnalysis.NONE

    doSeperate = False

    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-m"):
            lepton = MUON
        elif o in ("-e"):
            lepton = ELECTRON
        elif o in ("-s"):
            doSeperate = True
        elif o in ("-l", "--lepton"):
            if a == "electron":
                lepton = ELECTRON
            elif a == "muon":
                lepton = MUON
            else:
                print "*** Lepton must be 'electron' or 'muon ****"
                sys.exit(1)
        elif o in ("-p", "--plots"):
            if a == "NO_SEL":
                plots = TtbarSystAnalysis.NO_SEL
            elif a == "PRESEL":
                plots = TtbarSystAnalysis.PRESEL
            elif a == "SR":
                plots = TtbarSystAnalysis.SR
            elif a == "WCR":
                plots = TtbarSystAnalysis.WCR
            elif a == "TCR" or a == "HMT":
                plots = TtbarSystAnalysis.TCR
            elif a == "QCD":
                plots = TtbarSystAnalysis.QCD
            elif a == "XR1":
                plots = TtbarSystAnalysis.XR1
            elif a == "XR2" or a == "HMET":
                plots = TtbarSystAnalysis.XR2
            else:
                print "*** plots type unknown ****"
                sys.exit(1)
        elif o in ("--met"):
            if a == "nominal":
                metType = TtbarSystAnalysis.MET_DEFAULT
            elif a == "plus":
                metType = TtbarSystAnalysis.MET_PLUS
            elif a == "minus":
                metType = TtbarSystAnalysis.MET_MINUS
            elif a == "muon":
                metType = TtbarSystAnalysis.MET_MUON
            elif a == "full":
                metType = TtbarSystAnalysis.MET_FULL

        elif o in ("--syst"):
            if a == "none":
                ttbarSystType = TtbarSystAnalysis.NONE
            elif a == "nophoton":
                ttbarSystType = TtbarSystAnalysis.TTBAR_NOPHOTON
            elif a == "elasphoton":
                ttbarSystType = TtbarSystAnalysis.TTBAR_ELASPHOTON
            else:
                print "systematic of type",a,"not understood."
                sys.exit(1)

    RunAnalysis(lepton, plots, metType, ttbarSystType, doSeperate)
