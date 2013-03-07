#!/usr/bin/env python

from __future__ import division

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

import math
import xml.dom.minidom

#fileName = 'Cuts_600_200_MET_pt.xml'
#fileName = 'Cuts_600_200_MET_pt_mT_pt25.xml'
#fileName = 'Cuts_600_200_MET_pt_mT.xml'
#fileName = 'Cuts_600_200_MET_pt_pt_mT.xml'
fileName = 'TMVAClassification_Cuts.weights.xml'


# this is using the pt50 cuts
#sigYield = 37
#sigYield = 80.2657
#backYield = 30621.3

# This is using the pt25 cuts
#sigYield = 170.922
#sigYield = 42.42
#backYield = 226381

# # 600_200
# sigYield = 207
# backYield = 3625

# # 1500_200
# sigYield = 226
# backYield = 3625

# # 1500_300
# sigYield = 42.0
# backYield = 3625

# # 1500_300 but with mT cut > 110 GeV
# sigYield = 26.2
# backYield = 342

# 1500_350
#sigYield = 19.9
#backYield = 3625

# 800_500
sigYield = 24.1
backYield = 3625

def GetSig():
    myfile = open(fileName, 'r')
    mystring = myfile.read()
    dom = xml.dom.minidom.parseString(mystring)

    xmlTag = dom.getElementsByTagName('Bin')

    sz = len(xmlTag)

    hsig = ROOT.TH1D("hsig", "Significance of cut", sz+1, 0, sz+1)

    for i in xmlTag:
        ibin = int(i.getAttribute('ibin'))
        sig = sigYield * float(i.getAttribute('effS'))
        back = backYield * float(i.getAttribute('effB'))


        if back <= 0.0:
            back = 0.01

        if sig <= 0.0:
            signif = 0
        else:
            signif = math.sqrt(2 * ((sig + back) * math.log(1 + sig / back) - sig))


        cuts = i.getElementsByTagName('Cuts')[0]

        print ibin, sig, back, signif, float(cuts.getAttribute('cutMin_0')), float(cuts.getAttribute('cutMin_1')), float(cuts.getAttribute('cutMin_2'))

        hsig.SetBinContent(ibin+1, signif)

    return hsig


