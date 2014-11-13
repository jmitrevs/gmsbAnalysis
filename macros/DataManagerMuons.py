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

print "Lepton is MUON."
#path = "/data/jmitrevs/output/muphoton/v140912/mergedFiles/"
path = "/data/jmitrevs/output/muphoton/v141108/mergedFiles/"

# format is (name, xsec in pb, kfac, eff, dsid)
names = (('Wmunugamma', 0.71781, 1.0, 1.0, 126744),
         ('Wtaunugamma', 0.71925, 1.0, 1.0, 158727),
         ('dilep', 22.134, 1.1997, 1.0, 181087), 
         ('ttbargamma', 1.3963, 1.9, 7.0707E-02, 177998))

binToLookAt = 12 #1 more than last Fill value because this count starts at 1

values = {}

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
