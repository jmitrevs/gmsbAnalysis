/////////////////////////////////////////////////////////////////////////
//code used to calculate the photon efficiencies
//    eff_trk = (n1+2n2)/2(n1+n2+n3)
//and also plot the lhood efficiency vs detector eta with and without 
// E/P requirement
////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <fstream>
#include <iomanip>
#include <TApplication.h>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TH1.h>
#include <TF1.h>
#include <TPostScript.h>
#include <TCanvas.h>
#include <TStyle.h>
#include <TGraphErrors.h>

#include "HistogramParams.hpp"
#include "MakeEfficiencies.hpp"

using namespace effMacros;

// the range over which a fit is sought

//const Option_t *FIT_OPTIONS="L0";


////////////////////////////////////
// Main Program
////////////////////////////////////
int main(int argc, char** argv){

  // Set the style for making plots
  gROOT->SetBatch(kTRUE);
  gStyle->SetOptFit(kTRUE);
  Color_t white=10;
  gStyle->SetCanvasColor(white);
//   gStyle->SetStatColor(white);
//   gStyle->SetTitleColor(white);
//   gStyle->SetLabelOffset(0.015,"XYZ");
//   //gStyle->SetOptStat(1111);
//   //  gStyle->SetOptStat(111111);
//   gStyle->SetOptFit(1111);
        
  gStyle->SetOptStat(0);
  
  if(argc != 2) {
    std::cout << "You have to provide the ROOT file to process" << std::endl
	      << "The command line must be: run_PhotonEff *.root" << std::endl;
    return 1;
  }
  
  // Process the command line.
  char *inROOT = argv[1];
  
  // Try to open the ROOT tuple: issue an error if this is not possible.
  TFile *finROOT;
  try {
    finROOT = new TFile(inROOT,"READ");
  } catch (...) {
    std::cout << "Can not open the file " << inROOT << std::endl;
    return 1;
  }
  
  TCanvas *c1 = new TCanvas("c1","1",50,10,700,800);
  // c1->SetLogy();
  TPostScript *hist = new TPostScript("PhotonEff.ps");  
  TFile *Target = TFile::Open( "PhotonEff.root", "RECREATE" );


  // container efficiency vs eta
  TH1F *ph_eta_truth = (TH1F *)finROOT -> Get("Photon/ph_eta_truth");
  TH1F *ph_eta_cont = (TH1F *)finROOT -> Get("Photon/ph_eta_cont");

  ph_eta_truth->Rebin(4);
  ph_eta_cont->Rebin(4);

  TH1F *ph_eta_cont_eff = 
    new TH1F("ph_eta_cont_eff", 
	     "Photon container efficiency;#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_cont_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_cont_eff->Sumw2();

  Efficiency(ph_eta_cont, ph_eta_truth, ph_eta_cont_eff);

  hist -> NewPage();
  ph_eta_cont_eff->SetMarkerStyle(8);
  ph_eta_cont_eff->Draw();
  ph_eta_cont_eff->Write();
  c1->Update();

  // container efficiency vs pt
  TH1F *ph_pt_truth = (TH1F *)finROOT -> Get("Photon/ph_pt_truth");
  TH1F *ph_pt_cont = (TH1F *)finROOT -> Get("Photon/ph_pt_cont");

  ph_pt_truth->Rebin(10);
  ph_pt_cont->Rebin(10);

  TH1F *ph_pt_cont_eff = 
    new TH1F("ph_pt_cont_eff", 
	     "Photon container efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_cont_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_cont_eff->Sumw2();

  Efficiency(ph_pt_cont, ph_pt_truth, ph_pt_cont_eff);

  hist -> NewPage();
  ph_pt_cont_eff->SetMarkerStyle(8);
  ph_pt_cont_eff->Draw();
  ph_pt_cont_eff->Write();
  c1->Update();

  // loose efficiency vs eta (rel truth)
  TH1F *ph_eta_loose = (TH1F *)finROOT -> Get("Photon/ph_eta_loose");

  ph_eta_loose->Rebin(4);

  TH1F *ph_eta_loose_eff = 
    new TH1F("ph_eta_loose_eff", 
	     "Photon loose efficiency;#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_loose_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_loose_eff->Sumw2();

  Efficiency(ph_eta_loose, ph_eta_truth, ph_eta_loose_eff);

  hist -> NewPage();
  ph_eta_loose_eff->SetMarkerStyle(8);
  ph_eta_loose_eff->Draw();
  ph_eta_loose_eff->Write();
  c1->Update();

  // loose efficiency vs pt (rel truth)
  TH1F *ph_pt_loose = (TH1F *)finROOT -> Get("Photon/ph_pt_loose");

  ph_pt_loose->Rebin(10);

  TH1F *ph_pt_loose_eff = 
    new TH1F("ph_pt_loose_eff", 
	     "Photon loose efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_loose_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_loose_eff->Sumw2();

  Efficiency(ph_pt_loose, ph_pt_truth, ph_pt_loose_eff);

  hist -> NewPage();
  ph_pt_loose_eff->SetMarkerStyle(8);
  ph_pt_loose_eff->Draw();
  ph_pt_loose_eff->Write();
  c1->Update();


  // tight efficiency vs eta (rel truth)
  TH1F *ph_eta_tight = (TH1F *)finROOT -> Get("Photon/ph_eta_tight");

  ph_eta_tight->Rebin(4);

  TH1F *ph_eta_tight_eff = 
    new TH1F("ph_eta_tight_eff", 
	     "Photon tight efficiency;#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_tight_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_tight_eff->Sumw2();

  Efficiency(ph_eta_tight, ph_eta_truth, ph_eta_tight_eff);

  hist -> NewPage();
  ph_eta_tight_eff->SetMarkerStyle(8);
  ph_eta_tight_eff->Draw();
  ph_eta_tight_eff->Write();
  c1->Update();

  // tight efficiency vs pt (rel truth)
  TH1F *ph_pt_tight = (TH1F *)finROOT -> Get("Photon/ph_pt_tight");

  ph_pt_tight->Rebin(10);

  TH1F *ph_pt_tight_eff = 
    new TH1F("ph_pt_tight_eff", 
	     "Photon tight efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_tight_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_tight_eff->Sumw2();

  Efficiency(ph_pt_tight, ph_pt_truth, ph_pt_tight_eff);

  hist -> NewPage();
  ph_pt_tight_eff->SetMarkerStyle(8);
  ph_pt_tight_eff->Draw();
  ph_pt_tight_eff->Write();
  c1->Update();

  ///////////////////////////////
  // unconverted
  ///////////////////////////////
  // loose efficiency vs eta (rel container)
  TH1F *ph_eta_cont_unconv = (TH1F *)finROOT -> Get("Photon/ph_eta_cont_unconv");
  TH1F *ph_eta_loose_unconv = (TH1F *)finROOT -> Get("Photon/ph_eta_loose_unconv");

  ph_eta_cont_unconv->Rebin(4);
  ph_eta_loose_unconv->Rebin(4);

  TH1F *ph_eta_loose_unconv_eff = 
    new TH1F("ph_eta_loose_unconv_eff", 
	     "Photon loose_unconv efficiency;#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_loose_unconv_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_loose_unconv_eff->Sumw2();

  Efficiency(ph_eta_loose_unconv, ph_eta_cont_unconv, ph_eta_loose_unconv_eff);

  hist -> NewPage();
  ph_eta_loose_unconv_eff->SetMarkerStyle(8);
  ph_eta_loose_unconv_eff->Draw();
  ph_eta_loose_unconv_eff->Write();
  c1->Update();

  // loose_unconv efficiency vs pt (rel container)
  TH1F *ph_pt_cont_unconv = (TH1F *)finROOT -> Get("Photon/ph_pt_cont_unconv");
  TH1F *ph_pt_loose_unconv = (TH1F *)finROOT -> Get("Photon/ph_pt_loose_unconv");

  ph_pt_cont_unconv->Rebin(10);
  ph_pt_loose_unconv->Rebin(10);

  TH1F *ph_pt_loose_unconv_eff = 
    new TH1F("ph_pt_loose_unconv_eff", 
	     "Photon loose_unconv efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_loose_unconv_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_loose_unconv_eff->Sumw2();

  Efficiency(ph_pt_loose_unconv, ph_pt_cont_unconv, ph_pt_loose_unconv_eff);

  hist -> NewPage();
  ph_pt_loose_unconv_eff->SetMarkerStyle(8);
  ph_pt_loose_unconv_eff->Draw();
  ph_pt_loose_unconv_eff->Write();
  c1->Update();


  // tight efficiency vs eta (rel cont)
  TH1F *ph_eta_tight_unconv = (TH1F *)finROOT -> Get("Photon/ph_eta_tight_unconv");

  ph_eta_tight_unconv->Rebin(4);

  TH1F *ph_eta_tight_unconv_eff = 
    new TH1F("ph_eta_tight_unconv_eff", 
	     "Photon tight_unconv efficiency;#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_tight_unconv_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_tight_unconv_eff->Sumw2();

  Efficiency(ph_eta_tight_unconv, ph_eta_cont_unconv, ph_eta_tight_unconv_eff);

  hist -> NewPage();
  ph_eta_tight_unconv_eff->SetMarkerStyle(8);
  ph_eta_tight_unconv_eff->Draw();
  ph_eta_tight_unconv_eff->Write();
  c1->Update();

  // tight_unconv efficiency vs pt (rel container)
  TH1F *ph_pt_tight_unconv = (TH1F *)finROOT -> Get("Photon/ph_pt_tight_unconv");

  ph_pt_tight_unconv->Rebin(10);

  TH1F *ph_pt_tight_unconv_eff = 
    new TH1F("ph_pt_tight_unconv_eff", 
	     "Photon tight_unconv efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_tight_unconv_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_tight_unconv_eff->Sumw2();

  Efficiency(ph_pt_tight_unconv, ph_pt_cont_unconv, ph_pt_tight_unconv_eff);

  hist -> NewPage();
  ph_pt_tight_unconv_eff->SetMarkerStyle(8);
  ph_pt_tight_unconv_eff->Draw();
  ph_pt_tight_unconv_eff->Write();
  c1->Update();


  ///////////////////////////////
  // one-track conversions
  ///////////////////////////////
  // loose efficiency vs eta (rel container)
  TH1F *ph_eta_cont_conv1 = (TH1F *)finROOT -> Get("Photon/ph_eta_cont_conv1");
  TH1F *ph_eta_loose_conv1 = (TH1F *)finROOT -> Get("Photon/ph_eta_loose_conv1");

  ph_eta_cont_conv1->Rebin(4);
  ph_eta_loose_conv1->Rebin(4);

  TH1F *ph_eta_loose_conv1_eff = 
    new TH1F("ph_eta_loose_conv1_eff", 
	     "Photon loose_conv1 efficiency;#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_loose_conv1_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_loose_conv1_eff->Sumw2();

  Efficiency(ph_eta_loose_conv1, ph_eta_cont_conv1, ph_eta_loose_conv1_eff);

  hist -> NewPage();
  ph_eta_loose_conv1_eff->SetMarkerStyle(8);
  ph_eta_loose_conv1_eff->Draw();
  ph_eta_loose_conv1_eff->Write();
  c1->Update();

  // loose_conv1 efficiency vs pt (rel container)
  TH1F *ph_pt_cont_conv1 = (TH1F *)finROOT -> Get("Photon/ph_pt_cont_conv1");
  TH1F *ph_pt_loose_conv1 = (TH1F *)finROOT -> Get("Photon/ph_pt_loose_conv1");

  ph_pt_cont_conv1->Rebin(10);
  ph_pt_loose_conv1->Rebin(10);

  TH1F *ph_pt_loose_conv1_eff = 
    new TH1F("ph_pt_loose_conv1_eff", 
	     "Photon loose_conv1 efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_loose_conv1_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_loose_conv1_eff->Sumw2();

  Efficiency(ph_pt_loose_conv1, ph_pt_cont_conv1, ph_pt_loose_conv1_eff);

  hist -> NewPage();
  ph_pt_loose_conv1_eff->SetMarkerStyle(8);
  ph_pt_loose_conv1_eff->Draw();
  ph_pt_loose_conv1_eff->Write();
  c1->Update();


  // tight efficiency vs eta (rel cont)
  TH1F *ph_eta_tight_conv1 = (TH1F *)finROOT -> Get("Photon/ph_eta_tight_conv1");

  ph_eta_tight_conv1->Rebin(4);

  TH1F *ph_eta_tight_conv1_eff = 
    new TH1F("ph_eta_tight_conv1_eff", 
	     "Photon tight_conv1 efficiency;#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_tight_conv1_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_tight_conv1_eff->Sumw2();

  Efficiency(ph_eta_tight_conv1, ph_eta_cont_conv1, ph_eta_tight_conv1_eff);

  hist -> NewPage();
  ph_eta_tight_conv1_eff->SetMarkerStyle(8);
  ph_eta_tight_conv1_eff->Draw();
  ph_eta_tight_conv1_eff->Write();
  c1->Update();

  // tight_conv1 efficiency vs pt (rel container)
  TH1F *ph_pt_tight_conv1 = (TH1F *)finROOT -> Get("Photon/ph_pt_tight_conv1");

  ph_pt_tight_conv1->Rebin(10);

  TH1F *ph_pt_tight_conv1_eff = 
    new TH1F("ph_pt_tight_conv1_eff", 
	     "Photon tight_conv1 efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_tight_conv1_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_tight_conv1_eff->Sumw2();

  Efficiency(ph_pt_tight_conv1, ph_pt_cont_conv1, ph_pt_tight_conv1_eff);

  hist -> NewPage();
  ph_pt_tight_conv1_eff->SetMarkerStyle(8);
  ph_pt_tight_conv1_eff->Draw();
  ph_pt_tight_conv1_eff->Write();
  c1->Update();


  ///////////////////////////////
  // two-track conversion
  ///////////////////////////////
  // loose efficiency vs eta (rel container)
  TH1F *ph_eta_cont_conv2 = (TH1F *)finROOT -> Get("Photon/ph_eta_cont_conv2");
  TH1F *ph_eta_loose_conv2 = (TH1F *)finROOT -> Get("Photon/ph_eta_loose_conv2");

  ph_eta_cont_conv2->Rebin(4);
  ph_eta_loose_conv2->Rebin(4);

  TH1F *ph_eta_loose_conv2_eff = 
    new TH1F("ph_eta_loose_conv2_eff", 
	     "Photon loose_conv2 efficiency;#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_loose_conv2_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_loose_conv2_eff->Sumw2();

  Efficiency(ph_eta_loose_conv2, ph_eta_cont_conv2, ph_eta_loose_conv2_eff);

  hist -> NewPage();
  ph_eta_loose_conv2_eff->SetMarkerStyle(8);
  ph_eta_loose_conv2_eff->Draw();
  ph_eta_loose_conv2_eff->Write();
  c1->Update();

  // loose_conv2 efficiency vs pt (rel container)
  TH1F *ph_pt_cont_conv2 = (TH1F *)finROOT -> Get("Photon/ph_pt_cont_conv2");
  TH1F *ph_pt_loose_conv2 = (TH1F *)finROOT -> Get("Photon/ph_pt_loose_conv2");

  ph_pt_cont_conv2->Rebin(10);
  ph_pt_loose_conv2->Rebin(10);

  TH1F *ph_pt_loose_conv2_eff = 
    new TH1F("ph_pt_loose_conv2_eff", 
	     "Photon loose_conv2 efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_loose_conv2_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_loose_conv2_eff->Sumw2();

  Efficiency(ph_pt_loose_conv2, ph_pt_cont_conv2, ph_pt_loose_conv2_eff);

  hist -> NewPage();
  ph_pt_loose_conv2_eff->SetMarkerStyle(8);
  ph_pt_loose_conv2_eff->Draw();
  ph_pt_loose_conv2_eff->Write();
  c1->Update();


  // tight efficiency vs eta (rel cont)
  TH1F *ph_eta_tight_conv2 = (TH1F *)finROOT -> Get("Photon/ph_eta_tight_conv2");

  ph_eta_tight_conv2->Rebin(4);

  TH1F *ph_eta_tight_conv2_eff = 
    new TH1F("ph_eta_tight_conv2_eff", 
	     "Photon tight_conv2 efficiency;#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_tight_conv2_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_tight_conv2_eff->Sumw2();

  Efficiency(ph_eta_tight_conv2, ph_eta_cont_conv2, ph_eta_tight_conv2_eff);

  hist -> NewPage();
  ph_eta_tight_conv2_eff->SetMarkerStyle(8);
  ph_eta_tight_conv2_eff->Draw();
  ph_eta_tight_conv2_eff->Write();
  c1->Update();

  // tight_conv2 efficiency vs pt (rel container)
  TH1F *ph_pt_tight_conv2 = (TH1F *)finROOT -> Get("Photon/ph_pt_tight_conv2");

  ph_pt_tight_conv2->Rebin(10);

  TH1F *ph_pt_tight_conv2_eff = 
    new TH1F("ph_pt_tight_conv2_eff", 
	     "Photon tight_conv2 efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_tight_conv2_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_tight_conv2_eff->Sumw2();

  Efficiency(ph_pt_tight_conv2, ph_pt_cont_conv2, ph_pt_tight_conv2_eff);

  hist -> NewPage();
  ph_pt_tight_conv2_eff->SetMarkerStyle(8);
  ph_pt_tight_conv2_eff->Draw();
  ph_pt_tight_conv2_eff->Write();
  c1->Update();

  // Our Isolation

  // cont efficiency vs eta (rel container)
  TH1F *ph_eta_cont_iso = (TH1F *)finROOT -> Get("Photon/ph_eta_cont_iso");

  ph_eta_cont_iso->Rebin(4);

  TH1F *ph_eta_cont_iso_eff = 
    new TH1F("ph_eta_cont_iso_eff", 
	     "Photon cont iso efficiency (rel truth);#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_cont_iso_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_cont_iso_eff->Sumw2();

  Efficiency(ph_eta_cont_iso, ph_eta_truth, ph_eta_cont_iso_eff);

  hist -> NewPage();
  ph_eta_cont_iso_eff->SetMarkerStyle(8);
  ph_eta_cont_iso_eff->Draw();
  ph_eta_cont_iso_eff->Write();
  c1->Update();

  // cont_iso efficiency vs pt
  TH1F *ph_pt_cont_iso = (TH1F *)finROOT -> Get("Photon/ph_pt_cont_iso");

  ph_pt_cont_iso->Rebin(10);

  TH1F *ph_pt_cont_iso_eff = 
    new TH1F("ph_pt_cont_iso_eff", 
	     "Photon cont_iso efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_cont_iso_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_cont_iso_eff->Sumw2();

  Efficiency(ph_pt_cont_iso, ph_pt_truth, ph_pt_cont_iso_eff);

  hist -> NewPage();
  ph_pt_cont_iso_eff->SetMarkerStyle(8);
  ph_pt_cont_iso_eff->Draw();
  ph_pt_cont_iso_eff->Write();
  c1->Update();

  // loose efficiency vs eta
  TH1F *ph_eta_loose_iso = (TH1F *)finROOT -> Get("Photon/ph_eta_loose_iso");

  ph_eta_loose_iso->Rebin(4);

  TH1F *ph_eta_loose_iso_eff = 
    new TH1F("ph_eta_loose_iso_eff", 
	     "Photon loose iso efficiency (rel truth);#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_loose_iso_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_loose_iso_eff->Sumw2();

  Efficiency(ph_eta_loose_iso, ph_eta_truth, ph_eta_loose_iso_eff);

  hist -> NewPage();
  ph_eta_loose_iso_eff->SetMarkerStyle(8);
  ph_eta_loose_iso_eff->Draw();
  ph_eta_loose_iso_eff->Write();
  c1->Update();

  // loose_iso efficiency vs pt (rel container)
  TH1F *ph_pt_loose_iso = (TH1F *)finROOT -> Get("Photon/ph_pt_loose_iso");

  ph_pt_loose_iso->Rebin(10);

  TH1F *ph_pt_loose_iso_eff = 
    new TH1F("ph_pt_loose_iso_eff", 
	     "Photon loose_iso efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_loose_iso_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_loose_iso_eff->Sumw2();

  Efficiency(ph_pt_loose_iso, ph_pt_truth, ph_pt_loose_iso_eff);

  hist -> NewPage();
  ph_pt_loose_iso_eff->SetMarkerStyle(8);
  ph_pt_loose_iso_eff->Draw();
  ph_pt_loose_iso_eff->Write();
  c1->Update();

  // tight efficiency vs eta (rel container)
  TH1F *ph_eta_tight_iso = (TH1F *)finROOT -> Get("Photon/ph_eta_tight_iso");

  ph_eta_tight_iso->Rebin(4);

  TH1F *ph_eta_tight_iso_eff = 
    new TH1F("ph_eta_tight_iso_eff", 
	     "Photon tight iso efficiency (rel truth);#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_tight_iso_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_tight_iso_eff->Sumw2();

  Efficiency(ph_eta_tight_iso, ph_eta_truth, ph_eta_tight_iso_eff);

  hist -> NewPage();
  ph_eta_tight_iso_eff->SetMarkerStyle(8);
  ph_eta_tight_iso_eff->Draw();
  ph_eta_tight_iso_eff->Write();
  c1->Update();

  // tight_iso efficiency vs pt (rel container)
  TH1F *ph_pt_tight_iso = (TH1F *)finROOT -> Get("Photon/ph_pt_tight_iso");

  ph_pt_tight_iso->Rebin(10);

  TH1F *ph_pt_tight_iso_eff = 
    new TH1F("ph_pt_tight_iso_eff", 
	     "Photon tight_iso efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_tight_iso_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_tight_iso_eff->Sumw2();

  Efficiency(ph_pt_tight_iso, ph_pt_truth, ph_pt_tight_iso_eff);

  hist -> NewPage();
  ph_pt_tight_iso_eff->SetMarkerStyle(8);
  ph_pt_tight_iso_eff->Draw();
  ph_pt_tight_iso_eff->Write();
  c1->Update();

  // Direct Photon Isolation

  // cont efficiency vs eta (rel container)
  TH1F *ph_eta_cont_isodp = (TH1F *)finROOT -> Get("Photon/ph_eta_cont_isodp");

  ph_eta_cont_isodp->Rebin(4);

  TH1F *ph_eta_cont_isodp_eff = 
    new TH1F("ph_eta_cont_isodp_eff", 
	     "Photon cont iso efficiency (rel truth);#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_cont_isodp_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_cont_isodp_eff->Sumw2();

  Efficiency(ph_eta_cont_isodp, ph_eta_truth, ph_eta_cont_isodp_eff);

  hist -> NewPage();
  ph_eta_cont_isodp_eff->SetMarkerStyle(8);
  ph_eta_cont_isodp_eff->Draw();
  ph_eta_cont_isodp_eff->Write();
  c1->Update();

  // cont_isodp efficiency vs pt
  TH1F *ph_pt_cont_isodp = (TH1F *)finROOT -> Get("Photon/ph_pt_cont_isodp");

  ph_pt_cont_isodp->Rebin(10);

  TH1F *ph_pt_cont_isodp_eff = 
    new TH1F("ph_pt_cont_isodp_eff", 
	     "Photon cont_isodp efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_cont_isodp_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_cont_isodp_eff->Sumw2();

  Efficiency(ph_pt_cont_isodp, ph_pt_truth, ph_pt_cont_isodp_eff);

  hist -> NewPage();
  ph_pt_cont_isodp_eff->SetMarkerStyle(8);
  ph_pt_cont_isodp_eff->Draw();
  ph_pt_cont_isodp_eff->Write();
  c1->Update();

  // loose efficiency vs eta
  TH1F *ph_eta_loose_isodp = (TH1F *)finROOT -> Get("Photon/ph_eta_loose_isodp");

  ph_eta_loose_isodp->Rebin(4);

  TH1F *ph_eta_loose_isodp_eff = 
    new TH1F("ph_eta_loose_isodp_eff", 
	     "Photon loose iso efficiency (rel truth);#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_loose_isodp_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_loose_isodp_eff->Sumw2();

  Efficiency(ph_eta_loose_isodp, ph_eta_truth, ph_eta_loose_isodp_eff);

  hist -> NewPage();
  ph_eta_loose_isodp_eff->SetMarkerStyle(8);
  ph_eta_loose_isodp_eff->Draw();
  ph_eta_loose_isodp_eff->Write();
  c1->Update();

  // loose_isodp efficiency vs pt (rel container)
  TH1F *ph_pt_loose_isodp = (TH1F *)finROOT -> Get("Photon/ph_pt_loose_isodp");

  ph_pt_loose_isodp->Rebin(10);

  TH1F *ph_pt_loose_isodp_eff = 
    new TH1F("ph_pt_loose_isodp_eff", 
	     "Photon loose_isodp efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_loose_isodp_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_loose_isodp_eff->Sumw2();

  Efficiency(ph_pt_loose_isodp, ph_pt_truth, ph_pt_loose_isodp_eff);

  hist -> NewPage();
  ph_pt_loose_isodp_eff->SetMarkerStyle(8);
  ph_pt_loose_isodp_eff->Draw();
  ph_pt_loose_isodp_eff->Write();
  c1->Update();

  // tight efficiency vs eta (rel container)
  TH1F *ph_eta_tight_isodp = (TH1F *)finROOT -> Get("Photon/ph_eta_tight_isodp");

  ph_eta_tight_isodp->Rebin(4);

  TH1F *ph_eta_tight_isodp_eff = 
    new TH1F("ph_eta_tight_isodp_eff", 
	     "Photon tight iso efficiency (rel truth);#eta", eta_bins/4, eta_low, eta_high);
  ph_eta_tight_isodp_eff->SetAxisRange(0, 1.2, "Y");
  ph_eta_tight_isodp_eff->Sumw2();

  Efficiency(ph_eta_tight_isodp, ph_eta_truth, ph_eta_tight_isodp_eff);

  hist -> NewPage();
  ph_eta_tight_isodp_eff->SetMarkerStyle(8);
  ph_eta_tight_isodp_eff->Draw();
  ph_eta_tight_isodp_eff->Write();
  c1->Update();

  // tight_isodp efficiency vs pt (rel container)
  TH1F *ph_pt_tight_isodp = (TH1F *)finROOT -> Get("Photon/ph_pt_tight_isodp");

  ph_pt_tight_isodp->Rebin(10);

  TH1F *ph_pt_tight_isodp_eff = 
    new TH1F("ph_pt_tight_isodp_eff", 
	     "Photon tight_isodp efficiency;p_{T} [GeV]", pt_bins/10, pt_low, pt_high);
  ph_pt_tight_isodp_eff->SetAxisRange(0, 1.2, "Y");
  ph_pt_tight_isodp_eff->Sumw2();

  Efficiency(ph_pt_tight_isodp, ph_pt_truth, ph_pt_tight_isodp_eff);

  hist -> NewPage();
  ph_pt_tight_isodp_eff->SetMarkerStyle(8);
  ph_pt_tight_isodp_eff->Draw();
  ph_pt_tight_isodp_eff->Write();
  c1->Update();


  ////// let's output the distributions

  hist -> NewPage();
  ph_eta_truth->SetMarkerStyle(8);
  ph_eta_truth->Draw();
  ph_eta_truth->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_cont->SetMarkerStyle(8);
  ph_eta_cont->Draw();
  ph_eta_cont->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_loose->SetMarkerStyle(8);
  ph_eta_loose->Draw();
  ph_eta_loose->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_tight->SetMarkerStyle(8);
  ph_eta_tight->Draw();
  ph_eta_tight->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_cont_unconv->SetMarkerStyle(8);
  ph_eta_cont_unconv->Draw();
  ph_eta_cont_unconv->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_loose_unconv->SetMarkerStyle(8);
  ph_eta_loose_unconv->Draw();
  ph_eta_loose_unconv->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_tight_unconv->SetMarkerStyle(8);
  ph_eta_tight_unconv->Draw();
  ph_eta_tight_unconv->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_cont_conv1->SetMarkerStyle(8);
  ph_eta_cont_conv1->Draw();
  ph_eta_cont_conv1->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_loose_conv1->SetMarkerStyle(8);
  ph_eta_loose_conv1->Draw();
  ph_eta_loose_conv1->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_tight_conv1->SetMarkerStyle(8);
  ph_eta_tight_conv1->Draw();
  ph_eta_tight_conv1->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_cont_conv2->SetMarkerStyle(8);
  ph_eta_cont_conv2->Draw();
  ph_eta_cont_conv2->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_loose_conv2->SetMarkerStyle(8);
  ph_eta_loose_conv2->Draw();
  ph_eta_loose_conv2->Write();
  c1->Update();

  hist -> NewPage();
  ph_eta_tight_conv2->SetMarkerStyle(8);
  ph_eta_tight_conv2->Draw();
  ph_eta_tight_conv2->Write();
  c1->Update();


  hist -> NewPage();
  ph_pt_truth->SetMarkerStyle(8);
  ph_pt_truth->Draw();
  ph_pt_truth->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_cont->SetMarkerStyle(8);
  ph_pt_cont->Draw();
  ph_pt_cont->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_loose->SetMarkerStyle(8);
  ph_pt_loose->Draw();
  ph_pt_loose->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_tight->SetMarkerStyle(8);
  ph_pt_tight->Draw();
  ph_pt_tight->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_cont_unconv->SetMarkerStyle(8);
  ph_pt_cont_unconv->Draw();
  ph_pt_cont_unconv->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_loose_unconv->SetMarkerStyle(8);
  ph_pt_loose_unconv->Draw();
  ph_pt_loose_unconv->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_tight_unconv->SetMarkerStyle(8);
  ph_pt_tight_unconv->Draw();
  ph_pt_tight_unconv->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_cont_conv1->SetMarkerStyle(8);
  ph_pt_cont_conv1->Draw();
  ph_pt_cont_conv1->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_loose_conv1->SetMarkerStyle(8);
  ph_pt_loose_conv1->Draw();
  ph_pt_loose_conv1->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_tight_conv1->SetMarkerStyle(8);
  ph_pt_tight_conv1->Draw();
  ph_pt_tight_conv1->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_cont_conv2->SetMarkerStyle(8);
  ph_pt_cont_conv2->Draw();
  ph_pt_cont_conv2->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_loose_conv2->SetMarkerStyle(8);
  ph_pt_loose_conv2->Draw();
  ph_pt_loose_conv2->Write();
  c1->Update();

  hist -> NewPage();
  ph_pt_tight_conv2->SetMarkerStyle(8);
  ph_pt_tight_conv2->Draw();
  ph_pt_tight_conv2->Write();
  c1->Update();

  hist->Close();
  Target->Close();

}
