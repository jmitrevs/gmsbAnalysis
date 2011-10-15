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
  double m_leadPhotonPtCut;

  bool m_applyTriggers; //only really meant for MC
  std::string m_triggers;

  bool m_doSmartVeto;

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

  // for bookkeeping
  double numEventsCut[NUM_CUTS];

  AccumulateUncert accUnc;  // for leading photon
  AccumulateFFUncert accFFUnc;
  AccumulateUncert accUnc2; // for second photon
  AccumulateFFUncert accFFUnc2;

  mutable TRandom3 m_rand3;
};

#endif // GMSBANALYSIS_SIGNALGAMMALEPTON_H
