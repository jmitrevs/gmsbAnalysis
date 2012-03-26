#! /usr/bin/env python

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

Wjets = ROOT.TFile("WjetsHist.root")
Wgamma = ROOT.TFile("WgammaHist.root")
ttbar = ROOT.TFile("ttbarHist.root")
ttbargamma = ROOT.TFile("ttbargammaHist.root")
st = ROOT.TFile("stHist.root")
diboson = ROOT.TFile("dibosonHist.root")
Zjets = ROOT.TFile("ZjetsHist.root")
Zgamma = ROOT.TFile("ZgammaHist.root")
gammaJets = ROOT.TFile("gammaJetsHist.root")
total = ROOT.TFile("total.root")

WjetsSR = Wjets.Get("nSIG")
WgammaSR = Wgamma.Get("nSIG")
ttbarSR = ttbar.Get("nSIG")
ttbargammaSR = ttbargamma.Get("nSIG")
stSR = st.Get("nSIG")
dibosonSR = diboson.Get("nSIG")
ZjetsSR = Zjets.Get("nSIG")
ZgammaSR = Zgamma.Get("nSIG")
gammaJetsSR = gammaJets.Get("nSIG")
totalSR = total.Get("nSIG")

WjetsWCR = Wjets.Get("nWCR")
WgammaWCR = Wgamma.Get("nWCR")
ttbarWCR = ttbar.Get("nWCR")
ttbargammaWCR = ttbargamma.Get("nWCR")
stWCR = st.Get("nWCR")
dibosonWCR = diboson.Get("nWCR")
ZjetsWCR = Zjets.Get("nWCR")
ZgammaWCR = Zgamma.Get("nWCR")
gammaJetsWCR = gammaJets.Get("nWCR")
totalWCR = total.Get("nWCR")

WjetsTCR = Wjets.Get("nTCR")
WgammaTCR = Wgamma.Get("nTCR")
ttbarTCR = ttbar.Get("nTCR")
ttbargammaTCR = ttbargamma.Get("nTCR")
stTCR = st.Get("nTCR")
dibosonTCR = diboson.Get("nTCR")
ZjetsTCR = Zjets.Get("nTCR")
ZgammaTCR = Zgamma.Get("nTCR")
gammaJetsTCR = gammaJets.Get("nTCR")
totalTCR = total.Get("nTCR")

WjetsQCD = Wjets.Get("nQCD")
WgammaQCD = Wgamma.Get("nQCD")
ttbarQCD = ttbar.Get("nQCD")
ttbargammaQCD = ttbargamma.Get("nQCD")
stQCD = st.Get("nQCD")
dibosonQCD = diboson.Get("nQCD")
ZjetsQCD = Zjets.Get("nQCD")
ZgammaQCD = Zgamma.Get("nQCD")
gammaJetsQCD = gammaJets.Get("nQCD")
totalQCD = total.Get("nQCD")

WjetsXR1 = Wjets.Get("nXR1")
WgammaXR1 = Wgamma.Get("nXR1")
ttbarXR1 = ttbar.Get("nXR1")
ttbargammaXR1 = ttbargamma.Get("nXR1")
stXR1 = st.Get("nXR1")
dibosonXR1 = diboson.Get("nXR1")
ZjetsXR1 = Zjets.Get("nXR1")
ZgammaXR1 = Zgamma.Get("nXR1")
gammaJetsXR1 = gammaJets.Get("nXR1")
totalXR1 = total.Get("nXR1")

WjetsXR2 = Wjets.Get("nXR2")
WgammaXR2 = Wgamma.Get("nXR2")
ttbarXR2 = ttbar.Get("nXR2")
ttbargammaXR2 = ttbargamma.Get("nXR2")
stXR2 = st.Get("nXR2")
dibosonXR2 = diboson.Get("nXR2")
ZjetsXR2 = Zjets.Get("nXR2")
ZgammaXR2 = Zgamma.Get("nXR2")
gammaJetsXR2 = gammaJets.Get("nXR2")
totalXR2 = total.Get("nXR2")

print "*****************************"
print "****         SR        ******"
print "*****************************"
print "Wjets =", WjetsSR.GetBinContent(1),"+-", WjetsSR.GetBinError(1)
print "Wgamma =", WgammaSR.GetBinContent(1),"+-", WgammaSR.GetBinError(1)
print "ttbar =", ttbarSR.GetBinContent(1),"+-", ttbarSR.GetBinError(1)
print "ttbargamma =", ttbargammaSR.GetBinContent(1),"+-", ttbargammaSR.GetBinError(1)
print "single top =", stSR.GetBinContent(1),"+-", stSR.GetBinError(1)
print "diboson =", dibosonSR.GetBinContent(1),"+-", dibosonSR.GetBinError(1)
print "Zjets =", ZjetsSR.GetBinContent(1),"+-", ZjetsSR.GetBinError(1)
print "Zgamma =", ZgammaSR.GetBinContent(1),"+-", ZgammaSR.GetBinError(1)
print "gamma+jet =", gammaJetsSR.GetBinContent(1),"+-", gammaJetsSR.GetBinError(1)
print "total =", totalSR.GetBinContent(1),"+-", totalSR.GetBinError(1)

print "*****************************"
print "****         WCR        ******"
print "*****************************"
print "Wjets =", WjetsWCR.GetBinContent(1),"+-", WjetsWCR.GetBinError(1)
print "Wgamma =", WgammaWCR.GetBinContent(1),"+-", WgammaWCR.GetBinError(1)
print "ttbar =", ttbarWCR.GetBinContent(1),"+-", ttbarWCR.GetBinError(1)
print "ttbargamma =", ttbargammaWCR.GetBinContent(1),"+-", ttbargammaWCR.GetBinError(1)
print "single top =", stWCR.GetBinContent(1),"+-", stWCR.GetBinError(1)
print "diboson =", dibosonWCR.GetBinContent(1),"+-", dibosonWCR.GetBinError(1)
print "Zjets =", ZjetsWCR.GetBinContent(1),"+-", ZjetsWCR.GetBinError(1)
print "Zgamma =", ZgammaWCR.GetBinContent(1),"+-", ZgammaWCR.GetBinError(1)
print "gamma+jet =", gammaJetsWCR.GetBinContent(1),"+-", gammaJetsWCR.GetBinError(1)
print "total =", totalWCR.GetBinContent(1),"+-", totalWCR.GetBinError(1)

print "*****************************"
print "****         TCR        ******"
print "*****************************"
print "Wjets =", WjetsTCR.GetBinContent(1),"+-", WjetsTCR.GetBinError(1)
print "Wgamma =", WgammaTCR.GetBinContent(1),"+-", WgammaTCR.GetBinError(1)
print "ttbar =", ttbarTCR.GetBinContent(1),"+-", ttbarTCR.GetBinError(1)
print "ttbargamma =", ttbargammaTCR.GetBinContent(1),"+-", ttbargammaTCR.GetBinError(1)
print "single top =", stTCR.GetBinContent(1),"+-", stTCR.GetBinError(1)
print "diboson =", dibosonTCR.GetBinContent(1),"+-", dibosonTCR.GetBinError(1)
print "Zjets =", ZjetsTCR.GetBinContent(1),"+-", ZjetsTCR.GetBinError(1)
print "Zgamma =", ZgammaTCR.GetBinContent(1),"+-", ZgammaTCR.GetBinError(1)
print "gamma+jet =", gammaJetsTCR.GetBinContent(1),"+-", gammaJetsTCR.GetBinError(1)
print "total =", totalTCR.GetBinContent(1),"+-", totalTCR.GetBinError(1)

print "*****************************"
print "****         QCD        ******"
print "*****************************"
print "Wjets =", WjetsQCD.GetBinContent(1),"+-", WjetsQCD.GetBinError(1)
print "Wgamma =", WgammaQCD.GetBinContent(1),"+-", WgammaQCD.GetBinError(1)
print "ttbar =", ttbarQCD.GetBinContent(1),"+-", ttbarQCD.GetBinError(1)
print "ttbargamma =", ttbargammaQCD.GetBinContent(1),"+-", ttbargammaQCD.GetBinError(1)
print "single top =", stQCD.GetBinContent(1),"+-", stQCD.GetBinError(1)
print "diboson =", dibosonQCD.GetBinContent(1),"+-", dibosonQCD.GetBinError(1)
print "Zjets =", ZjetsQCD.GetBinContent(1),"+-", ZjetsQCD.GetBinError(1)
print "Zgamma =", ZgammaQCD.GetBinContent(1),"+-", ZgammaQCD.GetBinError(1)
print "gamma+jet =", gammaJetsQCD.GetBinContent(1),"+-", gammaJetsQCD.GetBinError(1)
print "total =", totalQCD.GetBinContent(1),"+-", totalQCD.GetBinError(1)

print "*****************************"
print "****         XR1       ******"
print "*****************************"
print "Wjets =", WjetsXR1.GetBinContent(1),"+-", WjetsXR1.GetBinError(1)
print "Wgamma =", WgammaXR1.GetBinContent(1),"+-", WgammaXR1.GetBinError(1)
print "ttbar =", ttbarXR1.GetBinContent(1),"+-", ttbarXR1.GetBinError(1)
print "ttbargamma =", ttbargammaXR1.GetBinContent(1),"+-", ttbargammaXR1.GetBinError(1)
print "single top =", stXR1.GetBinContent(1),"+-", stXR1.GetBinError(1)
print "diboson =", dibosonXR1.GetBinContent(1),"+-", dibosonXR1.GetBinError(1)
print "Zjets =", ZjetsXR1.GetBinContent(1),"+-", ZjetsXR1.GetBinError(1)
print "Zgamma =", ZgammaXR1.GetBinContent(1),"+-", ZgammaXR1.GetBinError(1)
print "gamma+jet =", gammaJetsXR1.GetBinContent(1),"+-", gammaJetsXR1.GetBinError(1)
print "total =", totalXR1.GetBinContent(1),"+-", totalXR1.GetBinError(1)

print "*****************************"
print "****         XR2       ******"
print "*****************************"
print "Wjets =", WjetsXR2.GetBinContent(1),"+-", WjetsXR2.GetBinError(1)
print "Wgamma =", WgammaXR2.GetBinContent(1),"+-", WgammaXR2.GetBinError(1)
print "ttbar =", ttbarXR2.GetBinContent(1),"+-", ttbarXR2.GetBinError(1)
print "ttbargamma =", ttbargammaXR2.GetBinContent(1),"+-", ttbargammaXR2.GetBinError(1)
print "single top =", stXR2.GetBinContent(1),"+-", stXR2.GetBinError(1)
print "diboson =", dibosonXR2.GetBinContent(1),"+-", dibosonXR2.GetBinError(1)
print "Zjets =", ZjetsXR2.GetBinContent(1),"+-", ZjetsXR2.GetBinError(1)
print "Zgamma =", ZgammaXR2.GetBinContent(1),"+-", ZgammaXR2.GetBinError(1)
print "gamma+jet =", gammaJetsXR2.GetBinContent(1),"+-", gammaJetsXR2.GetBinError(1)
print "total =", totalXR2.GetBinContent(1),"+-", totalXR2.GetBinError(1)


