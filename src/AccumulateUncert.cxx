#include "gmsbAnalysis/AccumulateUncert.h"

void AccumulateUncert::AddObject(double pt, bool isBarrel, bool isConv, double weight)
{
  m_denom += weight;

  double num = Uncertainty(pt, isBarrel, isConv);

  m_num += weight*num;
  m_num2 += weight*num*num;

}

void AccumulateUncert::AddObjects(double pt1, bool isBarrel1, bool isConv1,
				  double pt2, bool isBarrel2, bool isConv2, double weight)
{
  m_denom += weight;

  double num1 = Uncertainty(pt1, isBarrel1, isConv1);
  double num2 = Uncertainty(pt2, isBarrel2, isConv2);

  m_num += weight*(num1+num2);
  m_num2 += weight*hypot(num1,num2);

}
		 
double AccumulateUncert::Uncertainty(double pt, bool isBarrel, bool isConv) const
{
  double num = 0.0;

  if (isConv) {
    if (isBarrel) {
      if (pt < 20000) {
	num = 7.7;
      } else if (pt < 25000) {
	num = 5.4;
      } else if (pt < 30000) {
	num = 4.7;
      } else if (pt < 35000) {
	num = 4.0;
      } else if (pt < 40000) {
	num = 4.3;
      } else if (pt < 50000) {
	num = 3.6;
      } else if (pt < 60000) {
	num = 1;
      } else {
	num = 3;
      }
    } else {
      if (pt < 20000) {
	num = 7.6;
      } else if (pt < 25000) {
	num = 8.1;
      } else if (pt < 30000) {
	num = 6.9;
      } else if (pt < 35000) {
	num = 6.0;
      } else if (pt < 40000) {
	num = 5.5;
      } else if (pt < 50000) {
	num = 5.3;
      } else if (pt < 60000) {
	num = 4;
      } else {
	num = 5;
      }
    }
  } else {
    if (isBarrel) {
      if (pt < 20000) {
	num = 4.1;
      } else if (pt < 25000) {
	num = 3.6;
      } else if (pt < 30000) {
	num = 2.7;
      } else if (pt < 35000) {
	num = 2.0;
      } else if (pt < 40000) {
	num = 1.7;
      } else if (pt < 50000) {
	num = 1.3;
      } else if (pt < 60000) {
	num = 0.3;
      } else {
	num = 0.6;
      }
    } else {
      if (pt < 20000) {
	num = 3.9;
      } else if (pt < 25000) {
	num = 2.6;
      } else if (pt < 30000) {
	num = 1.5;
      } else if (pt < 35000) {
	num = 1.2;
      } else if (pt < 40000) {
	num = 0;
      } else if (pt < 50000) {
	num = 0.6;
      } else if (pt < 60000) {
	num = 2;
      } else {
	num = 0;
      }
    }
  }

  return num;
}
