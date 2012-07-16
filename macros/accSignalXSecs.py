#! /usr/bin/env python

import math
import ROOT
ROOT.gROOT.SetBatch()
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

def accSignalXsecs(ttree):
    # print "mgl, mC1, finalState, crossSection, Tot_error, K"
    xsec = {}
    for ev in ttree:
        key = "%.0f, %.0f" % (ev.mgl, ev.mC1)
        if key in xsec:
            xsec[key][0] += ev.crossSection
            xsec[key][1] += (ev.crossSection*ev.Tot_error)**2
        else:
            xsec[key] = [ev.crossSection, (ev.crossSection*ev.Tot_error)**2]

    for key, item in xsec.items():
        print "%s & %.3f & %.3f \\\\" % (key, item[0], math.sqrt(item[1])/item[0])

if __name__ == "__main__":
    f = ROOT.TFile("output_gl_wino.root")
    ttree = f.Get("SignalUncertainties")
    accSignalXsecs(ttree)

        
