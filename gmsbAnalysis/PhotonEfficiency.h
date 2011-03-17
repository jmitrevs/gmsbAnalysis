#ifndef GMSBANALYSIS_PHOTONEFFICIENCY_H
#define GMSBANALYSIS_PHOTONEFFICIENCY_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"

#include "TDatabasePDG.h"

class Jet;
namespace Reco  { class ITrackToVertex; }

/////////////////////////////////////////////////////////////////////////////
class PhotonEfficiency:public AthAlgorithm {
public:
  PhotonEfficiency (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

private:

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  std::map<std::string, TH1*> m_histograms;

  // a PDG database that can be used to get particle properties
  TDatabasePDG m_pdg;

  /** name of the AOD truth particle container to retrieve from StoreGate */
  std::string m_truthParticleContainerName;

};

#endif // GMSBANALYSIS_PHOTONEFFICIENCY_H
