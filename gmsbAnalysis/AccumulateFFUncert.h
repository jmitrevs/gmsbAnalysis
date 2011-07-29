#ifndef GMSBANALYSIS_ACCUMULATEFFUNCERT_H
#define GMSBANALYSIS_ACCUMULATEFFUNCERT_H

#include <cmath>

class AccumulateFFUncert {
public:
  AccumulateFFUncert() : m_num(0), m_num2(0), m_denom(0) {};
  double Uncert() const {return m_denom ? m_num/m_denom : 0;};
  double Uncert2() const {return m_denom ? m_num2/m_denom : 0;};
  void AddObject(double pt, double eta, bool isConv, double weight);
  void AddObjects(double pt1, double eta1, bool isConv1, 
		  double pt2, double eta2, bool isConv2, double weight);

private:

  double Uncertainty(double pt, double eta, bool isConv) const;

  double m_num;
  double m_num2;
  double m_denom;
};

#endif
