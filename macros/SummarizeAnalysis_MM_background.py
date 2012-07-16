#! /usr/bin/env python

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

Zjets = ROOT.TFile("ZjetsHist.root")
Zgamma = ROOT.TFile("ZgammaHist.root")
diphotons = ROOT.TFile("diphotonsHist.root")
total = ROOT.TFile("total.root")

ZjetsSR = Zjets.Get("nSIG")
ZgammaSR = Zgamma.Get("nSIG")
diphotonsSR = diphotons.Get("nSIG")
totalSR = total.Get("nSIG")

ZjetsWCR = Zjets.Get("nWCR")
ZgammaWCR = Zgamma.Get("nWCR")
diphotonsWCR = diphotons.Get("nWCR")
totalWCR = total.Get("nWCR")

ZjetsWCRTight = Zjets.Get("nWCRTight")
ZgammaWCRTight = Zgamma.Get("nWCRTight")
diphotonsWCRTight = diphotons.Get("nWCRTight")
totalWCRTight = total.Get("nWCRTight")

ZjetsTCR = Zjets.Get("nTCR")
ZgammaTCR = Zgamma.Get("nTCR")
diphotonsTCR = diphotons.Get("nTCR")
totalTCR = total.Get("nTCR")

ZjetsQCD = Zjets.Get("nQCD")
ZgammaQCD = Zgamma.Get("nQCD")
diphotonsQCD = diphotons.Get("nQCD")
totalQCD = total.Get("nQCD")

ZjetsQCDTight = Zjets.Get("nQCDTight")
ZgammaQCDTight = Zgamma.Get("nQCDTight")
diphotonsQCDTight = diphotons.Get("nQCDTight")
totalQCDTight = total.Get("nQCDTight")

ZjetsXR1 = Zjets.Get("nXR1")
ZgammaXR1 = Zgamma.Get("nXR1")
diphotonsXR1 = diphotons.Get("nXR1")
totalXR1 = total.Get("nXR1")

ZjetsXR2 = Zjets.Get("nXR2")
ZgammaXR2 = Zgamma.Get("nXR2")
diphotonsXR2 = diphotons.Get("nXR2")
totalXR2 = total.Get("nXR2")

print "*****************************"
print "****         SR        ******"
print "*****************************"
print "Zjets =", ZjetsSR.GetBinContent(1),"+-", ZjetsSR.GetBinError(1)
print "Zgamma =", ZgammaSR.GetBinContent(1),"+-", ZgammaSR.GetBinError(1)
print "gamma+jet =", diphotonsSR.GetBinContent(1),"+-", diphotonsSR.GetBinError(1)
print "total =", totalSR.GetBinContent(1),"+-", totalSR.GetBinError(1)

print "*****************************"
print "****         WCR        ******"
print "*****************************"
print "Zjets =", ZjetsWCR.GetBinContent(1),"+-", ZjetsWCR.GetBinError(1)
print "Zgamma =", ZgammaWCR.GetBinContent(1),"+-", ZgammaWCR.GetBinError(1)
print "gamma+jet =", diphotonsWCR.GetBinContent(1),"+-", diphotonsWCR.GetBinError(1)
print "total =", totalWCR.GetBinContent(1),"+-", totalWCR.GetBinError(1)

print "*****************************"
print "****      WCRtight     ******"
print "*****************************"
print "Zjets =", ZjetsWCRTight.GetBinContent(1),"+-", ZjetsWCRTight.GetBinError(1)
print "Zgamma =", ZgammaWCRTight.GetBinContent(1),"+-", ZgammaWCRTight.GetBinError(1)
print "gamma+jet =", diphotonsWCRTight.GetBinContent(1),"+-", diphotonsWCRTight.GetBinError(1)
print "total =", totalWCRTight.GetBinContent(1),"+-", totalWCRTight.GetBinError(1)

print "*****************************"
print "****         TCR        ******"
print "*****************************"
print "Zjets =", ZjetsTCR.GetBinContent(1),"+-", ZjetsTCR.GetBinError(1)
print "Zgamma =", ZgammaTCR.GetBinContent(1),"+-", ZgammaTCR.GetBinError(1)
print "gamma+jet =", diphotonsTCR.GetBinContent(1),"+-", diphotonsTCR.GetBinError(1)
print "total =", totalTCR.GetBinContent(1),"+-", totalTCR.GetBinError(1)

print "*****************************"
print "****         QCD        ******"
print "*****************************"
print "Zjets =", ZjetsQCD.GetBinContent(1),"+-", ZjetsQCD.GetBinError(1)
print "Zgamma =", ZgammaQCD.GetBinContent(1),"+-", ZgammaQCD.GetBinError(1)
print "gamma+jet =", diphotonsQCD.GetBinContent(1),"+-", diphotonsQCD.GetBinError(1)
print "total =", totalQCD.GetBinContent(1),"+-", totalQCD.GetBinError(1)

print "*****************************"
print "****      QCDTight     ******"
print "*****************************"
print "Zjets =", ZjetsQCDTight.GetBinContent(1),"+-", ZjetsQCDTight.GetBinError(1)
print "Zgamma =", ZgammaQCDTight.GetBinContent(1),"+-", ZgammaQCDTight.GetBinError(1)
print "gamma+jet =", diphotonsQCDTight.GetBinContent(1),"+-", diphotonsQCDTight.GetBinError(1)
print "total =", totalQCDTight.GetBinContent(1),"+-", totalQCDTight.GetBinError(1)

print "*****************************"
print "****         XR1       ******"
print "*****************************"
print "Zjets =", ZjetsXR1.GetBinContent(1),"+-", ZjetsXR1.GetBinError(1)
print "Zgamma =", ZgammaXR1.GetBinContent(1),"+-", ZgammaXR1.GetBinError(1)
print "gamma+jet =", diphotonsXR1.GetBinContent(1),"+-", diphotonsXR1.GetBinError(1)
print "total =", totalXR1.GetBinContent(1),"+-", totalXR1.GetBinError(1)

print "*****************************"
print "****         XR2       ******"
print "*****************************"
print "Zjets =", ZjetsXR2.GetBinContent(1),"+-", ZjetsXR2.GetBinError(1)
print "Zgamma =", ZgammaXR2.GetBinContent(1),"+-", ZgammaXR2.GetBinError(1)
print "gamma+jet =", diphotonsXR2.GetBinContent(1),"+-", diphotonsXR2.GetBinError(1)
print "total =", totalXR2.GetBinContent(1),"+-", totalXR2.GetBinError(1)


