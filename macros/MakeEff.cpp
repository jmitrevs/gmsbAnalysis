#include <iostream>
#include <string>
#include "TH1F.h"
#include "TPad.h"
#include "TBox.h"
#include "TLatex.h"
#include "TCanvas.h"
#include <cmath>

float EfficiencyError(float a,float b){
  return sqrt((a+1.0)*(b-a+1.0)/(b+2.0)/(b+2.0)/(b+3.0));
//   if (b >= a && b > 0) {
//     return TMath::Sqrt(a*(b-a)/pow(b,3));
//   } else { 
//     return 0;
//   }
}  

void Efficiency(TH1 *h1, TH1 *h2, TH1 *h) {
  // Calculate the efficiency bin by bin as the ratio of two histograms.
  // Errors on the efficiency are calculated properly.
  
  if (h1 == NULL || h2 == NULL || h == NULL) {
    std::cerr << "Efficiency is called with a NULL histogram" << std::endl;
  }

  int nbinsx = h->GetNbinsX();
  int nbinsy = h->GetNbinsY();
  int nbinsz = h->GetNbinsZ();
  
  // Check histogram compatibility
  if (nbinsx != h1->GetNbinsX() || nbinsy != h1->GetNbinsY() || nbinsz != h1->GetNbinsZ() || 
      nbinsx != h2->GetNbinsX() || nbinsy != h2->GetNbinsY() || nbinsz != h2->GetNbinsZ()) {
    std::cerr << "Attempt to divide histograms with different number of bins" << std::endl;
    return;
  }
  
  // Issue a Warning if histogram limits are different
  if (h->GetXaxis()->GetXmin() != h1->GetXaxis()->GetXmin() ||
      h->GetXaxis()->GetXmax() != h1->GetXaxis()->GetXmax() ||
      h->GetYaxis()->GetXmin() != h1->GetYaxis()->GetXmin() ||
      h->GetYaxis()->GetXmax() != h1->GetYaxis()->GetXmax() ||
      h->GetZaxis()->GetXmin() != h1->GetZaxis()->GetXmin() ||
      h->GetZaxis()->GetXmax() != h1->GetZaxis()->GetXmax()) {
    std::cerr << "Attempt to divide histograms with different axis limits" << std::endl;
  }

  if (h->GetXaxis()->GetXmin() != h2->GetXaxis()->GetXmin() ||
      h->GetXaxis()->GetXmax() != h2->GetXaxis()->GetXmax() ||
      h->GetYaxis()->GetXmin() != h2->GetYaxis()->GetXmin() ||
      h->GetYaxis()->GetXmax() != h2->GetYaxis()->GetXmax() ||
      h->GetZaxis()->GetXmin() != h2->GetZaxis()->GetXmin() ||
      h->GetZaxis()->GetXmax() != h2->GetZaxis()->GetXmax()) {
    std::cerr << "Attempt to divide histograms with different axis limits" << std::endl;
  }

  if (h->GetDimension() < 2) nbinsy = -1;
  if (h->GetDimension() < 3) nbinsz = -1;
  
  // Loop on bins (including underflows/overflows)
  int bin, binx, biny, binz;
  double b1,b2,effi,erro;
  for (binz=0;binz<=nbinsz+1;binz++) {
    for (biny=0;biny<=nbinsy+1;biny++) {
      for (binx=0;binx<=nbinsx+1;binx++) {
        bin = binx +(nbinsx+2)*(biny + (nbinsy+2)*binz);
        b1  = h1->GetBinContent(bin);
        b2  = h2->GetBinContent(bin);
        if ( b2 ) {
          effi = b1/b2;
          erro = EfficiencyError(b1, b2);
        } else {
          effi = 0;
          erro = 0;
        }
        h->SetBinContent(bin,effi);
        h->SetBinError(bin,erro);
      }
    }
  }
//  Stat_t s[10];
//  h->GetStats(s);
//  h->PutStats(s);
}

void EfficiencyIntegrate(TH1 *h1, TH1 *h2, TH1 *h) {
  // Calculate the efficiency as the ratio of two histograms.
  // Errors on the efficiency are calculated properly.
  // This is different from the plain old Efficiency in that
  // the results bin x in h is for the sum of the bins
  // <= x in h1 and h2, hence Integrate

  if (h1 == NULL || h2 == NULL || h == NULL) {
    std::cerr << "Efficiency is called with a NULL histogram" << std::endl;
  }

  int nbinsx = h->GetNbinsX();
  int nbinsy = h->GetNbinsY();
  int nbinsz = h->GetNbinsZ();
  
  // Check histogram compatibility
  if (nbinsx != h1->GetNbinsX() || nbinsy != h1->GetNbinsY() || nbinsz != h1->GetNbinsZ() || 
      nbinsx != h2->GetNbinsX() || nbinsy != h2->GetNbinsY() || nbinsz != h2->GetNbinsZ()) {
    std::cerr << "Attempt to divide histograms with different number of bins" << std::endl;
    return;
  }
  
  // Issue a Warning if histogram limits are different
  if (h->GetXaxis()->GetXmin() != h1->GetXaxis()->GetXmin() ||
      h->GetXaxis()->GetXmax() != h1->GetXaxis()->GetXmax() ||
      h->GetYaxis()->GetXmin() != h1->GetYaxis()->GetXmin() ||
      h->GetYaxis()->GetXmax() != h1->GetYaxis()->GetXmax() ||
      h->GetZaxis()->GetXmin() != h1->GetZaxis()->GetXmin() ||
      h->GetZaxis()->GetXmax() != h1->GetZaxis()->GetXmax()) {
    std::cerr << "Attempt to divide histograms with different axis limits" << std::endl;
  }

  if (h->GetXaxis()->GetXmin() != h2->GetXaxis()->GetXmin() ||
      h->GetXaxis()->GetXmax() != h2->GetXaxis()->GetXmax() ||
      h->GetYaxis()->GetXmin() != h2->GetYaxis()->GetXmin() ||
      h->GetYaxis()->GetXmax() != h2->GetYaxis()->GetXmax() ||
      h->GetZaxis()->GetXmin() != h2->GetZaxis()->GetXmin() ||
      h->GetZaxis()->GetXmax() != h2->GetZaxis()->GetXmax()) {
    std::cerr << "Attempt to divide histograms with different axis limits" << std::endl;
  }

  if (h->GetDimension() < 2) nbinsy = -1;
  if (h->GetDimension() < 3) nbinsz = -1;
  
  // Loop on bins (including underflows/overflows)
  int bin, binx, biny, binz;
  double b1 = 0.0;
  double b2 = 0.0;
  double effi,erro;
  
  for (binz=0;binz<=nbinsz+1;binz++) {
    for (biny=0;biny<=nbinsy+1;biny++) {
      for (binx=0;binx<=nbinsx+1;binx++) {
        bin = binx +(nbinsx+2)*(biny + (nbinsy+2)*binz);
        b1 += h1->GetBinContent(bin);
        b2 += h2->GetBinContent(bin);
        if ( b2 ) {
          effi = b1/b2;
          erro = EfficiencyError(b1, b2);
        } else {
          effi = 0;
          erro = 0;
        }
        h->SetBinContent(bin,effi);
        h->SetBinError(bin,erro);
      }
    }
  }
//  Stat_t s[10];
//  h->GetStats(s);
//  h->PutStats(s);
}



