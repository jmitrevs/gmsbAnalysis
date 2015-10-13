#! /usr/bin/env python

from __future__ import division

import ROOT
#ROOT.gROOT.SetBatch()
#ROOT.gROOT.LoadMacro("AtlasStyle.C") 
#ROOT.SetAtlasStyle()

import sys
import math

TTREE = 'GammaLepton'

if len(sys.argv) != 2:
    print "Usage: %s <input file>" % sys.argv[0]
    sys.exit(1)

f = ROOT.TFile(sys.argv[1])
ttree=f.Get(TTREE)


form = ROOT.TTreeFormula('form', "sqrt(Metx**2 + Mety**2)", ttree)

for ev in ttree:
    #print "Metx =", ev.Metx,
    #print "Mety =", ev.Mety,
    #print "sqrt(Metx**2 + Mety**2) =", math.hypot(ev.Metx, ev.Mety),
    print "fomula =", form.EvalInstance()
