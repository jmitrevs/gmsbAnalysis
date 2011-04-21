/////////////////////////////////////////////////////////////////////////
//code used to calculate the photon efficiencies
//    eff_trk = (n1+2n2)/2(n1+n2+n3)
//and also plot the lhood efficiency vs detector eta with and without 
// E/P requirement
////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <TApplication.h>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TH1.h>
#include <TH2.h>
#include <TF1.h>
#include <TPostScript.h>
#include <TCanvas.h>
#include <TStyle.h>
#include <TGraphErrors.h>
#include <cmath>

//#include "HistogramParams.hpp"
//#include "MakeEfficiencies.hpp"

//using namespace effMacros;

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
  
  if(argc != 4) {
    std::cout << "You have to provide the ROOT files to process" << std::endl
	      << "The command line must be: run_IsoStudy DataSig.root DataBack.root MC.root" << std::endl;
    return 1;
  }
  
  // Process the command line.
  char *inDataSig = argv[1];
  char *inDataBack = argv[2];
  char *inMC = argv[3];
  
  // Try to open the ROOT tuple: issue an error if this is not possible.
  TFile *finDataSig;
  try {
    finDataSig = new TFile(inDataSig,"READ");
  } catch (...) {
    std::cout << "Can not open the file " << inDataSig << std::endl;
    return 1;
  }

  // Try to open the ROOT tuple: issue an error if this is not possible.
  TFile *finDataBack;
  try {
    finDataBack = new TFile(inDataBack,"READ");
  } catch (...) {
    std::cout << "Can not open the file " << inDataBack << std::endl;
    return 1;
  }

  // Try to open the ROOT tuple: issue an error if this is not possible.
  TFile *finMC;
  try {
    finMC = new TFile(inMC,"READ");
  } catch (...) {
    std::cout << "Can not open the file " << inMC << std::endl;
    return 1;
  }

  
  TCanvas *c1 = new TCanvas("c1","1",50,10,700,800);
  // c1->SetLogy();
  TPostScript *hist = new TPostScript("IsoStudy.ps");  
  TFile *Target = TFile::Open( "IsoStudy.root", "RECREATE" );

  std::cout << "**** etcone20 |eta| < 0.6 ****" << std::endl;

  // container efficiency vs eta
  TH2D *hetcone20_0p6_sig = (TH2D *)finDataSig -> Get("hetcone20_0p6");
  TH2D *hetcone20_0p6_back = (TH2D *)finDataBack -> Get("hetcone20_0p6");
  TH2D *hetcone20_0p6_mc = (TH2D *)finMC -> Get("hetcone20_0p6");

  for (int i = 1; i <= hetcone20_0p6_sig->GetNbinsY(); i++) {
    std::stringstream ss_sig, ss_back, ss_mc, ss_bssig;
    ss_sig << "hetcone20_0p6_sig_bin" << i;
    ss_back << "hetcone20_0p6_back_bin" << i;
    ss_mc << "hetcone20_0p6_mc_bin" << i;

    // the background subtracted signal
    ss_bssig << "hetcone20_0p6_bssig_bin" << i;

    TH1D *hsig = hetcone20_0p6_sig->ProjectionX(ss_sig.str().c_str(), i, i);
    TH1D *hback = hetcone20_0p6_back->ProjectionX(ss_back.str().c_str(), i, i);
    TH1D *hmc = hetcone20_0p6_mc->ProjectionX(ss_mc.str().c_str(), i, i);

    hsig->Sumw2();
    hback->Sumw2();
    hmc->Sumw2();


    // const double etCenter = hetcone20_0p6_sig->GetYaxis()->GetBinCenter(i);
    // const double etLow = hetcone20_0p6_sig->GetYaxis()->GetBinLowEdge(i);

    // std::cout << "low et = " << etLow << ", center et = " << etCenter << std::endl; 

    const Int_t numBinsX = hsig->GetNbinsX();

    const Double_t meanSigRaw = hsig->GetMean();
    const Double_t rmsSigRaw = hsig->GetRMS();

    const Double_t intEdge = meanSigRaw + 2*rmsSigRaw;

    TAxis *xaxis = hsig->GetXaxis();
    Int_t bin = xaxis->FindBin(intEdge); //return bin number corresponding to xvalue

    const Double_t sigInt = hsig->Integral(bin, numBinsX);
    const Double_t backInt = hback->Integral(bin, numBinsX);

    hsig->Scale(1.0/sigInt);
    hback->Scale(1.0/backInt);

    // the background subtraced signal
    TH1D *hbsSig = (TH1D *) hsig->Clone(ss_bssig.str().c_str());
    
    hbsSig->Add(hback, -1);	// actually do the subtraction

    hbsSig->Scale(1.0/hbsSig->Integral());
    hmc->Scale(1.0/hmc->Integral());

    hist -> NewPage();
    hsig->SetMarkerStyle(8);
    hsig->SetLineColor(2);
    hsig->Draw();
    hback->Draw("same");
    c1->Update();

    hist -> NewPage();
    hmc->SetLineColor(4);
    hmc->Draw();
    hbsSig->SetMarkerStyle(8);
    hbsSig->SetLineColor(2);
    hbsSig->Draw("same");
    c1->Update();

    hsig->Write();
    hbsSig->Write();
    hback->Write();
    hmc->Write();

    const Double_t meanSig = hbsSig->GetMean();
    const Double_t meanSigError = hbsSig->GetMeanError();
    const Double_t meanMC = hmc->GetMean();
    const Double_t meanMCError = hmc->GetMeanError();
    const Double_t ratio = meanSig/meanMC;

    std::cout << "Bin " << i <<", data/MC diff: " << meanSig - meanMC
	      << " +- " << hypot(meanSigError, meanMCError)
	      << ", scale = " << ratio 
	      << " +- " << hypot(meanSigError/meanSig, meanMCError/meanMC) * ratio << std::endl; 

  }
  std::cout << std::endl;

  std::cout << "**** etcone20 0.6 < |eta| < 1.37 ****" << std::endl;

  // container efficiency vs eta
  TH2D *hetcone20_1p37_sig = (TH2D *)finDataSig -> Get("hetcone20_1p37");
  TH2D *hetcone20_1p37_back = (TH2D *)finDataBack -> Get("hetcone20_1p37");
  TH2D *hetcone20_1p37_mc = (TH2D *)finMC -> Get("hetcone20_1p37");

  for (int i = 1; i <= hetcone20_1p37_sig->GetNbinsY(); i++) {
    std::stringstream ss_sig, ss_back, ss_mc, ss_bssig;
    ss_sig << "hetcone20_1p37_sig_bin" << i;
    ss_back << "hetcone20_1p37_back_bin" << i;
    ss_mc << "hetcone20_1p37_mc_bin" << i;

    // the background subtracted signal
    ss_bssig << "hetcone20_1p37_bssig_bin" << i;

    TH1D *hsig = hetcone20_1p37_sig->ProjectionX(ss_sig.str().c_str(), i, i);
    TH1D *hback = hetcone20_1p37_back->ProjectionX(ss_back.str().c_str(), i, i);
    TH1D *hmc = hetcone20_1p37_mc->ProjectionX(ss_mc.str().c_str(), i, i);

    hsig->Sumw2();
    hback->Sumw2();
    hmc->Sumw2();

    const Int_t numBinsX = hsig->GetNbinsX();

    const Double_t meanSigRaw = hsig->GetMean();
    const Double_t rmsSigRaw = hsig->GetRMS();

    const Double_t intEdge = meanSigRaw + 2*rmsSigRaw;

    TAxis *xaxis = hsig->GetXaxis();
    Int_t bin = xaxis->FindBin(intEdge); //return bin number corresponding to xvalue

    const Double_t sigInt = hsig->Integral(bin, numBinsX);
    const Double_t backInt = hback->Integral(bin, numBinsX);

    hsig->Scale(1.0/sigInt);
    hback->Scale(1.0/backInt);

    // the background subtraced signal
    TH1D *hbsSig = (TH1D *) hsig->Clone(ss_bssig.str().c_str());
    
    hbsSig->Add(hback, -1);	// actually do the subtraction

    hbsSig->Scale(1.0/hbsSig->Integral());
    hmc->Scale(1.0/hmc->Integral());

    hist -> NewPage();
    hsig->SetMarkerStyle(8);
    hsig->SetLineColor(2);
    hsig->Draw();
    hback->Draw("same");
    c1->Update();

    hist -> NewPage();
    hmc->SetLineColor(4);
    hmc->Draw();
    hbsSig->SetMarkerStyle(8);
    hbsSig->SetLineColor(2);
    hbsSig->Draw("same");
    c1->Update();

    hsig->Write();
    hbsSig->Write();
    hback->Write();
    hmc->Write();

    const Double_t meanSig = hbsSig->GetMean();
    const Double_t meanSigError = hbsSig->GetMeanError();
    const Double_t meanMC = hmc->GetMean();
    const Double_t meanMCError = hmc->GetMeanError();
    const Double_t ratio = meanSig/meanMC;

    std::cout << "Bin " << i <<", data/MC diff: " << meanSig - meanMC
	      << " +- " << hypot(meanSigError, meanMCError)
	      << ", scale = " << ratio 
	      << " +- " << hypot(meanSigError/meanSig, meanMCError/meanMC) * ratio << std::endl; 


  }
  std::cout << std::endl;

  std::cout << "**** etcone20 1.37 < |eta| < 1.81 ****" << std::endl;

  // container efficiency vs eta
  TH2D *hetcone20_1p81_sig = (TH2D *)finDataSig -> Get("hetcone20_1p81");
  TH2D *hetcone20_1p81_back = (TH2D *)finDataBack -> Get("hetcone20_1p81");
  TH2D *hetcone20_1p81_mc = (TH2D *)finMC -> Get("hetcone20_1p81");

  for (int i = 1; i <= hetcone20_1p81_sig->GetNbinsY(); i++) {
    std::stringstream ss_sig, ss_back, ss_mc, ss_bssig;
    ss_sig << "hetcone20_1p81_sig_bin" << i;
    ss_back << "hetcone20_1p81_back_bin" << i;
    ss_mc << "hetcone20_1p81_mc_bin" << i;

    // the background subtracted signal
    ss_bssig << "hetcone20_1p81_bssig_bin" << i;

    TH1D *hsig = hetcone20_1p81_sig->ProjectionX(ss_sig.str().c_str(), i, i);
    TH1D *hback = hetcone20_1p81_back->ProjectionX(ss_back.str().c_str(), i, i);
    TH1D *hmc = hetcone20_1p81_mc->ProjectionX(ss_mc.str().c_str(), i, i);

    hsig->Sumw2();
    hback->Sumw2();
    hmc->Sumw2();

    const Int_t numBinsX = hsig->GetNbinsX();

    const Double_t meanSigRaw = hsig->GetMean();
    const Double_t rmsSigRaw = hsig->GetRMS();

    const Double_t intEdge = meanSigRaw + 2*rmsSigRaw;

    TAxis *xaxis = hsig->GetXaxis();
    Int_t bin = xaxis->FindBin(intEdge); //return bin number corresponding to xvalue

    const Double_t sigInt = hsig->Integral(bin, numBinsX);
    const Double_t backInt = hback->Integral(bin, numBinsX);

    hsig->Scale(1.0/sigInt);
    hback->Scale(1.0/backInt);

    // the background subtraced signal
    TH1D *hbsSig = (TH1D *) hsig->Clone(ss_bssig.str().c_str());
    
    hbsSig->Add(hback, -1);	// actually do the subtraction

    hbsSig->Scale(1.0/hbsSig->Integral());
    hmc->Scale(1.0/hmc->Integral());

    hist -> NewPage();
    hsig->SetMarkerStyle(8);
    hsig->SetLineColor(2);
    hsig->Draw();
    hback->Draw("same");
    c1->Update();

    hist -> NewPage();
    hmc->SetLineColor(4);
    hmc->Draw();
    hbsSig->SetMarkerStyle(8);
    hbsSig->SetLineColor(2);
    hbsSig->Draw("same");
    c1->Update();

    hsig->Write();
    hbsSig->Write();
    hback->Write();
    hmc->Write();

    const Double_t meanSig = hbsSig->GetMean();
    const Double_t meanSigError = hbsSig->GetMeanError();
    const Double_t meanMC = hmc->GetMean();
    const Double_t meanMCError = hmc->GetMeanError();
    const Double_t ratio = meanSig/meanMC;

    std::cout << "Bin " << i <<", data/MC diff: " << meanSig - meanMC
	      << " +- " << hypot(meanSigError, meanMCError)
	      << ", scale = " << ratio 
	      << " +- " << hypot(meanSigError/meanSig, meanMCError/meanMC) * ratio << std::endl; 

  }
  std::cout << std::endl;

  /// And now the etcone20/et

  std::cout << "**** etcone20/et |eta| < 0.6 ****" << std::endl;

  // container efficiency vs eta
  TH2D *hetcone20ovet_0p6_sig = (TH2D *)finDataSig -> Get("hetcone20ovet_0p6");
  TH2D *hetcone20ovet_0p6_back = (TH2D *)finDataBack -> Get("hetcone20ovet_0p6");
  TH2D *hetcone20ovet_0p6_mc = (TH2D *)finMC -> Get("hetcone20ovet_0p6");

  for (int i = 1; i <= hetcone20ovet_0p6_sig->GetNbinsY(); i++) {
    std::stringstream ss_sig, ss_back, ss_mc, ss_bssig;
    ss_sig << "hetcone20ovet_0p6_sig_bin" << i;
    ss_back << "hetcone20ovet_0p6_back_bin" << i;
    ss_mc << "hetcone20ovet_0p6_mc_bin" << i;

    // the background subtracted signal
    ss_bssig << "hetcone20ovet_0p6_bssig_bin" << i;

    TH1D *hsig = hetcone20ovet_0p6_sig->ProjectionX(ss_sig.str().c_str(), i, i);
    TH1D *hback = hetcone20ovet_0p6_back->ProjectionX(ss_back.str().c_str(), i, i);
    TH1D *hmc = hetcone20ovet_0p6_mc->ProjectionX(ss_mc.str().c_str(), i, i);

    hsig->Sumw2();
    hback->Sumw2();
    hmc->Sumw2();

    const Int_t numBinsX = hsig->GetNbinsX();

    const Double_t meanSigRaw = hsig->GetMean();
    const Double_t rmsSigRaw = hsig->GetRMS();

    const Double_t intEdge = meanSigRaw + 2*rmsSigRaw;

    TAxis *xaxis = hsig->GetXaxis();
    Int_t bin = xaxis->FindBin(intEdge); //return bin number corresponding to xvalue

    const Double_t sigInt = hsig->Integral(bin, numBinsX);
    const Double_t backInt = hback->Integral(bin, numBinsX);

    hsig->Scale(1.0/sigInt);
    hback->Scale(1.0/backInt);

    // the background subtraced signal
    TH1D *hbsSig = (TH1D *) hsig->Clone(ss_bssig.str().c_str());
    
    hbsSig->Add(hback, -1);	// actually do the subtraction

    hbsSig->Scale(1.0/hbsSig->Integral());
    hmc->Scale(1.0/hmc->Integral());

    hist -> NewPage();
    hsig->SetMarkerStyle(8);
    hsig->SetLineColor(2);
    hsig->Draw();
    hback->Draw("same");
    c1->Update();

    hist -> NewPage();
    hmc->SetLineColor(4);
    hmc->Draw();
    hbsSig->SetMarkerStyle(8);
    hbsSig->SetLineColor(2);
    hbsSig->Draw("same");
    c1->Update();

    hsig->Write();
    hbsSig->Write();
    hback->Write();
    hmc->Write();

    const Double_t meanSig = hbsSig->GetMean();
    const Double_t meanSigError = hbsSig->GetMeanError();
    const Double_t meanMC = hmc->GetMean();
    const Double_t meanMCError = hmc->GetMeanError();
    const Double_t ratio = meanSig/meanMC;

    std::cout << "Bin " << i <<", data/MC diff: " << meanSig - meanMC
	      << " +- " << hypot(meanSigError, meanMCError)
	      << ", scale = " << ratio 
	      << " +- " << hypot(meanSigError/meanSig, meanMCError/meanMC) * ratio << std::endl; 


  }
  std::cout << std::endl;

  std::cout << "**** etcone20/et 0.6 < |eta| < 1.37 ****" << std::endl;

  // container efficiency vs eta
  TH2D *hetcone20ovet_1p37_sig = (TH2D *)finDataSig -> Get("hetcone20ovet_1p37");
  TH2D *hetcone20ovet_1p37_back = (TH2D *)finDataBack -> Get("hetcone20ovet_1p37");
  TH2D *hetcone20ovet_1p37_mc = (TH2D *)finMC -> Get("hetcone20ovet_1p37");

  for (int i = 1; i <= hetcone20ovet_1p37_sig->GetNbinsY(); i++) {
    std::stringstream ss_sig, ss_back, ss_mc, ss_bssig;
    ss_sig << "hetcone20ovet_1p37_sig_bin" << i;
    ss_back << "hetcone20ovet_1p37_back_bin" << i;
    ss_mc << "hetcone20ovet_1p37_mc_bin" << i;

    // the background subtracted signal
    ss_bssig << "hetcone20ovet_1p37_bssig_bin" << i;

    TH1D *hsig = hetcone20ovet_1p37_sig->ProjectionX(ss_sig.str().c_str(), i, i);
    TH1D *hback = hetcone20ovet_1p37_back->ProjectionX(ss_back.str().c_str(), i, i);
    TH1D *hmc = hetcone20ovet_1p37_mc->ProjectionX(ss_mc.str().c_str(), i, i);

    hsig->Sumw2();
    hback->Sumw2();
    hmc->Sumw2();

    const Int_t numBinsX = hsig->GetNbinsX();

    const Double_t meanSigRaw = hsig->GetMean();
    const Double_t rmsSigRaw = hsig->GetRMS();

    const Double_t intEdge = meanSigRaw + 2*rmsSigRaw;

    TAxis *xaxis = hsig->GetXaxis();
    Int_t bin = xaxis->FindBin(intEdge); //return bin number corresponding to xvalue

    const Double_t sigInt = hsig->Integral(bin, numBinsX);
    const Double_t backInt = hback->Integral(bin, numBinsX);

    hsig->Scale(1.0/sigInt);
    hback->Scale(1.0/backInt);

    // the background subtraced signal
    TH1D *hbsSig = (TH1D *) hsig->Clone(ss_bssig.str().c_str());
    
    hbsSig->Add(hback, -1);	// actually do the subtraction

    hbsSig->Scale(1.0/hbsSig->Integral());
    hmc->Scale(1.0/hmc->Integral());

    hist -> NewPage();
    hsig->SetMarkerStyle(8);
    hsig->SetLineColor(2);
    hsig->Draw();
    hback->Draw("same");
    c1->Update();

    hist -> NewPage();
    hmc->SetLineColor(4);
    hmc->Draw();
    hbsSig->SetMarkerStyle(8);
    hbsSig->SetLineColor(2);
    hbsSig->Draw("same");
    c1->Update();

    hsig->Write();
    hbsSig->Write();
    hback->Write();
    hmc->Write();

    const Double_t meanSig = hbsSig->GetMean();
    const Double_t meanSigError = hbsSig->GetMeanError();
    const Double_t meanMC = hmc->GetMean();
    const Double_t meanMCError = hmc->GetMeanError();
    const Double_t ratio = meanSig/meanMC;

    std::cout << "Bin " << i <<", data/MC diff: " << meanSig - meanMC
	      << " +- " << hypot(meanSigError, meanMCError)
	      << ", scale = " << ratio 
	      << " +- " << hypot(meanSigError/meanSig, meanMCError/meanMC) * ratio << std::endl; 


  }
  std::cout << std::endl;

  std::cout << "**** etcone20/et 1.37 < |eta| < 1.81 ****" << std::endl;

  // container efficiency vs eta
  TH2D *hetcone20ovet_1p81_sig = (TH2D *)finDataSig -> Get("hetcone20ovet_1p81");
  TH2D *hetcone20ovet_1p81_back = (TH2D *)finDataBack -> Get("hetcone20ovet_1p81");
  TH2D *hetcone20ovet_1p81_mc = (TH2D *)finMC -> Get("hetcone20ovet_1p81");

  for (int i = 1; i <= hetcone20ovet_1p81_sig->GetNbinsY(); i++) {
    std::stringstream ss_sig, ss_back, ss_mc, ss_bssig;
    ss_sig << "hetcone20ovet_1p81_sig_bin" << i;
    ss_back << "hetcone20ovet_1p81_back_bin" << i;
    ss_mc << "hetcone20ovet_1p81_mc_bin" << i;

    // the background subtracted signal
    ss_bssig << "hetcone20ovet_1p81_bssig_bin" << i;

    TH1D *hsig = hetcone20ovet_1p81_sig->ProjectionX(ss_sig.str().c_str(), i, i);
    TH1D *hback = hetcone20ovet_1p81_back->ProjectionX(ss_back.str().c_str(), i, i);
    TH1D *hmc = hetcone20ovet_1p81_mc->ProjectionX(ss_mc.str().c_str(), i, i);

    hsig->Sumw2();
    hback->Sumw2();
    hmc->Sumw2();

    const Int_t numBinsX = hsig->GetNbinsX();

    const Double_t meanSigRaw = hsig->GetMean();
    const Double_t rmsSigRaw = hsig->GetRMS();

    const Double_t intEdge = meanSigRaw + 2*rmsSigRaw;

    TAxis *xaxis = hsig->GetXaxis();
    Int_t bin = xaxis->FindBin(intEdge); //return bin number corresponding to xvalue

    const Double_t sigInt = hsig->Integral(bin, numBinsX);
    const Double_t backInt = hback->Integral(bin, numBinsX);

    hsig->Scale(1.0/sigInt);
    hback->Scale(1.0/backInt);

    // the background subtraced signal
    TH1D *hbsSig = (TH1D *) hsig->Clone(ss_bssig.str().c_str());
    
    hbsSig->Add(hback, -1);	// actually do the subtraction

    hbsSig->Scale(1.0/hbsSig->Integral());
    hmc->Scale(1.0/hmc->Integral());

    hist -> NewPage();
    hsig->SetMarkerStyle(8);
    hsig->SetLineColor(2);
    hsig->Draw();
    hback->Draw("same");
    c1->Update();

    hist -> NewPage();
    hmc->SetLineColor(4);
    hmc->Draw();
    hbsSig->SetMarkerStyle(8);
    hbsSig->SetLineColor(2);
    hbsSig->Draw("same");
    c1->Update();

    hsig->Write();
    hbsSig->Write();
    hback->Write();
    hmc->Write();

    const Double_t meanSig = hbsSig->GetMean();
    const Double_t meanSigError = hbsSig->GetMeanError();
    const Double_t meanMC = hmc->GetMean();
    const Double_t meanMCError = hmc->GetMeanError();
    const Double_t ratio = meanSig/meanMC;

    std::cout << "Bin " << i <<", data/MC diff: " << meanSig - meanMC
	      << " +- " << hypot(meanSigError, meanMCError)
	      << ", scale = " << ratio 
	      << " +- " << hypot(meanSigError/meanSig, meanMCError/meanMC) * ratio << std::endl; 


  }
  std::cout << std::endl;


  hist->Close();
  Target->Close();

}
