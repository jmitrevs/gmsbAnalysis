#include "gmsbAnalysis/AccumulateFFUncert.h"

void AccumulateFFUncert::AddObject(double pt, double eta, bool isConv, double weight)
{
  eta = fabs(eta);

  m_denom += weight;

  double num = Uncertainty(pt, eta, isConv);

  m_num += weight*num;
  m_num2 += weight*num*num;

}

void AccumulateFFUncert::AddObjects(double pt1, double eta1, bool isConv1,
				    double pt2, double eta2, bool isConv2, double weight)
{
  eta1 = fabs(eta1);
  eta2 = fabs(eta2);

  m_denom += weight;

  double num1 = Uncertainty(pt1, eta1, isConv1);
  double num2 = Uncertainty(pt2, eta2, isConv2);

  m_num += weight*(num1+num2);
  m_num2 += weight*hypot(num1,num2);

}
		 
double AccumulateFFUncert::Uncertainty(double pt, double eta, bool isConv) const
{
  double num = 0.0;

  if (isConv) {
   if (eta < 0.6) {
      if (pt < 20000) {
	num = 3.18;
      } else if (pt < 25000) {
	num = 2.62;
      } else if (pt < 30000) {
	num = 0.61;
      } else if (pt < 35000) {
	num = 2.02; 
      } else if (pt < 40000) {
	num = 1.01;
      } else if (pt < 45000) {
	num = 2.53;
      } else if (pt < 55000) {
	num = 0.00;
      } else if (pt < 70000) {
	num = 0.92;
      } else if (pt < 85000) {
	num = 1.81;
      } else if (pt < 100000) {
	num = 0.15;
      } else if (pt < 125000) {
	num = 0.65;
      } else if (pt < 150000) {
	num = 0.38;
      } else if (pt < 200000) {
	num = 0.65;
      } else {
	num = 0.19;
      }
    } else if (eta < 1.37) {
      if (pt < 20000) {
	num = 2.38;
      } else if (pt < 25000) {
	num = 2.25;
      } else if (pt < 30000) {
	num = 0.62;
      } else if (pt < 35000) {
	num = 2.05; 
      } else if (pt < 40000) {
	num = 0.33;
      } else if (pt < 45000) {
	num = 0.68;
      } else if (pt < 55000) {
	num = 0.19;
      } else if (pt < 70000) {
	num = 0.64;
      } else if (pt < 85000) {
	num = 0.42;
      } else if (pt < 100000) {
	num = 0.15;
      } else if (pt < 125000) {
	num = 0.36;
      } else if (pt < 150000) {
	num = 0.06;
      } else if (pt < 200000) {
	num = 0.07;
      } else {
	num = 0.06;
      }
    } else {
      if (pt < 20000) {
	num = 2.89;
      } else if (pt < 25000) {
	num = 3.02;
      } else if (pt < 30000) {
	num = 0.29;
      } else if (pt < 35000) {
	num = 2.35; 
      } else if (pt < 40000) {
	num = 1.82;
      } else if (pt < 45000) {
	num = 2.34;
      } else if (pt < 55000) {
	num = 1.61;
      } else if (pt < 70000) {
	num = 0.95;
      } else if (pt < 85000) {
	num = 0.36;
      } else if (pt < 100000) {
	num = 0.17;
      } else if (pt < 125000) {
	num = 0.66;
      } else if (pt < 150000) {
	num = 0.11;
      } else if (pt < 200000) {
	num = 1.45;
      } else {
	num = 0.08;
      }
    }
  } else {
    if (eta < 0.6) {
      if (pt < 20000) {
	num = 1.34;
      } else if (pt < 25000) {
	num = 1.28;
      } else if (pt < 30000) {
	num = 0.38;
      } else if (pt < 35000) {
	num = 0.42; 
      } else if (pt < 40000) {
	num = 0.77;
      } else if (pt < 45000) {
	num = 3.84;
      } else if (pt < 55000) {
	num = 0.81;
      } else if (pt < 70000) {
	num = 0.99;
      } else if (pt < 85000) {
	num = 0.18;
      } else if (pt < 100000) {
	num = 0.71;
      } else if (pt < 125000) {
	num = 0.67;
      } else if (pt < 150000) {
	num = 1.05;
      } else if (pt < 200000) {
	num = 0.07;
      } else {
	num = 0.26;
      }
    } else if (eta < 1.37) {
      if (pt < 20000) {
	num = 1.40;
      } else if (pt < 25000) {
	num = 2.21;
      } else if (pt < 30000) {
	num = 0.80;
      } else if (pt < 35000) {
	num = 1.10; 
      } else if (pt < 40000) {
	num = 0.19;
      } else if (pt < 45000) {
	num = 1.31;
      } else if (pt < 55000) {
	num = 0.08;
      } else if (pt < 70000) {
	num = 0.58;
      } else if (pt < 85000) {
	num = 0.43;
      } else if (pt < 100000) {
	num = 0.66;
      } else if (pt < 125000) {
	num = 1.40;
      } else if (pt < 150000) {
	num = 0.54;
      } else if (pt < 200000) {
	num = 0.05;
      } else {
	num = 0.53;
      }
    } else {
      if (pt < 20000) {
	num = 0.91;
      } else if (pt < 25000) {
	num = 4.55;
      } else if (pt < 30000) {
	num = 1.67;
      } else if (pt < 35000) {
	num = 2.18; 
      } else if (pt < 40000) {
	num = 0.89;
      } else if (pt < 45000) {
	num = 2.07;
      } else if (pt < 55000) {
	num = 0.09;
      } else if (pt < 70000) {
	num = 0.37;
      } else if (pt < 85000) {
	num = 0.06;
      } else if (pt < 100000) {
	num = 0.20;
      } else if (pt < 125000) {
	num = 1.27;
      } else if (pt < 150000) {
	num = 1.38;
      } else if (pt < 200000) {
	num = 3.26;
      } else {
	num = 0.03;
      }
    }
  }
  return num;
}
