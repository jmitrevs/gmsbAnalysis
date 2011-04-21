#ifndef MAKEEFFICIENCIES_HPP
#define MAKEEFFICIENCIES_HPP

#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include <string>
#include "TCanvas.h"

float EfficiencyError(float a,float b);
void Efficiency(TH1 *h1, TH1 *h2, TH1 *h);
void EfficiencyIntegrate(TH1 *h1, TH1 *h2, TH1 *h);

#endif
