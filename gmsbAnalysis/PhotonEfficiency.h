#ifndef GMSBANALYSIS_PHOTONEFFICIENCY_H
#define GMSBANALYSIS_PHOTONEFFICIENCY_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"
#include "egammaOQUtils/checkOQ.h"
#include "GaudiKernel/ToolHandle.h"

#include "TDatabasePDG.h"

class Jet;
namespace Reco  { class ITrackToVertex; }

namespace HepMC {
  class GenVertex;
  class GenParticle;
  class GenEvent;
  class FourVector;
}

class PhotonContainer;
class IPAUcaloIsolationTool;

/////////////////////////////////////////////////////////////////////////////
class PhotonEfficiency:public AthAlgorithm {
public:
  PhotonEfficiency (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

private:

  HepMC::GenVertex* getMCHardInteraction(const HepMC::GenEvent *const ge) const;

   // also adds the pT of each particle
  void PrintDecayTree(const HepMC::GenVertex *vtx, int extraSpaces=0);

   // also adds the pT of each particle
  void PrintDecayTreeAnnotated(const HepMC::GenVertex *vtx, int extraSpaces=0);

  // some utilities for it
  bool StatusGood(int status) const;
  const HepMC::GenVertex *FindNextVertex(const HepMC::GenParticle *pcl) const;

  void CalcPhotonEfficiency(const HepMC::FourVector &p);

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  std::map<std::string, TH1*> m_histograms;

  // a PDG database that can be used to get particle properties
  TDatabasePDG m_pdg;

  /** name of the AOD truth particle container to retrieve from StoreGate */
  std::string m_truthParticleContainerName;

  /** name of the AOD truth particle container to retrieve from StoreGate */
  std::string m_photonContainerName;
  const PhotonContainer*  m_photons;

  // the max deltaR for truth-reco photon match
  double m_deltaR;
  double m_weight;

  double m_pT; 			// pt cut for plots (other than pt)

  bool m_printDecayTree;

  // the OQ utility
  mutable egammaOQ m_OQ;

  int m_OQRunNum;

  ToolHandle<IPAUcaloIsolationTool> m_PAUcaloIsolationTool;

};

inline bool PhotonEfficiency::StatusGood(int status) const 
{
  return (status == 1 || status == 3);
} 


#endif // GMSBANALYSIS_PHOTONEFFICIENCY_H
