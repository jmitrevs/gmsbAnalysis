#ifndef __JETID__
#define __JETID__

namespace JetID
{
  typedef enum  { LooseBad, TightBad  } BadJetCategory;
  bool isBad(BadJetCategory criteria, double quality, double n90, double emf, double hecf, double time,double fmax, double eta);
}

#endif
