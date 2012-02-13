#!/usr/bin/env python

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
sigYield = 80.2657
backYield = 30621.3

# This is using the pt25 cuts
#sigYield = 170.922
#sigYield = 42.42
#backYield = 226381

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

        print ibin, sig, back

        if back <= 0.0:
            back = 0.01

        if sig <= 0.0:
            signif = 0
        else:
            signif = math.sqrt(2 * ((sig + back) * math.log(1 + sig / back) - sig))

        hsig.SetBinContent(ibin+1, signif)

    return hsig


