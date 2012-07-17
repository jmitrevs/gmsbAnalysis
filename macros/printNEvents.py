#! /usr/bin/env python

'''
Module to store all the source files, yields, etc, for electron channel.
'''

from glob import glob
import sys
import ROOT
# ROOT.gROOT.LoadMacro("AtlasStyle.C") 
# ROOT.SetAtlasStyle()

PRINT_YIELDS = True

Lumi = 4812.34 # really electron only

print "Lepton is ELECTRON."
path = "/data3/jmitrevs/lepphoton/min_grid/mergedFiles/"

for mgl in range(0, 1600, 100):
    for mC1 in range(0, mgl, 50) + [mgl-20]:
        filelist = glob(path + 'wino_%d_%d.root' % (mgl, mC1))
        if len(filelist) > 1:
            print >> sys.stderr, "Something wrong: filelist has size", len(filelist)  
            sys.exit(1)
        if len(filelist) == 1:
            winoFileName = filelist[0]
            winoFile = ROOT.TFile(winoFileName)
            OrigStrongwino = winoFile.Get("Global/OrigStrong")
            keyWeak = "%.0f, %.0f, 0" % (mgl, mC1)
            keyStrong = "%.0f, %.0f, 1" % (mgl, mC1)
            nWeak = OrigStrongwino.GetBinContent(1)
            nStrong = OrigStrongwino.GetBinContent(2)
            print 'nOrigEvents["%s"] = %d' % (keyWeak, nWeak)
            print 'nOrigEvents["%s"] = %d' % (keyStrong, nStrong)
