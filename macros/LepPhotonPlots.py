#! /usr/bin/env python

# code to make all the plots in a file

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

ELECTRON = 0
MUON = 1

def LepPhotonPlots(lepton):

    Lumi = 5000.0


    if lepton == ELECTRON:

        print "Lepton is ELECTRON."
        path = "/data3/jmitrevs/lepphoton/elphoton_ph50/mergedFiles/"

        WlepnuFileName_Np0 = path + "Wenu_Np0.root"
        WlepnuFileName_Np1 = path + "Wenu_Np1.root"
        WlepnuFileName_Np2 = path + "Wenu_Np2.root"
        WlepnuFileName_Np3 = path + "Wenu_Np3.root"
        WlepnuFileName_Np4 = path + "Wenu_Np4.root"
        WlepnuFileName_Np5 = path + "Wenu_Np5.root"
        st_tchan_lepnuFileName   = path + "st_tchan_enu.root"
        st_schan_lepnuFileName   = path + "st_schan_enu.root"
    elif lepton == MUON:

        print "Lepton is MUON."
        path = "/data3/jmitrevs/lepphoton/old/mergedFiles/"

        WlepnuFileName_Np0 = path + "Wmunu_Np0.root"
        WlepnuFileName_Np1 = path + "Wmunu_Np1.root"
        WlepnuFileName_Np2 = path + "Wmunu_Np2.root"
        WlepnuFileName_Np3 = path + "Wmunu_Np3.root"
        WlepnuFileName_Np4 = path + "Wmunu_Np4.root"
        WlepnuFileName_Np5 = path + "Wmunu_Np5.root"
        st_tchan_lepnuFileName   = path + "st_tchan_munu.root"
        st_schan_lepnuFileName   = path + "st_schan_munu.root"
    else:
        print "Lepton has to be ELECTRON or MUON."
        return

    
    WtaunuFileName_Np0 = path + "Wtaunu_Np0.root"
    WtaunuFileName_Np1 = path + "Wtaunu_Np1.root"
    WtaunuFileName_Np2 = path + "Wtaunu_Np2.root"
    WtaunuFileName_Np3 = path + "Wtaunu_Np3.root"
    WtaunuFileName_Np4 = path + "Wtaunu_Np4.root"
    WtaunuFileName_Np5 = path + "Wtaunu_Np5.root"

    st_tchan_taunuFileName = path + "st_tchan_taunu.root"    
    st_schan_taunuFileName = path + "st_schan_taunu.root"
    st_WtFileName   = path + "st_Wt.root"    
    
    WgammaFileName_Np0 = path + "Wgamma_Np0.root"
    WgammaFileName_Np1 = path + "Wgamma_Np1.root"
    WgammaFileName_Np2 = path + "Wgamma_Np2.root"
    WgammaFileName_Np3 = path + "Wgamma_Np3.root"
    WgammaFileName_Np4 = path + "Wgamma_Np4.root"
    WgammaFileName_Np5 = path + "Wgamma_Np5.root"
    
    ttbarFileName = path + "ttbar.root"
    
    
    ###########################################

    WlepnuFile_Np0 = ROOT.TFile(WlepnuFileName_Np0)
    WlepnuFile_Np1 = ROOT.TFile(WlepnuFileName_Np1)
    WlepnuFile_Np2 = ROOT.TFile(WlepnuFileName_Np2)
    WlepnuFile_Np3 = ROOT.TFile(WlepnuFileName_Np3)
    WlepnuFile_Np4 = ROOT.TFile(WlepnuFileName_Np4)
    WlepnuFile_Np5 = ROOT.TFile(WlepnuFileName_Np5)
    
    WtaunuFile_Np0 = ROOT.TFile(WtaunuFileName_Np0)
    WtaunuFile_Np1 = ROOT.TFile(WtaunuFileName_Np1)
    WtaunuFile_Np2 = ROOT.TFile(WtaunuFileName_Np2)
    WtaunuFile_Np3 = ROOT.TFile(WtaunuFileName_Np3)
    WtaunuFile_Np4 = ROOT.TFile(WtaunuFileName_Np4)
    WtaunuFile_Np5 = ROOT.TFile(WtaunuFileName_Np5)
    
    WgammaFile_Np0 = ROOT.TFile(WgammaFileName_Np0)
    WgammaFile_Np1 = ROOT.TFile(WgammaFileName_Np1)
    WgammaFile_Np2 = ROOT.TFile(WgammaFileName_Np2)
    WgammaFile_Np3 = ROOT.TFile(WgammaFileName_Np3)
    WgammaFile_Np4 = ROOT.TFile(WgammaFileName_Np4)
    WgammaFile_Np5 = ROOT.TFile(WgammaFileName_Np5)
    
    ttbarFile = ROOT.TFile(ttbarFileName)
    
    st_tchan_lepnuFile   = ROOT.TFile(st_tchan_lepnuFileName)
    st_tchan_taunuFile = ROOT.TFile(st_tchan_taunuFileName)
    
    st_schan_lepnuFile   = ROOT.TFile(st_schan_lepnuFileName)
    st_schan_taunuFile = ROOT.TFile(st_schan_taunuFileName)
    
    st_WtFile   = ROOT.TFile(st_WtFileName)
    
    ##############################

    nOrigHistWlepnu_Np0 = WlepnuFile_Np0.Get("Global/nOriginalEvents")
    nOrigHistWlepnu_Np1 = WlepnuFile_Np1.Get("Global/nOriginalEvents")
    nOrigHistWlepnu_Np2 = WlepnuFile_Np2.Get("Global/nOriginalEvents")
    nOrigHistWlepnu_Np3 = WlepnuFile_Np3.Get("Global/nOriginalEvents")
    nOrigHistWlepnu_Np4 = WlepnuFile_Np4.Get("Global/nOriginalEvents")
    nOrigHistWlepnu_Np5 = WlepnuFile_Np5.Get("Global/nOriginalEvents")

    nOrigHistWtaunu_Np0 = WtaunuFile_Np0.Get("Global/nOriginalEvents")
    nOrigHistWtaunu_Np1 = WtaunuFile_Np1.Get("Global/nOriginalEvents")
    nOrigHistWtaunu_Np2 = WtaunuFile_Np2.Get("Global/nOriginalEvents")
    nOrigHistWtaunu_Np3 = WtaunuFile_Np3.Get("Global/nOriginalEvents")
    nOrigHistWtaunu_Np4 = WtaunuFile_Np4.Get("Global/nOriginalEvents")
    nOrigHistWtaunu_Np5 = WtaunuFile_Np5.Get("Global/nOriginalEvents")

    nOrigHistWgamma_Np0 = WgammaFile_Np0.Get("Global/nOriginalEvents")
    nOrigHistWgamma_Np1 = WgammaFile_Np1.Get("Global/nOriginalEvents")
    nOrigHistWgamma_Np2 = WgammaFile_Np2.Get("Global/nOriginalEvents")
    nOrigHistWgamma_Np3 = WgammaFile_Np3.Get("Global/nOriginalEvents")
    nOrigHistWgamma_Np4 = WgammaFile_Np4.Get("Global/nOriginalEvents")
    nOrigHistWgamma_Np5 = WgammaFile_Np5.Get("Global/nOriginalEvents")

    nOrigHistttbar = ttbarFile.Get("Global/nOriginalEvents")

    nOrigHistst_tchan_lepnu = st_tchan_lepnuFile.Get("Global/nOriginalEvents")
    nOrigHistst_tchan_taunu = st_tchan_taunuFile.Get("Global/nOriginalEvents")

    nOrigHistst_schan_lepnu = st_schan_lepnuFile.Get("Global/nOriginalEvents")
    nOrigHistst_schan_taunu = st_schan_taunuFile.Get("Global/nOriginalEvents")

    nOrigHistst_Wt   = st_WtFile.Get("Global/nOriginalEvents")

    #########################################################

    nOrigWlepnu_Np0 = nOrigHistWlepnu_Np0.GetBinContent(1)
    nOrigWlepnu_Np1 = nOrigHistWlepnu_Np1.GetBinContent(1)
    nOrigWlepnu_Np2 = nOrigHistWlepnu_Np2.GetBinContent(1)
    nOrigWlepnu_Np3 = nOrigHistWlepnu_Np3.GetBinContent(1)
    nOrigWlepnu_Np4 = nOrigHistWlepnu_Np4.GetBinContent(1)
    nOrigWlepnu_Np5 = nOrigHistWlepnu_Np5.GetBinContent(1)
    
    nOrigWtaunu_Np0 = nOrigHistWtaunu_Np0.GetBinContent(1)
    nOrigWtaunu_Np1 = nOrigHistWtaunu_Np1.GetBinContent(1)
    nOrigWtaunu_Np2 = nOrigHistWtaunu_Np2.GetBinContent(1)
    nOrigWtaunu_Np3 = nOrigHistWtaunu_Np3.GetBinContent(1)
    nOrigWtaunu_Np4 = nOrigHistWtaunu_Np4.GetBinContent(1)
    nOrigWtaunu_Np5 = nOrigHistWtaunu_Np5.GetBinContent(1)
    
    nOrigWgamma_Np0 = nOrigHistWgamma_Np0.GetBinContent(1)
    nOrigWgamma_Np1 = nOrigHistWgamma_Np1.GetBinContent(1)
    nOrigWgamma_Np2 = nOrigHistWgamma_Np2.GetBinContent(1)
    nOrigWgamma_Np3 = nOrigHistWgamma_Np3.GetBinContent(1)
    nOrigWgamma_Np4 = nOrigHistWgamma_Np4.GetBinContent(1)
    nOrigWgamma_Np5 = nOrigHistWgamma_Np5.GetBinContent(1)
    
    nOrigttbar = nOrigHistttbar.GetBinContent(1)
    
    nOrigst_tchan_lepnu = nOrigHistst_tchan_lepnu.GetBinContent(1)
    nOrigst_tchan_taunu = nOrigHistst_tchan_taunu.GetBinContent(1)
    
    nOrigst_schan_lepnu = nOrigHistst_schan_lepnu.GetBinContent(1)
    nOrigst_schan_taunu = nOrigHistst_schan_taunu.GetBinContent(1)
    
    nOrigst_Wt   = nOrigHistst_Wt.GetBinContent(1)
    

    # let's print out the number of events for debugging
    print "Number of input events:"
    print "\tnOrigWlepnu_Np0 = ", nOrigWlepnu_Np0
    print "\tnOrigWlepnu_Np1 = ", nOrigWlepnu_Np1
    print "\tnOrigWlepnu_Np2 = ", nOrigWlepnu_Np2
    print "\tnOrigWlepnu_Np3 = ", nOrigWlepnu_Np3
    print "\tnOrigWlepnu_Np4 = ", nOrigWlepnu_Np4
    print "\tnOrigWlepnu_Np5 = ", nOrigWlepnu_Np5
    
    print "\tnOrigWtaunu_Np0 = ", nOrigWtaunu_Np0
    print "\tnOrigWtaunu_Np1 = ", nOrigWtaunu_Np1
    print "\tnOrigWtaunu_Np2 = ", nOrigWtaunu_Np2
    print "\tnOrigWtaunu_Np3 = ", nOrigWtaunu_Np3
    print "\tnOrigWtaunu_Np4 = ", nOrigWtaunu_Np4
    print "\tnOrigWtaunu_Np5 = ", nOrigWtaunu_Np5
    
    print "\tnOrigWgamma_Np0 = ", nOrigWgamma_Np0
    print "\tnOrigWgamma_Np1 = ", nOrigWgamma_Np1
    print "\tnOrigWgamma_Np2 = ", nOrigWgamma_Np2
    print "\tnOrigWgamma_Np3 = ", nOrigWgamma_Np3
    print "\tnOrigWgamma_Np4 = ", nOrigWgamma_Np4
    print "\tnOrigWgamma_Np5 = ", nOrigWgamma_Np5
    
    print "\tnOrigttbar = ", nOrigttbar
    
    print "\tnOrigst_tchan_lepnu = ", nOrigst_tchan_lepnu
    print "\tnOrigst_tchan_taunu = ", nOrigst_tchan_taunu
    
    print "\tnOrigst_schan_lepnu = ", nOrigst_schan_lepnu
    print "\tnOrigst_schan_taunu = ", nOrigst_schan_taunu
    
    print "\tnOrigst_Wt   = ", nOrigst_Wt

#   // scale is lumi * xsec * kfact / numEvents

#     Wlepnu_Np0_scale     =  Lumi  *  6921.60 * 1.20   / nOrigWlepnu_Np0
#     Wlepnu_Np1_scale     =  Lumi  *  1304.30 * 1.20   / nOrigWlepnu_Np1
#     Wlepnu_Np2_scale     =  Lumi  *   378.29 * 1.20   / nOrigWlepnu_Np2
#     Wlepnu_Np3_scale     =  Lumi  *   101.43 * 1.20   / nOrigWlepnu_Np3
#     Wlepnu_Np4_scale     =  Lumi  *    25.87 * 1.20   / nOrigWlepnu_Np4
#     Wlepnu_Np5_scale     =  Lumi  *     7.00 * 1.20   / nOrigWlepnu_Np5

#     Wtaunu_Np0_scale   =  Lumi  *  6919.60 * 1.20   / nOrigWtaunu_Np0
#     Wtaunu_Np1_scale   =  Lumi  *  1303.20 * 1.20   / nOrigWtaunu_Np1
#     Wtaunu_Np2_scale   =  Lumi  *   378.18 * 1.20   / nOrigWtaunu_Np2
#     Wtaunu_Np3_scale   =  Lumi  *   101.43 * 1.20   / nOrigWtaunu_Np3
#     Wtaunu_Np4_scale   =  Lumi  *    25.87 * 1.20   / nOrigWtaunu_Np4
#     Wtaunu_Np5_scale   =  Lumi  *     6.92 * 1.20   / nOrigWtaunu_Np5

#     ttbar_scale          =  Lumi  * 147.49  / nOrigttbar

#     Wgamma_Np0_scale     =  Lumi  *  213.270 * 1.45   / nOrigWgamma_Np0
#     Wgamma_Np1_scale     =  Lumi  *   52.238 * 1.45   / nOrigWgamma_Np1
#     Wgamma_Np2_scale     =  Lumi  *   17.259 * 1.45   / nOrigWgamma_Np2
#     Wgamma_Np3_scale     =  Lumi  *    5.3339 * 1.45   / nOrigWgamma_Np3
#     Wgamma_Np4_scale     =  Lumi  *    1.3762 * 1.45   / nOrigWgamma_Np4
#     Wgamma_Np5_scale     =  Lumi  *    0.34445 * 1.45   / nOrigWgamma_Np5

#   //  Zeegamma_scale        =  Lumi  *  10.022 *  1.22   / nOrigZeegamma
#   //  Ztautaugamma_scale    =  Lumi  *   9.7639 * 1.22   / nOrigZtautaugamma

#     st_tchan_lepnu_scale   = Lumi * 6.8317 / nOrigst_tchan_lepnu
#     st_tchan_taunu_scale = Lumi * 6.8053 / nOrigst_tchan_taunu

#     st_schan_lepnu_scale   = Lumi * 0.46117 / nOrigst_schan_lepnu
#     st_schan_taunu_scale = Lumi * 0.46158 / nOrigst_schan_taunu

#     st_Wt_scale = Lumi * 14.372 / nOrigst_Wt


#   ////////////////////////

#   // now make a list of histogram names
#   std::vector<std::string> histNames

#   // take the ttbar as the input that defines what should be in every file
#   TKey *key
#   TIter nextkey(ttbarFile->GetListOfKeys())
#   while (key = (TKey*) nextkey()) {
#     TObject* obj = key->ReadObj()
#     if ( obj->IsA()->InheritsFrom("TDirectory") ){
    

#   ////////////////////////////

#   Wlepnu_Np0->Scale(Wlepnu_Np0_scale)
#   Wlepnu_Np1->Scale(Wlepnu_Np1_scale)
#   Wlepnu_Np2->Scale(Wlepnu_Np2_scale)
#   Wlepnu_Np3->Scale(Wlepnu_Np3_scale)
#   Wlepnu_Np4->Scale(Wlepnu_Np4_scale)
#   Wlepnu_Np5->Scale(Wlepnu_Np5_scale)

#   Wmunu_Np0->Scale(Wmunu_Np0_scale)
#   Wmunu_Np1->Scale(Wmunu_Np1_scale)
#   Wmunu_Np2->Scale(Wmunu_Np2_scale)
#   Wmunu_Np3->Scale(Wmunu_Np3_scale)
#   Wmunu_Np4->Scale(Wmunu_Np4_scale)
#   Wmunu_Np5->Scale(Wmunu_Np5_scale)

#   Wtaunu_Np0->Scale(Wtaunu_Np0_scale)
#   Wtaunu_Np1->Scale(Wtaunu_Np1_scale)
#   Wtaunu_Np2->Scale(Wtaunu_Np2_scale)
#   Wtaunu_Np3->Scale(Wtaunu_Np3_scale)
#   Wtaunu_Np4->Scale(Wtaunu_Np4_scale)
#   Wtaunu_Np5->Scale(Wtaunu_Np5_scale)

#   Wgamma_Np0->Scale(Wgamma_Np0_scale)
#   Wgamma_Np1->Scale(Wgamma_Np1_scale)
#   Wgamma_Np2->Scale(Wgamma_Np2_scale)
#   Wgamma_Np3->Scale(Wgamma_Np3_scale)
#   Wgamma_Np4->Scale(Wgamma_Np4_scale)
#   Wgamma_Np5->Scale(Wgamma_Np5_scale)

#   ttbar->Scale(ttbar_scale)

#   st_tchan_lepnu->Scale(st_tchan_lepnu_scale)
#   st_tchan_munu->Scale(st_tchan_munu_scale)
#   st_tchan_taunu->Scale(st_tchan_taunu_scale)

#   st_schan_lepnu->Scale(st_schan_lepnu_scale)
#   st_schan_munu->Scale(st_schan_munu_scale)
#   st_schan_taunu->Scale(st_schan_taunu_scale)

#   st_Wt->Scale(st_Wt_scale)

#   ////////////////////

#   TH1F* Wlepnu = Wlepnu_Np0->Clone()
#   Wlepnu->Add(Wlepnu_Np1)
#   Wlepnu->Add(Wlepnu_Np2)
#   Wlepnu->Add(Wlepnu_Np3)
#   Wlepnu->Add(Wlepnu_Np4)
#   Wlepnu->Add(Wlepnu_Np5)

#   TH1F* Wmunu = Wmunu_Np0->Clone()
#   Wmunu->Add(Wmunu_Np1)
#   Wmunu->Add(Wmunu_Np2)
#   Wmunu->Add(Wmunu_Np3)
#   Wmunu->Add(Wmunu_Np4)
#   Wmunu->Add(Wmunu_Np5)

#   TH1F* Wtaunu = Wtaunu_Np0->Clone()
#   Wtaunu->Add(Wtaunu_Np1)
#   Wtaunu->Add(Wtaunu_Np2)
#   Wtaunu->Add(Wtaunu_Np3)
#   Wtaunu->Add(Wtaunu_Np4)
#   Wtaunu->Add(Wtaunu_Np5)

#   TH1F* Wjets = Wlepnu->Clone()
#   Wjets->Add(Wmunu)
#   Wjets->Add(Wtaunu)

#   TH1F* Wgamma = Wgamma_Np0->Clone()
#   Wgamma->Add(Wgamma_Np1)
#   Wgamma->Add(Wgamma_Np2)
#   Wgamma->Add(Wgamma_Np3)
#   Wgamma->Add(Wgamma_Np4)
#   Wgamma->Add(Wgamma_Np5)

#   TH1F* st_tchan = st_tchan_lepnu->Clone()
#   st_tchan->Add(st_tchan_munu)
#   st_tchan->Add(st_tchan_taunu)

#   TH1F* st_schan = st_schan_lepnu->Clone()
#   st_schan->Add(st_schan_munu)
#   st_schan->Add(st_schan_taunu)

#   TH1F* st = st_tchan->Clone()
#   st->Add(st_schan)
#   st->Add(st_Wt)

#   c_paper = new TCanvas("Paper","Paper",700,410,500,400)
#   //c_paper->SetLogy()

#   THStack *bg = new THStack("bg","stacked bgE_{T}^{miss} [GeV]Events")

#   //bg->SetXTitle("E_{T}^{miss} [GeV]") 

#   Wjets->SetFillStyle(1001)
#   Wgamma->SetFillStyle(1001)
#   ttbar->SetFillStyle(1001)
#   st->SetFillStyle(1001)

#   Wjets->SetFillColor(3)
#   Wjets->SetLineColor(3)
#   Wgamma->SetFillColor(7)
#   Wgamma->SetLineColor(7)
#   ttbar->SetFillColor(2)
#   ttbar->SetLineColor(2)
#   st->SetFillColor(9)
#   st->SetLineColor(9)
  
#   bg->Add(Wjets)
#   bg->Add(Wgamma)
#   bg->Add(ttbar)
#   bg->Add(st)

#   bg->Draw()

#   legb = new TLegend(0.5,0.55,0.93,0.92)
#   legb->SetFillColor(0)
#   legb->SetBorderSize(0)
#   legb->SetTextSize(0.045)
#   legb->AddEntry(Wjets,"W+jets","f")
#   legb->AddEntry(Wgamma,"Wgamma","f")
#   legb->AddEntry(ttbar,"ttbar","f")
#   legb->AddEntry(st,"singe top","f")
#   legb->Draw()

#   c_paper->Print("MetPlot.eps")
#   c_paper->Print("MetPlot.png")
  
# }

    
