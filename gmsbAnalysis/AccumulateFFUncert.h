#ifndef GMSBANALYSIS_ACCUMULATEFFUNCERT_H
#define GMSBANALYSIS_ACCUMULATEFFUNCERT_H

#include <cmath>

class AccumulateFFUncert {
public:
  AccumulateFFUncert() : m_num(0), m_denom(0) {};
  double Uncert() const {return m_denom ? m_num/m_denom : 0;};
  double Uncert2() const {return m_denom ? sqrt(m_num2/m_denom) : 0;};
  void AddObject(double pt, double eta, bool isConv, double weight);

private:
  double m_num;
  double m_num2;
  double m_denom;
};

#endif
