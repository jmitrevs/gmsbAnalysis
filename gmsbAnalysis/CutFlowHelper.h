#ifndef GMSBANALYSIS_CUTFLOWHELPER_H
#define GMSBANALYSIS_CUTFLOWHELPER_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"

//#include "egammaAnalysisUtils/egammaSFclass.h"

/////////////////////////////////////////////////////////////////////////////
class CutFlowHelper:public AthAlgorithm {
public:
  CutFlowHelper (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

private:

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histName;

  bool m_isMC;

  /** truth container name **/
  std::string m_McEventContainerName;

};

#endif // GMSBANALYSIS_CUTFLOWHELPER_H
