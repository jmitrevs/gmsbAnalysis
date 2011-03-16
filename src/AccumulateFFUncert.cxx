#include "gmsbAnalysis/AccumulateFFUncert.h"

void AccumulateFFUncert::AddObject(double pt, double eta, bool isConv, double weight)
{
  eta = fabs(eta);

  m_denom += weight;

  double num = 0.0;

  if (isConv) {
   if (eta < 0.6) {
      if (pt < 20000) {
	num = weight * 3.18;
      } else if (pt < 25000) {
	num = weight * 2.62;
      } else if (pt < 30000) {
	num = weight * 0.61;
      } else if (pt < 35000) {
	num = weight * 2.02; 
      } else if (pt < 40000) {
	num = weight * 1.01;
      } else if (pt < 45000) {
	num = weight * 2.53;
      } else if (pt < 55000) {
	num = weight * 0.00;
      } else if (pt < 70000) {
	num = weight * 0.92;
      } else if (pt < 85000) {
	num = weight * 1.81;
      } else if (pt < 100000) {
	num = weight * 0.15;
      } else if (pt < 125000) {
	num = weight * 0.65;
      } else if (pt < 150000) {
	num = weight * 0.38;
      } else if (pt < 200000) {
	num = weight * 0.65;
      } else {
	num = weight * 0.19;
      }
    } else if (eta < 1.37) {
      if (pt < 20000) {
	num = weight * 2.38;
      } else if (pt < 25000) {
	num = weight * 2.25;
      } else if (pt < 30000) {
	num = weight * 0.62;
      } else if (pt < 35000) {
	num = weight * 2.05; 
      } else if (pt < 40000) {
	num = weight * 0.33;
      } else if (pt < 45000) {
	num = weight * 0.68;
      } else if (pt < 55000) {
	num = weight * 0.19;
      } else if (pt < 70000) {
	num = weight * 0.64;
      } else if (pt < 85000) {
	num = weight * 0.42;
      } else if (pt < 100000) {
	num = weight * 0.15;
      } else if (pt < 125000) {
	num = weight * 0.36;
      } else if (pt < 150000) {
	num = weight * 0.06;
      } else if (pt < 200000) {
	num = weight * 0.07;
      } else {
	num = weight * 0.06;
      }
    } else {
      if (pt < 20000) {
	num = weight * 2.89;
      } else if (pt < 25000) {
	num = weight * 3.02;
      } else if (pt < 30000) {
	num = weight * 0.29;
      } else if (pt < 35000) {
	num = weight * 2.35; 
      } else if (pt < 40000) {
	num = weight * 1.82;
      } else if (pt < 45000) {
	num = weight * 2.34;
      } else if (pt < 55000) {
	num = weight * 1.61;
      } else if (pt < 70000) {
	num = weight * 0.95;
      } else if (pt < 85000) {
	num = weight * 0.36;
      } else if (pt < 100000) {
	num = weight * 0.17;
      } else if (pt < 125000) {
	num = weight * 0.66;
      } else if (pt < 150000) {
	num = weight * 0.11;
      } else if (pt < 200000) {
	num = weight * 1.45;
      } else {
	num = weight * 0.08;
      }
    }
  } else {
    if (eta < 0.6) {
      if (pt < 20000) {
	num = weight * 1.34;
      } else if (pt < 25000) {
	num = weight * 1.28;
      } else if (pt < 30000) {
	num = weight * 0.38;
      } else if (pt < 35000) {
	num = weight * 0.42; 
      } else if (pt < 40000) {
	num = weight * 0.77;
      } else if (pt < 45000) {
	num = weight * 3.84;
      } else if (pt < 55000) {
	num = weight * 0.81;
      } else if (pt < 70000) {
	num = weight * 0.99;
      } else if (pt < 85000) {
	num = weight * 0.18;
      } else if (pt < 100000) {
	num = weight * 0.71;
      } else if (pt < 125000) {
	num = weight * 0.67;
      } else if (pt < 150000) {
	num = weight * 1.05;
      } else if (pt < 200000) {
	num = weight * 0.07;
      } else {
	num = weight * 0.26;
      }
    } else if (eta < 1.37) {
      if (pt < 20000) {
	num = weight * 1.40;
      } else if (pt < 25000) {
	num = weight * 2.21;
      } else if (pt < 30000) {
	num = weight * 0.80;
      } else if (pt < 35000) {
	num = weight * 1.10; 
      } else if (pt < 40000) {
	num = weight * 0.19;
      } else if (pt < 45000) {
	num = weight * 1.31;
      } else if (pt < 55000) {
	num = weight * 0.08;
      } else if (pt < 70000) {
	num = weight * 0.58;
      } else if (pt < 85000) {
	num = weight * 0.43;
      } else if (pt < 100000) {
	num = weight * 0.66;
      } else if (pt < 125000) {
	num = weight * 1.40;
      } else if (pt < 150000) {
	num = weight * 0.54;
      } else if (pt < 200000) {
	num = weight * 0.05;
      } else {
	num = weight * 0.53;
      }
    } else {
      if (pt < 20000) {
	num = weight * 0.91;
      } else if (pt < 25000) {
	num = weight * 4.55;
      } else if (pt < 30000) {
	num = weight * 1.67;
      } else if (pt < 35000) {
	num = weight * 2.18; 
      } else if (pt < 40000) {
	num = weight * 0.89;
      } else if (pt < 45000) {
	num = weight * 2.07;
      } else if (pt < 55000) {
	num = weight * 0.09;
      } else if (pt < 70000) {
	num = weight * 0.37;
      } else if (pt < 85000) {
	num = weight * 0.06;
      } else if (pt < 100000) {
	num = weight * 0.20;
      } else if (pt < 125000) {
	num = weight * 1.27;
      } else if (pt < 150000) {
	num = weight * 1.38;
      } else if (pt < 200000) {
	num = weight * 3.26;
      } else {
	num = weight * 0.03;
      }
    }
  }

  m_num += num;
  m_num2 += num*num;

}
		 
