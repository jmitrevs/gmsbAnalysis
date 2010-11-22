/**
   Author Nikola Makovec <makovec@cern.ch>
   
  Purpose: define the jet identification criteria

  - Version 1.0 (27 September 2010):  
      - only bad jet definition criteria are implemented
        according to the recommendation from the 2010 Pisa workshop  (rel 15 data)

  Usage:
  bool isbad_tight = JetID::isBad(JetID::TightBad, quality,  n90,  emf,  hecf,  time, fmax, eta);
  bool isbad_loose = JetID::isBad(JetID::LooseBad, quality,  n90,  emf,  hecf,  time, fmax, eta);
   
   
*/


#include "gmsbAnalysis/JetID.h"
#include <cmath>
namespace JetID
{
  
  bool isBad(BadJetCategory criteria, double quality, double n90, double emf, double hecf, double time,double fmax, double eta)
  {
    if(criteria==LooseBad || criteria==TightBad)
      {
	if( emf>0.95 && fabs(quality)>0.8 )       return true;
	if( hecf>0.8 && n90<=5 )                  return true;
	if( hecf> 0.5 && fabs(quality)>0.5)      return true;	
	if( fabs(time)>25 )                      return true;
	if( emf<0.05)                            return true;
	if( fmax>0.99&&fabs(eta)<2)              return true;
      }
    
  
    if(criteria==TightBad)
      {
	if( emf<0.1)                          return true;
	if( hecf> 1-fabs(quality))            return true; 
	if( emf>0.9 && fabs(quality)>0.6 )     return true;
	if( hecf> 0.3 && fabs(quality)>0.3)   return true;
	if( fmax>0.95&&fabs(eta)<2)           return true;
      }
    return false;
  }
}

