#ifndef GMSBANALYSIS_SIGNALGAMMALEPTON_H
#define GMSBANALYSIS_SIGNALGAMMALEPTON_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"
#include "AthenaKernel/IUserDataSvc.h"

#include "gmsbTools/gmsbPreparationTool.h"
#include "gmsbTools/gmsbOverlapRemovalTool.h"
#include "gmsbAnalysis/AccumulateUncert.h"
#include "gmsbAnalysis/AccumulateFFUncert.h"

#include "gmsbAnalysis/FakeMetEstimator.h"

#include "TRandom3.h"
#include "TTree.h"

class Jet;
namespace Reco  { class ITrackToVertex; }
class ISUSYPhotonJetCleaningTool;
namespace Trig  { class TrigDecisionTool; }

/////////////////////////////////////////////////////////////////////////////
class SignalGammaLepton:public AthAlgorithm {
public:
  SignalGammaLepton (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

  enum NUM_CUTS_t {NUM_CUTS = 20};

private:

  /** MET selecton */
  std::string m_METContainerName;

  bool m_isMC;
  unsigned int m_numPhotonsReq;
  unsigned int m_numMuonsReq;
  unsigned int m_numElectronsReq;

  bool m_applyTriggers; //only really meant for MC
  std::string m_triggers;

  bool m_doSmartVeto;

  // whether to write out all the histograms. Cut flow always outputted
  bool m_outputHistograms;
  // whether to write out the ntuples
  bool m_outputNtuple;

  /** primary vertex container */
  std::string m_vxCandidatesName;

  /** truth container name **/
  std::string m_McEventContainerName;

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

  /** @brief Tool handle for track extrapolation to vertex */
  ToolHandle< Reco::ITrackToVertex > m_trackToVertexTool;

  /** @brief Tool handle for jet cleaning */  
  ToolHandle<ISUSYPhotonJetCleaningTool>  m_JetCleaningTool;

  /** @brief trigger decision tool */    
  ToolHandle< Trig::TrigDecisionTool > m_trigDec;

  FakeMetEstimator m_fakeMetEstimator;
  FakeMetEstimator m_fakeMetEstimatorEmulNoHole;

  // user data
  ServiceHandle<IUserDataSvc> m_userdatasvc;

  AccumulateUncert accUnc;  // for leading photon
  AccumulateFFUncert accFFUnc;
  AccumulateUncert accUnc2; // for second photon
  AccumulateFFUncert accFFUnc2;

  mutable TRandom3 m_rand3;

  // The variables if one outputs an ntuple
  TTree* m_tree;
  unsigned int m_runNumber;
  unsigned int m_eventNumber;
  unsigned int m_lumiBlock;
  float m_weight;

  std::vector<float>* m_ph_pt;
  std::vector<float>* m_ph_eta;
  std::vector<float>* m_ph_phi;

  std::vector<float>* m_el_pt;
  std::vector<float>* m_el_eta;
  std::vector<float>* m_el_phi;

  std::vector<float>* m_mu_pt;
  std::vector<float>* m_mu_eta;
  std::vector<float>* m_mu_phi;

  unsigned int m_numPh;
  unsigned int m_numEl;
  unsigned int m_numMu;
  unsigned int m_numJets;

  // MET
  float m_metx;
  float m_mety;

  float m_ph_el_minv;
  float m_ph_mu_minv;

  float m_deltaPhiPhMET;
  float m_deltaPhiElMET;
  float m_deltaPhiMuMET;

  float m_HT;
  float m_mTel;
  float m_mTmu;
  float m_meff;


};

#endif // GMSBANALYSIS_SIGNALGAMMALEPTON_H
