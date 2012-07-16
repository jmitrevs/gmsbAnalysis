#! /usr/bin/env python

import math
import ROOT
ROOT.gROOT.SetBatch()
#ROOT.gROOT.LoadMacro("AtlasStyle.C") 
#ROOT.SetAtlasStyle()

class signalXsecs:
    def __init__(self, ttree):
        'This function returns the cross sections seprated between weak and strong'
        self.xsec = {}
        for ev in ttree:
            key = "%.0f, %.0f, %d" % (ev.mgl, ev.mC1, self.isStrong(ev.finalState))
            if key in self.xsec:
                self.xsec[key][0] += ev.crossSection
                self.xsec[key][1] += (ev.crossSection*ev.Tot_error)**2
            else:
                self.xsec[key] = [ev.crossSection, (ev.crossSection*ev.Tot_error)**2]
                
        # for key, item in self.xsec.items():
        #     print "%s & %.3f & %.3f \\\\" % (key, item[0], math.sqrt(item[1])/item[0])

    

    def isStrong(self, finalState):
        return finalState == 2

    def getXsec(self, mgl, mC1, isStrong):
        key = "%.0f, %.0f, %d" % (mgl, mC1, isStrong)
        return self.xsec[key][0]

    def getXsecRelError(self, mgl, mC1, isStrong):
        key = "%.0f, %.0f, %d" % (mgl, mC1, isStrong)
        return math.sqrt(self.xsec[key][1])/self.xsec[key][0]

if __name__ == "__main__":
    f = ROOT.TFile("output_gl_wino.root")
    ttree = f.Get("SignalUncertainties")
    signalXsecs(ttree)

        
