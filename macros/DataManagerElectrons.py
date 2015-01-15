#! /usr/bin/env python
'''
Module to store all the source files, yields, etc, for electron channel.
'''

from __future__ import division

import ROOT
# ROOT.gROOT.LoadMacro("AtlasStyle.C") 
# ROOT.SetAtlasStyle()

PRINT_YIELDS = False

#Lumi = 4812.34 # old
#Lumi = 4816.68 # old (but done again)
Lumi = 20300.0

DOSTANDARD = True
DOSYST = True

print "Lepton is ELECTRON."
path = "/data/jmitrevs/output/elphoton/v141110/mergedFiles/"

# format is (name, xsec in pb, kfac, eff, dsid)
names = (('Wenugamma', 0.71925, 1.0, 1.0, 126741),
         ('Wtaunugamma', 0.71925, 1.0, 1.0, 158727),
         ('dilep', 22.134, 1.1997, 1.0, 181087), 
         ('ttbargamma', 1.3963, 1.9, 7.0707E-02, 177998),
         ('singletop_tchan', 25.748, 1.1043, 1.0, 110101),
         ('tW', 20.461, 1.0933, 1.0, 110140),
         ('singletop_tchan_gamma', 0.187298, 1.000000, 0.121980, 202621),
         ('singletop_tchan_gammaDec', 0.313866, 1.000000, 0.012927, 202622),
         ('tW_dilep_gamma', 0.012915, 1.000000, 0.164370, 202623),
         ('tW_dilep_gammatDec', 0.014538, 1.000000, 0.028748, 202624),
         ('tW_dilep_gammaWDec', 0.010405, 1.000000, 0.075489, 202625),
         ('tW_tlepWhad_gamma', 0.025825, 1.000000, 0.162440, 202626),
         ('tW_tlepWhad_gammatDec', 0.029084, 1.000000, 0.027609, 202627),
         ('tW_tlepWhad_gammaWDec', 0.011594, 1.000000, 0.064709, 202628),
         ('tW_thadWlep_gamma', 0.025817, 1.000000, 0.161780, 202629),
         ('tW_thadWlep_gammatDec', 0.020127, 1.000000, 0.041977, 202630),
         ('tW_thadWlep_gammaWDec', 0.020788, 1.000000, 0.075740, 202631)
         )

pathSyst = "/data/jmitrevs/output/elphoton/v141113_truth/mergedFiles/"
namesSyst = (('Wenugamma_ckkw15', 0.71925, 1.0, 1.0, 204731),
             ('Wenugamma_ckkw30', 0.71925, 1.0, 1.0, 204732),
             ('Wenugamma_fac025', 0.71925, 1.0, 1.0, 204733),
             ('Wenugamma_fac4', 0.71925, 1.0, 1.0, 204734),
             ('Wenugamma_renorm025', 0.71925, 1.0, 1.0, 204735),
             ('Wenugamma_renorm4', 0.71925, 1.0, 1.0, 204736),
             ('ttbargamma_nom', 1.3963, 1.9, 7.0707E-02, 177998),
             ('ttbargamma_scaleUP', 1.3963, 1.9, 7.0707E-02, 202332),
             ('ttbargamma_scaleDN', 1.3963, 1.9, 7.0707E-02, 202333),
             ('ttbargamma_alpsUP', 1.3963, 1.9, 7.0707E-02, 202334),
             ('ttbargamma_alpsDN', 1.3963, 1.9, 7.0707E-02, 202335),
             ('ttbargamma_lessFSR', 1.3963, 1.9, 7.0707E-02, 202336),
             ('ttbargamma_moreFSR', 1.3963, 1.9, 7.0707E-02, 202337)
             )

binToLookAt = 12 #1 more than last Fill value because this count starts at 1

values = {}

if DOSTANDARD:
    for i in range(len(names)):
        name = names[i][0]
        fileName = path + name + ".root"
        fl = ROOT.TFile(fileName)
        cutFlow = fl.Get("Global/CutFlow")
        nOrig = cutFlow.GetBinContent(1)

        xsec = names[i][1]
        kfac = names[i][2]
        eff = names[i][3]
        scale = Lumi * xsec * kfac * eff / nOrig
        nAfterPreselect = cutFlow.GetBinContent(binToLookAt)
        yd = nAfterPreselect * scale

        values[name] = (fl, scale)

        if PRINT_YIELDS:
            print "name: nOrig =", nOrig, "scale =", scale, "yield =", yd

if DOSYST:
    for i in range(len(namesSyst)):
        name = namesSyst[i][0]
        fileName = pathSyst + name + ".root"
        fl = ROOT.TFile(fileName)
        cutFlow = fl.Get("Global/CutFlow")
        nOrig = cutFlow.GetBinContent(1)

        xsec = namesSyst[i][1]
        kfac = namesSyst[i][2]
        eff = namesSyst[i][3]
        scale = Lumi * xsec * kfac * eff / nOrig
        nAfterPreselect = cutFlow.GetBinContent(binToLookAt)
        yd = nAfterPreselect * scale

        values[name] = (fl, scale)

        if PRINT_YIELDS:
            print "name: nOrig =", nOrig, "scale =", scale, "yield =", yd
