#ifndef HISTOGRAMPARAMS_HPP
#define HISTOGRAMPARAMS_HPP
///////////////////////////////////////////////////////////////////////////////
//
// 
//         File: HistogramParams.hpp
//
//         Created:  Jovan Mitrevski   11/10/2004
///////////////////////////////////////////////////////////////////////////////

// Dependencies (#includes)
 
#include "TROOT.h"
#include "TMath.h"

///////////////////////////////////////////////////////////////////////////////

namespace effMacros {

  const Int_t eta_bins = 120;
  const Axis_t eta_low = -3;
  const Axis_t eta_high = 3;

  // in GeV
  const Int_t pt_bins = 1000;
  const Axis_t pt_low = 0;
  const Axis_t pt_high = 1000;

}//namespace emcertify
#endif





