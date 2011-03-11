#include "gmsbAnalysis/BackgroundModelEE.h"
#include "gmsbAnalysis/JetID.h"

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

#include "ITrackToVertex/ITrackToVertex.h"
#include "TH2.h"

/////////////////////////////////////////////////////////////////////////////
BackgroundModelEE::BackgroundModelEE(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator),
  m_trackToVertexTool("Reco::TrackToVertex"),
  m_userdatasvc("UserDataSvc", name)
{
  declareProperty("HistFileName", m_histFileName = "BackgroundModelEE");

  declareProperty("LeadingElPtCut", m_leadElPtCut = 30.0*GeV);

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

  declareProperty("WindowLow", m_windowLow = 80*GeV);
  declareProperty("WindowHigh", m_windowHigh = 100*GeV);

  // Tool for track extrapolation to vertex
  declareProperty("trackToVertexTool", m_trackToVertexTool,
		  "Tool for track extrapolation to vertex");


}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::initialize(){

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

  m_histograms["eta1"] = new TH1F("eta1","Psuedorapidity of the leading electrons;#eta_{reco}", 100, -3,3);
  m_histograms["pt1"] = new TH1F("pt1","Transvers momentum of the leading electrons;p_{T} [GeV]", 250, 0, 250);
  m_histograms["eta2"] = new TH1F("eta2","Psuedorapidity of the second electrons;#eta_{reco}", 100, -3,3);
  m_histograms["pt2"] = new TH1F("pt2","Transvers momentum of the second electrons;p_{T} [GeV]", 250, 0, 250);

  m_histograms["minv"] = new TH1F("minv", "The invariante mass of the two leading electrons;M_{inv} [GeV]", 120, 0, 120);
  m_histograms["numEl"] = new TH1F("numEl", "The number of electrons that pass cuts;N_{electrons}", 9, -0.5, 8.5);
  m_histograms["numJets"] = new TH1F("numJets", "The number of jets that pass cuts;N_{jets}", 9, -0.5, 8.5);

  m_histograms["etcone20"] = new TH1F("etcone20", "etcone20;E_{T}^{leak} [GeV]", 100, 0, 20);
  m_histograms["etcone20vspt"] = new TH2F("etcone20vspt", "etcone20 vs object p_{T};E_{T}^{leak} [GeV];p_{T} [GeV]", 100, 0, 20, 50, 0, 250);

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

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta1" , m_histograms["eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt1" , m_histograms["pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta2" , m_histograms["eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt2" , m_histograms["pt2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/minv" , m_histograms["minv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/numEl" , m_histograms["numEl"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/etcone20" , m_histograms["etcone20"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/etcone20vspt" , m_histograms["etcone20vspt"]).ignore();
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
StatusCode BackgroundModelEE::execute() 
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


  // rewiegh for the Z sample and W sample
  switch (runNum) {

  //   // Z r1831_r1700 
  // case 107650:
  //   weight = 661.9/303405.0;
  //   break;
  // case 107651:
  //   weight = 133.3/63484.0;
  //   break;
  // case 107652:
  //   weight = 40.3/19496.0; 
  //   break;
  // case 107653:
  //   weight = 11.2/5500.0;
  //   break;
  // case 107654:
  //   weight = 2.7/1500.0;
  //   break;
  // case 107655:
  //   weight = 0.8/500.0;
  //   break;

    // Z r1831_r2040
  case 107650:
    weight = 661.9/303348.0;
    break;
  case 107651:
    weight = 133.3/63447.0;
    break;
  case 107652:
    weight = 40.3/19480.0; 
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

  //   // Z r1652_r1700 
  // case 107650:
  //   weight = 661.9/29992.0;
  //   break;
  // case 107651:
  //   weight = 133.3/19995.0;
  //   break;
  // case 107652:
  //   weight = 40.3/19496.0; 
  //   break;
  // case 107653:
  //   weight = 11.2/5500.0;
  //   break;
  // case 107654:
  //   weight = 2.7/1500.0;
  //   break;
  // case 107655:
  //   weight = 0.8/500.0;
  //   break;

  //   // Z r1659_r2040 
  // case 107650:
  //   weight = 661.9/302914.0;
  //   break;
  // case 107651:
  //   weight = 133.3/269957.0;
  //   break;
  // case 107652:
  //   weight = 40.3/19280.0; 
  //   break;
  // case 107653:
  //   weight = 11.2/5500.0;
  //   break;
  // case 107654:
  //   weight = 2.7/21276.0;
  //   break;
  // case 107655:
  //   weight = 0.8/7996.0;
  //   break;


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

  ATH_MSG_DEBUG("About to prepare selection");

  numEventsCut[0] += weight;

  // do the selecton and overlap removal
  sc = m_PreparationTool->execute();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Preparation Failed - selection ");
    return sc;
  }

  // do the selecton and overlap removal
  sc = m_CrackPreparationTool->execute();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Preparation Failed - crack selection ");
    return sc;
  }

  sc = m_OverlapRemovalTool1->execute();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("OverlaPremval 1 Failed");
    return sc;
  }

  sc = m_OverlapRemovalTool2->execute();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("OverlaPremval 1 Failed");
    return sc;
  }

  ATH_MSG_DEBUG("Done preparing selection");

  const PhotonContainer *photons = m_OverlapRemovalTool2->finalStatePhotons();
  const PhotonContainer *crackPhotons = m_CrackPreparationTool->selectedPhotons();
  const ElectronContainer *electrons = m_OverlapRemovalTool2->finalStateElectrons();
  const ElectronContainer *crackElectrons = m_CrackPreparationTool->selectedElectrons();

  const Analysis::MuonContainer *muons = m_PreparationTool->selectedMuons();

  const JetCollection *allJets =  m_PreparationTool->selectedJets();

  const JetCollection *jets = m_OverlapRemovalTool2->finalStateJets();


  ATH_MSG_DEBUG("Got the containers");

  // jet cleaning
  for (JetCollection::const_iterator jet = allJets->begin();
       jet != allJets->end();
       jet++) {

    if (isBad(*jet)) {
      return StatusCode::SUCCESS; // reject event
    }
  }

  numEventsCut[1] += weight;
  ATH_MSG_DEBUG("Passed jet cleaning");

  // check the primary vertex
  if (vxContainer->size() < 2) {
    return StatusCode::SUCCESS; // reject event
  }

  bool foundVx = false;
  for (VxContainer::const_iterator vx = vxContainer->begin();
       vx != vxContainer->end();
       vx++) {
    const std::vector<Trk::VxTrackAtVertex*>* vxtracks = 
      (*vx)->vxTrackAtVertex();

    if (vxtracks->size() > 4) {
      foundVx = true;
      break;
    }
  }
  if (!foundVx) {
    return StatusCode::SUCCESS; // reject event
  }
  numEventsCut[2] += weight;
  ATH_MSG_DEBUG("Passed vertex");

  // veto events if they have a tight photon
  // loop over photons
  for (PhotonContainer::const_iterator ph  = photons->begin();
       ph != photons->end();
       ph++) {

    return StatusCode::SUCCESS; // reject event
  }

  numEventsCut[3] += weight;
  ATH_MSG_DEBUG("Passed photons");

  // loop over crack electrons
  for (ElectronContainer::const_iterator ph = crackElectrons->begin();
       ph != crackElectrons->end();
       ph++) {
    
    return StatusCode::SUCCESS; // reject event
  }

  numEventsCut[4] += weight;
  ATH_MSG_DEBUG("Passed crack electron");

  // loop over crack photons
  for (PhotonContainer::const_iterator ph = crackPhotons->begin();
       ph != crackPhotons->end();
       ph++) {
    
    return StatusCode::SUCCESS; // reject event
  }

  numEventsCut[5] += weight;
  ATH_MSG_DEBUG("Passed crack photon");

  for (Analysis::MuonContainer::const_iterator mu = muons->begin();
       mu != muons->end();
       mu++) {
    
    const Trk::MeasuredPerigee* newMeasPerigee =
      m_trackToVertexTool->perigeeAtVertex(*((*mu)->track()), vxContainer->at(0)->recVertex().position());
    const double dz = newMeasPerigee->parameters()[Trk::z0];
    ATH_MSG_DEBUG("dZ = " << dz);
    if (dz >= 10.0) {
      return StatusCode::SUCCESS; // reject event
    }      
  }
  numEventsCut[6] += weight;
  ATH_MSG_DEBUG("Passed muon rejection");

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
  
  if (numElPass < 2 || leadingElPt < m_leadElPtCut) {
    return StatusCode::SUCCESS; // reject event
  }

  numEventsCut[7] += weight;
  ATH_MSG_DEBUG("Passed electrons");

  int numJets = 0;

  // Count number of jets
  for (JetCollection::const_iterator jet = jets->begin();
       jet != jets->end();
       jet++) {

    if ((*jet)->eta() < 2.5) {
      numJets++;
    }
  }

  ATH_MSG_DEBUG("finished jets");

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



  if (met_eta4p5 > 125*GeV) {
    numEventsCut[8] += weight;
  }

  if (met_eta4p5_muon > 125*GeV) {
    numEventsCut[9] += weight;
  }

  if (met_eta4p5 > 100*GeV) {
    numEventsCut[10] += weight;
  }

  if (met_eta4p5_muon > 100*GeV) {
    numEventsCut[11] += weight;
  }

  if (met_eta4p5 > 75*GeV) {
    numEventsCut[12] += weight;
  }

  if (met_eta4p5_muon > 75*GeV) {
    numEventsCut[13] += weight;
  }

  if (met_eta4p5 > 150*GeV) {
    numEventsCut[14] += weight;
  }

  if (met_eta4p5_muon > 150*GeV) {
    numEventsCut[15] += weight;
  }


  // event accepted, so let's make plots

  m_histograms["eta1"]->Fill(leadingEl->eta(), weight);
  m_histograms["pt1"]->Fill(leadingElPt/GeV, weight);
  m_histograms["eta2"]->Fill(secondEl->eta(), weight);
  m_histograms["pt2"]->Fill(secondElPt/GeV, weight);
  m_histograms["numEl"]->Fill(numElPass, weight);

  const double minv = P4Helpers::invMass(leadingEl, secondEl);
  m_histograms["minv"]->Fill(minv/GeV, weight);
  
  if (minv > m_windowLow && minv < m_windowHigh) {

    // let's do the leakage
    const EMShower* leadingShower = leadingEl->detail<EMShower>();
    if(leadingShower) {
      m_histograms["etcone20"]->Fill(leadingShower->etcone20()/GeV, weight);
      TH2F *etconevspt = (TH2F *) m_histograms["etcone20vspt"];
      etconevspt->Fill(leadingShower->etcone20()/GeV, leadingElPt/GeV, weight);
    }

    // let's do the leakage
    const EMShower* secondShower = secondEl->detail<EMShower>();
    if(secondShower) {
      m_histograms["etcone20"]->Fill(secondShower->etcone20()/GeV, weight);
      TH2F *etconevspt = (TH2F *) m_histograms["etcone20vspt"];
      etconevspt->Fill(secondShower->etcone20()/GeV, secondElPt/GeV, weight);
    }

    m_histograms["numJets"]->Fill(numJets, weight);

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

  }


  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::finalize() {
    
    ATH_MSG_INFO ("finalize()");
    // initialize cut flow table
    ATH_MSG_INFO("Cut Flow Table");
    ATH_MSG_INFO("--------------");

    for (int i = 0; i < NUM_CUTS; i++) {
      ATH_MSG_INFO("After cut " << i << ": " << numEventsCut[i] << " events");
    }
    
    return StatusCode::SUCCESS;
}


bool BackgroundModelEE::isBad(const Jet* jet) const {
  int SamplingMax=CaloSampling::Unknown;
  return JetID::isBad(JetID::LooseBad,jet->getMoment("LArQuality"),jet->getMoment("n90"),
		      JetCaloHelper::jetEMFraction(jet),JetCaloQualityUtils::hecF(jet),jet->getMoment("Timing"),
		      JetCaloQualityUtils::fracSamplingMax(jet,SamplingMax),jet->eta(P4SignalState::JETEMSCALE));
}
