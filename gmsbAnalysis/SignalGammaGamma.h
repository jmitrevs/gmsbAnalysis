#ifndef GMSBANALYSIS_SIGNALGAMMAGAMMA_H
#define GMSBANALYSIS_SIGNALGAMMAGAMMA_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"

#include "gmsbTools/gmsbPreparationTool.h"
#include "gmsbTools/gmsbOverlapRemovalTool.h"

class Jet;

/////////////////////////////////////////////////////////////////////////////
class SignalGammaGamma:public AthAlgorithm {
public:
  SignalGammaGamma (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

private:

  bool isBad(const Jet *) const;

  /** run number to use for OQ: -1 means use event run number */
  int m_OQRunNum;

  /** MET selecton */
  std::string m_METContainerName;

  double m_leadPhotonPtCut;

  /** primary vertex container */
  std::string m_vxCandidatesName;

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  std::map<std::string, TH1*> m_histograms;

  // tools for selection

  /** get a handle on the user tool for pre-selection and overlap removal */
  ToolHandle<gmsbPreparationTool>     m_PreparationTool;
  ToolHandle<gmsbPreparationTool>     m_CrackPreparationTool;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool1;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool2;

  
};

#endif // GMSBANALYSIS_SIGNALGAMMAGAMMA_H
