#include "gmsbAnalysis/SignalGammaGamma.h"
#include "gmsbAnalysis/JetID.h"

#include "TH1.h"

#include "EventInfo/EventInfo.h"
#include "EventInfo/EventID.h"

#include "egammaEvent/ElectronContainer.h"
#include "egammaEvent/Electron.h"
#include "egammaEvent/PhotonContainer.h"
#include "egammaEvent/Photon.h"
#include "egammaEvent/egammaPIDdefs.h"

#include "muonEvent/MuonContainer.h"

#include "JetEvent/JetCollection.h"
#include "JetUtils/JetCaloHelper.h"
#include "JetUtils/JetCaloQualityUtils.h"

#include "MissingETEvent/MissingET.h"

#include "VxVertex/VxContainer.h"

#include "ITrackToVertex/ITrackToVertex.h"

/////////////////////////////////////////////////////////////////////////////
SignalGammaGamma::SignalGammaGamma(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator),
  m_trackToVertexTool("Reco::TrackToVertex")
{
  declareProperty("HistFileName", m_histFileName = "SignalGammaGamma");

  declareProperty("LeadingPhotonPtCut", m_leadPhotonPtCut = 30.0*GeV);

  //declareProperty("METContainerName", m_METContainerName = "MET_LocHadTopo");
  declareProperty("METContainerName", m_METContainerName = "MET_RefFinal");
 
  // Name of the primary vertex candidates
  declareProperty("PrimaryVertexCandidates",
		  m_vxCandidatesName="VxPrimaryCandidate",
		  "Name of the primary vertex candidates");

  declareProperty("PreparationTool",     m_PreparationTool);
  declareProperty("CrackPreparationTool", m_CrackPreparationTool);
  declareProperty("OverlapRemovalTool1",  m_OverlapRemovalTool1);
  declareProperty("OverlapRemovalTool2",  m_OverlapRemovalTool2);

  // Tool for track extrapolation to vertex
  declareProperty("trackToVertexTool", m_trackToVertexTool,
		  "Tool for track extrapolation to vertex");


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

  /// histogram location
  sc = service("THistSvc", m_thistSvc);
  if(sc.isFailure()) {
    ATH_MSG_ERROR("Unable to retrieve pointer to THistSvc");
    return sc;
  }

  m_histograms["ph_eta1"] = new TH1F("ph_eta1","Psuedorapidity of the leading photons;#eta_{reco}", 100, -3,3);
  m_histograms["ph_pt1"] = new TH1F("ph_pt1","Transvers momentum of the leading photons;#p_{T} [GeV]", 250, 0, 250);
  m_histograms["ph_eta2"] = new TH1F("ph_eta2","Psuedorapidity of the second photons;#eta_{reco}", 100, -3,3);
  m_histograms["ph_pt2"] = new TH1F("ph_pt2","Transvers momentum of the second photons;#p_{T} [GeV]", 250, 0, 250);

  m_histograms["el_eta1"] = new TH1F("el_eta1","Psuedorapidity of the leading electrons;#eta_{reco}", 100, -3,3);
  m_histograms["el_pt1"] = new TH1F("el_pt1","Transvers momentum of the leading electrons;#p_{T} [GeV]", 250, 0, 250);
  m_histograms["el_eta2"] = new TH1F("el_eta2","Psuedorapidity of the second electrons;#eta_{reco}", 100, -3,3);
  m_histograms["el_pt2"] = new TH1F("el_pt2","Transvers momentum of the second electrons;#p_{T} [GeV]", 250, 0, 250);

  m_histograms["el_minv"] = new TH1F("el_minv", "The invariante mass of the two leading electrons;M_{inv} [GeV]", 120, 0, 120);

  m_histograms["numPh"] = new TH1F("numPh", "The number of photons that pass cuts;N_{electrons}", 9, -0.5, 8.5);
  m_histograms["numEl"] = new TH1F("numEl", "The number of electrons that pass cuts;N_{electrons}", 9, -0.5, 8.5);
  m_histograms["numJets"] = new TH1F("numJets", "The number of jets that pass cuts;N_{jets}", 9, -0.5, 8.5);

  // MET
  m_histograms["met"] = new TH1F("met", "The MET distribution;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met0J"] = new TH1F("met0J", "The MET distribution of events with zero jets;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met1J"] = new TH1F("met1J", "The MET distribution of events with one jet;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met2J"] = new TH1F("met2J", "The MET distribution of events with two jets;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met3J"] = new TH1F("met3J", "The MET distribution of events with three jets;Etmiss [GeV]", 250, 0, 250);
  m_histograms["met4J"] = new TH1F("met4J", "The MET distribution of events with four jets;Etmiss [GeV]", 250, 0, 250);

  m_histograms["metExtended"] = new TH1F("metExtended", "The MET distribution;Etmiss [GeV]", 250, 0, 1250);


  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta1" , m_histograms["ph_eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt1" , m_histograms["ph_pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta2" , m_histograms["ph_eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt2" , m_histograms["ph_pt2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/numPh" , m_histograms["numPh"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta1" , m_histograms["el_eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt1" , m_histograms["el_pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta2" , m_histograms["el_eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt2" , m_histograms["el_pt2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/minv" , m_histograms["el_minv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/numEl" , m_histograms["numEl"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Jets/numJets" , m_histograms["numJets"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met" , m_histograms["met"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met0J" , m_histograms["met0J"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met1J" , m_histograms["met1J"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met2J" , m_histograms["met2J"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met3J" , m_histograms["met3J"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met4J" , m_histograms["met4J"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/metExtended" , m_histograms["metExtended"]).ignore();

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
    ATH_MSG_ERROR("No continer "<< m_METContainerName <<" container found in TDS");
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

  const PhotonContainer *photonsBeforeOverlapRemoval = m_PreparationTool->selectedPhotons();
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

    ATH_MSG_DEBUG("Looking at jet with pt = " << (*jet)->pt() << ", eta = " << (*jet)->eta() << ", phi = " << (*jet)->phi());
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


  // loop over crack electrons
  for (ElectronContainer::const_iterator ph = crackElectrons->begin();
       ph != crackElectrons->end();
       ph++) {
    
    return StatusCode::SUCCESS; // reject event
  }

  numEventsCut[3] += weight;
  ATH_MSG_DEBUG("Passed crack electron");

  //ATH_MSG_DEBUG("finished crack electron");

  // loop over crack photons
  for (PhotonContainer::const_iterator ph = crackPhotons->begin();
       ph != crackPhotons->end();
       ph++) {
    
    return StatusCode::SUCCESS; // reject event
  }

  numEventsCut[4] += weight;
  ATH_MSG_DEBUG("Passed crack photon");

  //ATH_MSG_DEBUG("finished crack photon");
  
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
  numEventsCut[5] += weight;
  ATH_MSG_DEBUG("Passed muon rejection");


  // loop over photons
  int numPhPass = 0; // this is per event
  Analysis::Photon *leadingPh = 0;
  Analysis::Photon *secondPh = 0;
  
  double leadingPhPt = 0;
  double secondPhPt = 0;

  ATH_MSG_DEBUG("Before overlap removal photons size at input = " << photonsBeforeOverlapRemoval->size());
  ATH_MSG_DEBUG("Overlap-removed photons size at input = " << photons->size());

  for (PhotonContainer::const_iterator ph  = photons->begin();
       ph != photons->end();
       ph++) {
    
    const double pt = (*ph)->pt();

    
    numPhPass++;
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

  numEventsCut[6] += weight;
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

    const double pt = (*el)->pt();
    
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
  

  //ATH_MSG_DEBUG("finished electron");

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

  if (met->et() > 125*GeV) {
    numEventsCut[7] += weight;
  }

  // event accepted, so let's make plots

  // let's print out run, lb, and event numbers,...
  ATH_MSG_INFO("Selected: " << runNum << " " << lbNum << " " << evNum << " " << numPhPass << " " << numElPass << " - " << met->et()/GeV);

  m_histograms["ph_eta1"]->Fill(leadingPh->eta(), weight);
  m_histograms["ph_pt1"]->Fill(leadingPhPt/GeV, weight);
  m_histograms["ph_eta2"]->Fill(secondPh->eta(), weight);
  m_histograms["ph_pt2"]->Fill(secondPhPt/GeV, weight);
  m_histograms["numPh"]->Fill(numPhPass, weight);
  
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
  m_histograms["met"]->Fill(met->et()/GeV, weight);
  m_histograms["metExtended"]->Fill(met->et()/GeV, weight);
  switch(numJets) {
  case 0:
    m_histograms["met0J"]->Fill(met->et()/GeV, weight);
    break;
  case 1:
    m_histograms["met1J"]->Fill(met->et()/GeV, weight);
    break;
  case 2:
    m_histograms["met2J"]->Fill(met->et()/GeV, weight);
    break;
  case 3:
    m_histograms["met3J"]->Fill(met->et()/GeV, weight);
    break;
  default:
    m_histograms["met4J"]->Fill(met->et()/GeV, weight);
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

    return StatusCode::SUCCESS;
}


bool SignalGammaGamma::isBad(const Jet* jet) const {
  int SamplingMax=CaloSampling::Unknown;
  return JetID::isBad(JetID::LooseBad,jet->getMoment("LArQuality"),jet->getMoment("n90"),
		      JetCaloHelper::jetEMFraction(jet),JetCaloQualityUtils::hecF(jet),jet->getMoment("Timing"),
		      JetCaloQualityUtils::fracSamplingMax(jet,SamplingMax),jet->eta(P4SignalState::JETEMSCALE));
}
