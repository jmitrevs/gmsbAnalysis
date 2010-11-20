#ifndef GMSBANALYSIS_BACKGROUNDMODELEE_H
#define GMSBANALYSIS_BACKGROUNDMODELEE_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"

/////////////////////////////////////////////////////////////////////////////
class BackgroundModelEE:public AthAlgorithm {
public:
  BackgroundModelEE (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

private:

  /** Electron selection */
  std::string m_ElectronContainerName;
  int m_electronIsEM;

  /** Photon selection */
  std::string m_PhotonContainerName;
  int m_photonIsEM;

  /** MET selecton */
  std::string m_METContainerName;

  std::string m_JetContainerName;

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  std::map<std::string, TH1*> m_histograms;
  
};

#endif // GMSBANALYSIS_BACKGROUNDMODELEE_H
