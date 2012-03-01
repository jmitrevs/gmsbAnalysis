#! /usr/bin/env python

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()



Wjets = ROOT.TFile("WjetsHist.root")
Wgamma = ROOT.TFile("WgammaHist.root")
ttbar = ROOT.TFile("ttbarHist.root")
st = ROOT.TFile("stHist.root")
diboson = ROOT.TFile("dibosonHist.root")
Z = ROOT.TFile("ZHist.root")
gammaJets = ROOT.TFile("gammaJetsHist.root")
total = ROOT.TFile("total.root")

WjetsSR = Wjets.Get("nSIG")
WgammaSR = Wgamma.Get("nSIG")
ttbarSR = ttbar.Get("nSIG")
stSR = st.Get("nSIG")
dibosonSR = diboson.Get("nSIG")
ZSR = Z.Get("nSIG")
gammaJetsSR = gammaJets.Get("nSIG")
totalSR = total.Get("nSIG")

WjetsCR = Wjets.Get("nCR")
WgammaCR = Wgamma.Get("nCR")
ttbarCR = ttbar.Get("nCR")
stCR = st.Get("nCR")
dibosonCR = diboson.Get("nCR")
ZCR = Z.Get("nCR")
gammaJetsCR = gammaJets.Get("nCR")
totalCR = total.Get("nCR")

WjetsQCD = Wjets.Get("nQCD")
WgammaQCD = Wgamma.Get("nQCD")
ttbarQCD = ttbar.Get("nQCD")
stQCD = st.Get("nQCD")
dibosonQCD = diboson.Get("nQCD")
ZQCD = Z.Get("nQCD")
gammaJetsQCD = gammaJets.Get("nQCD")
totalQCD = total.Get("nQCD")

WjetsXR1 = Wjets.Get("nXR1")
WgammaXR1 = Wgamma.Get("nXR1")
ttbarXR1 = ttbar.Get("nXR1")
stXR1 = st.Get("nXR1")
dibosonXR1 = diboson.Get("nXR1")
ZXR1 = Z.Get("nXR1")
gammaJetsXR1 = gammaJets.Get("nXR1")
totalXR1 = total.Get("nXR1")

WjetsXR2 = Wjets.Get("nXR2")
WgammaXR2 = Wgamma.Get("nXR2")
ttbarXR2 = ttbar.Get("nXR2")
stXR2 = st.Get("nXR2")
dibosonXR2 = diboson.Get("nXR2")
ZXR2 = Z.Get("nXR2")
gammaJetsXR2 = gammaJets.Get("nXR2")
totalXR2 = total.Get("nXR2")

print "*****************************"
print "****         SR        ******"
print "*****************************"
print "Wjets =", WjetsSR.GetBinContent(1),"+-", WjetsSR.GetBinError(1)
print "Wgamma =", WgammaSR.GetBinContent(1),"+-", WgammaSR.GetBinError(1)
print "ttbar =", ttbarSR.GetBinContent(1),"+-", ttbarSR.GetBinError(1)
print "single top =", stSR.GetBinContent(1),"+-", stSR.GetBinError(1)
print "diboson =", dibosonSR.GetBinContent(1),"+-", dibosonSR.GetBinError(1)
print "Z =", ZSR.GetBinContent(1),"+-", ZSR.GetBinError(1)
print "gamma+jet =", gammaJetsSR.GetBinContent(1),"+-", gammaJetsSR.GetBinError(1)
print "total =", totalSR.GetBinContent(1),"+-", totalSR.GetBinError(1)

print "*****************************"
print "****         CR        ******"
print "*****************************"
print "Wjets =", WjetsCR.GetBinContent(1),"+-", WjetsCR.GetBinError(1)
print "Wgamma =", WgammaCR.GetBinContent(1),"+-", WgammaCR.GetBinError(1)
print "ttbar =", ttbarCR.GetBinContent(1),"+-", ttbarCR.GetBinError(1)
print "single top =", stCR.GetBinContent(1),"+-", stCR.GetBinError(1)
print "diboson =", dibosonCR.GetBinContent(1),"+-", dibosonCR.GetBinError(1)
print "Z =", ZCR.GetBinContent(1),"+-", ZCR.GetBinError(1)
print "gamma+jet =", gammaJetsCR.GetBinContent(1),"+-", gammaJetsCR.GetBinError(1)
print "total =", totalCR.GetBinContent(1),"+-", totalCR.GetBinError(1)

print "*****************************"
print "****         QCD        ******"
print "*****************************"
print "Wjets =", WjetsQCD.GetBinContent(1),"+-", WjetsQCD.GetBinError(1)
print "Wgamma =", WgammaQCD.GetBinContent(1),"+-", WgammaQCD.GetBinError(1)
print "ttbar =", ttbarQCD.GetBinContent(1),"+-", ttbarQCD.GetBinError(1)
print "single top =", stQCD.GetBinContent(1),"+-", stQCD.GetBinError(1)
print "diboson =", dibosonQCD.GetBinContent(1),"+-", dibosonQCD.GetBinError(1)
print "Z =", ZQCD.GetBinContent(1),"+-", ZQCD.GetBinError(1)
print "gamma+jet =", gammaJetsQCD.GetBinContent(1),"+-", gammaJetsQCD.GetBinError(1)
print "total =", totalQCD.GetBinContent(1),"+-", totalQCD.GetBinError(1)

print "*****************************"
print "****         XR1       ******"
print "*****************************"
print "Wjets =", WjetsXR1.GetBinContent(1),"+-", WjetsXR1.GetBinError(1)
print "Wgamma =", WgammaXR1.GetBinContent(1),"+-", WgammaXR1.GetBinError(1)
print "ttbar =", ttbarXR1.GetBinContent(1),"+-", ttbarXR1.GetBinError(1)
print "single top =", stXR1.GetBinContent(1),"+-", stXR1.GetBinError(1)
print "diboson =", dibosonXR1.GetBinContent(1),"+-", dibosonXR1.GetBinError(1)
print "Z =", ZXR1.GetBinContent(1),"+-", ZXR1.GetBinError(1)
print "gamma+jet =", gammaJetsXR1.GetBinContent(1),"+-", gammaJetsXR1.GetBinError(1)
print "total =", totalXR1.GetBinContent(1),"+-", totalXR1.GetBinError(1)

print "*****************************"
print "****         XR2       ******"
print "*****************************"
print "Wjets =", WjetsXR2.GetBinContent(1),"+-", WjetsXR2.GetBinError(1)
print "Wgamma =", WgammaXR2.GetBinContent(1),"+-", WgammaXR2.GetBinError(1)
print "ttbar =", ttbarXR2.GetBinContent(1),"+-", ttbarXR2.GetBinError(1)
print "single top =", stXR2.GetBinContent(1),"+-", stXR2.GetBinError(1)
print "diboson =", dibosonXR2.GetBinContent(1),"+-", dibosonXR2.GetBinError(1)
print "Z =", ZXR2.GetBinContent(1),"+-", ZXR2.GetBinError(1)
print "gamma+jet =", gammaJetsXR2.GetBinContent(1),"+-", gammaJetsXR2.GetBinError(1)
print "total =", totalXR2.GetBinContent(1),"+-", totalXR2.GetBinError(1)

