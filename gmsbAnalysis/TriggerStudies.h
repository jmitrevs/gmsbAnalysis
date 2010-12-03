#ifndef GMSBANALYSIS_TRIGGERSTUDIES_H
#define GMSBANALYSIS_TRIGGERSTUDIES_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"

#include "gmsbTools/gmsbPreparationTool.h"
#include "gmsbTools/gmsbOverlapRemovalTool.h"

#include "egammaOQUtils/checkOQ.h"

class Jet;

/////////////////////////////////////////////////////////////////////////////
class TriggerStudies : public AthAlgorithm {
public:
  TriggerStudies (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

private:

  bool isBad(const Jet *) const;

  /** run number to use for OQ: -1 means use event run number */
  int m_OQRunNum;
  bool m_doOQ; 			// whether or not to do OQ

  /** MET selecton */
  std::string m_METContainerName;

  double m_leadPhotonPtCut;

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  double m_numEvents; 		// a weighted count of the number of events

  std::map<std::string, TH1*> m_histograms;

  // tools for selection

  /** get a handle on the user tool for pre-selection and overlap removal */
  ToolHandle<gmsbPreparationTool>     m_PreparationTool;
  ToolHandle<gmsbPreparationTool>     m_CrackPreparationTool;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool1;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool2;

  // the OQ utility
  egammaOQ m_OQ;
  
};

#endif // GMSBANALYSIS_TRIGGERSTUDIES_H
