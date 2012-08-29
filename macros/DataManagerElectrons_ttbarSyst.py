#! /usr/bin/env python

'''
Module to store all the source files, yields, etc, for electron channel.
'''

import ROOT
# ROOT.gROOT.LoadMacro("AtlasStyle.C") 
# ROOT.SetAtlasStyle()

PRINT_YIELDS = True

Lumi = 4812.34 # really electron only

print "Lepton is ELECTRON."
#path = "/data3/jmitrevs/lepphoton/elphoton_ttbarSyst_noTrig/mergedFiles/"
path = "/data3/jmitrevs/lepphoton/elphoton_ttbarSyst/mergedFiles/"

ttbarFileName = path + "ttbar.root"
ttbar_ph_jmFileName = path + "ttbar_powheg_jimmy.root"
ttbar_ph_pyFileName = path + "ttbar_powheg_pythia.root"
ttbar_ac_mpsFileName = path + "ttbar_acer_moreps.root"
ttbar_ac_lpsFileName = path + "ttbar_acer_lessps.root"

ttbarFile = ROOT.TFile(ttbarFileName)
ttbar_ph_jmFile = ROOT.TFile(ttbar_ph_jmFileName)
ttbar_ph_pyFile = ROOT.TFile(ttbar_ph_pyFileName)
ttbar_ac_mpsFile = ROOT.TFile(ttbar_ac_mpsFileName)
ttbar_ac_lpsFile = ROOT.TFile(ttbar_ac_lpsFileName)

cutFlowttbar = ttbarFile.Get("Global/CutFlow")
cutFlowttbar_ph_jm = ttbar_ph_jmFile.Get("Global/CutFlow")
cutFlowttbar_ph_py = ttbar_ph_pyFile.Get("Global/CutFlow")
cutFlowttbar_ac_mps = ttbar_ac_mpsFile.Get("Global/CutFlow")
cutFlowttbar_ac_lps = ttbar_ac_lpsFile.Get("Global/CutFlow")

nOrigttbar = cutFlowttbar.GetBinContent(1)
nOrigttbar_ph_jm = cutFlowttbar_ph_jm.GetBinContent(1)
nOrigttbar_ph_py = cutFlowttbar_ph_py.GetBinContent(1)
nOrigttbar_ac_mps = cutFlowttbar_ac_mps.GetBinContent(1)
nOrigttbar_ac_lps = cutFlowttbar_ac_lps.GetBinContent(1)


if PRINT_YIELDS:
    ######################################################
    # let's print out the number of events for debugging
    print "Number of input events:"

    print "\tnOrigttbar =", nOrigttbar
    print "\tnOrigttbar_ph_jm =", nOrigttbar_ph_jm
    print "\tnOrigttbar_ph_py =", nOrigttbar_ph_py
    print "\tnOrigttbar_ac_mps =", nOrigttbar_ac_mps
    print "\tnOrigttbar_ac_lps =", nOrigttbar_ac_lps

    print

##############################################
#   scale is lumi * xsec * kfact * filter / numEvents

ttbarLepjetExtraScale = 1

ttbar_scale          =  Lumi  *  79.01 * 1.146 / nOrigttbar
ttbarLepjets_scale   =  Lumi  *  79.01 * 1.146 * ttbarLepjetExtraScale / nOrigttbar
ttbar_ph_jm_scale          =  Lumi  *  80.85 * 1.120 / nOrigttbar_ph_jm
ttbar_ph_jmLepjets_scale   =  Lumi  *  80.85 * 1.120 * ttbarLepjetExtraScale / nOrigttbar_ph_jm
ttbar_ph_py_scale          =  Lumi  *  80.07 * 1.131 / nOrigttbar_ph_py
ttbar_ph_pyLepjets_scale   =  Lumi  *  80.07 * 1.131 * ttbarLepjetExtraScale / nOrigttbar_ph_py
ttbar_ac_mps_scale          =  Lumi  * 61.96 * 1.462 / nOrigttbar_ac_mps
ttbar_ac_mpsLepjets_scale   =  Lumi  * 61.96 * 1.462 * ttbarLepjetExtraScale / nOrigttbar_ac_mps
ttbar_ac_lps_scale          =  Lumi  * 61.65 * 1.469 / nOrigttbar_ac_lps
ttbar_ac_lpsLepjets_scale   =  Lumi  * 61.65 * 1.469 * ttbarLepjetExtraScale / nOrigttbar_ac_lps

if PRINT_YIELDS:
    ##########################################################
    # let's print out the scales

    print "Scale (weight) for each sample:"
    
    print "\tttbar_scale =", ttbar_scale
    print "\tttbar_ph_jm_scale =", ttbar_ph_jm_scale
    print "\tttbar_ph_py_scale =", ttbar_ph_py_scale
    print "\tttbar_ac_mps_scale =", ttbar_ac_mps_scale
    print "\tttbar_ac_lps_scale =", ttbar_ac_lps_scale
    print

#########################################################
# let's print the yield before any cuts
#########################################################

binToLookAt = 12 #1 more than last Fill value because this count starts at 1

nAfterPreselectttbar = cutFlowttbar.GetBinContent(binToLookAt)
nAfterPreselectttbar_ph_jm = cutFlowttbar_ph_jm.GetBinContent(binToLookAt)
nAfterPreselectttbar_ph_py = cutFlowttbar_ph_py.GetBinContent(binToLookAt)
nAfterPreselectttbar_ac_mps = cutFlowttbar_ac_mps.GetBinContent(binToLookAt)
nAfterPreselectttbar_ac_lps = cutFlowttbar_ac_lps.GetBinContent(binToLookAt)

if PRINT_YIELDS:
    #############################################################
    # let's print out the yield after preselection
    print "Yield after Preselection:"

    print "Yield ttbar =", nAfterPreselectttbar * ttbar_scale
    print "Yield ttbar_ph_jm =", nAfterPreselectttbar_ph_jm * ttbar_ph_jm_scale
    print "Yield ttbar_ph_py =", nAfterPreselectttbar_ph_py * ttbar_ph_py_scale
    print "Yield ttbar_ac_mps =", nAfterPreselectttbar_ac_mps * ttbar_ac_mps_scale
    print "Yield ttbar_ac_lps =", nAfterPreselectttbar_ac_lps * ttbar_ac_lps_scale
