#ifndef GMSBANALYSIS_BACKGROUNDMODELEE_H
#define GMSBANALYSIS_BACKGROUNDMODELEE_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"

#include "UserAnalysisUtils/UserAnalysisPreparationTool.h"
#include "UserAnalysisUtils/UserAnalysisOverlapRemovalTool.h"

/////////////////////////////////////////////////////////////////////////////
class BackgroundModelEE:public AthAlgorithm {
public:
  BackgroundModelEE (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

private:

  /** run number to use for OQ: -1 means use event run number */
  int m_OQRunNum;

  /** Electron selection */
  std::string m_ElectronContainerName;
  int m_electronIsEM;

  /** Photon selection */
  std::string m_PhotonContainerName;
  int m_photonIsEM;

  /** MET selecton */
  std::string m_METContainerName;

  std::string m_JetContainerName;

  double m_minPtForCrack;

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  std::map<std::string, TH1*> m_histograms;

  // tools for selection

  /** get a handle on the user tool for pre-selection and overlap removal */
  ToolHandle<UserAnalysisPreparationTool>     m_analysisPreparationTool;
  ToolHandle<UserAnalysisPreparationTool>     m_analysisCrackPreparationTool;
  ToolHandle<UserAnalysisOverlapRemovalTool>  m_analysisOverlapRemovalTool1;
  ToolHandle<UserAnalysisOverlapRemovalTool>  m_analysisOverlapRemovalTool2;

  
};

#endif // GMSBANALYSIS_BACKGROUNDMODELEE_H
