
#include <string>
#include <iostream>

#include "TH1.h"
#include "TFile.h"
#include "THStack.h"
#include "TCanvas.h"

#include <vector>

void LepPhotonPlots() 

{

  const double Lumi = 5000.0;


  /////////////////////////////////////

  const std::string path = "/data3/jmitrevs/lepphoton/mergedFiles/";

  const std::string WenuFileName_Np0 = path + "Wenu_Np0.root";
  const std::string WenuFileName_Np1 = path + "Wenu_Np1.root";
  const std::string WenuFileName_Np2 = path + "Wenu_Np2.root";
  const std::string WenuFileName_Np3 = path + "Wenu_Np3.root";
  const std::string WenuFileName_Np4 = path + "Wenu_Np4.root";
  const std::string WenuFileName_Np5 = path + "Wenu_Np5.root";

  const std::string WtaunuFileName_Np0 = path + "Wtaunu_Np0.root";
  const std::string WtaunuFileName_Np1 = path + "Wtaunu_Np1.root";
  const std::string WtaunuFileName_Np2 = path + "Wtaunu_Np2.root";
  const std::string WtaunuFileName_Np3 = path + "Wtaunu_Np3.root";
  const std::string WtaunuFileName_Np4 = path + "Wtaunu_Np4.root";
  const std::string WtaunuFileName_Np5 = path + "Wtaunu_Np5.root";

  const std::string WgammaFileName_Np0 = path + "Wgamma_Np0.root";
  const std::string WgammaFileName_Np1 = path + "Wgamma_Np1.root";
  const std::string WgammaFileName_Np2 = path + "Wgamma_Np2.root";
  const std::string WgammaFileName_Np3 = path + "Wgamma_Np3.root";
  const std::string WgammaFileName_Np4 = path + "Wgamma_Np4.root";
  const std::string WgammaFileName_Np5 = path + "Wgamma_Np5.root";

  const std::string ttbarFileName = path + "ttbar.root";

  const std::string st_tchan_enuFileName   = path + "st_tchan_enu.root";
  const std::string st_tchan_taunuFileName = path + "st_tchan_taunu.root";

  const std::string st_schan_enuFileName   = path + "st_schan_enu.root";
  const std::string st_schan_taunuFileName = path + "st_schan_taunu.root";

  const std::string st_WtFileName   = path + "st_Wt.root";

  /////////////////////////////////////

  const TFile *WenuFile_Np0 = new TFile(WenuFileName_Np0.c_str());
  const TFile *WenuFile_Np1 = new TFile(WenuFileName_Np1.c_str());
  const TFile *WenuFile_Np2 = new TFile(WenuFileName_Np2.c_str());
  const TFile *WenuFile_Np3 = new TFile(WenuFileName_Np3.c_str());
  const TFile *WenuFile_Np4 = new TFile(WenuFileName_Np4.c_str());
  const TFile *WenuFile_Np5 = new TFile(WenuFileName_Np5.c_str());

  const TFile *WtaunuFile_Np0 = new TFile(WtaunuFileName_Np0.c_str());
  const TFile *WtaunuFile_Np1 = new TFile(WtaunuFileName_Np1.c_str());
  const TFile *WtaunuFile_Np2 = new TFile(WtaunuFileName_Np2.c_str());
  const TFile *WtaunuFile_Np3 = new TFile(WtaunuFileName_Np3.c_str());
  const TFile *WtaunuFile_Np4 = new TFile(WtaunuFileName_Np4.c_str());
  const TFile *WtaunuFile_Np5 = new TFile(WtaunuFileName_Np5.c_str());

  const TFile *WgammaFile_Np0 = new TFile(WgammaFileName_Np0.c_str());
  const TFile *WgammaFile_Np1 = new TFile(WgammaFileName_Np1.c_str());
  const TFile *WgammaFile_Np2 = new TFile(WgammaFileName_Np2.c_str());
  const TFile *WgammaFile_Np3 = new TFile(WgammaFileName_Np3.c_str());
  const TFile *WgammaFile_Np4 = new TFile(WgammaFileName_Np4.c_str());
  const TFile *WgammaFile_Np5 = new TFile(WgammaFileName_Np5.c_str());

  const TFile *ttbarFile = new TFile(ttbarFileName.c_str());

  const TFile *st_tchan_enuFile   = new TFile(st_tchan_enuFileName.c_str());
  const TFile *st_tchan_taunuFile = new TFile(st_tchan_taunuFileName.c_str());

  const TFile *st_schan_enuFile   = new TFile(st_schan_enuFileName.c_str());
  const TFile *st_schan_taunuFile = new TFile(st_schan_taunuFileName.c_str());
  
  const TFile *st_WtFile   = new TFile(st_WtFileName.c_str());

  ///////////////////////////////////////////

  TH1D *nOrigHistWenu_Np0 = ((TH1D *) WenuFile_Np0->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWenu_Np1 = ((TH1D *) WenuFile_Np1->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWenu_Np2 = ((TH1D *) WenuFile_Np2->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWenu_Np3 = ((TH1D *) WenuFile_Np3->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWenu_Np4 = ((TH1D *) WenuFile_Np4->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWenu_Np5 = ((TH1D *) WenuFile_Np5->Get("Global/nOriginalEvents"))->Clone();

  TH1D *nOrigHistWtaunu_Np0 = ((TH1D *) WtaunuFile_Np0->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWtaunu_Np1 = ((TH1D *) WtaunuFile_Np1->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWtaunu_Np2 = ((TH1D *) WtaunuFile_Np2->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWtaunu_Np3 = ((TH1D *) WtaunuFile_Np3->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWtaunu_Np4 = ((TH1D *) WtaunuFile_Np4->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWtaunu_Np5 = ((TH1D *) WtaunuFile_Np5->Get("Global/nOriginalEvents"))->Clone();

  TH1D *nOrigHistWgamma_Np0 = ((TH1D *) WgammaFile_Np0->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWgamma_Np1 = ((TH1D *) WgammaFile_Np1->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWgamma_Np2 = ((TH1D *) WgammaFile_Np2->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWgamma_Np3 = ((TH1D *) WgammaFile_Np3->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWgamma_Np4 = ((TH1D *) WgammaFile_Np4->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistWgamma_Np5 = ((TH1D *) WgammaFile_Np5->Get("Global/nOriginalEvents"))->Clone();

  TH1D *nOrigHistttbar = ((TH1D *) ttbarFile->Get("Global/nOriginalEvents"))->Clone();

  TH1D *nOrigHistst_tchan_enu = ((TH1D *) st_tchan_enuFile->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistst_tchan_taunu = ((TH1D *) st_tchan_taunuFile->Get("Global/nOriginalEvents"))->Clone();

  TH1D *nOrigHistst_schan_enu = ((TH1D *) st_schan_enuFile->Get("Global/nOriginalEvents"))->Clone();
  TH1D *nOrigHistst_schan_taunu = ((TH1D *) st_schan_taunuFile->Get("Global/nOriginalEvents"))->Clone();

  TH1D *nOrigHistst_Wt   = ((TH1D *) st_WtFile->Get("Global/nOriginalEvents"))->Clone();

  ////////////////////////////////////////////////

  const double nOrigWenu_Np0 = nOrigHistWenuFile_Np0->GetBinContent(1);
  const double nOrigWenu_Np1 = nOrigHistWenuFile_Np1->GetBinContent(1);
  const double nOrigWenu_Np2 = nOrigHistWenuFile_Np2->GetBinContent(1);
  const double nOrigWenu_Np3 = nOrigHistWenuFile_Np3->GetBinContent(1);
  const double nOrigWenu_Np4 = nOrigHistWenuFile_Np4->GetBinContent(1);
  const double nOrigWenu_Np5 = nOrigHistWenuFile_Np5->GetBinContent(1);

  const double nOrigWtaunu_Np0 = nOrigHistWtaunuFile_Np0->GetBinContent(1);
  const double nOrigWtaunu_Np1 = nOrigHistWtaunuFile_Np1->GetBinContent(1);
  const double nOrigWtaunu_Np2 = nOrigHistWtaunuFile_Np2->GetBinContent(1);
  const double nOrigWtaunu_Np3 = nOrigHistWtaunuFile_Np3->GetBinContent(1);
  const double nOrigWtaunu_Np4 = nOrigHistWtaunuFile_Np4->GetBinContent(1);
  const double nOrigWtaunu_Np5 = nOrigHistWtaunuFile_Np5->GetBinContent(1);

  const double nOrigWgamma_Np0 = nOrigHistWgammaFile_Np0->GetBinContent(1);
  const double nOrigWgamma_Np1 = nOrigHistWgammaFile_Np1->GetBinContent(1);
  const double nOrigWgamma_Np2 = nOrigHistWgammaFile_Np2->GetBinContent(1);
  const double nOrigWgamma_Np3 = nOrigHistWgammaFile_Np3->GetBinContent(1);
  const double nOrigWgamma_Np4 = nOrigHistWgammaFile_Np4->GetBinContent(1);
  const double nOrigWgamma_Np5 = nOrigHistWgammaFile_Np5->GetBinContent(1);

  const double nOrigttbar = nOrigHistttbarFile->GetBinContent(1);

  const double nOrigst_tchan_enu = nOrigHistst_tchan_enuFile->GetBinContent(1);
  const double nOrigst_tchan_taunu = nOrigHistst_tchan_taunuFile->GetBinContent(1);

  const double nOrigst_schan_enu = nOrigHistst_schan_enuFile->GetBinContent(1);
  const double nOrigst_schan_taunu = nOrigHistst_schan_taunuFile->GetBinContent(1);

  const double nOrigst_Wt   = nOrigHistst_WtFile->GetBinContent(1);


  // let's print out the number of events for debugging
  std::cout << "Number of input events:\n";
  std::cout << "\tnOrigWenu_Np0 = " << nOrigWenuFile_Np0 << std::endl;
  std::cout << "\tnOrigWenu_Np1 = " << nOrigWenuFile_Np1 << std::endl;
  std::cout << "\tnOrigWenu_Np2 = " << nOrigWenuFile_Np2 << std::endl;
  std::cout << "\tnOrigWenu_Np3 = " << nOrigWenuFile_Np3 << std::endl;
  std::cout << "\tnOrigWenu_Np4 = " << nOrigWenuFile_Np4 << std::endl;
  std::cout << "\tnOrigWenu_Np5 = " << nOrigWenuFile_Np5 << std::endl;

  std::cout << "\tnOrigWtaunu_Np0 = " << nOrigWtaunuFile_Np0 << std::endl;
  std::cout << "\tnOrigWtaunu_Np1 = " << nOrigWtaunuFile_Np1 << std::endl;
  std::cout << "\tnOrigWtaunu_Np2 = " << nOrigWtaunuFile_Np2 << std::endl;
  std::cout << "\tnOrigWtaunu_Np3 = " << nOrigWtaunuFile_Np3 << std::endl;
  std::cout << "\tnOrigWtaunu_Np4 = " << nOrigWtaunuFile_Np4 << std::endl;
  std::cout << "\tnOrigWtaunu_Np5 = " << nOrigWtaunuFile_Np5 << std::endl;

  std::cout << "\tnOrigWgamma_Np0 = " << nOrigWgammaFile_Np0 << std::endl;
  std::cout << "\tnOrigWgamma_Np1 = " << nOrigWgammaFile_Np1 << std::endl;
  std::cout << "\tnOrigWgamma_Np2 = " << nOrigWgammaFile_Np2 << std::endl;
  std::cout << "\tnOrigWgamma_Np3 = " << nOrigWgammaFile_Np3 << std::endl;
  std::cout << "\tnOrigWgamma_Np4 = " << nOrigWgammaFile_Np4 << std::endl;
  std::cout << "\tnOrigWgamma_Np5 = " << nOrigWgammaFile_Np5 << std::endl;

  std::cout << "\tnOrigttbar = " << nOrigttbarFile << std::endl;

  std::cout << "\tnOrigst_tchan_enu = " << nOrigst_tchan_enuFile << std::endl;
  std::cout << "\tnOrigst_tchan_taunu = " << nOrigst_tchan_taunuFile << std::endl;

  std::cout << "\tnOrigst_schan_enu = " << nOrigst_schan_enuFile << std::endl;
  std::cout << "\tnOrigst_schan_taunu = " << nOrigst_schan_taunuFile << std::endl;

  std::cout << "\tnOrigst_Wt   = " << nOrigst_WtFile << std::endl;

  // scale is lumi * xsec * kfact / numEvents

  const double  Wenu_Np0_scale     =  Lumi  *  6921.60 * 1.20   / nOrigWenu_Np0;
  const double  Wenu_Np1_scale     =  Lumi  *  1304.30 * 1.20   / nOrigWenu_Np1;
  const double  Wenu_Np2_scale     =  Lumi  *   378.29 * 1.20   / nOrigWenu_Np2;
  const double  Wenu_Np3_scale     =  Lumi  *   101.43 * 1.20   / nOrigWenu_Np3;
  const double  Wenu_Np4_scale     =  Lumi  *    25.87 * 1.20   / nOrigWenu_Np4;
  const double  Wenu_Np5_scale     =  Lumi  *     7.00 * 1.20   / nOrigWenu_Np5;

  const double  Wtaunu_Np0_scale   =  Lumi  *  6919.60 * 1.20   / nOrigWtaunu_Np0;
  const double  Wtaunu_Np1_scale   =  Lumi  *  1303.20 * 1.20   / nOrigWtaunu_Np1;
  const double  Wtaunu_Np2_scale   =  Lumi  *   378.18 * 1.20   / nOrigWtaunu_Np2;
  const double  Wtaunu_Np3_scale   =  Lumi  *   101.43 * 1.20   / nOrigWtaunu_Np3;
  const double  Wtaunu_Np4_scale   =  Lumi  *    25.87 * 1.20   / nOrigWtaunu_Np4;
  const double  Wtaunu_Np5_scale   =  Lumi  *     6.92 * 1.20   / nOrigWtaunu_Np5;

  const double  ttbar_scale          =  Lumi  * 147.49  / nOrigttbar;

  const double  Wgamma_Np0_scale     =  Lumi  *  213.270 * 1.45   / nOrigWgamma_Np0;
  const double  Wgamma_Np1_scale     =  Lumi  *   52.238 * 1.45   / nOrigWgamma_Np1;
  const double  Wgamma_Np2_scale     =  Lumi  *   17.259 * 1.45   / nOrigWgamma_Np2;
  const double  Wgamma_Np3_scale     =  Lumi  *    5.3339 * 1.45   / nOrigWgamma_Np3;
  const double  Wgamma_Np4_scale     =  Lumi  *    1.3762 * 1.45   / nOrigWgamma_Np4;
  const double  Wgamma_Np5_scale     =  Lumi  *    0.34445 * 1.45   / nOrigWgamma_Np5;

  //const double  Zeegamma_scale        =  Lumi  *  10.022 *  1.22   / nOrigZeegamma;
  //const double  Ztautaugamma_scale    =  Lumi  *   9.7639 * 1.22   / nOrigZtautaugamma;

  const double  st_tchan_enu_scale   = Lumi * 6.8317 / nOrigst_tchan_enu;
  const double  st_tchan_taunu_scale = Lumi * 6.8053 / nOrigst_tchan_taunu;

  const double  st_schan_enu_scale   = Lumi * 0.46117 / nOrigst_schan_enu;
  const double  st_schan_taunu_scale = Lumi * 0.46158 / nOrigst_schan_taunu;

  const double  st_Wt_scale = Lumi * 14.372 / nOrigst_Wt;


  ////////////////////////

  // now make a list of histogram names
  std::vector<std::string> histNames;

  // take the ttbar as the input that defines what should be in every file
  TKey *key;
  TIter nextkey(ttbarFile->GetListOfKeys());
  while (key = (TKey*) nextkey()) {
    TObject* obj = key->ReadObj();
    if ( obj->IsA()->InheritsFrom("TDirectory") ){
    

  ////////////////////////////

  Wenu_Np0->Scale(Wenu_Np0_scale);
  Wenu_Np1->Scale(Wenu_Np1_scale);
  Wenu_Np2->Scale(Wenu_Np2_scale);
  Wenu_Np3->Scale(Wenu_Np3_scale);
  Wenu_Np4->Scale(Wenu_Np4_scale);
  Wenu_Np5->Scale(Wenu_Np5_scale);

  Wmunu_Np0->Scale(Wmunu_Np0_scale);
  Wmunu_Np1->Scale(Wmunu_Np1_scale);
  Wmunu_Np2->Scale(Wmunu_Np2_scale);
  Wmunu_Np3->Scale(Wmunu_Np3_scale);
  Wmunu_Np4->Scale(Wmunu_Np4_scale);
  Wmunu_Np5->Scale(Wmunu_Np5_scale);

  Wtaunu_Np0->Scale(Wtaunu_Np0_scale);
  Wtaunu_Np1->Scale(Wtaunu_Np1_scale);
  Wtaunu_Np2->Scale(Wtaunu_Np2_scale);
  Wtaunu_Np3->Scale(Wtaunu_Np3_scale);
  Wtaunu_Np4->Scale(Wtaunu_Np4_scale);
  Wtaunu_Np5->Scale(Wtaunu_Np5_scale);

  Wgamma_Np0->Scale(Wgamma_Np0_scale);
  Wgamma_Np1->Scale(Wgamma_Np1_scale);
  Wgamma_Np2->Scale(Wgamma_Np2_scale);
  Wgamma_Np3->Scale(Wgamma_Np3_scale);
  Wgamma_Np4->Scale(Wgamma_Np4_scale);
  Wgamma_Np5->Scale(Wgamma_Np5_scale);

  ttbar->Scale(ttbar_scale);

  st_tchan_enu->Scale(st_tchan_enu_scale);
  st_tchan_munu->Scale(st_tchan_munu_scale);
  st_tchan_taunu->Scale(st_tchan_taunu_scale);

  st_schan_enu->Scale(st_schan_enu_scale);
  st_schan_munu->Scale(st_schan_munu_scale);
  st_schan_taunu->Scale(st_schan_taunu_scale);

  st_Wt->Scale(st_Wt_scale);

  ////////////////////

  TH1F* Wenu = Wenu_Np0->Clone();
  Wenu->Add(Wenu_Np1);
  Wenu->Add(Wenu_Np2);
  Wenu->Add(Wenu_Np3);
  Wenu->Add(Wenu_Np4);
  Wenu->Add(Wenu_Np5);

  TH1F* Wmunu = Wmunu_Np0->Clone();
  Wmunu->Add(Wmunu_Np1);
  Wmunu->Add(Wmunu_Np2);
  Wmunu->Add(Wmunu_Np3);
  Wmunu->Add(Wmunu_Np4);
  Wmunu->Add(Wmunu_Np5);

  TH1F* Wtaunu = Wtaunu_Np0->Clone();
  Wtaunu->Add(Wtaunu_Np1);
  Wtaunu->Add(Wtaunu_Np2);
  Wtaunu->Add(Wtaunu_Np3);
  Wtaunu->Add(Wtaunu_Np4);
  Wtaunu->Add(Wtaunu_Np5);

  TH1F* Wjets = Wenu->Clone();
  Wjets->Add(Wmunu);
  Wjets->Add(Wtaunu);

  TH1F* Wgamma = Wgamma_Np0->Clone();
  Wgamma->Add(Wgamma_Np1);
  Wgamma->Add(Wgamma_Np2);
  Wgamma->Add(Wgamma_Np3);
  Wgamma->Add(Wgamma_Np4);
  Wgamma->Add(Wgamma_Np5);

  TH1F* st_tchan = st_tchan_enu->Clone();
  st_tchan->Add(st_tchan_munu);
  st_tchan->Add(st_tchan_taunu);

  TH1F* st_schan = st_schan_enu->Clone();
  st_schan->Add(st_schan_munu);
  st_schan->Add(st_schan_taunu);

  TH1F* st = st_tchan->Clone();
  st->Add(st_schan);
  st->Add(st_Wt);

  c_paper = new TCanvas("Paper","Paper",700,410,500,400);
  //c_paper->SetLogy();

  THStack *bg = new THStack("bg","stacked bg;E_{T}^{miss} [GeV];Events");

  //bg->SetXTitle("E_{T}^{miss} [GeV]"); 

  Wjets->SetFillStyle(1001);
  Wgamma->SetFillStyle(1001);
  ttbar->SetFillStyle(1001);
  st->SetFillStyle(1001);

  Wjets->SetFillColor(3);
  Wjets->SetLineColor(3);
  Wgamma->SetFillColor(7);
  Wgamma->SetLineColor(7);
  ttbar->SetFillColor(2);
  ttbar->SetLineColor(2);
  st->SetFillColor(9);
  st->SetLineColor(9);
  
  bg->Add(Wjets);
  bg->Add(Wgamma);
  bg->Add(ttbar);
  bg->Add(st);

  bg->Draw();

  legb = new TLegend(0.5,0.55,0.93,0.92);
  legb->SetFillColor(0);
  legb->SetBorderSize(0);
  legb->SetTextSize(0.045);
  legb->AddEntry(Wjets,"W+jets","f");
  legb->AddEntry(Wgamma,"Wgamma","f");
  legb->AddEntry(ttbar,"ttbar","f");
  legb->AddEntry(st,"singe top","f");
  legb->Draw();

  c_paper->Print("MetPlot.eps");
  c_paper->Print("MetPlot.png");
  
}

    
