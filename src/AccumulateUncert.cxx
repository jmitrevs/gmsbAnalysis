#include "gmsbAnalysis/AccumulateUncert.h"

void AccumulateUncert::AddObject(double pt, bool isBarrel, bool isConv, double weight)
{
  m_denom += weight;
  if (isConv) {
    if (isBarrel) {
      if (pt < 20000) {
	m_num += weight * 7.7;
      } else if (pt < 25000) {
	m_num += weight * 5.4;
      } else if (pt < 30000) {
	m_num += weight * 4.7;
      } else if (pt < 35000) {
	m_num += weight * 4.0;
      } else if (pt < 40000) {
	m_num += weight * 4.3;
      } else if (pt < 50000) {
	m_num += weight * 3.6;
      } else if (pt < 60000) {
	m_num += weight * 1;
      } else {
	m_num += weight * 3;
      }
    } else {
      if (pt < 20000) {
	m_num += weight * 7.6;
      } else if (pt < 25000) {
	m_num += weight * 8.1;
      } else if (pt < 30000) {
	m_num += weight * 6.9;
      } else if (pt < 35000) {
	m_num += weight * 6.0;
      } else if (pt < 40000) {
	m_num += weight * 5.5;
      } else if (pt < 50000) {
	m_num += weight * 5.3;
      } else if (pt < 60000) {
	m_num += weight * 4;
      } else {
	m_num += weight * 5;
      }
    }
  } else {
    if (isBarrel) {
      if (pt < 20000) {
	m_num += weight * 4.1;
      } else if (pt < 25000) {
	m_num += weight * 3.6;
      } else if (pt < 30000) {
	m_num += weight * 2.7;
      } else if (pt < 35000) {
	m_num += weight * 2.0;
      } else if (pt < 40000) {
	m_num += weight * 1.7;
      } else if (pt < 50000) {
	m_num += weight * 1.3;
      } else if (pt < 60000) {
	m_num += weight * 0.3;
      } else {
	m_num += weight * 0.6;
      }
    } else {
      if (pt < 20000) {
	m_num += weight * 3.9;
      } else if (pt < 25000) {
	m_num += weight * 2.6;
      } else if (pt < 30000) {
	m_num += weight * 1.5;
      } else if (pt < 35000) {
	m_num += weight * 1.2;
      } else if (pt < 40000) {
	m_num += weight * 0;
      } else if (pt < 50000) {
	m_num += weight * 0.6;
      } else if (pt < 60000) {
	m_num += weight * 2;
      } else {
	m_num += weight * 0;
      }
    }
  }
}
		 
