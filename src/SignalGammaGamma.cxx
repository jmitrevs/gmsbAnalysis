#include "gmsbAnalysis/SignalGammaGamma.h"
#include "SUSYPhotonJetCleaningTool/ISUSYPhotonJetCleaningTool.h"

#include "TH1.h"

#include "EventInfo/EventInfo.h"
#include "EventInfo/EventID.h"

#include "egammaEvent/ElectronContainer.h"
#include "egammaEvent/Electron.h"
#include "egammaEvent/PhotonContainer.h"
#include "egammaEvent/Photon.h"
#include "egammaEvent/egammaPIDdefs.h"
#include "egammaEvent/EMShower.h"

#include "muonEvent/MuonContainer.h"

#include "JetEvent/JetCollection.h"
#include "JetUtils/JetCaloHelper.h"
#include "JetUtils/JetCaloQualityUtils.h"

#include "MissingETEvent/MissingET.h"

#include "VxVertex/VxContainer.h"

#include "TrigDecisionTool/TrigDecisionTool.h"

#include "ITrackToVertex/ITrackToVertex.h"

const unsigned int LAST_RUN_BEFORE_HOLE = 180481;
const unsigned int FIRST_RUN_AFTER_HOLE = 180614;

/////////////////////////////////////////////////////////////////////////////
SignalGammaGamma::SignalGammaGamma(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator),
  m_trackToVertexTool("Reco::TrackToVertex"),
  m_trigDec("Trig::TrigDecisionTool/TrigDecisionTool"),
  m_fakeMetEstimator("fest_periodF_v1.root"),
  m_fakeMetEstimatorEmulNoHole("fest_periodD_v1.root"),
  m_userdatasvc("UserDataSvc", name)
{
  declareProperty("HistFileName", m_histFileName = "SignalGammaGamma");

  declareProperty("LeadingPhotonPtCut", m_leadPhotonPtCut = 25.0*GeV);

  // this is effectively hardcoded it probably won't work otherwse
  declareProperty("METContainerName", m_METContainerName = "MET_LocHadTopo");
  //declareProperty("METContainerName", m_METContainerName = "MET_RefFinal");
 
  // Name of the primary vertex candidates
  declareProperty("PrimaryVertexCandidates",
		  m_vxCandidatesName="VxPrimaryCandidate",
		  "Name of the primary vertex candidates");

  declareProperty("PreparationTool",     m_PreparationTool);
  declareProperty("CrackPreparationTool", m_CrackPreparationTool);
  declareProperty("OverlapRemovalTool1",  m_OverlapRemovalTool1);
  declareProperty("OverlapRemovalTool2",  m_OverlapRemovalTool2);

  declareProperty("JetCleaningTool", m_JetCleaningTool);

  // Tool for track extrapolation to vertex
  declareProperty("trackToVertexTool", m_trackToVertexTool,
		  "Tool for track extrapolation to vertex");

  declareProperty("isMC", m_isMC = false);
  declareProperty("trigDecisionTool", m_trigDec);
  declareProperty("applyTrigger", m_applyTriggers = false); //only really meant for MC
  declareProperty("triggers", m_triggers = "EF_2g20_loose");

  declareProperty("doSmartVeto", m_doSmartVeto = true);

}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode SignalGammaGamma::initialize(){

  ATH_MSG_DEBUG("initialize()");
 
  StatusCode sc = m_PreparationTool.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on analysis preparation tool");
    return sc;
  }

  sc = m_CrackPreparationTool.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on crack preparation tool");
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

  if (m_applyTriggers) {
    sc = m_trigDec.retrieve();
    if ( sc.isFailure() ) {
      ATH_MSG_ERROR("Failed to retrieve tool " << m_trigDec);
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

  m_histograms["ph_numConv"] = new TH1F("ph_numConv","Number of converted photons;number converted photons", 4, -0.5, 3.5);

  m_histograms["ph_eta1"] = new TH1F("ph_eta1","Psuedorapidity of the leading photons;#eta_{reco}", 100, -3,3);
  m_histograms["ph_pt1"] = new TH1F("ph_pt1","Transverse momentum of the leading photons;#p_{T} [GeV]", 250, 0, 250);
  m_histograms["ph_eta2"] = new TH1F("ph_eta2","Psuedorapidity of the second photons;#eta_{reco}", 100, -3,3);
  m_histograms["ph_pt2"] = new TH1F("ph_pt2","Transverse momentum of the second photons;#p_{T} [GeV]", 250, 0, 250);

  m_histograms["ph_ptB_unconv"] = new TH1F("ph_ptB_unconv","Transverse momentum of the unconverted Barrel photons;#p_{T} [GeV]", 250, 0, 250);
  m_histograms["ph_ptEC_unconv"] = new TH1F("ph_ptEC_unconv","Transverse momentum of the unconverted EC photons;#p_{T} [GeV]", 250, 0, 250);

  m_histograms["ph_ptB_conv"] = new TH1F("ph_ptB_conv","Transverse momentum of the converted Barrel photons;#p_{T} [GeV]", 250, 0, 250);
  m_histograms["ph_ptEC_conv"] = new TH1F("ph_ptEC_conv","Transverse momentum of the converted EC photons;#p_{T} [GeV]", 250, 0, 250);


  m_histograms["el_eta1"] = new TH1F("el_eta1","Psuedorapidity of the leading electrons;#eta_{reco}", 100, -3,3);
  m_histograms["el_pt1"] = new TH1F("el_pt1","Transverse momentum of the leading electrons;#p_{T} [GeV]", 100, 0, 500);
  m_histograms["el_eta2"] = new TH1F("el_eta2","Psuedorapidity of the second electrons;#eta_{reco}", 100, -3,3);
  m_histograms["el_pt2"] = new TH1F("el_pt2","Transverse momentum of the second electrons;#p_{T} [GeV]", 100, 0, 500);

  m_histograms["el_minv"] = new TH1F("el_minv", "The invariante mass of the two leading electrons;M_{inv} [GeV]", 120, 0, 120);

  m_histograms["numPh"] = new TH1F("numPh", "The number of photons that pass cuts;N_{electrons}", 9, -0.5, 8.5);
  m_histograms["numEl"] = new TH1F("numEl", "The number of electrons that pass cuts;N_{electrons}", 9, -0.5, 8.5);
  m_histograms["numJets"] = new TH1F("numJets", "The number of jets that pass cuts;N_{jets}", 9, -0.5, 8.5);

  // MET
  m_histograms["metWoMuonCorr"] = new TH1F("metWoMuonCorr", "The MET distribution;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met0JWoMuonCorr"] = new TH1F("met0JWoMuonCorr", "The MET distribution of events with zero jets;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met1JWoMuonCorr"] = new TH1F("met1JWoMuonCorr", "The MET distribution of events with one jet;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met2JWoMuonCorr"] = new TH1F("met2JWoMuonCorr", "The MET distribution of events with two jets;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met3JWoMuonCorr"] = new TH1F("met3WoMuonCorrJ", "The MET distribution of events with three jets;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met4JWoMuonCorr"] = new TH1F("met4JWoMuonCorr", "The MET distribution of events with four jets;Etmiss [GeV]", 250, 0, 250);

  m_histograms["metExtendedWoMuonCorr"] = new TH1F("metExtendedWoMuonCorr", "The MET distribution;Etmiss [GeV]", 250, 0, 1250);

  m_histograms["metWMuonCorr"] = new TH1F("metWMuonCorr", "The MET distribution;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met0JWMuonCorr"] = new TH1F("met0JWMuonCorr", "The MET distribution of events with zero jets;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met1JWMuonCorr"] = new TH1F("met1JWMuonCorr", "The MET distribution of events with one jet;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met2JWMuonCorr"] = new TH1F("met2JWMuonCorr", "The MET distribution of events with two jets;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met3JWMuonCorr"] = new TH1F("met3WMuonCorrJ", "The MET distribution of events with three jets;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met4JWMuonCorr"] = new TH1F("met4JWMuonCorr", "The MET distribution of events with four jets;Etmiss [GeV]", 250, 0, 250);

  m_histograms["metExtendedWMuonCorr"] = new TH1F("metExtendedWMuonCorr", "The MET distribution;Etmiss [GeV]", 250, 0, 1250);


  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/numConv" , m_histograms["ph_numConv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta1" , m_histograms["ph_eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt1" , m_histograms["ph_pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta2" , m_histograms["ph_eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt2" , m_histograms["ph_pt2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ptB_unconv" , m_histograms["ph_ptB_unconv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ptEC_unconv" , m_histograms["ph_ptEC_unconv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ptB_conv" , m_histograms["ph_ptB_conv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/ptEC_conv" , m_histograms["ph_ptEC_conv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/numPh" , m_histograms["numPh"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta1" , m_histograms["el_eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt1" , m_histograms["el_pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta2" , m_histograms["el_eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt2" , m_histograms["el_pt2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/minv" , m_histograms["el_minv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/numEl" , m_histograms["numEl"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Jets/numJets" , m_histograms["numJets"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/metWoMuonCorr" , m_histograms["metWoMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met0JWoMuonCorr" , m_histograms["met0JWoMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met1JWoMuonCorr" , m_histograms["met1JWoMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met2JWoMuonCorr" , m_histograms["met2JWoMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met3JWoMuonCorr" , m_histograms["met3JWoMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met4JWoMuonCorr" , m_histograms["met4JWoMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/metExtendedWoMuonCorr" , m_histograms["metExtendedWoMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/metWMuonCorr" , m_histograms["metWMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met0JWMuonCorr" , m_histograms["met0JWMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met1JWMuonCorr" , m_histograms["met1JWMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met2JWMuonCorr" , m_histograms["met2JWMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met3JWMuonCorr" , m_histograms["met3JWMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met4JWMuonCorr" , m_histograms["met4JWMuonCorr"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/metExtendedWMuonCorr" , m_histograms["metExtendedWMuonCorr"]).ignore();

  // initialize cut flow table
  for (int i = 0; i < NUM_CUTS; i++) {
    numEventsCut[i] = 0;
  }

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode SignalGammaGamma::execute() 
{
  ATH_MSG_DEBUG("execute");


  double weight = 1.0;

  // The missing ET object
  const MissingET* met(0);
  StatusCode sc = evtStore()->retrieve( met, m_METContainerName );
  if( sc.isFailure()  ||  !met ) {
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

  const unsigned runNum = evtInfo->event_ID()->run_number();
  const unsigned lbNum = evtInfo->event_ID()->lumi_block();
  const unsigned evNum = evtInfo->event_ID()->event_number();

  const EventInfo::EventFlagErrorState larError = evtInfo->errorState(EventInfo::LAr);

  // rewiegh for the Z sample and W sample
  switch (runNum) {
  case 107650:
    weight = 661.9/303405.0;
    break;
  case 107651:
    weight = 133.3/63484.0;
    break;
  case 107652:
    weight = 40.3/19496.0; 
    break;
  case 107653:
    weight = 11.2/5500.0;
    break;
  case 107654:
    weight = 2.7/1500.0;
    break;
  case 107655:
    weight = 0.8/500.0;
    break;
  case 107680:
    weight = 6913.3/1382306.0;
    break;
  case 107681:
    weight = 1293.0/641361.0;
    break;
  case 107682:
    weight = 377.1/188956.0;
    break;
  case 107683:
    weight = 100.9/50476.0;
    break;
  case 107684:
    weight = 25.3/12990.0;
    break;
  case 107685:
    weight = 6.9/3497.0;
    break;
  case 118619:
    weight = 1.4597e-2/9998 * 35;
    break;
  case 118618:
    weight = 4.0558e-2/9998 * 35;
    break;
  case 118617:
    weight = 3.9128e-2/9999 * 35;
    break;
  case 118616:
    weight = 2.9366e-2/9998 * 35;
    break;
  case 118615:
    weight = 3.9201e-2/9994 * 35;
    break;
  }

  ATH_MSG_DEBUG("About to prepare selection: " << runNum << " " << lbNum << " " << evNum);

  // get the user data
  if (m_isMC) {
    float pileupWeight(0);
    if (m_userdatasvc->getInMemEventDecoration(std::string("pileupWeight"), pileupWeight)
	!= StatusCode::SUCCESS) {
      ATH_MSG_ERROR("Error in geting event weight decoration");
      return StatusCode::FAILURE;
    }
    
    if (pileupWeight == -1) {
      ATH_MSG_ERROR("for some reason there was no weight set");
      return StatusCode::FAILURE;
    }
    
    weight *= pileupWeight;
  }

  numEventsCut[0] += weight;

  if (m_applyTriggers) {
    if (! m_trigDec->isPassed(m_triggers)) {
      return StatusCode::SUCCESS; // reject event
    }
  }

  ATH_MSG_DEBUG("Passed trig");
  numEventsCut[1] += weight;

  if (larError) {
    return StatusCode::SUCCESS; // reject event
  }
    
  ATH_MSG_DEBUG("Passed larError");
  numEventsCut[2] += weight;


  // now chose a run number for the LAr hole veto
  const double feb_lumi_fraction = (1067.4-165.468)/1067.4; // Fraction of lumi with hole
  bool hasFEBHole = runNum > LAST_RUN_BEFORE_HOLE;
  
  unsigned int pretendRunNum = runNum;

  if(m_isMC) {
    m_rand3.SetSeed(runNum + evNum);
    const double roll_result = m_rand3.Rndm();
    hasFEBHole = roll_result >= feb_lumi_fraction;
    pretendRunNum = (hasFEBHole) ? FIRST_RUN_AFTER_HOLE : LAST_RUN_BEFORE_HOLE; 
  }


  // do the selecton and overlap removal
  sc = m_PreparationTool->execute(pretendRunNum);
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Preparation Failed - selection ");
    return sc;
  }

  // // do the selecton and overlap removal
  // sc = m_CrackPreparationTool->execute(pretendRunNum);
  // if ( sc.isFailure() ) {
  //   ATH_MSG_ERROR("Preparation Failed - crack selection ");
  //   return sc;
  // }

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
  //const PhotonContainer *crackPhotons = m_CrackPreparationTool->selectedPhotons();
  const ElectronContainer *electrons = m_OverlapRemovalTool2->finalStateElectrons();
  // const ElectronContainer *crackElectrons = m_CrackPreparationTool->selectedElectrons();

  const Analysis::MuonContainer *muons = m_PreparationTool->selectedMuons();

  // const JetCollection *allJets =  m_PreparationTool->selectedJets();

  const JetCollection *jets = m_OverlapRemovalTool2->finalStateJets();


  ATH_MSG_DEBUG("Got the containers");

  // jet cleaning
  if (!m_isMC) {
    for (JetCollection::const_iterator jet = jets->begin();
	 jet != jets->end();
	 jet++) {
      
      ATH_MSG_DEBUG("Looking at jet with pt = " << (*jet)->pt() << ", eta = " << (*jet)->eta() << ", phi = " << (*jet)->phi());
      if (!m_JetCleaningTool->passCleaningCuts(*jet, JetIDCriteria::LooseBad)) {
	return StatusCode::SUCCESS; // reject event
      }
    }
  }
  numEventsCut[3] += weight;
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
 
  numEventsCut[4] += weight;
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

  numEventsCut[5] += weight;
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

  numEventsCut[6] += weight;
  ATH_MSG_DEBUG("Passed vertex");


  // moun cleaning
  for (Analysis::MuonContainer::const_iterator mu = muons->begin();
       mu != muons->end();
       mu++) {
    
    const Trk::MeasuredPerigee* newMeasPerigee =
      m_trackToVertexTool->perigeeAtVertex(*((*mu)->track()), vxContainer->at(0)->recVertex().position());
    const double dz = newMeasPerigee->parameters()[Trk::z0];
    const double dd = newMeasPerigee->parameters()[Trk::d0];
    ATH_MSG_DEBUG("dZ = " << dz << ", dd = " << dd);
    if (dz >= 1.0 || dd >= 0.2) {
      return StatusCode::SUCCESS; // reject event
    }      
  }
  numEventsCut[7] += weight;
  ATH_MSG_DEBUG("Passed muon rejection");


  // loop over photons
  int numPhPass = 0; // this is per event
  int numConvPhPass = 0; // this is per event
  Analysis::Photon *leadingPh = 0;
  Analysis::Photon *secondPh = 0;
  
  double leadingPhPt = 0;
  double secondPhPt = 0;

  ATH_MSG_DEBUG("Before overlap removal photons size at input = " << photonsBeforeOverlapRemoval->size());
  ATH_MSG_DEBUG("Overlap-removed photons size at input = " << photons->size());

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

    ATH_MSG_DEBUG("Original photon pt = " << (*ph)->pt() << ", corrected = " << pt); 

    
    numPhPass++;
    if ((*ph)->conversion()) numConvPhPass++;
    ATH_MSG_DEBUG("Found photon with pt = " << pt << " and etaBE2 = " << (*ph)->cluster()->etaBE(2));
    
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

  if (numPhPass < 2 || leadingPhPt < m_leadPhotonPtCut) {
    return StatusCode::SUCCESS;
  }

  numEventsCut[8] += weight;
  ATH_MSG_DEBUG("Passed photons");


  //ATH_MSG_DEBUG("finished photon");


  // DEAL WITH ELECTRONS
  int numElPass = 0; // this is per event
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

    ATH_MSG_DEBUG("Original electron pt = " << (*el)->pt() << ", corrected = " << pt); 
    
    numElPass++;
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
  

  // lets correct the MET
  double met_eta4p5=0;
  double etMiss_eta4p5_etx=0;
  double etMiss_eta4p5_ety=0;
  //Regions for lochad topo
  const MissingEtRegions* caloReg = met->getRegions();
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
  
  const double met_eta4p5_muon = hypot(etMiss_eta4p5_etx_muon, etMiss_eta4p5_ety_muon);


  int numJets = 0;

  // Count number of jets
  for (JetCollection::const_iterator jet = jets->begin();
       jet != jets->end();
       jet++) {

    if ((*jet)->eta() < 2.5) {
      numJets++;
    }

    if (m_doSmartVeto) {
      bool eventFails = false;
      if(m_isMC) {
	if (hasFEBHole) {
	  eventFails = m_fakeMetEstimator.isBadEmul((*jet)->pt(),(*jet)->eta(),(*jet)->phi(),
						    etMiss_eta4p5_etx_muon,etMiss_eta4p5_ety_muon,
						    (*jet)->getMoment("BCH_CORR_JET"),
						    (*jet)->getMoment("BCH_CORR_CELL"),
						    (*jet)->getMoment("BCH_CORR_DOTX"));
	} else {
	  eventFails = m_fakeMetEstimatorEmulNoHole.isBadEmul((*jet)->pt(),(*jet)->eta(),(*jet)->phi(),
							      etMiss_eta4p5_etx_muon,etMiss_eta4p5_ety_muon,
							      (*jet)->getMoment("BCH_CORR_JET"),
							      (*jet)->getMoment("BCH_CORR_CELL"),
							      (*jet)->getMoment("BCH_CORR_DOTX"));
	}
      } else {
	eventFails = m_fakeMetEstimator.isBad((*jet)->pt(),(*jet)->getMoment("BCH_CORR_JET"),
					      (*jet)->getMoment("BCH_CORR_CELL"),
					      (*jet)->getMoment("BCH_CORR_DOTX"),
					      (*jet)->phi(),
					      etMiss_eta4p5_etx_muon,etMiss_eta4p5_ety_muon);
      }
      if (eventFails) {
	return StatusCode::SUCCESS;
      }
      
    }

  }

  ATH_MSG_DEBUG("Passed smart veto");
  numEventsCut[9] += weight;

  if (met_eta4p5_muon > 125*GeV) {
    numEventsCut[10] += weight;
  }

  if (met_eta4p5_muon > 100*GeV) {
    numEventsCut[11] += weight;
  }

  if (met_eta4p5_muon > 75*GeV) {
    numEventsCut[12] += weight;
  }

  if (met_eta4p5_muon > 150*GeV) {
    numEventsCut[13] += weight;
  }

  // event accepted, so let's make plots

  // if (met_eta4p5 > 125*GeV) {
  // let's print out run, lb, and event numbers,...
  ATH_MSG_INFO("Selected: " << runNum << " " << lbNum << " " << evNum << " " << numPhPass << " " << numElPass << " " 
	       << muons->size() << " " << met_eta4p5_muon/GeV);

  m_histograms["ph_eta1"]->Fill(leadingPh->eta(), weight);
  m_histograms["ph_pt1"]->Fill(leadingPhPt/GeV, weight);

  accFFUnc.AddObject(leadingPhPt, leadingPh->cluster()->etaBE(2), leadingPh->conversion(), weight);

  if (fabs(leadingPh->cluster()->eta()) < 1.45) {
    if (leadingPh->conversion()) {
      m_histograms["ph_ptB_conv"]->Fill(leadingPhPt/GeV, weight);
      accUnc.AddObject(leadingPhPt, true, true, weight);
    } else {
      m_histograms["ph_ptB_unconv"]->Fill(leadingPhPt/GeV, weight);
      accUnc.AddObject(leadingPhPt, true, false, weight);
    }
  } else {
    if (leadingPh->conversion()) {
      m_histograms["ph_ptEC_conv"]->Fill(leadingPhPt/GeV, weight);
      accUnc.AddObject(leadingPhPt, false, true, weight);
    } else {
      m_histograms["ph_ptEC_unconv"]->Fill(leadingPhPt/GeV, weight);
      accUnc.AddObject(leadingPhPt, false, false, weight);
    }
  }    

  m_histograms["ph_eta2"]->Fill(secondPh->eta(), weight);
  m_histograms["ph_pt2"]->Fill(secondPhPt/GeV, weight);

  if (fabs(secondPh->cluster()->eta()) < 1.45) {
    if (secondPh->conversion()) {
      m_histograms["ph_ptB_conv"]->Fill(secondPhPt/GeV, weight);
      accUnc.AddObject(secondPhPt, true, true, weight);
    } else {
      m_histograms["ph_ptB_unconv"]->Fill(secondPhPt/GeV, weight);
      accUnc.AddObject(secondPhPt, true, false, weight);
    }
  } else {
    if (secondPh->conversion()) {
      m_histograms["ph_ptEC_conv"]->Fill(secondPhPt/GeV, weight);
      accUnc.AddObject(secondPhPt, false, true, weight);
    } else {
      m_histograms["ph_ptEC_unconv"]->Fill(secondPhPt/GeV, weight);
      accUnc.AddObject(secondPhPt, false, false, weight);
    }
  }    

  m_histograms["numPh"]->Fill(numPhPass, weight);
  m_histograms["ph_numConv"]->Fill(numConvPhPass, weight);

  
  // ATH_MSG_DEBUG("filled photon plots");
  if (leadingEl) {
    m_histograms["el_eta1"]->Fill(leadingEl->eta(), weight);
    m_histograms["el_pt1"]->Fill(leadingElPt/GeV, weight);
  }
  if (secondEl) {
    m_histograms["el_eta2"]->Fill(secondEl->eta(), weight);
    m_histograms["el_pt2"]->Fill(secondElPt/GeV, weight);
  }
  m_histograms["numEl"]->Fill(numElPass, weight);
  //ATH_MSG_DEBUG("filled electron plots");


  if (numElPass >= 2) {
    const double minv = P4Helpers::invMass(leadingEl, secondEl);
    m_histograms["el_minv"]->Fill(minv/GeV, weight);
  }

  m_histograms["numJets"]->Fill(numJets, weight);

  // } // end of if on MET
  m_histograms["metWoMuonCorr"]->Fill(met_eta4p5/GeV, weight);
  m_histograms["metExtendedWoMuonCorr"]->Fill(met_eta4p5/GeV, weight);
  switch(numJets) {
  case 0:
    m_histograms["met0JWoMuonCorr"]->Fill(met_eta4p5/GeV, weight);
    break;
  case 1:
    m_histograms["met1JWoMuonCorr"]->Fill(met_eta4p5/GeV, weight);
    break;
  case 2:
    m_histograms["met2JWoMuonCorr"]->Fill(met_eta4p5/GeV, weight);
    break;
  case 3:
    m_histograms["met3JWoMuonCorr"]->Fill(met_eta4p5/GeV, weight);
    break;
  default:
    m_histograms["met4JWoMuonCorr"]->Fill(met_eta4p5/GeV, weight);
    break;
  }

  m_histograms["metWMuonCorr"]->Fill(met_eta4p5_muon/GeV, weight);
  m_histograms["metExtendedWMuonCorr"]->Fill(met_eta4p5_muon/GeV, weight);
  switch(numJets) {
  case 0:
    m_histograms["met0JWMuonCorr"]->Fill(met_eta4p5_muon/GeV, weight);
    break;
  case 1:
    m_histograms["met1JWMuonCorr"]->Fill(met_eta4p5_muon/GeV, weight);
    break;
  case 2:
    m_histograms["met2JWMuonCorr"]->Fill(met_eta4p5_muon/GeV, weight);
    break;
  case 3:
    m_histograms["met3JWMuonCorr"]->Fill(met_eta4p5_muon/GeV, weight);
    break;
  default:
    m_histograms["met4JWMuonCorr"]->Fill(met_eta4p5_muon/GeV, weight);
    break;
  }


  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode SignalGammaGamma::finalize() {
    
    ATH_MSG_INFO ("finalize()");
    // initialize cut flow table
    ATH_MSG_INFO("Cut Flow Table");
    ATH_MSG_INFO("--------------");

    for (int i = 0; i < NUM_CUTS; i++) {
      ATH_MSG_INFO("After cut " << i << ": " << numEventsCut[i] << " events");
    }
    ATH_MSG_INFO("--------------");
    ATH_MSG_INFO("Average material error: " << accUnc.Uncert());
    ATH_MSG_INFO("Average material error using sum of squares: " << accUnc.Uncert2());
    ATH_MSG_INFO("Average FF error: " << accFFUnc.Uncert());
    ATH_MSG_INFO("Average FF error using sum of squares: " << accFFUnc.Uncert2());

    return StatusCode::SUCCESS;
}
