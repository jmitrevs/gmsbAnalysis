#include "gmsbAnalysis/SignalGammaLepton.h"
#include "ObjectSelectorCore/IAthSelectorTool.h"

#include "TH1.h"

#include "EventInfo/EventInfo.h"
#include "EventInfo/EventID.h"

#include "egammaEvent/ElectronContainer.h"
#include "egammaEvent/Electron.h"
#include "egammaEvent/PhotonContainer.h"
#include "egammaEvent/Photon.h"
#include "egammaEvent/egammaPIDdefs.h"
#include "egammaEvent/EMShower.h"
#include "egammaEvent/EMConvert.h"

#include "muonEvent/MuonContainer.h"

#include "JetEvent/JetCollection.h"
#include "JetUtils/JetCaloHelper.h"
#include "JetUtils/JetCaloQualityUtils.h"

#include "MissingETEvent/MissingET.h"

#include "VxVertex/VxContainer.h"

#include "TrigMuonEvent/TrigMuonEFInfoContainer.h"
#include "TrigDecisionTool/TrigDecisionTool.h"
#include "TrigObjectMatching/TrigMatchTool.h"

#include "GeneratorObjects/McEventCollection.h"
#include "HepMC/GenEvent.h"

#include "ITrackToVertex/ITrackToVertex.h"

#include "FourMomUtils/P4Helpers.h"
#include "TrkTrackLink/ITrackLink.h"
#include "TrkParticleBase/LinkToTrackParticleBase.h"
#include "TrkParticleBase/TrackParticleBaseCollection.h"
#include "VxVertex/VxTrackAtVertex.h"


#include <climits>


const unsigned int LAST_RUN_BEFORE_HOLE = 180481;
const unsigned int FIRST_RUN_AFTER_HOLE = 180614;

bool SignalGammaLepton::isInLArHole(Jet* jet) const
{
  const double etamin = -0.1;
  const double etamax = 1.5; 
  const double phimin = -0.9;
  const double  phimax = -0.5;

  const double eta = jet->eta();
  const double phi = jet->phi();
  if (eta < etamin || eta > etamax) return false;
  if (phi < phimin || phi > phimax) return false;
  return true;
}


/////////////////////////////////////////////////////////////////////////////
SignalGammaLepton::SignalGammaLepton(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator),
  m_trackToVertexTool("Reco::TrackToVertex"),
  m_trigDec("Trig::TrigDecisionTool/Trig::TrigDecisionTool"),
  m_trigMatch("TrigMatchTool/TrigMatchTool"),
  m_fakeMetEstimator("fest_periodF_v1.root"),
  //m_fakeMetEstimatorEmulNoHole("fest_periodD_v1.root"),
  m_userdatasvc("UserDataSvc", name)
{
  declareProperty("HistFileName", m_histFileName = "SignalGammaLepton");

  declareProperty("NumPhotons", m_numPhotonsReq = 1);
  declareProperty("NumElectrons", m_numElectronsReq = 0);
  declareProperty("NumMuons", m_numMuonsReq = 0);

  declareProperty("NumPhotonsMax", m_numPhotonsMax = UINT_MAX);
  declareProperty("NumElectronsMax", m_numElectronsMax = UINT_MAX);
  declareProperty("NumMuonsMax", m_numMuonsMax = UINT_MAX);

  // this is effectively hardcoded it probably won't work otherwse
  declareProperty("METContainerName", m_METContainerName = "MET_LocHadTopo");
  //declareProperty("METContainerName", m_METContainerName = "MET_RefFinal");
 
  // Name of the McEventCollection Container
  declareProperty("McEventContainerName",
		  m_McEventContainerName="GEN_AOD",
		  "Name of the McEventCollection container");

  // Name of the primary vertex candidates
  declareProperty("PrimaryVertexCandidates",
		  m_vxCandidatesName="VxPrimaryCandidate",
		  "Name of the primary vertex candidates");

  declareProperty("PreparationTool",      m_PreparationTool);
  declareProperty("FinalSelectionTool",   m_FinalSelectionTool);
  declareProperty("OverlapRemovalTool1",  m_OverlapRemovalTool1);
  declareProperty("OverlapRemovalTool2",  m_OverlapRemovalTool2);

  declareProperty("JetCleaningTool", m_JetCleaningTool);

  declareProperty("TruthStudiesTool", m_truth);
  declareProperty("doTruthStudies", m_doTruthStudies = false);
  declareProperty("filterWJets", m_filterWJets = false);
  declareProperty("filterTTbar", m_filterTTbar = NO_TTBARFILT);

  // Tool for track extrapolation to vertex
  declareProperty("trackToVertexTool", m_trackToVertexTool,
		  "Tool for track extrapolation to vertex");

  declareProperty("Blind", m_blind = false);
  declareProperty("BlindMET", m_blindMET = 100*GeV);
  declareProperty("BlindMT", m_blindMT = 100*GeV);

  declareProperty("isMC", m_isMC = false);
  declareProperty("trigDecisionTool", m_trigDec);
  declareProperty("trigMatchingTool", m_trigMatch);
  declareProperty("applyTrigger", m_applyTriggers = false); //only really meant for MC
  declareProperty("matchTrigger", m_matchTriggers = NONE); //for both data and MC
  declareProperty("triggers", m_triggers = "EF_2g20_loose"); // for matching or applying

  declareProperty("doSmartVeto", m_doSmartVeto = true);
  declareProperty("outputHistograms", m_outputHistograms = true);
  declareProperty("outputNtuple", m_outputNtuple = false);

}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode SignalGammaLepton::initialize(){

  ATH_MSG_DEBUG("initialize()");
 
  StatusCode sc = m_PreparationTool.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on analysis preparation tool");
    return sc;
  }

  sc = m_FinalSelectionTool.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on final selection tool");
    return sc;
  }

  sc = m_OverlapRemovalTool1.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on first analysis overlap removal tool");
    return sc;
  }

  sc = m_OverlapRemovalTool2.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on secnd analysis overlap removal tool");
    return sc;
  }

  // retrieving TrackToVertex:
  sc = m_trackToVertexTool.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Failed to retrieve tool " << m_trackToVertexTool);
    return sc;
  }

  // retrieving jet cleaning tool
  sc = m_JetCleaningTool.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Failed to retrieve tool " << m_JetCleaningTool);
    return sc;
  }

  // retrieving the truth studies tool
  if (m_doTruthStudies || m_filterWJets || m_filterTTbar) {
    sc = m_truth.retrieve();
    if ( sc.isFailure() ) {
      ATH_MSG_ERROR("Failed to retrieve tool " << m_truth);
      return sc;
    }
  }
      
  if (m_applyTriggers || m_matchTriggers) {
    sc = m_trigDec.retrieve();
    if ( sc.isFailure() ) {
      ATH_MSG_ERROR("Failed to retrieve tool " << m_trigDec);
      return sc;
    }
  }

  if (m_matchTriggers) {
    sc = m_trigMatch.retrieve();
    if ( sc.isFailure() ) {
      ATH_MSG_ERROR("Failed to retrieve tool " << m_trigMatch);
      return sc;
    }
  }

  if ( !m_userdatasvc.retrieve().isSuccess() ) {
    ATH_MSG_ERROR("Unable to retrieve pointer to UserDataSvc");
    return StatusCode::FAILURE;
  }

  /// histogram location
  sc = service("THistSvc", m_thistSvc);
  if(sc.isFailure()) {
    ATH_MSG_ERROR("Unable to retrieve pointer to THistSvc");
    return sc;
  }

  // this gets created no matter what
  m_histograms["CutFlow"] = new TH1D("CutFlow", "CutFlow", NUM_CUTS, 0, NUM_CUTS);
  // always output the cutflow
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Global/CutFlow" , m_histograms["CutFlow"]).ignore();

  if (m_outputHistograms) {
    m_histograms["ph_numConv"] = new TH1F("ph_numConv","Number of converted photons;number converted photons", 4, -0.5, 3.5);

    m_histograms["ph_eta1"] = new TH1F("ph_eta1","Psuedorapidity of the leading photons;#eta_{reco}", 100, -3,3);
    m_histograms["ph_pt1"] = new TH1F("ph_pt1","Transverse momentum of the leading photons;p_{T} [GeV]", 500, 0, 500);
    m_histograms["ph_eta2"] = new TH1F("ph_eta2","Psuedorapidity of the second photons;#eta_{reco}", 100, -3,3);
    m_histograms["ph_pt2"] = new TH1F("ph_pt2","Transverse momentum of the second photons;p_{T} [GeV]", 500, 0, 500);

    m_histograms["ph_pt_input"] = new TH1F("ph_pt_input","Transverse momentum of the leading photons passing selection criteria;p_{T} [GeV]", 500, 0, 500);

    m_histograms["ph_ptB_unconv"] = new TH1F("ph_ptB_unconv","Transverse momentum of the unconverted Barrel photons;p_{T} [GeV]", 500, 0, 500);
    m_histograms["ph_ptEC_unconv"] = new TH1F("ph_ptEC_unconv","Transverse momentum of the unconverted EC photons;p_{T} [GeV]", 500, 0, 500);

    m_histograms["ph_ptB_conv"] = new TH1F("ph_ptB_conv","Transverse momentum of the converted Barrel photons;p_{T} [GeV]", 500, 0, 500);
    m_histograms["ph_ptEC_conv"] = new TH1F("ph_ptEC_conv","Transverse momentum of the converted EC photons;p_{T} [GeV]", 500, 0, 500);


    m_histograms["mu_eta1"] = new TH1F("mu_eta1","Psuedorapidity of the leading muons;#eta_{reco}", 100, -3,3);
    m_histograms["mu_pt1"] = new TH1F("mu_pt1","Transverse momentum of the leading muons;p_{T} [GeV]", 100, 0, 500);

    m_histograms["el_eta1"] = new TH1F("el_eta1","Psuedorapidity of the leading electrons;#eta_{reco}", 100, -3,3);
    m_histograms["el_pt1"] = new TH1F("el_pt1","Transverse momentum of the leading electrons;p_{T} [GeV]", 100, 0, 500);
    m_histograms["el_eta2"] = new TH1F("el_eta2","Psuedorapidity of the second electrons;#eta_{reco}", 100, -3,3);
    m_histograms["el_pt2"] = new TH1F("el_pt2","Transverse momentum of the second electrons;p_{T} [GeV]", 100, 0, 500);

    m_histograms["ph_el_minv"] = new TH1F("ph_el_minv", "The invariant mass of the leading photon and electron;M_{inv} [GeV]", 120, 0, 120);
    m_histograms["ph_mu_minv"] = new TH1F("ph_mu_minv", "The invariant mass of the leading photon and muon;M_{inv} [GeV]", 120, 0, 120);

    m_histograms["numPh"] = new TH1F("numPh", "The number of photons that pass cuts;N_{photons}", 9, -0.5, 8.5);
    m_histograms["numEl"] = new TH1F("numEl", "The number of electrons that pass cuts;N_{electrons}", 9, -0.5, 8.5);
    m_histograms["numMu"] = new TH1F("numMu", "The number of muons that pass cuts;N_{muons}", 9, -0.5, 8.5);
    m_histograms["numJets"] = new TH1F("numJets", "The number of jets that pass cuts;N_{jets}", 9, -0.5, 8.5);

    // MET
    m_histograms["met"] = new TH1F("met", "The MET distribution;Etmiss [GeV]", 500, 0, 500);
    m_histograms["met0J"] = new TH1F("met0J", "The MET distribution of events with zero jets;Etmiss [GeV]", 500, 0, 500);
    m_histograms["met1J"] = new TH1F("met1J", "The MET distribution of events with one jet;Etmiss [GeV]", 500, 0, 500);
    m_histograms["met2J"] = new TH1F("met2J", "The MET distribution of events with two jets;Etmiss [GeV]", 500, 0, 500);
    m_histograms["met3J"] = new TH1F("met3J", "The MET distribution of events with three jets;Etmiss [GeV]", 500, 0, 500);
    m_histograms["met4J"] = new TH1F("met4J", "The MET distribution of events with four jets;Etmiss [GeV]", 500, 0, 500);

    m_histograms["metExtended"] = new TH1F("metExtended", "The MET distribution;Etmiss [GeV]", 250, 0, 1250);

    m_histograms["deltaPhiPhMETvsMET"] = new TH2F("deltaPhiPhMETvsMET", 
						  "The DeltaPhi(Photon,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  100, 0, M_PI, 250, 0, 250);

    m_histograms["deltaPhiElMETvsMET"] = new TH2F("deltaPhiElMETvsMET", 
						  "The DeltaPhi(Electron,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  100, 0, M_PI, 250, 0, 250);

    m_histograms["deltaPhiMuMETvsMET"] = new TH2F("deltaPhiMuMETvsMET", 
						  "The DeltaPhi(Muon,MET) distribution vs. MET;#Delta#phi;Etmiss [GeV]",
						  100, 0, M_PI, 250, 0, 250);

    m_histograms["HT"] = new TH1F("HT", "The H_{T} distribution;H_{T} [GeV]", 300, 0, 1500);
    m_histograms["mTel"] = new TH1F("mTel", "The m_{T} distribution;m_{T} [GeV]", 500, 0, 500);
    m_histograms["mTmu"] = new TH1F("mTmu", "The m_{T} distribution;m_{T} [GeV]", 500, 0, 500);
    m_histograms["meff"] = new TH1F("meff", "The m_{eff} distribution;m_{eff} [GeV]", 300, 0, 1500);

    m_histograms["eventType"] = new TH1F("eventType", "The event type, based on truth;event type", 
					 TruthStudies::numEventTypes, 0, TruthStudies::numEventTypes);

    m_histograms["isStrong"] = new TH1F("isStrong", "The type of production", 2, 0, 2); 
    m_histograms["numTruthPh"] = new TH1F("numTruthPh", "The number of truth photons;N_{truth photons}", 10, -1.5, 8.5);

    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/numConv" , m_histograms["ph_numConv"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta1" , m_histograms["ph_eta1"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt1" , m_histograms["ph_pt1"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta2" , m_histograms["ph_eta2"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt2" , m_histograms["ph_pt2"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_input" , m_histograms["ph_pt_input"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ptB_unconv" , m_histograms["ph_ptB_unconv"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ptEC_unconv" , m_histograms["ph_ptEC_unconv"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ptB_conv" , m_histograms["ph_ptB_conv"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ptEC_conv" , m_histograms["ph_ptEC_conv"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/numPh" , m_histograms["numPh"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/numTruthPh" , m_histograms["numTruthPh"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Muon/eta1" , m_histograms["mu_eta1"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Muon/pt1" , m_histograms["mu_pt1"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta1" , m_histograms["el_eta1"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt1" , m_histograms["el_pt1"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta2" , m_histograms["el_eta2"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt2" , m_histograms["el_pt2"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ph_el_minv" , m_histograms["ph_el_minv"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ph_mu_minv" , m_histograms["ph_mu_minv"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/numEl" , m_histograms["numEl"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Muon/numMu" , m_histograms["numMu"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Jets/numJets" , m_histograms["numJets"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met" , m_histograms["met"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met0J" , m_histograms["met0J"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met1J" , m_histograms["met1J"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met2J" , m_histograms["met2J"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met3J" , m_histograms["met3J"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met4J" , m_histograms["met4J"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/metExtended" , m_histograms["metExtended"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/deltaPhiPhMETvsMET" , m_histograms["deltaPhiPhMETvsMET"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/deltaPhiElMETvsMET" , m_histograms["deltaPhiElMETvsMET"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/deltaPhiMuMETvsMET" , m_histograms["deltaPhiMuMETvsMET"]).ignore();
    
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Global/HT" , m_histograms["HT"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Global/mTel" , m_histograms["mTel"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Global/mTmu" , m_histograms["mTmu"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Global/meff" , m_histograms["meff"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Global/eventType" , m_histograms["eventType"]).ignore();
    m_thistSvc->regHist(std::string("/")+m_histFileName+"/Global/isStrong" , m_histograms["isStrong"]).ignore();
  }


  if (m_outputNtuple) {

    m_ph_pt = new std::vector<float>;
    m_ph_eta = new std::vector<float>;
    m_ph_phi = new std::vector<float>;

    m_ph_AR = new std::vector<int>;
    m_ph_convType = new std::vector<int>;
    m_ph_numSi0 = new std::vector<int>;
    m_ph_numSi1 = new std::vector<int>;
    m_ph_numPix0 = new std::vector<int>;
    m_ph_numPix1 = new std::vector<int>;
    m_ph_numSiEl = new std::vector<int>;
    m_ph_numPixEl = new std::vector<int>;
    m_ph_numBEl = new std::vector<int>;

    m_el_pt = new std::vector<float>;
    m_el_eta = new std::vector<float>;
    m_el_phi = new std::vector<float>;

    m_mu_pt = new std::vector<float>;
    m_mu_eta = new std::vector<float>;
    m_mu_phi = new std::vector<float>;

    // the TTree
    m_tree = new TTree("GammaLepton","TTree for GammaLepton analysis");
    sc = m_thistSvc->regTree(std::string("/")+m_histFileName+"/GammaLepton", m_tree);
    if(sc.isFailure()) {
      ATH_MSG_ERROR("Unable to register tree to THistSvc");
      return sc;
    }
    // first add Event info stuff
    m_tree->Branch("Run",  &m_runNumber,   "Run/i");    // run number
    m_tree->Branch("Event",&m_eventNumber, "Event/i");  // event number
    m_tree->Branch("LumiBlock", &m_lumiBlock,"LumiBlock/i"); // lum block num
    m_tree->Branch("Weight", &m_weight, "Weight/F"); // weight

    // now event (vs object) variables
    m_tree->Branch("numPh",  &m_numPh, "numPh/i");
    m_tree->Branch("numTruthPh",  &m_numTruthPh, "numTruthPh/I");
    m_tree->Branch("numEl",  &m_numEl, "numEl/i");
    m_tree->Branch("numMu",  &m_numMu, "numMu/i");
    m_tree->Branch("numJets",  &m_numJets, "numJets/i");

    m_tree->Branch("numPhPresel",  &m_numPhPresel, "numPh/i");
    m_tree->Branch("numElPresel",  &m_numElPresel, "numEl/i");
    m_tree->Branch("numMuPresel",  &m_numMuPresel, "numMu/i");

    m_tree->Branch("Metx", &m_metx, "Metx/F"); 
    m_tree->Branch("Mety", &m_mety, "Mety/F"); 

    m_tree->Branch("PhElMinv", &m_ph_el_minv, "Weight/F"); // invariant mass photon electron
    m_tree->Branch("PhMuMinv", &m_ph_mu_minv, "Weight/F"); // invariant mass photon muon
    m_tree->Branch("ElMinv", &m_el_minv, "Weight/F"); // invariant mass leading electron
    m_tree->Branch("MuMinv", &m_mu_minv, "Weight/F"); // invariant mass leading muons
    
    m_tree->Branch("deltaPhiPhMET", &m_deltaPhiPhMET, "deltaPhiPhMET/F"); 
    m_tree->Branch("deltaPhiElMET", &m_deltaPhiElMET, "deltaPhiPhMET/F"); 
    m_tree->Branch("deltaPhiMuMET", &m_deltaPhiMuMET, "deltaPhiPhMET/F"); 

    m_tree->Branch("HT", &m_HT, "HT/F"); 
    m_tree->Branch("mTel", &m_mTel, "mTel/F"); 
    m_tree->Branch("mTmu", &m_mTmu, "mTmu/F"); 
    m_tree->Branch("meff", &m_meff, "meff/F"); 

    m_tree->Branch("eventType",  &m_type, "eventType/I");
    m_tree->Branch("isStrong",  &m_isStrong, "isStrong/I");

    // now now the arrays
    m_tree->Branch("PhotonPt", &m_ph_pt);
    m_tree->Branch("PhotonEta", &m_ph_eta);
    m_tree->Branch("PhotonPhi", &m_ph_phi);

    m_tree->Branch("PhotonAR", &m_ph_AR);
    m_tree->Branch("PhotonConvType", &m_ph_convType);
    m_tree->Branch("PhotonNumSi0", &m_ph_numSi0);
    m_tree->Branch("PhotonNumSi1", &m_ph_numSi1);
    m_tree->Branch("PhotonNumPix0", &m_ph_numPix0);
    m_tree->Branch("PhotonNumPix1", &m_ph_numPix1);
    m_tree->Branch("PhotonNumSiEl", &m_ph_numSiEl);
    m_tree->Branch("PhotonNumPixEl", &m_ph_numPixEl);
    m_tree->Branch("PhotonNumBEl", &m_ph_numBEl);

    m_tree->Branch("ElectronPt", &m_el_pt);
    m_tree->Branch("ElectronEta", &m_el_eta);
    m_tree->Branch("ElectronPhi", &m_el_phi);

    m_tree->Branch("MuonPt", &m_mu_pt);
    m_tree->Branch("MuonEta", &m_mu_eta);
    m_tree->Branch("MuonPhi", &m_mu_phi);
  }

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode SignalGammaLepton::execute() 
{
  ATH_MSG_DEBUG("execute");


  m_weight = 1.0;

  // The missing ET object
  const MissingET* metCont(0);
  StatusCode sc = evtStore()->retrieve( metCont, m_METContainerName );
  if( sc.isFailure()  ||  !metCont ) {
    ATH_MSG_ERROR("No "<< m_METContainerName <<" container found in TDS");
    return StatusCode::RECOVERABLE;
  }

  const MissingET* met_muonboyContainer =0;
  sc = evtStore()->retrieve(met_muonboyContainer , "MET_MuonBoy" );
  if( sc.isFailure()  ||  !met_muonboyContainer ) {
    ATH_MSG_ERROR("No MET_MuonBoy container found in TDS");
    return StatusCode::RECOVERABLE;
  }

  const MissingET* met_refmuontrackContainer =0;
  sc = evtStore()->retrieve( met_refmuontrackContainer, "MET_RefMuon_Track" );
  if( sc.isFailure()  ||  !met_refmuontrackContainer ) {
    ATH_MSG_ERROR("No MET_RefMuon_Track container found in TDS");
    return StatusCode::RECOVERABLE;
  }

  // retrieve the container of Vertex
  const VxContainer* vxContainer(0);
  sc = evtStore()->retrieve(vxContainer, m_vxCandidatesName);
  if (sc != StatusCode::SUCCESS) {
    ATH_MSG_ERROR("no primary vertex container for this egamma, vxContainer: "<<vxContainer);
    return StatusCode::RECOVERABLE;
  }

  const EventInfo*  evtInfo = 0;
  sc = evtStore()->retrieve(evtInfo);
  if(sc.isFailure() || !evtInfo) {
    ATH_MSG_ERROR("could not retrieve event info");
    return StatusCode::RECOVERABLE;
  }

  if (m_outputNtuple) {
    m_ph_pt->clear();
    m_ph_eta->clear();
    m_ph_phi->clear();

    m_ph_AR->clear();
    m_ph_convType->clear();
    m_ph_numSi0->clear();
    m_ph_numSi1->clear();
    m_ph_numPix0->clear();
    m_ph_numPix1->clear();
    m_ph_numSiEl->clear();
    m_ph_numPixEl->clear();
    m_ph_numBEl->clear();

    m_el_pt->clear();
    m_el_eta->clear();
    m_el_phi->clear();

    m_mu_pt->clear();
    m_mu_eta->clear();
    m_mu_phi->clear();
  }
  
  m_runNumber = evtInfo->event_ID()->run_number();
  m_lumiBlock = evtInfo->event_ID()->lumi_block();
  m_eventNumber = evtInfo->event_ID()->event_number();

  const EventInfo::EventFlagErrorState larError = evtInfo->errorState(EventInfo::LAr);

  if (m_isMC) {
    
    const McEventCollection * aMcEventContainer;
    sc = evtStore()->retrieve(aMcEventContainer, m_McEventContainerName);
    
    if(sc.isSuccess()) {
      ATH_MSG_DEBUG("Found aMcEventContainer, m_McEventContainerName = " << m_McEventContainerName);
      const HepMC::GenEvent * aGenEvent = *(aMcEventContainer->begin());
      const HepMC::WeightContainer& weightContainer = aGenEvent->weights();
      
      unsigned int Size = weightContainer.size();
      if(Size > 0) m_weight = weightContainer[0];
    } else {
      ATH_MSG_WARNING("did not find aMcEventContainer, m_McEventContainerName = " << m_McEventContainerName);
    }

  }

  ATH_MSG_DEBUG("About to prepare selection: " << m_runNumber << " " << m_lumiBlock << " " 
		<< m_eventNumber << "; weight: " << m_weight);


  // // get the user data
  // if (m_isMC) {
  //   float pileupWeight(0);
  //   if (m_userdatasvc->getInMemEventDecoration(std::string("pileupWeight"), pileupWeight)
  // 	!= StatusCode::SUCCESS) {
  //     ATH_MSG_ERROR("Error in geting event weight decoration");
  //     return StatusCode::FAILURE;
  //   }
    
  //   if (pileupWeight == -1) {
  //     ATH_MSG_ERROR("for some reason there was no weight set");
  //     return StatusCode::FAILURE;
  //   }
    
  //   m_weight *= pileupWeight;
  // }


  m_HT = 0.0;

  m_histograms["CutFlow"]->Fill(0.0, m_weight);


  if (larError) {
    return StatusCode::SUCCESS; // reject event
  }
    
  ATH_MSG_DEBUG("Passed larError");

  // also do truth-level filtering here
  // if (m_filterWJets) {
  //   if (
  m_histograms["CutFlow"]->Fill(1.0, m_weight);


  // now chose a run number for the LAr hole veto
  // const double feb_lumi_fraction = (1067.4-165.468)/1067.4; // Fraction of lumi with hole
  // bool hasFEBHole = runNum > LAST_RUN_BEFORE_HOLE;
  
  unsigned int pretendRunNum = m_runNumber;

  // if(m_isMC) {
  //   m_rand3.SetSeed(m_runNumber + m_eventNumber);
  //   const double roll_result = m_rand3.Rndm();
  //   hasFEBHole = roll_result < feb_lumi_fraction;
  //   pretendRunNum = (hasFEBHole) ? FIRST_RUN_AFTER_HOLE : LAST_RUN_BEFORE_HOLE; 
  // }

  // // overwrite it 
  // hasFEBHole = false;
  // pretendRunNum = LAST_RUN_BEFORE_HOLE; 

  // do the selecton and overlap removal
  sc = m_PreparationTool->execute(pretendRunNum);
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Preparation Failed - selection ");
    return sc;
  }

  sc = m_OverlapRemovalTool1->execute();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("OverlapRemoval 1 Failed");
    return sc;
  }

  sc = m_OverlapRemovalTool2->execute();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("OverlapRemoval 2 Failed");
    return sc;
  }

  ATH_MSG_DEBUG("Done preparing selection");

  const PhotonContainer *photonsBeforeOverlapRemoval = m_PreparationTool->selectedPhotons();
  const PhotonContainer *photons = m_OverlapRemovalTool2->finalStatePhotons();
  const ElectronContainer *electrons = m_OverlapRemovalTool2->finalStateElectrons();

  const Analysis::MuonContainer *muonsBeforeOverlapRemoval = m_PreparationTool->selectedMuons();
  const Analysis::MuonContainer *muons = m_OverlapRemovalTool2->finalStateMuons();

  // const JetCollection *allJets =  m_PreparationTool->selectedJets();

  const JetCollection *jets = m_OverlapRemovalTool2->finalStateJets();


  ATH_MSG_DEBUG("Got the containers");

  if (m_outputHistograms && photons->size() > 0) {
    // let's plot all the photons

    m_histograms["ph_pt_input"]->Fill(photons->at(0)->pt()/GeV, m_weight);

  }
  // jet cleaning
  for (JetCollection::const_iterator jet = jets->begin();
       jet != jets->end();
       jet++) {
    
    ATH_MSG_DEBUG("Looking at jet with pt = " << (*jet)->pt() << ", eta = " << (*jet)->eta() << ", phi = " << (*jet)->phi());
    if (!m_JetCleaningTool->accept(*jet)) {
      return StatusCode::SUCCESS; // reject event
    }
  }
  m_histograms["CutFlow"]->Fill(2.0, m_weight);
  ATH_MSG_DEBUG("Passed jet cleaning");

  // define some bitmasks
  const unsigned int LArCleaning = 1 << egammaPID::LArQCleaning;
  const unsigned int LArTiming = 1 << egammaPID::OutTime;

  // photon cleaning
 
  for (PhotonContainer::const_iterator ph = photons->begin();
       ph != photons->end();
       ph++) {
    if ((*ph)->isgoodoq(LArTiming)) {
      // fails timing if nonzero
      return StatusCode::SUCCESS; // reject event
    }

    const EMShower *shower = (*ph)->detail<EMShower>();
    const double e233   = shower->e233(); 
    const double e237   = shower->e237(); 
    const double e277   = shower->e277(); 
    const double Reta37 = fabs(e277)>0. ? e237/e277 : 0.;
    const double Rphi33 = fabs(e237)>0. ? e233/e237 : 0.;
    

    if ((*ph)->isgoodoq(LArCleaning) && (Reta37 > 0.98 || Rphi33 > 1.0)) {
      return StatusCode::SUCCESS; // reject event
    }

  }
 
  m_histograms["CutFlow"]->Fill(3.0, m_weight);
  ATH_MSG_DEBUG("Passed photon cleaning");

  // electron cleaning
  for (ElectronContainer::const_iterator el = electrons->begin();
       el != electrons->end();
       el++) {
    if ((*el)->isgoodoq(LArTiming)) {
      // fails timing if nonzero
      return StatusCode::SUCCESS; // reject event
    }

    // const EMShower *shower = (*el)->detail<EMShower>();
    // const double e233   = shower->e233(); 
    // const double e237   = shower->e237(); 
    // const double e277   = shower->e277(); 
    // const double Reta37 = fabs(e277)>0. ? e237/e277 : 0.;
    // const double Rphi33 = fabs(e237)>0. ? e233/e237 : 0.;
    

    // if ((*el)->isgoodoq(LArCleaning) && (Reta37 > 0.98 || Rphi33 > 1.0)) {
    //   return StatusCode::SUCCESS; // reject event
    // }      
  }

  m_histograms["CutFlow"]->Fill(4.0, m_weight);
  ATH_MSG_DEBUG("Passed electron cleaning");


  // check the primary vertex
  if (vxContainer->size() < 2) {
    return StatusCode::SUCCESS; // reject event
  }

  const std::vector<Trk::VxTrackAtVertex*>* vxtracks = 
    vxContainer->at(0)->vxTrackAtVertex();

  if (vxtracks->size() <= 4) {
    return StatusCode::SUCCESS; // reject event
  }

  m_histograms["CutFlow"]->Fill(5.0, m_weight);
  ATH_MSG_DEBUG("Passed vertex");


  // moun cleaning -- bad muons
  for (Analysis::MuonContainer::const_iterator mu = muonsBeforeOverlapRemoval->begin();
       mu != muonsBeforeOverlapRemoval->end();
       mu++) {
   
    const Rec::TrackParticle* track = (*mu)->track();
    bool trackok = (track && track->measuredPerigee()->localErrorMatrix().covariance().num_row() != 0);
    if(!trackok && track) {
      ATH_MSG_WARNING("MuonTrackAtPVFiller: muon (primary) track has null covariance matrix.");
      return StatusCode::RECOVERABLE;
    }

    const Trk::MeasuredPerigee* newMeasPerigee =
      m_trackToVertexTool->perigeeAtVertex(*track, vxContainer->at(0)->recVertex().position());
    const double qoverp_exPV = newMeasPerigee->parameters()[Trk::qOverP];
    const Trk::ErrorMatrix errormat = newMeasPerigee->localErrorMatrix();
    const double cov_qoverp_exPV = errormat.covValue(Trk::qOverP);
    delete newMeasPerigee;
    ATH_MSG_DEBUG("qoverp_exPV = " << qoverp_exPV << ", cov_qoverp_exPV = " << cov_qoverp_exPV);
    
    if (qoverp_exPV != 0 && qoverp_exPV > -99999.) {
      double qoperror = sqrt(cov_qoverp_exPV)/fabs(qoverp_exPV);
      if (qoperror >= 0.2) return StatusCode::SUCCESS; // reject event 
    }
  }

  // muon cleaning -- cosmic muons
  for (Analysis::MuonContainer::const_iterator mu = muons->begin();
       mu != muons->end();
       mu++) {
   
    const Trk::MeasuredPerigee* newMeasPerigee =
      m_trackToVertexTool->perigeeAtVertex(*((*mu)->track()), vxContainer->at(0)->recVertex().position());
    const double dz = newMeasPerigee->parameters()[Trk::z0];
    const double dd = newMeasPerigee->parameters()[Trk::d0];
    delete newMeasPerigee;
    ATH_MSG_DEBUG("dZ = " << dz << ", dd = " << dd);
    if (fabs(dz) >= 1.0 || fabs(dd) >= 0.2) {
      return StatusCode::SUCCESS; // reject event
    }      
  }
  m_histograms["CutFlow"]->Fill(6.0, m_weight);
  ATH_MSG_DEBUG("Passed muon rejection");

  // loop over photons
  m_numPhPresel = photons->size();

  unsigned int numConvPhPass = 0; // this is per event
  Analysis::Photon *leadingPh = 0;
  Analysis::Photon *secondPh = 0;
  
  double leadingPhPt = 0;
  double secondPhPt = 0;

  ATH_MSG_DEBUG("Before overlap removal photons size at input = " << photonsBeforeOverlapRemoval->size());
  ATH_MSG_DEBUG("Overlap-removed photons size at input = " << photons->size());
  
  m_numPh = 0;
  for (PhotonContainer::const_iterator ph  = photons->begin();
       ph != photons->end();
       ph++) {

    double pt = 0;

    // get the user data
    if (m_userdatasvc->getInMemElementDecoration(**ph, std::string("corrPt"), pt)
	!= StatusCode::SUCCESS) {
      ATH_MSG_ERROR("Error in geting photon decoration");
      return StatusCode::FAILURE;
    }

    if (! m_FinalSelectionTool->isSelected(*ph, 0, 0, pt) ) continue;     

    ATH_MSG_DEBUG("Original photon pt = " << (*ph)->pt() << ", corrected = " << pt); 

    // photon is OK
    m_numPh++;

    m_HT += pt;

    // let's do the AR studies

    int convType = 0;
    int numSi0 = -9;
    int numPix0 = -9;
    int numSi1 = -9;
    int numPix1 = -9;

    const Trk::VxCandidate*  convVtx = (*ph)->conversion();

    ATH_MSG_DEBUG("Will start covnersions");

    if (convVtx) {
      const std::vector<Trk::VxTrackAtVertex*> *trkAtVxPtr = convVtx->vxTrackAtVertex();
      if (trkAtVxPtr->size() == 1) {
	ATH_MSG_DEBUG("1-track");

	convType = 1;
	// first track
	Trk::VxTrackAtVertex* tmpTrkAtVtx1 = trkAtVxPtr->at(0);
	const Trk::ITrackLink * trLink =tmpTrkAtVtx1->trackOrParticleLink();
	const Trk::TrackParticleBase* tempTrk1PB(0);
	if (0!= trLink) {
	  const Trk::LinkToTrackParticleBase * linkToTrackPB =  dynamic_cast<const Trk::LinkToTrackParticleBase *>(trLink);  
	  if (0!= linkToTrackPB) {
	    if(linkToTrackPB->isValid()) tempTrk1PB = linkToTrackPB->cachedElement(); 
	  } 
	}
	if ( tempTrk1PB!=NULL){  
	  const Trk::TrackSummary* summary1 = tempTrk1PB->trackSummary();
	  if (summary1 != NULL){
	    numPix0 = summary1->get(Trk::numberOfPixelHits);
	    numSi0 = summary1->get(Trk::numberOfSCTHits)+ numPix0;
	  }
	}
      } else if (int(trkAtVxPtr->size())==2) {
	ATH_MSG_DEBUG("2-track");
	convType = 2;

	// first track
	Trk::VxTrackAtVertex* tmpTrkAtVtx1 = trkAtVxPtr->at(0);
	const Trk::ITrackLink * trLink1 =tmpTrkAtVtx1->trackOrParticleLink();
	const Trk::TrackParticleBase* tempTrk1PB(0);
	if (0!= trLink1) {
	  const Trk::LinkToTrackParticleBase * linkToTrackPB =  dynamic_cast<const Trk::LinkToTrackParticleBase *>(trLink1);  
	  if (0!= linkToTrackPB) {
	    if(linkToTrackPB->isValid()) tempTrk1PB = linkToTrackPB->cachedElement(); 
	  } 
	}
	if ( tempTrk1PB!=NULL){  
	  const Trk::TrackSummary* summary1 = tempTrk1PB->trackSummary();
	  if (summary1 != NULL){
	    numPix0 = summary1->get(Trk::numberOfPixelHits);
	    numSi0 = summary1->get(Trk::numberOfSCTHits)+numPix0;
	  }
	}
	Trk::VxTrackAtVertex* tmpTrkAtVtx2 = trkAtVxPtr->at(1);
	const Trk::ITrackLink * trLink2 =tmpTrkAtVtx2->trackOrParticleLink();
	const Trk::TrackParticleBase* tempTrk2PB(0);
	if (0!= trLink2) {
	  const Trk::LinkToTrackParticleBase * linkToTrackPB =  dynamic_cast<const Trk::LinkToTrackParticleBase *>(trLink2);  
	  if (0!= linkToTrackPB) {
	    if (linkToTrackPB->isValid()) tempTrk2PB = linkToTrackPB->cachedElement(); 
	  } 
	}
	if ( tempTrk2PB!=NULL) {
	  const Trk::TrackSummary* summary2 = tempTrk2PB->trackSummary();
	  if (summary2 != NULL){
	    numPix1 = summary2->get(Trk::numberOfPixelHits);
	    numSi1 = summary2->get(Trk::numberOfSCTHits) + numPix1;
	  }
	}
      }
    }

    ATH_MSG_DEBUG("electron track");

    int numBEl = -9;
    int numSiEl = -9;
    int numPixEl = -9;

    const Rec::TrackParticle * trParticle = (*ph)->trackParticle();
    if (trParticle) {
      const Trk::TrackSummary* sum = trParticle->trackSummary();
      if (sum != NULL)  {
	numPixEl = sum->get(Trk::numberOfPixelHits);
	numSiEl = sum->get(Trk::numberOfSCTHits)+ numPixEl;
	numBEl = sum->get(Trk::numberOfBLayerHits);
      }
    }

    ATH_MSG_DEBUG("will push back stuff");

    if (m_outputNtuple) {
      m_ph_pt->push_back(pt);
      m_ph_eta->push_back((*ph)->eta());
      m_ph_phi->push_back((*ph)->phi());

      const EMConvert *convert = (*ph)->detail<EMConvert>();
      
      if (!convert) {
	ATH_MSG_ERROR("Selected photon had now EMConvert");
	return StatusCode::FAILURE;
      }
      m_ph_AR->push_back(convert->ambiguityResult());
      m_ph_convType->push_back(convType);
      m_ph_numSi0->push_back(numSi0);
      m_ph_numSi1->push_back(numSi1);
      m_ph_numPix0->push_back(numPix0);
      m_ph_numPix1->push_back(numPix1);
      m_ph_numSiEl->push_back(numSiEl);
      m_ph_numPixEl->push_back(numPixEl);
      m_ph_numBEl->push_back(numBEl);
    }

    if ((*ph)->conversion()) numConvPhPass++;
    ATH_MSG_DEBUG("Found photon with pt = " << pt << ", etaBE2 = " << (*ph)->cluster()->etaBE(2)
		  << ", phi = " << (*ph)->phi());
    
    if (pt > leadingPhPt ) {
      secondPh = leadingPh;
      leadingPh = *ph;
      secondPhPt = leadingPhPt;
      leadingPhPt = pt;
    } else if (pt > secondPhPt) {
      secondPh = *ph;
      secondPhPt = pt;
    }

  }


  if (m_numPh < m_numPhotonsReq || m_numPh > m_numPhotonsMax) {
    return StatusCode::SUCCESS;
  }

  m_histograms["CutFlow"]->Fill(7.0, m_weight);
  ATH_MSG_DEBUG("Passed photons");


  m_numEl = 0;
  m_numMu = 0;

  // DEAL WITH ELECTRONS

  m_numElPresel = electrons->size();

  Analysis::Electron *leadingEl = 0;
  Analysis::Electron *secondEl = 0;
  
  double leadingElPt = 0;
  double secondElPt = 0;

  // loop over electrons
  for (ElectronContainer::const_iterator el  = electrons->begin();
       el != electrons->end();
       el++) {


    double pt;
    // get the user data
    if (m_userdatasvc->getInMemElementDecoration(**el, std::string("corrPt"), pt)
	!= StatusCode::SUCCESS) {
      ATH_MSG_ERROR("Error in geting photon decoration");
      return StatusCode::FAILURE;
    }

    if (! m_FinalSelectionTool->isSelected(*el, 0, 0, pt) ) continue; 

    //ATH_MSG_DEBUG("Original electron pt = " << (*el)->pt() << ", corrected = " << pt); 
    ATH_MSG_DEBUG("electron with pt = " << (*el)->pt() 
		  << ", eta = " << (*el)->eta() 
		  << ", phi = " << (*el)->phi()); 
    
    m_HT += pt;

    m_numEl++;

    if (m_outputNtuple) {
      m_el_pt->push_back(pt);
      m_el_eta->push_back((*el)->eta());
      m_el_phi->push_back((*el)->phi());
    }

    if (pt > leadingElPt ) {
      secondEl = leadingEl;
      leadingEl = *el;
      secondElPt = leadingElPt;
      leadingElPt = pt;
    } else if (pt > secondElPt) {
      secondEl = *el;
      secondElPt = pt;
    }    
  }

  // DEAL WITH MUONS
  m_numMuPresel = muons->size();

  Analysis::Muon *leadingMu = 0;
  Analysis::Muon *secondMu = 0;
  
  double leadingMuPt = 0;
  double secondMuPt = 0;

  for (Analysis::MuonContainer::const_iterator mu = muons->begin();
       mu != muons->end();
       mu++) {

    if (! m_FinalSelectionTool->isSelected(*mu) ) continue; 

    m_numMu++;
   
    const double pt = (*mu)->pt();

    m_HT += pt;
    if (m_outputNtuple) {
      m_mu_pt->push_back((*mu)->pt());
      m_mu_eta->push_back((*mu)->eta());
      m_mu_phi->push_back((*mu)->phi());
    }

    if (pt > leadingMuPt ) {
      secondMu = leadingMu;
      leadingMu = *mu;
      secondMuPt = leadingMuPt;
      leadingMuPt = pt;
    } else if (pt > secondMuPt) {
      secondMu = *mu;
      secondMuPt = pt;
    }

  }

  if (m_numEl < m_numElectronsReq || m_numMu < m_numMuonsReq ||
      m_numEl > m_numElectronsMax || m_numMu > m_numMuonsMax ) {
    return StatusCode::SUCCESS;
  }

  ATH_MSG_DEBUG("Passed lepton");
   
  m_histograms["CutFlow"]->Fill(8.0, m_weight);

  // lets correct the MET
  double met_eta4p5=0;
  double etMiss_eta4p5_etx=0;
  double etMiss_eta4p5_ety=0;
  //Regions for lochad topo
  const MissingEtRegions* caloReg = metCont->getRegions();
  if ( caloReg != 0 ) {
    double etMiss_topo_lochad_central_etx = caloReg->exReg(MissingEtRegions::Central);
    double etMiss_topo_lochad_central_ety = caloReg->eyReg(MissingEtRegions::Central);
    double etMiss_topo_lochad_endcap_etx = caloReg->exReg(MissingEtRegions::EndCap);
    double etMiss_topo_lochad_endcap_ety = caloReg->eyReg(MissingEtRegions::EndCap);  
    double etMiss_topo_lochad_forward_etx = caloReg->exReg(MissingEtRegions::Forward);
    double etMiss_topo_lochad_forward_ety = caloReg->eyReg(MissingEtRegions::Forward);

    etMiss_eta4p5_etx = etMiss_topo_lochad_central_etx + etMiss_topo_lochad_endcap_etx + etMiss_topo_lochad_forward_etx;
    etMiss_eta4p5_ety = etMiss_topo_lochad_central_ety + etMiss_topo_lochad_endcap_ety + etMiss_topo_lochad_forward_ety;
    met_eta4p5=hypot(etMiss_eta4p5_etx, etMiss_eta4p5_ety);
  } else {
    ATH_MSG_ERROR("caloReg does not exist");
    return StatusCode::FAILURE;
  }
  
  double etMiss_eta4p5_etx_muon =  etMiss_eta4p5_etx; //from above
  double etMiss_eta4p5_ety_muon =  etMiss_eta4p5_ety; // from above

  etMiss_eta4p5_etx_muon+= met_muonboyContainer->etx();
  etMiss_eta4p5_ety_muon+= met_muonboyContainer->ety();
  etMiss_eta4p5_etx_muon-= met_refmuontrackContainer->etx();
  etMiss_eta4p5_ety_muon-= met_refmuontrackContainer->ety();
  
  m_metx = etMiss_eta4p5_etx_muon;
  m_mety = etMiss_eta4p5_ety_muon;

  const double met_eta4p5_muon = hypot(etMiss_eta4p5_etx_muon, etMiss_eta4p5_ety_muon);
  const double met = met_eta4p5_muon;
  const double metPhi = (etMiss_eta4p5_ety_muon == 0.0 && etMiss_eta4p5_etx_muon == 0.0) 
    ? 0.0 : atan2(etMiss_eta4p5_ety_muon, etMiss_eta4p5_etx_muon);

  ATH_MSG_DEBUG("MET = " << met << ", metPhi = " << metPhi);

  m_numJets = 0;

  // Count number of jets
  for (JetCollection::const_iterator jet = jets->begin();
       jet != jets->end();
       jet++) {

    ATH_MSG_DEBUG("jet with pt = " << (*jet)->pt() 
		  << ", eta = " << (*jet)->eta() 
		  << ", phi = " << (*jet)->phi()); 

    if ((*jet)->eta() < 2.5) {
      m_HT += (*jet)->pt();
      m_numJets++;
    }

    if (m_doSmartVeto && isInLArHole(*jet)) {
      bool eventFails = m_fakeMetEstimator.isBad((*jet)->pt(),(*jet)->getMoment("BCH_CORR_JET"),
						 (*jet)->getMoment("BCH_CORR_CELL"),
						 (*jet)->getMoment("BCH_CORR_DOTX"),
						 (*jet)->phi(),
						 etMiss_eta4p5_etx_muon,etMiss_eta4p5_ety_muon);
      if (eventFails) {
       	return StatusCode::SUCCESS;
      }
    }
  }
  ATH_MSG_DEBUG("Passed LAr Hole");
  m_histograms["CutFlow"]->Fill(9.0, m_weight);
  

  if (m_applyTriggers) {
    if (! m_trigDec->isPassed(m_triggers)) {
      return StatusCode::SUCCESS; // reject event
    }
  }

  switch(m_matchTriggers) {
  case NONE:
    // do nothing
    break;
  case MUONS:
    if (m_numMu < 1) {
      ATH_MSG_ERROR("No muons found but attempting to match trigger. Should not be here. Probably misconfigured");
      return StatusCode::FAILURE;
    }
    TrigMatch::TrigMuonEFInfoHelper::setTrackToUse(TrigMatch::useCombinedTrack);
    if (!(m_trigMatch->matchToTriggerObject<TrigMuonEFInfo>(leadingMu, m_triggers, 
							    0.15, true))) {
      // did not match to a trigger object
      return StatusCode::FAILURE;
    } 
    break;
  default:
    ATH_MSG_WARNING("Trigger matching " << m_matchTriggers << " not supported.");
    break;
  }

  ATH_MSG_DEBUG("Passed trig");
  m_histograms["CutFlow"]->Fill(10.0, m_weight);


  m_meff = m_HT+met;
  m_ph_el_minv = -999;
  m_ph_mu_minv = -999;
  m_el_minv = -999;
  m_mu_minv = -999;
  if (m_numEl >= 1 && m_numPh >= 1) {
    m_ph_el_minv = P4Helpers::invMass(leadingPh, leadingEl);
  } 
  if (m_numMu >= 1 && m_numPh >= 1) {
    m_ph_mu_minv = P4Helpers::invMass(leadingPh, leadingMu);
  } 

  if (m_numElPresel >= 2) {
    m_el_minv = P4Helpers::invMass(electrons->at(0), electrons->at(1));
  }
  if (m_numMuPresel >= 2) {
    m_mu_minv = P4Helpers::invMass(muons->at(0), muons->at(1));
  }

  m_mTel = -999;
  m_mTmu = -999;
  m_deltaPhiPhMET = -999;
  m_deltaPhiElMET = -999;
  m_deltaPhiMuMET = -999;

  if (m_numPh >= 1) {
    m_deltaPhiPhMET = P4Helpers::deltaPhi(*leadingPh, metPhi);
  }
  if (m_numEl >= 1) {
    m_deltaPhiElMET = P4Helpers::deltaPhi(*leadingEl, metPhi);
    m_mTel = sqrt(2 * leadingElPt * met * (1 - cos(m_deltaPhiElMET)));
  }
  if (m_numMu >= 1) {
    m_deltaPhiMuMET = P4Helpers::deltaPhi(*leadingMu, metPhi);
    m_mTmu = sqrt(2 * leadingMu->pt() * met * (1 - cos(m_deltaPhiMuMET)));    
  }

  const float mT = (m_mTel > m_mTmu) ? m_mTel : m_mTmu;

  if (m_blind && (met > m_blindMET && mT > m_blindMT)) {
    // blind the event
    return StatusCode::SUCCESS;
  }
  ATH_MSG_DEBUG("Event passes blinding (or blinding disabled)");
  m_histograms["CutFlow"]->Fill(11.0, m_weight);

  // if (met > 75*GeV) {
  //   m_histograms["CutFlow"]->Fill(10.0, m_weight);
  // }

  // if (met > 100*GeV) {
  //   m_histograms["CutFlow"]->Fill(11.0, m_weight);
  // }

  // if (met > 125*GeV) {
  //   m_histograms["CutFlow"]->Fill(12.0, m_weight);
  // }

  // if (met > 150*GeV) {
  //   m_histograms["CutFlow"]->Fill(13.0, m_weight);
  // }

  // if (met < 140*GeV) {
  //   return StatusCode::SUCCESS; // reject event
  // }
  // if (mT < 110*GeV) {
  //   return StatusCode::SUCCESS; // reject event
  // }
  //  m_histograms["CutFlow"]->Fill(12.0, m_weight);


  /////////////////////////////////////////////////////
  // event accepted, so let's make plots and ntuple
  /////////////////////////////////////////////////////

  // let's print out run, lb, and event numbers,...
  ATH_MSG_INFO("Selected: " << m_runNumber << " " << m_lumiBlock << " " << m_eventNumber 
	       << " " << m_numPh << " " << m_numEl << " " 
	       << m_numMu << " " << met/GeV);


  m_type = TruthStudies::unknown;
  if (m_doTruthStudies) {
    sc = m_truth->execute();
    if ( sc.isFailure() ) {
      ATH_MSG_WARNING("TruthStudies Failed");
      return sc;
    }
    m_type = m_truth->GetEventType();
    m_isStrong = m_truth->isStrong();
    m_numTruthPh = m_truth->nPhotons();
  } else {
    m_numTruthPh = -1;
  }

  if (m_outputHistograms) {

    m_histograms["HT"]->Fill(m_HT/GeV, m_weight);
    m_histograms["meff"]->Fill(m_meff/GeV, m_weight);
    m_histograms["eventType"]->Fill(m_type, m_weight);
    m_histograms["isStrong"]->Fill(m_isStrong, m_weight);
    m_histograms["numTruthPh"]->Fill(m_numTruthPh, m_weight);

    if (leadingPh) {
      m_histograms["ph_eta1"]->Fill(leadingPh->eta(), m_weight);
      m_histograms["ph_pt1"]->Fill(leadingPhPt/GeV, m_weight);
      
      
      if (fabs(leadingPh->cluster()->eta()) < 1.45) {
	if (leadingPh->conversion()) {
	  m_histograms["ph_ptB_conv"]->Fill(leadingPhPt/GeV, m_weight);
	} else {
	  m_histograms["ph_ptB_unconv"]->Fill(leadingPhPt/GeV, m_weight);
	}
      } else {
	if (leadingPh->conversion()) {
	  m_histograms["ph_ptEC_conv"]->Fill(leadingPhPt/GeV, m_weight);
	} else {
	  m_histograms["ph_ptEC_unconv"]->Fill(leadingPhPt/GeV, m_weight);
	}
      }    
    
      if (secondPh) {
	m_histograms["ph_eta2"]->Fill(secondPh->eta(), m_weight);
	m_histograms["ph_pt2"]->Fill(secondPhPt/GeV, m_weight);
	
	accFFUnc.AddObjects(leadingPhPt, leadingPh->cluster()->etaBE(2), leadingPh->conversion(), 
			    secondPhPt, secondPh->cluster()->etaBE(2), secondPh->conversion(), m_weight);
	
	bool isBarrel1 = fabs(leadingPh->cluster()->eta()) < 1.45;
	bool isBarrel2 = fabs(secondPh->cluster()->eta()) < 1.45;
	
	
	accUnc.AddObjects(leadingPhPt, isBarrel1, leadingPh->conversion(),
			  secondPhPt, isBarrel2, secondPh->conversion(), m_weight);
	
	
	if (fabs(secondPh->cluster()->eta()) < 1.45) {
	  if (secondPh->conversion()) {
	    m_histograms["ph_ptB_conv"]->Fill(secondPhPt/GeV, m_weight);
	  } else {
	    m_histograms["ph_ptB_unconv"]->Fill(secondPhPt/GeV, m_weight);
	  }
	} else {
	  if (secondPh->conversion()) {
	    m_histograms["ph_ptEC_conv"]->Fill(secondPhPt/GeV, m_weight);
	  } else {
	    m_histograms["ph_ptEC_unconv"]->Fill(secondPhPt/GeV, m_weight);
	  }
	}    
      }
    }
    m_histograms["numPh"]->Fill(m_numPh, m_weight);
    m_histograms["ph_numConv"]->Fill(numConvPhPass, m_weight);
  
    if (leadingEl) {
      m_histograms["el_eta1"]->Fill(leadingEl->eta(), m_weight);
      m_histograms["el_pt1"]->Fill(leadingElPt/GeV, m_weight);
    }
    if (secondEl) {
      m_histograms["el_eta2"]->Fill(secondEl->eta(), m_weight);
      m_histograms["el_pt2"]->Fill(secondElPt/GeV, m_weight);
    }
    m_histograms["numEl"]->Fill(m_numEl, m_weight);
    m_histograms["numMu"]->Fill(m_numMu, m_weight);
    if (leadingMu) {
      m_histograms["mu_eta1"]->Fill(leadingMu->eta(), m_weight);
      m_histograms["mu_pt1"]->Fill(leadingMuPt/GeV, m_weight);
    }
    
    if (m_numEl >= 1 && m_numPh >= 1) {
      m_histograms["ph_el_minv"]->Fill(m_ph_el_minv/GeV, m_weight);
    }
    if (m_numMu >= 1 && m_numPh >= 1) {
      m_histograms["ph_mu_minv"]->Fill(m_ph_mu_minv/GeV, m_weight);
    }

    if (m_numPh >= 1) {
      static_cast<TH2F*>(m_histograms["deltaPhiPhMETvsMET"])->Fill(fabs(m_deltaPhiPhMET), met/GeV, m_weight);
    }
    
    if (m_numEl >= 1) {
      static_cast<TH2F*>(m_histograms["deltaPhiElMETvsMET"])->Fill(fabs(m_deltaPhiElMET), met/GeV, m_weight);
      m_histograms["mTel"]->Fill(m_mTel/GeV, m_weight);
    }
    
    if (m_numMu >= 1) {
      static_cast<TH2F*>(m_histograms["deltaPhiMuMETvsMET"])->Fill(fabs(m_deltaPhiMuMET), met/GeV, m_weight);
      m_histograms["mTmu"]->Fill(m_mTmu/GeV, m_weight);
    }

    m_histograms["numJets"]->Fill(m_numJets, m_weight);
    
    // } // end of if on MET
    
    m_histograms["met"]->Fill(met/GeV, m_weight);
    m_histograms["metExtended"]->Fill(met/GeV, m_weight);
    switch(m_numJets) {
    case 0:
      m_histograms["met0J"]->Fill(met/GeV, m_weight);
      break;
    case 1:
      m_histograms["met1J"]->Fill(met/GeV, m_weight);
      break;
    case 2:
      m_histograms["met2J"]->Fill(met/GeV, m_weight);
      break;
    case 3:
      m_histograms["met3J"]->Fill(met/GeV, m_weight);
      break;
    default:
      m_histograms["met4J"]->Fill(met/GeV, m_weight);
      break;
    }
  }

  if (m_outputNtuple) {
    m_tree->Fill();  
  }

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode SignalGammaLepton::finalize() {
    
    ATH_MSG_INFO ("finalize()");
    // initialize cut flow table
    ATH_MSG_INFO("Cut Flow Table");
    ATH_MSG_INFO("--------------");

    for (int i = 1; i <= NUM_CUTS; i++) {
      ATH_MSG_INFO("After cut " << i-1 << ": " << m_histograms["CutFlow"]->GetBinContent(i) << " events");
    }
    ATH_MSG_INFO("--------------");
    ATH_MSG_INFO("Average material error: " << accUnc.Uncert());
    ATH_MSG_INFO("Average material error using sum of squares: " << accUnc.Uncert2());
    ATH_MSG_INFO("Average material second photon error: " << accUnc2.Uncert());
    ATH_MSG_INFO("Average material second photon error using sum of squares: " << accUnc2.Uncert2());
    ATH_MSG_INFO("Average FF error: " << accFFUnc.Uncert());
    ATH_MSG_INFO("Average FF error using sum of squares: " << accFFUnc.Uncert2());
    ATH_MSG_INFO("Average FF error second photon: " << accFFUnc2.Uncert());
    ATH_MSG_INFO("Average FF error second photon using sum of squares: " << accFFUnc2.Uncert2());

    return StatusCode::SUCCESS;
}
