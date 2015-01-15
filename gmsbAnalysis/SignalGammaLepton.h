#ifndef GMSBANALYSIS_SIGNALGAMMALEPTON_H
#define GMSBANALYSIS_SIGNALGAMMALEPTON_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"
//#include "AthenaKernel/ICutFlowSvc.h"
//#include "AthenaKernel/IUserDataSvc.h"

#include "gmsbD3PDObjects/TruthParticleD3PDObject.h"

#include "gmsbTools/TruthStudies.h"
#include "gmsbTools/gmsbPreparationTool.h"
#include "gmsbTools/gmsbOverlapRemovalTool.h"
#include "gmsbTools/gmsbSystError.h"
//#include "gmsbAnalysis/AccumulateUncert.h"
//#include "gmsbAnalysis/AccumulateFFUncert.h"

#include "gmsbAnalysis/FakeMetEstimator.h"

#include "MissingETUtility/METUtility.h"
#include "gmsbD3PDObjects/MissingETCompositionD3PDObject.h"
#include "gmsbD3PDObjects/ElectronD3PDObject.h"
#include "gmsbD3PDObjects/MuonD3PDObject.h"
#include "gmsbD3PDObjects/JetD3PDObject.h"
#include "gmsbD3PDObjects/PhotonD3PDObject.h"
#include "gmsbD3PDObjects/RefFinalMETD3PDObject.h"

#include "PATCore/PATCoreEnums.h"

// PDFTool includes
#include "PDFTool/IPDFTool.h"

// grl includes
#include "GoodRunsLists/TGoodRunsList.h"

#include <utility>

//#include "TRandom3.h"
#include "TTree.h"

//class IAthSelectorTool;
//class TrigMatchTool;
namespace Analysis { class AnalysisMuonConfigurableScaleFactors; }
//class APReweightND;

namespace Root {
  class TPileupReweighting;
  class TElectronEfficiencyCorrectionTool;
  class TPhotonEfficiencyCorrectionTool;
}

#include "TileTripReader/AthTileTripReader.h"
//#include "BCHCleaningTool/BCHCleaningToolAthena.h"

class IMETUtilityAthD3PDTool;

namespace SUSYMet    /// STVF_JVF is onlymeant for studies
{
    typedef enum {
        Default, STVF, STVF_JVF
    } met_definition;
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

  bool IsBadMuon(float mu_staco_qoverp_exPV, 
		 float mu_staco_cov_qoverp_exPV) const;

  bool isHotTile(const int RunNumber,
		 const float j_fmax,
		 const int j_smax,
		 const float jeteta,
		 const float jetphi) const;

  int FindNumTruthPhotons(unsigned int mc_channel_number, 
			  const TruthParticleD3PDObject& truthObj) const;
  
  // bool isInLArHole(Jet* jet) const;

  METUtil::METObject GetMET(ElectronD3PDObject *electrons,
			    PhotonD3PDObject *photons,
			    MuonD3PDObject *muons,
			    const ElectronD3PDObject& origElectrons,
			    const JetD3PDObject& origJets,
			    const JetD3PDObject& calibJets,
			    const MissingETCompositionD3PDObject& jetComp,
			    const MissingETCompositionD3PDObject& elComp,
			    const MissingETCompositionD3PDObject& phComp,
			    const RefFinalMETD3PDObject& cellOut,
			    const RefFinalMETD3PDObject& cellOutEflow,
			    const float averageIntPerXing,
			    SUSYMet::met_definition whichmet,
			    SystErr::Syste whichsyste,
			    const bool doEgammaJetFix);
  
  // returns (sf . sf_unc)
  std::pair<float, float> GetSignalElecSF(float el_cl_eta,
					  float pt) const;

  std::pair<float, float> GetSignalPhotonSF(bool isConv, 
					    float eta2,
					    float pt) const;

  // StatusCode recordEtMissSystematics(const MissingET* old_met, const VxContainer* vx_container);
  // StatusCode recordEtMissMuonSystematics();
  // StatusCode recordTruthMET();

  // electron files
  std::string m_electron_reco_file;
  std::string m_electron_id_file;

  std::string m_photon_full_unc_file;
  std::string m_photon_full_con_file;

  std::string m_photon_af2_unc_file;
  std::string m_photon_af2_con_file;

  /** MET selecton */
  std::string m_METContainerName;
  std::string m_METCompositionName;
  // std::string m_topoClusterContainerName;
  std::string m_missingEtTruth;

  /** name of the AOD truth particle container to retrieve from StoreGate */
  std::string m_truthParticleContainerName;

  bool m_isMC; // set by JOs
  bool m_isAtlfast; // set by JOs
  bool m_isTruth; // set by JOs -- is NTUP_TRUTH
  PATCore::ParticleDataType::DataType m_dataType; // redundant, set based on upper info

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

  bool m_applyTriggers; 
  // int m_matchTriggers; // match offline to online (really TRIG_MATCH_t)
  // std::string m_triggers;  // hardcode for now

  std::string m_GRLFile; 
  Root::TGoodRunsList m_grl;

  bool m_doGRL; // set to false if m_GRLFile = ""

  //bool m_doSmartVeto;

  // whether to write out all the histograms. Cut flow always outputted
  bool m_outputHistograms;
  // whether to write out the ntuples
  bool m_outputNtuple;

  /** primary vertex container */
  std::string m_vxCandidatesName;

  /** truth container name **/
  std::string m_McEventContainerName;

  /// For muon cleaning
  float m_mu_qopcut;
  float m_mu_z0cut;
  float m_mu_d0cut;

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  std::map<std::string, TH1*> m_histograms;

  // tools for selection

  /** get a handle on the user tool for pre-selection and overlap removal */
  ToolHandle<gmsbPreparationTool>     m_PrePreparationTool;
  ToolHandle<gmsbPreparationTool>     m_PreparationTool;
  ToolHandle<gmsbSelectionTool>       m_FinalSelectionTool;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool1;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool2;

  // This is for ABCD method
  ToolHandle<gmsbSelectionTool>       m_AltSelectionTool;

  METUtility* m_METUtility;
  bool m_useMETUtility;

  // /** get a handle on the user tool for pre-selection and overlap removal */
  // ToolHandle<gmsbPreparationTool>     m_LoosePreparationTool;
  // ToolHandle<gmsbOverlapRemovalTool>  m_LooseOverlapRemovalTool1;
  // ToolHandle<gmsbOverlapRemovalTool>  m_LooseOverlapRemovalTool2;


  // /** @brief Tool handle for jet cleaning */  
  // ToolHandle<IAthSelectorTool>  m_JetCleaningTool;

  // /** @brief trigger matching tool */    
  // ToolHandle< TrigMatchTool > m_trigMatch;

  ToolHandle<TruthStudies> m_truth;
  bool m_doTruthStudies;
  bool m_filterWJets;
  enum ttbarfilt_t {NO_TTBARFILT = 0, LEPJETS, DILEP};
  int m_filterTTbar; // really the enum above

  // // for MET systematics
  // ToolHandle<ITopoSystematicsTool> m_topoSystematicsTool;
  // ToolHandle<IEtMissMuonSystematicsTool> m_muonSystematicsTool;
  // bool m_do_met_systematics;
  // bool m_do_met_muon_systematics;
  // bool m_do_truth_met;
  // bool m_topo_systematics_use_eta45;

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

  // AccumulateUncert accUnc;  // for leading photon
  // AccumulateFFUncert accFFUnc;
  // AccumulateUncert accUnc2; // for second photon
  // AccumulateFFUncert accFFUnc2;

  //mutable TRandom3 m_rand3;

  // for calculating scale factors for electrons and photons
  Root::TElectronEfficiencyCorrectionTool* m_electron_reco_SF;
  Root::TElectronEfficiencyCorrectionTool* m_electron_id_SF;

  Root::TPhotonEfficiencyCorrectionTool* m_tool_tight_con_SF;
  Root::TPhotonEfficiencyCorrectionTool* m_tool_tight_unc_SF; 

  Analysis::AnalysisMuonConfigurableScaleFactors* m_muon_sf;

  int m_applyPileupReweighting; // 0 = none, 1 = nominal, 2 = syst
  std::string m_pileupConfig;
  std::string m_lumiCalcFile;
  Root::TPileupReweighting *m_pileupTool;

  bool m_doPDFReweighting;
  /// Handles to Athena services
  ToolHandle< IPDFTool > m_pdfTool;

  //ToolHandle<BCHTool::BCHCleaningToolAthena> m_thebchTool;
  ToolHandle<AthTileTripReader> m_ttrHandle;

  std::vector<int> m_pdfs;

  // The variables if one outputs an ntuple
  TTree* m_tree;
  unsigned int m_runNumber;
  unsigned int m_randRunNumber;
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
  std::vector<float>* m_jet_E;
  std::vector<float>* m_jet_JVF;
  std::vector<float>* m_jet_MV1;
  
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
  float m_ph_sf_unc;

  // The scale factor for the leading electron
  float m_el_sf;
  float m_el_sf_unc;
  // The scale factor for the leading muon
  float m_mu_sf;
  float m_mu_sf_unc;

  float m_pileupWeight;

  std::vector<float>* m_pdfWeights;

  TruthStudies::EventType m_type;
  int m_isStrong;
  int m_numTruthPh;

  // MET
  float m_metx;
  float m_mety;
  float m_metxOrig;
  float m_metyOrig;
  // float m_metx_noMuon;
  // float m_mety_noMuon;
  // float m_metx_full_noMuon;
  // float m_mety_full_noMuon;
  // float m_metx_MuonBoy;
  // float m_mety_MuonBoy;
  // float m_metx_RefTrack;
  // float m_mety_RefTrack;
  // float m_metxPlus_noMuon;
  // float m_metyPlus_noMuon;
  // float m_metxMinus_noMuon;
  // float m_metyMinus_noMuon;

  // float m_metx_muon_smear;
  // float m_mety_muon_smear;

  float m_set;
  float m_setOrig;
  // float m_set_full_noMuon;
  // float m_set_MuonBoy;
  // float m_set_RefTrack;
  // float m_setPlus_noMuon;
  // float m_setMinus_noMuon;
  // float m_set_muon_smear;

  // std::vector<float> *m_metx_truth;
  // std::vector<float> *m_mety_truth;
  // std::vector<float> *m_set_truth;

  float m_ph_el_minv;
  float m_ph_mu_minv;

  float m_deltaPhiPhMET;
  float m_deltaPhiElMET;
  float m_deltaPhiMuMET;

  float m_HT;
  float m_HTjet;
  float m_mTel;
  float m_mTmu;
  float m_meff;

  float m_Wpt;

};

#endif // GMSBANALYSIS_SIGNALGAMMALEPTON_H
