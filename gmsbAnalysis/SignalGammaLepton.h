#ifndef GMSBANALYSIS_SIGNALGAMMALEPTON_H
#define GMSBANALYSIS_SIGNALGAMMALEPTON_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"
//#include "AthenaKernel/ICutFlowSvc.h"
//#include "AthenaKernel/IUserDataSvc.h"

#include "gmsbTools/TruthStudies.h"
#include "gmsbTools/gmsbPreparationTool.h"
#include "gmsbTools/gmsbOverlapRemovalTool.h"
#include "gmsbAnalysis/AccumulateUncert.h"
#include "gmsbAnalysis/AccumulateFFUncert.h"

#include "gmsbAnalysis/FakeMetEstimator.h"

#include "egammaAnalysisUtils/egammaSFclass.h"

#include "TRandom3.h"
#include "TTree.h"

class Jet;
namespace Reco  { class ITrackToVertex; }
class IAthSelectorTool;
namespace Trig  { class TrigDecisionTool; }
class TrigMatchTool;
class APReweightND;
class IMCTruthClassifier;
class IEtMissMuonSystematicsTool;

namespace Root {
  class TPileupReweighting;
}

/////////////////////////////////////////////////////////////////////////////
class SignalGammaLepton:public AthAlgorithm {
public:
  SignalGammaLepton (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

  enum NUM_CUTS_t {NUM_CUTS = 20};
  enum TRIG_MATCH_t {NONE = 0, MUONS}; // only muons implemented so far

private:

  bool isInLArHole(Jet* jet) const;

  // both should really be const.
  float GetSignalElecSF(float el_cl_eta, float et, int set, int rel = 6, int mode = 0, int range = 0);
  float GetSignalElecSFUnc(float el_cl_eta, float et, int set, int rel = 6, int mode = 0, int range = 0);

  int m_set; 			// electron scale factor set 

  /** MET selecton */
  std::string m_METContainerName;
  std::string m_topoClusterContainerName;
  std::string m_missingEtTruth;

  bool m_isMC;
  unsigned int m_numPhotonsReq;
  unsigned int m_numMuonsReq;
  unsigned int m_numElectronsReq;

  unsigned int m_numPhotonsMax;
  unsigned int m_numMuonsMax;
  unsigned int m_numElectronsMax;

  double m_minMuonPt; // preselection is lower, really only needed for studies
  // since final selection is right

  bool m_requireTightLep; // if this is false, only sets the variable.
  bool m_requireTightPho; // if this is false, only sets the variable.
  bool m_doABCDPho; // if true also sets alternate variables
  bool m_doABCDLep; // if true also sets alternate variables

  bool m_applyTriggers; //only really meant for MC
  int m_matchTriggers; // match offline to online (really TRIG_MATCH_t)
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
  ToolHandle<gmsbSelectionTool>       m_FinalSelectionTool;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool1;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool2;

  // This is for ABCD method
  ToolHandle<gmsbSelectionTool>       m_AltSelectionTool;

  // /** get a handle on the user tool for pre-selection and overlap removal */
  // ToolHandle<gmsbPreparationTool>     m_LoosePreparationTool;
  // ToolHandle<gmsbOverlapRemovalTool>  m_LooseOverlapRemovalTool1;
  // ToolHandle<gmsbOverlapRemovalTool>  m_LooseOverlapRemovalTool2;


  /** @brief Tool handle for track extrapolation to vertex */
  ToolHandle< Reco::ITrackToVertex > m_trackToVertexTool;

  /** @brief Tool handle for jet cleaning */  
  ToolHandle<IAthSelectorTool>  m_JetCleaningTool;

  /** @brief trigger decision tool */    
  ToolHandle< Trig::TrigDecisionTool > m_trigDec;
  /** @brief trigger matching tool */    
  ToolHandle< TrigMatchTool > m_trigMatch;

  /** @brief classify the event type */
  ToolHandle<IMCTruthClassifier> m_MCTruthClassifier;
  bool m_doTruthClassifier;

  ToolHandle<TruthStudies> m_truth;
  bool m_doTruthStudies;
  bool m_filterWJets;
  enum ttbarfilt_t {NO_TTBARFILT = 0, LEPJETS, DILEP};
  int m_filterTTbar; // really the enum above

  bool m_doOverlapElectrons; // for debugging

  /** @breif whether to blind or not */
  bool m_blind;
  double m_blindMET;
  double m_blindMT;

  FakeMetEstimator m_fakeMetEstimator;
  //FakeMetEstimator m_fakeMetEstimatorEmulNoHole;

  // user data
  //ServiceHandle<ICutFlowSvc> m_cutFlowSvc;
  //ServiceHandle<IUserDataSvc> m_userdatasvc;

  AccumulateUncert accUnc;  // for leading photon
  AccumulateFFUncert accFFUnc;
  AccumulateUncert accUnc2; // for second photon
  AccumulateFFUncert accFFUnc2;

  mutable TRandom3 m_rand3;

  // for calculating scale factors in electron channel
  egammaSFclass  m_egammaSFclass;

  std::string m_muonTrigWeightsFile;
  APReweightND *m_trigWeighter;

  int m_applyPileupReweighting; // 0 = none, 1 = nominal, 2 = syst
  std::string m_pileupConfig;
  std::string m_lumiCalcFile;
  Root::TPileupReweighting *m_pileupTool;

  // The variables if one outputs an ntuple
  TTree* m_tree;
  unsigned int m_runNumber;
  unsigned int m_eventNumber;
  unsigned int m_lumiBlock;
  float m_weight;

  std::vector<float>* m_ph_pt;
  std::vector<float>* m_ph_eta;
  std::vector<float>* m_ph_eta2;
  std::vector<float>* m_ph_phi;
  std::vector<float>* m_ph_etcone20;
  std::vector<int>* m_ph_tight;
  std::vector<int>* m_ph_alt; // for ABCD
  std::vector<int>* m_ph_truth; // for truth classifer
  std::vector<int>* m_ph_origin; // for truth classifer
  std::vector<unsigned int>* m_ph_isEM;

  // a bit more stuff for AR
  std::vector<int>* m_ph_AR;
  std::vector<int>* m_ph_convType;
  std::vector<int>* m_ph_numSi0;
  std::vector<int>* m_ph_numSi1;
  std::vector<int>* m_ph_numPix0;
  std::vector<int>* m_ph_numPix1;
  std::vector<int>* m_ph_numSiEl;
  std::vector<int>* m_ph_numPixEl;
  std::vector<int>* m_ph_numBEl;
  std::vector<int>* m_ph_expectBLayerHit;
  
  std::vector<float>* m_el_pt;
  std::vector<float>* m_el_eta;
  std::vector<float>* m_el_eta2;
  std::vector<float>* m_el_phi;
  std::vector<int>* m_el_tight;
  std::vector<int>* m_el_alt;

  std::vector<float>* m_mu_pt;
  std::vector<float>* m_mu_eta;
  std::vector<float>* m_mu_phi;
  std::vector<int>* m_mu_tight;
  std::vector<int>* m_mu_alt;

  std::vector<float>* m_jet_pt;
  std::vector<float>* m_jet_eta;
  std::vector<float>* m_jet_phi;
  std::vector<float>* m_jet_et;

  unsigned int m_numPh;
  unsigned int m_numEl;
  unsigned int m_numMu;
  unsigned int m_numPhPresel;
  unsigned int m_numElPresel;
  unsigned int m_numMuPresel;
  unsigned int m_numJets;

  float m_el_minv; // this uses preselected
  float m_mu_minv;

  // The scale factro for the leading photon
  float m_ph_sf;
  // no uncertainty provided

  // The scale factor for the leading electron
  float m_el_sf;
  float m_el_sf_unc;
  // The scale factor for the leading muon
  float m_mu_sf;
  float m_mu_sf_unc;
  // The weight for the muon trigger
  float m_mu_trig_weight;
  float m_mu_trig_weight_unc;

  float m_pileupWeight;

  TruthStudies::EventType m_type;
  int m_isStrong;
  int m_numTruthPh;

  // MET
  float m_metx;
  float m_mety;
  float m_metx_noMuon;
  float m_mety_noMuon;
  float m_metx_full_noMuon;
  float m_mety_full_noMuon;
  float m_metx_MuonBoy;
  float m_mety_MuonBoy;
  float m_metx_RefTrack;
  float m_mety_RefTrack;
  float m_metxPlus_noMuon;
  float m_metyPlus_noMuon;
  float m_metxMinus_noMuon;
  float m_metyMinus_noMuon;

  float m_metx_muon_smear;
  float m_mety_muon_smear;

  float m_set_noMuon;
  float m_set_full_noMuon;
  float m_set_MuonBoy;
  float m_set_RefTrack;
  float m_setPlus_noMuon;
  float m_setMinus_noMuon;
  float m_set_muon_smear;

  std::vector<float> *m_metx_truth;
  std::vector<float> *m_mety_truth;
  std::vector<float> *m_set_truth;

  float m_ph_el_minv;
  float m_ph_mu_minv;

  float m_deltaPhiPhMET;
  float m_deltaPhiElMET;
  float m_deltaPhiMuMET;

  float m_HT;
  float m_mTel;
  float m_mTmu;
  float m_meff;

  float m_Wpt;

};

#endif // GMSBANALYSIS_SIGNALGAMMALEPTON_H
