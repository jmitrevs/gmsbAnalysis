#ifndef GMSBANALYSIS_TRUTHPLOTS_H
#define GMSBANALYSIS_TRUTHPLOTS_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"

#include "gmsbTools/TruthStudies.h"

#include "TTree.h"

/////////////////////////////////////////////////////////////////////////////
class TruthPlots:public AthAlgorithm {
public:
  TruthPlots (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();


private:

  /** truth container name **/
  std::string m_McEventContainerName;

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  std::map<std::string, TH1*> m_histograms;

  // tools for selection

  ToolHandle<TruthStudies> m_truth;

};

#endif // GMSBANALYSIS_SIGNALGAMMALEPTON_H
