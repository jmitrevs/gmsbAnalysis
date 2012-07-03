#! /usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch()
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

def getSignalXsecs(ttree):
    print "mgl, mC1, finalState, crossSection, Tot_error, K"
    for ev in ttree:
        print ev.mgl, ev.mC1, ev.finalState, ev.crossSection, ev.Tot_error, ev.K

if __name__ == "__main__":
    f = ROOT.TFile("output_gl_wino.root")
    ttree = f.Get("SignalUncertainties")
    getSignalXsecs(ttree)

        
