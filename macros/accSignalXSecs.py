#! /usr/bin/env python

from __future__ import division

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
            xsec[key][2] += isStrong(ev.finalState) * ev.crossSection
        else:
            xsec[key] = [ev.crossSection, (ev.crossSection*ev.Tot_error)**2, 
                         isStrong(ev.finalState) * ev.crossSection]

    for key, item in xsec.items():
        print "%s & %.3f~~~ & %.1f\,\\%% & %.1f\,\\%% \\\\" % (key, item[0], 
                                                            math.sqrt(item[1])/item[0]*100, 
                                                            item[2]/item[0]*100)

def isStrong(finalState):
    return finalState == 2


if __name__ == "__main__":
    f = ROOT.TFile("output_gl_wino.root")
    ttree = f.Get("SignalUncertainties")
    accSignalXsecs(ttree)

        
