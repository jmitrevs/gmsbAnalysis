#ifndef GMSBANALYSIS_PHOTONISO_H
#define GMSBANALYSIS_PHOTONISO_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"
#include "egammaAnalysisUtils/checkOQ.h"
#include "GaudiKernel/ToolHandle.h"

#include "TTree.h"

class PhotonContainer;
class IPAUcaloIsolationTool;

/////////////////////////////////////////////////////////////////////////////
class PhotonIso:public AthAlgorithm {
public:
  PhotonIso (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode initEvent();
  StatusCode execute();
  StatusCode finalize();

private:

  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  /** name of the AOD truth particle container to retrieve from StoreGate */
  std::string m_photonContainerName;

  double m_deltaR;

  double m_ptCut;
  double m_etaCut;
  unsigned int m_isEMReq;
  unsigned int m_isEMVeto;
  bool m_applyVeto;

  // the OQ utility
  mutable egammaOQ m_OQ;

  int m_OQRunNum;

  ToolHandle<IPAUcaloIsolationTool> m_PAUcaloIsolationTool;


 // variables for "tree_Zll"
  TTree* m_tree;
  std::vector<int>*   m_photon_conv; // 0 unconv, or num tracks

  std::vector<double>* m_photon_et; // redundant, but easier
  std::vector<double>* m_photon_e;
  std::vector<double>* m_photon_eta; 
  std::vector<double>* m_photon_cluseta;
  std::vector<double>* m_photon_phi;

  std::vector<double>* m_photon_etcone20;
  std::vector<double>* m_photon_etcone40;
  
  // only filled in if tool passed.
  std::vector<double>* m_photon_etcone20_corrected;
  std::vector<double>* m_photon_etcone40_corrected;

  unsigned int    m_runNumber;
  unsigned int    m_eventNumber;
  unsigned int    m_lumiBlock;
  double m_weight;
  unsigned int m_numPhotons;
};


#endif // GMSBANALYSIS_PHOTONISO_H
