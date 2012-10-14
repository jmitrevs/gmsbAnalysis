#! /usr/bin/env python
import sys
import getopt

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

COMPATIBILITY=False
ELECTRON = 0
MUON = 1

BLIND = False

DEFAULTLEPTON = ELECTRON

try:
    # retrive command line options
    shortopts  = "eml:ct"
    longopts   = ["lepton="]
    opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )
except getopt.GetoptError:
    # print help information and exit:
    print "ERROR: unknown options in argument %s" % sys.argv[1:]
    sys.exit(1)

compat = COMPATIBILITY
lepton = DEFAULTLEPTON
printTable = False
for o, a in opts:
    if o in ("-m"):
        lepton = MUON
    elif o in ("-e"):
        lepton = ELECTRON
    elif o in ("-c"):
        compat = True
    elif o in ("-t"):
        printTable = True
    elif o in ("-l", "--lepton"):
        if a == "electron":
            lepton = ELECTRON
        elif a == "muon":
            lepton = MUON
        else:
            print "*** Lepton must be 'electron' or 'muon ****"
            sys.exit(1)


Wjets = ROOT.TFile("WjetsHist.root")
Wgamma = ROOT.TFile("WgammaHist.root")
ttbarDilep = ROOT.TFile("ttbarDilepHist.root")
ttbarLepjets = ROOT.TFile("ttbarLepjetsHist.root")
ttbargamma = ROOT.TFile("ttbargammaHist.root")
st = ROOT.TFile("stHist.root")
diboson = ROOT.TFile("dibosonHist.root")
Zjets = ROOT.TFile("ZjetsHist.root")
Zgamma = ROOT.TFile("ZgammaHist.root")
gammaJets = ROOT.TFile("gammaJetsHist.root")
total = ROOT.TFile("totalHist.root")
data = ROOT.TFile("data.root")
gj = ROOT.TFile("gjHist.root")
totalMM = ROOT.TFile("totalMMHist.root")
if lepton == ELECTRON:
    diphotons = ROOT.TFile("diphotonsHist.root")

WjetsSR = Wjets.Get("nSIG")
WgammaSR = Wgamma.Get("nSIG")
ttbarDilepSR = ttbarDilep.Get("nSIG")
ttbarLepjetsSR = ttbarLepjets.Get("nSIG")
ttbargammaSR = ttbargamma.Get("nSIG")
stSR = st.Get("nSIG")
dibosonSR = diboson.Get("nSIG")
ZjetsSR = Zjets.Get("nSIG")
ZgammaSR = Zgamma.Get("nSIG")
gammaJetsSR = gammaJets.Get("nSIG")
totalSR = total.Get("nSIG")
dataSR = data.Get("nSIG")
gjSR = gj.Get("nSIG")
totalMMSR = totalMM.Get("nSIG")
if lepton == ELECTRON:
    diphotonsSR = diphotons.Get("nSIG")

WjetsWCR = Wjets.Get("nWCR")
WgammaWCR = Wgamma.Get("nWCR")
ttbarDilepWCR = ttbarDilep.Get("nWCR")
ttbarLepjetsWCR = ttbarLepjets.Get("nWCR")
ttbargammaWCR = ttbargamma.Get("nWCR")
stWCR = st.Get("nWCR")
dibosonWCR = diboson.Get("nWCR")
ZjetsWCR = Zjets.Get("nWCR")
ZgammaWCR = Zgamma.Get("nWCR")
gammaJetsWCR = gammaJets.Get("nWCR")
totalWCR = total.Get("nWCR")
dataWCR = data.Get("nWCR")
gjWCR = gj.Get("nWCR")
totalMMWCR = totalMM.Get("nWCR")
if lepton == ELECTRON:
    diphotonsWCR = diphotons.Get("nWCR")

WjetsTCR = Wjets.Get("nTCR")
WgammaTCR = Wgamma.Get("nTCR")
ttbarDilepTCR = ttbarDilep.Get("nTCR")
ttbarLepjetsTCR = ttbarLepjets.Get("nTCR")
ttbargammaTCR = ttbargamma.Get("nTCR")
stTCR = st.Get("nTCR")
dibosonTCR = diboson.Get("nTCR")
ZjetsTCR = Zjets.Get("nTCR")
ZgammaTCR = Zgamma.Get("nTCR")
gammaJetsTCR = gammaJets.Get("nTCR")
totalTCR = total.Get("nTCR")
dataTCR = data.Get("nTCR")
gjTCR = gj.Get("nTCR")
totalMMTCR = totalMM.Get("nTCR")
if lepton == ELECTRON:
    diphotonsTCR = diphotons.Get("nTCR")

WjetsQCD = Wjets.Get("nQCD")
WgammaQCD = Wgamma.Get("nQCD")
ttbarDilepQCD = ttbarDilep.Get("nQCD")
ttbarLepjetsQCD = ttbarLepjets.Get("nQCD")
ttbargammaQCD = ttbargamma.Get("nQCD")
stQCD = st.Get("nQCD")
dibosonQCD = diboson.Get("nQCD")
ZjetsQCD = Zjets.Get("nQCD")
ZgammaQCD = Zgamma.Get("nQCD")
gammaJetsQCD = gammaJets.Get("nQCD")
totalQCD = total.Get("nQCD")
dataQCD = data.Get("nQCD")
gjQCD = gj.Get("nQCD")
totalMMQCD = totalMM.Get("nQCD")
if lepton == ELECTRON:
    diphotonsQCD = diphotons.Get("nQCD")

WjetsXR1 = Wjets.Get("nXR1")
WgammaXR1 = Wgamma.Get("nXR1")
ttbarDilepXR1 = ttbarDilep.Get("nXR1")
ttbarLepjetsXR1 = ttbarLepjets.Get("nXR1")
ttbargammaXR1 = ttbargamma.Get("nXR1")
stXR1 = st.Get("nXR1")
dibosonXR1 = diboson.Get("nXR1")
ZjetsXR1 = Zjets.Get("nXR1")
ZgammaXR1 = Zgamma.Get("nXR1")
gammaJetsXR1 = gammaJets.Get("nXR1")
totalXR1 = total.Get("nXR1")
dataXR1 = data.Get("nXR1")
gjXR1 = gj.Get("nXR1")
totalMMXR1 = totalMM.Get("nXR1")
if lepton == ELECTRON:
    diphotonsXR1 = diphotons.Get("nXR1")

WjetsXR2 = Wjets.Get("nXR2")
WgammaXR2 = Wgamma.Get("nXR2")
ttbarDilepXR2 = ttbarDilep.Get("nXR2")
ttbarLepjetsXR2 = ttbarLepjets.Get("nXR2")
ttbargammaXR2 = ttbargamma.Get("nXR2")
stXR2 = st.Get("nXR2")
dibosonXR2 = diboson.Get("nXR2")
ZjetsXR2 = Zjets.Get("nXR2")
ZgammaXR2 = Zgamma.Get("nXR2")
gammaJetsXR2 = gammaJets.Get("nXR2")
totalXR2 = total.Get("nXR2")
dataXR2 = data.Get("nXR2")
gjXR2 = gj.Get("nXR2")
totalMMXR2 = totalMM.Get("nXR2")
if lepton == ELECTRON:
    diphotonsXR2 = diphotons.Get("nXR2")

WjetsPRESEL = Wjets.Get("nPRESEL")
WgammaPRESEL = Wgamma.Get("nPRESEL")
ttbarDilepPRESEL = ttbarDilep.Get("nPRESEL")
ttbarLepjetsPRESEL = ttbarLepjets.Get("nPRESEL")
ttbargammaPRESEL = ttbargamma.Get("nPRESEL")
stPRESEL = st.Get("nPRESEL")
dibosonPRESEL = diboson.Get("nPRESEL")
ZjetsPRESEL = Zjets.Get("nPRESEL")
ZgammaPRESEL = Zgamma.Get("nPRESEL")
gammaJetsPRESEL = gammaJets.Get("nPRESEL")
totalPRESEL = total.Get("nPRESEL")
dataPRESEL = data.Get("nPRESEL")
gjPRESEL = gj.Get("nPRESEL")
totalMMPRESEL = totalMM.Get("nPRESEL")
if lepton == ELECTRON:
    diphotonsPRESEL = diphotons.Get("nPRESEL")

print "*****************************"
print "****         SR        ******"
print "*****************************"
print "Wjets =", WjetsSR.GetBinContent(1),"+-", WjetsSR.GetBinError(1)
print "Wgamma =", WgammaSR.GetBinContent(1),"+-", WgammaSR.GetBinError(1)
print "ttbarDilep =", ttbarDilepSR.GetBinContent(1),"+-", ttbarDilepSR.GetBinError(1)
print "ttbarLepjets =", ttbarLepjetsSR.GetBinContent(1),"+-", ttbarLepjetsSR.GetBinError(1)
print "ttbargamma =", ttbargammaSR.GetBinContent(1),"+-", ttbargammaSR.GetBinError(1)
print "singletop =", stSR.GetBinContent(1),"+-", stSR.GetBinError(1)
print "diboson =", dibosonSR.GetBinContent(1),"+-", dibosonSR.GetBinError(1)
print "Zjets =", ZjetsSR.GetBinContent(1),"+-", ZjetsSR.GetBinError(1)
print "Zgamma =", ZgammaSR.GetBinContent(1),"+-", ZgammaSR.GetBinError(1)
if not compat and lepton == ELECTRON:
    print "diphotons =", diphotonsSR.GetBinContent(1),"+-", diphotonsSR.GetBinError(1)
print "gamma+jet =", gammaJetsSR.GetBinContent(1),"+-", gammaJetsSR.GetBinError(1)
print "total =", totalSR.GetBinContent(1),"+-", totalSR.GetBinError(1)
if not compat:
    print "gamma+jet (from data) =", gjSR.GetBinContent(1),"+-", gjSR.GetBinError(1)
    print "total (from MM) =", totalMMSR.GetBinContent(1),"+-", totalMMSR.GetBinError(1)
    if not BLIND:
        print "data =", dataSR.GetBinContent(1),"+-",dataSR.GetBinError(1)
    
print "*****************************"
print "****         WCR        ******"
print "*****************************"
print "Wjets =", WjetsWCR.GetBinContent(1),"+-", WjetsWCR.GetBinError(1)
print "Wgamma =", WgammaWCR.GetBinContent(1),"+-", WgammaWCR.GetBinError(1)
print "ttbarDilep =", ttbarDilepWCR.GetBinContent(1),"+-", ttbarDilepWCR.GetBinError(1)
print "ttbarLepjets =", ttbarLepjetsWCR.GetBinContent(1),"+-", ttbarLepjetsWCR.GetBinError(1)
print "ttbargamma =", ttbargammaWCR.GetBinContent(1),"+-", ttbargammaWCR.GetBinError(1)
print "singletop =", stWCR.GetBinContent(1),"+-", stWCR.GetBinError(1)
print "diboson =", dibosonWCR.GetBinContent(1),"+-", dibosonWCR.GetBinError(1)
print "Zjets =", ZjetsWCR.GetBinContent(1),"+-", ZjetsWCR.GetBinError(1)
print "Zgamma =", ZgammaWCR.GetBinContent(1),"+-", ZgammaWCR.GetBinError(1)
if not compat and lepton == ELECTRON:
    print "diphotons =", diphotonsWCR.GetBinContent(1),"+-", diphotonsWCR.GetBinError(1)
print "gamma+jet =", gammaJetsWCR.GetBinContent(1),"+-", gammaJetsWCR.GetBinError(1)
print "total =", totalWCR.GetBinContent(1),"+-", totalWCR.GetBinError(1)
if not compat:
    print "gamma+jet (from data) =", gjWCR.GetBinContent(1),"+-", gjWCR.GetBinError(1)
    print "total (from MM) =", totalMMWCR.GetBinContent(1),"+-", totalMMWCR.GetBinError(1)
    print "data =", dataWCR.GetBinContent(1),"+-",dataWCR.GetBinError(1)

print "*****************************"
print "****         TCR        ******"
print "*****************************"
print "Wjets =", WjetsTCR.GetBinContent(1),"+-", WjetsTCR.GetBinError(1)
print "Wgamma =", WgammaTCR.GetBinContent(1),"+-", WgammaTCR.GetBinError(1)
print "ttbarDilep =", ttbarDilepTCR.GetBinContent(1),"+-", ttbarDilepTCR.GetBinError(1)
print "ttbarLepjets =", ttbarLepjetsTCR.GetBinContent(1),"+-", ttbarLepjetsTCR.GetBinError(1)
print "ttbargamma =", ttbargammaTCR.GetBinContent(1),"+-", ttbargammaTCR.GetBinError(1)
print "singletop =", stTCR.GetBinContent(1),"+-", stTCR.GetBinError(1)
print "diboson =", dibosonTCR.GetBinContent(1),"+-", dibosonTCR.GetBinError(1)
print "Zjets =", ZjetsTCR.GetBinContent(1),"+-", ZjetsTCR.GetBinError(1)
print "Zgamma =", ZgammaTCR.GetBinContent(1),"+-", ZgammaTCR.GetBinError(1)
if not compat and lepton == ELECTRON:
    print "diphotons =", diphotonsTCR.GetBinContent(1),"+-", diphotonsTCR.GetBinError(1)
print "gamma+jet =", gammaJetsTCR.GetBinContent(1),"+-", gammaJetsTCR.GetBinError(1)
print "total =", totalTCR.GetBinContent(1),"+-", totalTCR.GetBinError(1)
if not compat:
    print "gamma+jet (from data) =", gjTCR.GetBinContent(1),"+-", gjTCR.GetBinError(1)
    print "total (from MM) =", totalMMTCR.GetBinContent(1),"+-", totalMMTCR.GetBinError(1)
    print "data =", dataTCR.GetBinContent(1),"+-",dataTCR.GetBinError(1)

print "*****************************"
print "****         QCD        ******"
print "*****************************"
print "Wjets =", WjetsQCD.GetBinContent(1),"+-", WjetsQCD.GetBinError(1)
print "Wgamma =", WgammaQCD.GetBinContent(1),"+-", WgammaQCD.GetBinError(1)
print "ttbarDilep =", ttbarDilepQCD.GetBinContent(1),"+-", ttbarDilepQCD.GetBinError(1)
print "ttbarLepjets =", ttbarLepjetsQCD.GetBinContent(1),"+-", ttbarLepjetsQCD.GetBinError(1)
print "ttbargamma =", ttbargammaQCD.GetBinContent(1),"+-", ttbargammaQCD.GetBinError(1)
print "singletop =", stQCD.GetBinContent(1),"+-", stQCD.GetBinError(1)
print "diboson =", dibosonQCD.GetBinContent(1),"+-", dibosonQCD.GetBinError(1)
print "Zjets =", ZjetsQCD.GetBinContent(1),"+-", ZjetsQCD.GetBinError(1)
print "Zgamma =", ZgammaQCD.GetBinContent(1),"+-", ZgammaQCD.GetBinError(1)
if not compat and lepton == ELECTRON:
    print "diphotons =", diphotonsQCD.GetBinContent(1),"+-", diphotonsQCD.GetBinError(1)
print "gamma+jet =", gammaJetsQCD.GetBinContent(1),"+-", gammaJetsQCD.GetBinError(1)
print "total =", totalQCD.GetBinContent(1),"+-", totalQCD.GetBinError(1)
if not compat:
    print "gamma+jet (from data) =", gjQCD.GetBinContent(1),"+-", gjQCD.GetBinError(1)
    print "total (from MM) =", totalMMQCD.GetBinContent(1),"+-", totalMMQCD.GetBinError(1)
    print "data =", dataQCD.GetBinContent(1),"+-",dataQCD.GetBinError(1)

print "*****************************"
print "****         XR1       ******"
print "*****************************"
print "Wjets =", WjetsXR1.GetBinContent(1),"+-", WjetsXR1.GetBinError(1)
print "Wgamma =", WgammaXR1.GetBinContent(1),"+-", WgammaXR1.GetBinError(1)
print "ttbarDilep =", ttbarDilepXR1.GetBinContent(1),"+-", ttbarDilepXR1.GetBinError(1)
print "ttbarLepjets =", ttbarLepjetsXR1.GetBinContent(1),"+-", ttbarLepjetsXR1.GetBinError(1)
print "ttbargamma =", ttbargammaXR1.GetBinContent(1),"+-", ttbargammaXR1.GetBinError(1)
print "singletop =", stXR1.GetBinContent(1),"+-", stXR1.GetBinError(1)
print "diboson =", dibosonXR1.GetBinContent(1),"+-", dibosonXR1.GetBinError(1)
print "Zjets =", ZjetsXR1.GetBinContent(1),"+-", ZjetsXR1.GetBinError(1)
print "Zgamma =", ZgammaXR1.GetBinContent(1),"+-", ZgammaXR1.GetBinError(1)
if not compat and lepton == ELECTRON:
    print "diphotons =", diphotonsXR1.GetBinContent(1),"+-", diphotonsXR1.GetBinError(1)
print "gamma+jet =", gammaJetsXR1.GetBinContent(1),"+-", gammaJetsXR1.GetBinError(1)
print "total =", totalXR1.GetBinContent(1),"+-", totalXR1.GetBinError(1)
if not compat:
    print "gamma+jet (from data) =", gjXR1.GetBinContent(1),"+-", gjXR1.GetBinError(1)
    print "total (from MM) =", totalMMXR1.GetBinContent(1),"+-", totalMMXR1.GetBinError(1)
    print "data =", dataXR1.GetBinContent(1),"+-",dataXR1.GetBinError(1)

print "*****************************"
print "****         XR2       ******"
print "*****************************"
print "Wjets =", WjetsXR2.GetBinContent(1),"+-", WjetsXR2.GetBinError(1)
print "Wgamma =", WgammaXR2.GetBinContent(1),"+-", WgammaXR2.GetBinError(1)
print "ttbarDilep =", ttbarDilepXR2.GetBinContent(1),"+-", ttbarDilepXR2.GetBinError(1)
print "ttbarLepjets =", ttbarLepjetsXR2.GetBinContent(1),"+-", ttbarLepjetsXR2.GetBinError(1)
print "ttbargamma =", ttbargammaXR2.GetBinContent(1),"+-", ttbargammaXR2.GetBinError(1)
print "singletop =", stXR2.GetBinContent(1),"+-", stXR2.GetBinError(1)
print "diboson =", dibosonXR2.GetBinContent(1),"+-", dibosonXR2.GetBinError(1)
print "Zjets =", ZjetsXR2.GetBinContent(1),"+-", ZjetsXR2.GetBinError(1)
print "Zgamma =", ZgammaXR2.GetBinContent(1),"+-", ZgammaXR2.GetBinError(1)
if not compat and lepton == ELECTRON:
    print "diphotons =", diphotonsXR2.GetBinContent(1),"+-", diphotonsXR2.GetBinError(1)
print "gamma+jet =", gammaJetsXR2.GetBinContent(1),"+-", gammaJetsXR2.GetBinError(1)
print "total =", totalXR2.GetBinContent(1),"+-", totalXR2.GetBinError(1)
if not compat:
    print "gamma+jet (from data) =", gjXR2.GetBinContent(1),"+-", gjXR2.GetBinError(1)
    print "total (from MM) =", totalMMXR2.GetBinContent(1),"+-", totalMMXR2.GetBinError(1)
    print "data =", dataXR2.GetBinContent(1),"+-",dataXR2.GetBinError(1)

print "*****************************"
print "****       PRESEL      ******"
print "*****************************"
print "Wjets =", WjetsPRESEL.GetBinContent(1),"+-", WjetsPRESEL.GetBinError(1)
print "Wgamma =", WgammaPRESEL.GetBinContent(1),"+-", WgammaPRESEL.GetBinError(1)
print "ttbarDilep =", ttbarDilepPRESEL.GetBinContent(1),"+-", ttbarDilepPRESEL.GetBinError(1)
print "ttbarLepjets =", ttbarLepjetsPRESEL.GetBinContent(1),"+-", ttbarLepjetsPRESEL.GetBinError(1)
print "ttbargamma =", ttbargammaPRESEL.GetBinContent(1),"+-", ttbargammaPRESEL.GetBinError(1)
print "singletop =", stPRESEL.GetBinContent(1),"+-", stPRESEL.GetBinError(1)
print "diboson =", dibosonPRESEL.GetBinContent(1),"+-", dibosonPRESEL.GetBinError(1)
print "Zjets =", ZjetsPRESEL.GetBinContent(1),"+-", ZjetsPRESEL.GetBinError(1)
print "Zgamma =", ZgammaPRESEL.GetBinContent(1),"+-", ZgammaPRESEL.GetBinError(1)
if not compat and lepton == ELECTRON:
    print "diphotons =", diphotonsPRESEL.GetBinContent(1),"+-", diphotonsPRESEL.GetBinError(1)
print "gamma+jet =", gammaJetsPRESEL.GetBinContent(1),"+-", gammaJetsPRESEL.GetBinError(1)
print "total =", totalPRESEL.GetBinContent(1),"+-", totalPRESEL.GetBinError(1)
if not compat:
    print "gamma+jet (from data) =", gjPRESEL.GetBinContent(1),"+-", gjPRESEL.GetBinError(1)
    print "total (from MM) =", totalMMPRESEL.GetBinContent(1),"+-", totalMMPRESEL.GetBinError(1)
    print "data =", dataPRESEL.GetBinContent(1),"+-",dataPRESEL.GetBinError(1)


# This prints the latex yield table
if printTable:
    print " Yields & WCR & HMT & HMET & SR \\\\ \\hline"

    print " \\Wgamma & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        WgammaWCR.GetBinContent(1), WgammaWCR.GetBinError(1), WgammaTCR.GetBinContent(1), WgammaTCR.GetBinError(1),
        WgammaXR2.GetBinContent(1), WgammaXR2.GetBinError(1), WgammaSR.GetBinContent(1), WgammaSR.GetBinError(1))

    print " \\Wjets & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        WjetsWCR.GetBinContent(1), WjetsWCR.GetBinError(1), WjetsTCR.GetBinContent(1), WjetsTCR.GetBinError(1),
        WjetsXR2.GetBinContent(1), WjetsXR2.GetBinError(1), WjetsSR.GetBinContent(1), WjetsSR.GetBinError(1))

    print " \\ttbargamma & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        ttbargammaWCR.GetBinContent(1), ttbargammaWCR.GetBinError(1), ttbargammaTCR.GetBinContent(1), ttbargammaTCR.GetBinError(1),
        ttbargammaXR2.GetBinContent(1), ttbargammaXR2.GetBinError(1), ttbargammaSR.GetBinContent(1), ttbargammaSR.GetBinError(1))

    print " \\dilep & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        ttbarDilepWCR.GetBinContent(1), ttbarDilepWCR.GetBinError(1), ttbarDilepTCR.GetBinContent(1), ttbarDilepTCR.GetBinError(1),
        ttbarDilepXR2.GetBinContent(1), ttbarDilepXR2.GetBinError(1), ttbarDilepSR.GetBinContent(1), ttbarDilepSR.GetBinError(1))

    print " \\lepjets & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        ttbarLepjetsWCR.GetBinContent(1), ttbarLepjetsWCR.GetBinError(1), ttbarLepjetsTCR.GetBinContent(1), ttbarLepjetsTCR.GetBinError(1),
        ttbarLepjetsXR2.GetBinContent(1), ttbarLepjetsXR2.GetBinError(1), ttbarLepjetsSR.GetBinContent(1), ttbarLepjetsSR.GetBinError(1))

    print " single top & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        stWCR.GetBinContent(1), stWCR.GetBinError(1), stTCR.GetBinContent(1), stTCR.GetBinError(1),
        stXR2.GetBinContent(1), stXR2.GetBinError(1), stSR.GetBinContent(1), stSR.GetBinError(1))

    print " diboson & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        dibosonWCR.GetBinContent(1), dibosonWCR.GetBinError(1), dibosonTCR.GetBinContent(1), dibosonTCR.GetBinError(1),
        dibosonXR2.GetBinContent(1), dibosonXR2.GetBinError(1), dibosonSR.GetBinContent(1), dibosonSR.GetBinError(1))

    print " \\Zgamma & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        ZgammaWCR.GetBinContent(1), ZgammaWCR.GetBinError(1), ZgammaTCR.GetBinContent(1), ZgammaTCR.GetBinError(1),
        ZgammaXR2.GetBinContent(1), ZgammaXR2.GetBinError(1), ZgammaSR.GetBinContent(1), ZgammaSR.GetBinError(1))

    print " \\Zjets & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        ZjetsWCR.GetBinContent(1), ZjetsWCR.GetBinError(1), ZjetsTCR.GetBinContent(1), ZjetsTCR.GetBinError(1),
        ZjetsXR2.GetBinContent(1), ZjetsXR2.GetBinError(1), ZjetsSR.GetBinContent(1), ZjetsSR.GetBinError(1))

    if lepton == ELECTRON:
        print " diphoton & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
            diphotonsWCR.GetBinContent(1), diphotonsWCR.GetBinError(1), diphotonsTCR.GetBinContent(1), diphotonsTCR.GetBinError(1),
            diphotonsXR2.GetBinContent(1), diphotonsXR2.GetBinError(1), diphotonsSR.GetBinContent(1), diphotonsSR.GetBinError(1))

    print " \\gammajet & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        gjWCR.GetBinContent(1), gjWCR.GetBinError(1), gjTCR.GetBinContent(1), gjTCR.GetBinError(1),
        gjXR2.GetBinContent(1), gjXR2.GetBinError(1), gjSR.GetBinContent(1), gjSR.GetBinError(1))

    print "\\hline"

    print " total predicted & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ & $%.1f \pm %.1f$ \\\\" % (
        totalMMWCR.GetBinContent(1), totalMMWCR.GetBinError(1), totalMMTCR.GetBinContent(1), totalMMTCR.GetBinError(1),
        totalMMXR2.GetBinContent(1), totalMMXR2.GetBinError(1), totalMMSR.GetBinContent(1), totalMMSR.GetBinError(1))

    print "\\hline"

    if BLIND:
        print " data & $%.0f \pm %.1f$ & $%.0f \pm %.1f$ & $%.0f \pm %.1f$ & --- \\\\" % (
            dataWCR.GetBinContent(1), dataWCR.GetBinError(1), dataTCR.GetBinContent(1), dataTCR.GetBinError(1),
            dataXR2.GetBinContent(1), dataXR2.GetBinError(1))
    else:
        print " data & $%.0f \pm %.1f$ & $%.0f \pm %.1f$ & $%.0f \pm %.1f$ & $%.0f \pm %.1f$ \\\\" % (
            dataWCR.GetBinContent(1), dataWCR.GetBinError(1), dataTCR.GetBinContent(1), dataTCR.GetBinError(1),
            dataXR2.GetBinContent(1), dataXR2.GetBinError(1), dataSR.GetBinContent(1), dataSR.GetBinError(1))

    print "\\hline"
