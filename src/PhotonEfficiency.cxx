#include "gmsbAnalysis/PhotonEfficiency.h"

#include "TH1.h"

#include "EventInfo/EventInfo.h"
#include "EventInfo/EventID.h"

#include "egammaEvent/ElectronContainer.h"
#include "egammaEvent/Electron.h"
#include "egammaEvent/PhotonContainer.h"
#include "egammaEvent/Photon.h"
#include "egammaEvent/egammaPIDdefs.h"
#include "egammaEvent/EMShower.h"

#include "McParticleEvent/TruthParticleContainer.h"
#include "FourMomUtils/P4Helpers.h"
#include "GeneratorObjects/McEventCollection.h"

#include "PhotonAnalysisUtils/IPAUcaloIsolationTool.h"

/////////////////////////////////////////////////////////////////////////////
PhotonEfficiency::PhotonEfficiency(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator),
  m_PAUcaloIsolationTool(0)
{
  declareProperty("McParticleContainer", m_truthParticleContainerName = "SpclMC");
  declareProperty("McEventCollection", m_mcEventCollectionName = "TruthEvent");
  declareProperty("PhotonContainerName", m_photonContainerName = "PhotonAODCollection");
  declareProperty("HistFileName", m_histFileName = "PhotonEfficiency");
  declareProperty("PrintDecayTree", m_printDecayTree = true);

  declareProperty("DeltaR", m_deltaR = 0.4);

  declareProperty("pT", m_pT = 20*GeV);

  // for the OQ
  declareProperty("OQRunNum", m_OQRunNum = 161730);
  declareProperty("PAUcaloIsolationTool", m_PAUcaloIsolationTool);

}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonEfficiency::initialize(){

  ATH_MSG_DEBUG("initialize()");
 
  /// histogram location
  StatusCode sc = service("THistSvc", m_thistSvc);
  if(sc.isFailure()) {
    ATH_MSG_ERROR("Unable to retrieve pointer to THistSvc");
    return sc;
  }

  if(!m_PAUcaloIsolationTool.empty()) {
    if(m_PAUcaloIsolationTool.retrieve().isFailure()) {
      ATH_MSG_ERROR("Failed to retrieve " << m_PAUcaloIsolationTool);
      return StatusCode::FAILURE; // why success?
    }
    else {
      ATH_MSG_DEBUG("Retrieved PAUcaloIsolationTool " << m_PAUcaloIsolationTool); 
    }
  }
  m_histograms["ph_eta_truth"] = new TH1F("ph_eta_truth","Psuedorapidity of the truth photons;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_truth"] = new TH1F("ph_pt_truth","Transverse momentum of the truth photons;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_cont"] = new TH1F("ph_eta_cont","Psuedorapidity of the container photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_cont"] = new TH1F("ph_pt_cont","Transverse momentum of the container photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_cont_iso"] = new TH1F("ph_eta_cont_iso","Psuedorapidity of the cont photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_cont_iso"] = new TH1F("ph_pt_cont_iso","Transverse momentum of the cont photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_cont_isodp"] = new TH1F("ph_eta_cont_isodp","Psuedorapidity of the cont photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_cont_isodp"] = new TH1F("ph_pt_cont_isodp","Transverse momentum of the cont photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_cont_unconv"] = new TH1F("ph_eta_cont_unconv","Psuedorapidity of the container photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_cont_unconv"] = new TH1F("ph_pt_cont_unconv","Transverse momentum of the container photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_cont_conv1"] = new TH1F("ph_eta_cont_conv1","Psuedorapidity of the container photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_cont_conv1"] = new TH1F("ph_pt_cont_conv1","Transverse momentum of the container photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_cont_conv2"] = new TH1F("ph_eta_cont_conv2","Psuedorapidity of the container photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_cont_conv2"] = new TH1F("ph_pt_cont_conv2","Transverse momentum of the container photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_loose"] = new TH1F("ph_eta_loose","Psuedorapidity of the loose photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_loose"] = new TH1F("ph_pt_loose","Transverse momentum of the loose photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_loose_iso"] = new TH1F("ph_eta_loose_iso","Psuedorapidity of the loose photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_loose_iso"] = new TH1F("ph_pt_loose_iso","Transverse momentum of the loose photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_loose_isodp"] = new TH1F("ph_eta_loose_isodp","Psuedorapidity of the loose photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_loose_isodp"] = new TH1F("ph_pt_loose_isodp","Transverse momentum of the loose photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);
  m_histograms["ph_eta_loose_unconv"] = new TH1F("ph_eta_loose_unconv","Psuedorapidity of the loose photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_loose_unconv"] = new TH1F("ph_pt_loose_unconv","Transverse momentum of the loose photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_loose_conv1"] = new TH1F("ph_eta_loose_conv1","Psuedorapidity of the loose photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_loose_conv1"] = new TH1F("ph_pt_loose_conv1","Transverse momentum of the loose photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_loose_conv2"] = new TH1F("ph_eta_loose_conv2","Psuedorapidity of the loose photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_loose_conv2"] = new TH1F("ph_pt_loose_conv2","Transverse momentum of the loose photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_tight"] = new TH1F("ph_eta_tight","Psuedorapidity of the tight photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_tight"] = new TH1F("ph_pt_tight","Transverse momentum of the tight photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_tight_iso"] = new TH1F("ph_eta_tight_iso","Psuedorapidity of the tight photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_tight_iso"] = new TH1F("ph_pt_tight_iso","Transverse momentum of the tight photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_tight_isodp"] = new TH1F("ph_eta_tight_isodp","Psuedorapidity of the tight photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_tight_isodp"] = new TH1F("ph_pt_tight_isodp","Transverse momentum of the tight photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_tight_unconv"] = new TH1F("ph_eta_tight_unconv","Psuedorapidity of the tight photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_tight_unconv"] = new TH1F("ph_pt_tight_unconv","Transverse momentum of the tight photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_tight_conv1"] = new TH1F("ph_eta_tight_conv1","Psuedorapidity of the tight photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_tight_conv1"] = new TH1F("ph_pt_tight_conv1","Transverse momentum of the tight photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_histograms["ph_eta_tight_conv2"] = new TH1F("ph_eta_tight_conv2","Psuedorapidity of the tight photons matched to truth;#eta_{reco}", 120, -3, 3);
  m_histograms["ph_pt_tight_conv2"] = new TH1F("ph_pt_tight_conv2","Transverse momentum of the tight photons matched to truth;#p_{T} [GeV]", 1000, 0, 1000);

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_truth" , m_histograms["ph_eta_truth"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_truth" , m_histograms["ph_pt_truth"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_cont" , m_histograms["ph_eta_cont"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_cont" , m_histograms["ph_pt_cont"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_cont_iso" , m_histograms["ph_eta_cont_iso"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_cont_iso" , m_histograms["ph_pt_cont_iso"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_cont_isodp" , m_histograms["ph_eta_cont_isodp"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_cont_isodp" , m_histograms["ph_pt_cont_isodp"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_cont_unconv" , m_histograms["ph_eta_cont_unconv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_cont_unconv" , m_histograms["ph_pt_cont_unconv"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_cont_conv1" , m_histograms["ph_eta_cont_conv1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_cont_conv1" , m_histograms["ph_pt_cont_conv1"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_cont_conv2" , m_histograms["ph_eta_cont_conv2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_cont_conv2" , m_histograms["ph_pt_cont_conv2"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_loose" , m_histograms["ph_eta_loose"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_loose" , m_histograms["ph_pt_loose"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_loose_iso" , m_histograms["ph_eta_loose_iso"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_loose_iso" , m_histograms["ph_pt_loose_iso"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_loose_isodp" , m_histograms["ph_eta_loose_isodp"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_loose_isodp" , m_histograms["ph_pt_loose_isodp"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_loose_unconv" , m_histograms["ph_eta_loose_unconv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_loose_unconv" , m_histograms["ph_pt_loose_unconv"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_loose_conv1" , m_histograms["ph_eta_loose_conv1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_loose_conv1" , m_histograms["ph_pt_loose_conv1"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_loose_conv2" , m_histograms["ph_eta_loose_conv2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_loose_conv2" , m_histograms["ph_pt_loose_conv2"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_tight" , m_histograms["ph_eta_tight"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_tight" , m_histograms["ph_pt_tight"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_tight_iso" , m_histograms["ph_eta_tight_iso"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_tight_iso" , m_histograms["ph_pt_tight_iso"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_tight_isodp" , m_histograms["ph_eta_tight_isodp"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_tight_isodp" , m_histograms["ph_pt_tight_isodp"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_tight_unconv" , m_histograms["ph_eta_tight_unconv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_tight_unconv" , m_histograms["ph_pt_tight_unconv"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_tight_conv1" , m_histograms["ph_eta_tight_conv1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_tight_conv1" , m_histograms["ph_pt_tight_conv1"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/eta_tight_conv2" , m_histograms["ph_eta_tight_conv2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Photon/pt_tight_conv2" , m_histograms["ph_pt_tight_conv2"]).ignore();


  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonEfficiency::execute() 
{
  ATH_MSG_DEBUG("execute");


  m_weight = 1.0;

  StatusCode sc = StatusCode::SUCCESS;
  
  const HepMC::GenEvent *ge = 0;

  /** get the MC truth particle AOD or ESD container from StoreGate */
  const McEventCollection *mcEventCol = 0;
  if (evtStore()->contains<McEventCollection>(m_mcEventCollectionName)) {
    sc=evtStore()->retrieve( mcEventCol, m_mcEventCollectionName);
    if( sc.isFailure()  ||  !mcEventCol) {
      ATH_MSG_ERROR("could not retrieve MC event container");
      return StatusCode::RECOVERABLE;
    }
    ATH_MSG_DEBUG("McEventCollection found with name " <<  m_mcEventCollectionName);
    ge = mcEventCol->at(0);
  }
  
  if (!ge) {
    const TruthParticleContainer*  mcpartTES = 0;
    if (evtStore()->contains<TruthParticleContainer>(m_truthParticleContainerName)) {
      sc=evtStore()->retrieve( mcpartTES, m_truthParticleContainerName);
      if( sc.isFailure()  ||  !mcpartTES ) {
	ATH_MSG_ERROR("could not retrieve MC truth container");
	return StatusCode::RECOVERABLE;
      }
      ATH_MSG_DEBUG("McEventCollection found with name " <<  m_mcEventCollectionName);
      ge=mcpartTES->genEvent();
    }
  }


  /** get the MC truth particle AOD container from StoreGate */
  m_photons = 0;
  sc=evtStore()->retrieve( m_photons, m_photonContainerName);
  if( sc.isFailure()  ||  !m_photons ) {
    ATH_MSG_ERROR("could not retrieve photons container");
    return StatusCode::RECOVERABLE;
  }

  const EventInfo*  evtInfo = 0;
  sc = evtStore()->retrieve(evtInfo);
  if(sc.isFailure() || !evtInfo) {
    ATH_MSG_ERROR("could not retrieve event info");
    return StatusCode::RECOVERABLE;
  }

  const unsigned runNum = evtInfo->event_ID()->run_number();
  //const unsigned lbNum = evtInfo->event_ID()->lumi_block();
  //const unsigned evNum = evtInfo->event_ID()->event_number();



  //mLog <<MSG::DEBUG << "ge = " << (unsigned int) ge << endreq;

  const HepMC::GenVertex *pvtx = NULL;

  if (ge) {
    pvtx = ge->signal_process_vertex();
    // mLog <<MSG::DEBUG << "pvtx from signal_process_vertex = " << (unsigned int) pvtx << endreq;

    if (!pvtx) {
      pvtx = getMCHardInteraction(ge);
      // mLog <<MSG::DEBUG << "pvtx from getMCHardInteraction = " << (unsigned int) pvtx << endreq;
    }
    
    if (pvtx) {
      if (m_printDecayTree) {
	for (HepMC::GenVertex::particles_in_const_iterator init = pvtx->particles_in_const_begin();
	     init != pvtx->particles_in_const_end();
	     init++) {
	  msg(MSG::INFO) << std::setw(7) << std::left <<  m_pdg.GetParticle((*init)->pdg_id())->GetName();
	}
	msg(MSG::INFO) << " ->\t";
	
	
	PrintDecayTreeAnnotated(pvtx);
      }
    }
    
    DumpEntireTree(ge);
  }
  
  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonEfficiency::finalize() {
    
    ATH_MSG_DEBUG ("finalize()");
    return StatusCode::SUCCESS;
}

// This is how the hard interaction is gotten
// for now it's a heuristic and probably doesn't work in most cases
HepMC::GenVertex* PhotonEfficiency::getMCHardInteraction(const HepMC::GenEvent *const ge) const
{
  for (int i = -1; i > -20; --i) {
    HepMC::GenVertex* vtx = ge->barcode_to_vertex(i);
    if (vtx && vtx->particles_in_size() == 2) {
      return vtx;
    }
  }
  return NULL;
}

// used recursively
// prints the decay products of one vertex, calling itself to to
// further decay of SUSY particles, t, W, Z, higgses, (gamma? not now).
// Doesn't continue into Geant particles 
void PhotonEfficiency::PrintDecayTree(const HepMC::GenVertex *vtx, int extraSpaces)
{
  std::vector<const HepMC::GenVertex *> decayVertices;

  for (HepMC::GenVertex::particles_in_const_iterator outit = vtx->particles_out_const_begin();
       outit != vtx->particles_out_const_end();
       outit++) {
    if (StatusGood((*outit)->status())) {
      msg(MSG::INFO) << std::setw(11) << std::left << m_pdg.GetParticle((*outit)->pdg_id())->GetName();
      const HepMC::GenVertex *nextVertex = FindNextVertex(*outit);
      if (nextVertex) {
	decayVertices.push_back(FindNextVertex(*outit));
      } else if ((*outit)->pdg_id() == 22) {
	CalcPhotonEfficiency((*outit)->momentum());
      }
    }
  }
  msg(MSG::INFO) << endreq;
  for (int i = decayVertices.size(); i > 0; --i) {
    int index = i-1;
    if (decayVertices.at(index) != NULL) {
      msg(MSG::INFO) << "                 \t";
      for (int j = 0; j < index+extraSpaces; j++) {
	msg(MSG::INFO) << "                ";
      }
      PrintDecayTree(decayVertices.at(index), index+extraSpaces);
    }
  }
}

// used recursively
// prints the decay products of one vertex, calling itself to to
// further decay of SUSY particles, t, W, Z, higgses, (gamma? not now).
// Doesn't continue into Geant particles 
void PhotonEfficiency::PrintDecayTreeAnnotated(const HepMC::GenVertex *vtx, int extraSpaces) const
{
  std::vector<const HepMC::GenVertex *> decayVertices;
  
  //std::cout << "Working on vertex with barcode: " << vtx->barcode() << std::endl;

  for (HepMC::GenVertex::particles_in_const_iterator outit = vtx->particles_out_const_begin();
       outit != vtx->particles_out_const_end();
       outit++) {
    //    if (StatusGood((*outit)->status())) {
    if (1) {

      HepMC::FourVector p = (*outit)->momentum();
      //msg(MSG::INFO) << std::setw(4) << std::right << round(p.perp()/GeV) << " ";
      msg(MSG::INFO) << std::setw(4) << std::right << (*outit)->status() << " ";
      msg(MSG::INFO) << std::setw(11) << std::left << m_pdg.GetParticle((*outit)->pdg_id())->GetName();
      decayVertices.push_back(FindNextVertex(*outit));
    }
  }
  // msg(MSG::INFO) << "\t vertex = " << vtx->barcode();
  msg(MSG::INFO) << endreq;
  for (int i = decayVertices.size(); i > 0; --i) {
    int index = i-1;
    if (decayVertices.at(index) != NULL) {
      msg(MSG::INFO) << "                 \t";
      for (int j = 0; j < index+extraSpaces; j++) {
	msg(MSG::INFO) << "                ";
      }
      PrintDecayTreeAnnotated(decayVertices.at(index), index+extraSpaces);
    }
  }
}

const HepMC::GenVertex *PhotonEfficiency::FindNextVertex(const HepMC::GenParticle *pcl) const
{
  if (pcl->barcode() > 200000) return NULL;

  int pid = abs(pcl->pdg_id());

  if ((pid > 22 && pid < 38) || 
      (pid == 6) ||
      (pid > 1000000 && pid < 1000040) || 
      (pid > 2000000 && pid < 2000016)) { 

    // only show decay products of SUSY and massive guage particles and top

    const HepMC::GenVertex *nextVtx = pcl->end_vertex();
    while (nextVtx != NULL && nextVtx->particles_out_size() == 1) {
      const HepMC::GenParticle *np = *(nextVtx->particles_out_const_begin());
      if (np->barcode() > 200000) return NULL;
      nextVtx = np->end_vertex();
    }
    if (nextVtx && nextVtx->barcode() < -200000) return NULL;
    return nextVtx;
  } else {
    return NULL;
  }
}

void PhotonEfficiency::DumpEntireTree(const HepMC::GenEvent *ge) const
{
  for(HepMC::GenEvent::particle_const_iterator pitr=ge->particles_begin();
      pitr!=ge->particles_end(); ++pitr ){
    if( (*pitr)->status()==1 ) {
      ATH_MSG_INFO("Found particle of type " << m_pdg.GetParticle((*pitr)->pdg_id())->GetName() 
		   << " with pT = " << (*pitr)->momentum().perp());
    }
  }
}

void PhotonEfficiency::CalcPhotonEfficiency(const HepMC::FourVector &p)
{
  
  ATH_MSG_DEBUG("In CalcPhotonEfficiency");

  if (p.perp() < m_pT) return;

  // check OQ
  const double eta = p.eta();
  const double phi = p.phi();
  // const bool badOQ = m_OQ.checkOQClusterPhoton(m_OQRunNum, eta, phi)==3 || 
  //   m_OQ.checkOQClusterPhoton(m_OQRunNum, eta-0.1, phi)==3 || 
  //   m_OQ.checkOQClusterPhoton(m_OQRunNum, eta-0.2, phi)==3 || 
  //   m_OQ.checkOQClusterPhoton(m_OQRunNum, eta+0.1, phi)==3 || 
  //   m_OQ.checkOQClusterPhoton(m_OQRunNum, eta+0.2, phi)==3;
  
  //if (badOQ) return;

  const double abseta = fabs(eta);

  // cut 0.05 more around crack that default since this is phys eta
  const bool isFiducial = abseta < 1.32 || (abseta > 1.57 && abseta < 1.81);

  if (!isFiducial) return;

  m_histograms["ph_pt_truth"]->Fill(p.perp()/GeV, m_weight);
  m_histograms["ph_eta_truth"]->Fill(eta, m_weight);


  double deltaR;
  std::size_t indx = 0;

  ATH_MSG_DEBUG("before closestDeltaR, m_photons = " << m_photons);

  if (P4Helpers::closestDeltaR(eta, phi, *m_photons, indx, deltaR)) {
    if (deltaR < m_deltaR) {

      ATH_MSG_DEBUG("Found match");

      const Analysis::Photon *photon = m_photons->at(indx);

      const EMShower *shower = photon->detail<EMShower>();
      const double etcone20 = shower->etcone20();

      const bool passIso = (etcone20/photon->et() < 0.1);

      double pt_correction_40 = 0;
      double ED_correction_40 = 0;
      double etcone40_corrected = 100*GeV;

      if (!m_PAUcaloIsolationTool.empty()) {
	pt_correction_40 = m_PAUcaloIsolationTool->EtConeCorrectionPt(photon, .40) ;
	ED_correction_40 = m_PAUcaloIsolationTool->EtConeCorrectionJetAreas(photon, .40, 0);

	etcone40_corrected = shower->etcone40() 
	  - pt_correction_40 
	  - ED_correction_40;
      }
      
      const bool passIsoDP = (etcone40_corrected < 3*GeV);

      m_histograms["ph_eta_cont"]->Fill(eta, m_weight);
      if (isFiducial) m_histograms["ph_pt_cont"]->Fill(p.perp()/GeV, m_weight);

      if (passIso) {
	m_histograms["ph_eta_cont_iso"]->Fill(eta, m_weight);
	if (isFiducial) m_histograms["ph_pt_cont_iso"]->Fill(p.perp()/GeV, m_weight);
      }

      if (passIsoDP) {
	m_histograms["ph_eta_cont_isodp"]->Fill(eta, m_weight);
	if (isFiducial) m_histograms["ph_pt_cont_isodp"]->Fill(p.perp()/GeV, m_weight);
      }
      
      if (photon->isPhoton(egammaPID::PhotonLooseAR)) {

	m_histograms["ph_eta_loose"]->Fill(eta, m_weight);
	if (isFiducial) m_histograms["ph_pt_loose"]->Fill(p.perp()/GeV, m_weight);

	if (passIso) {
	  m_histograms["ph_eta_loose_iso"]->Fill(eta, m_weight);
	  if (isFiducial) m_histograms["ph_pt_loose_iso"]->Fill(p.perp()/GeV, m_weight);
	}

	if (passIsoDP) {
	  m_histograms["ph_eta_loose_isodp"]->Fill(eta, m_weight);
	  if (isFiducial) m_histograms["ph_pt_loose_isodp"]->Fill(p.perp()/GeV, m_weight);
	}
	
	if (photon->isPhoton(egammaPID::PhotonTightAR)) {

	  m_histograms["ph_eta_tight"]->Fill(eta, m_weight);
	  if (isFiducial) m_histograms["ph_pt_tight"]->Fill(p.perp()/GeV, m_weight);

	  if (passIso) {
	    m_histograms["ph_eta_tight_iso"]->Fill(eta, m_weight);
	    if (isFiducial) m_histograms["ph_pt_tight_iso"]->Fill(p.perp()/GeV, m_weight);
	  }
	  
	  if (passIsoDP) {
	    m_histograms["ph_eta_tight_isodp"]->Fill(eta, m_weight);
	    if (isFiducial) m_histograms["ph_pt_tight_isodp"]->Fill(p.perp()/GeV, m_weight);
	  }

	}
      }


      const Trk::VxCandidate*  convVtx = photon->conversion();
      if (convVtx) {
	const std::vector<Trk::VxTrackAtVertex*> *trkAtVxPtr = convVtx->vxTrackAtVertex();
	if (trkAtVxPtr->size() == 1) {
	  m_histograms["ph_eta_cont_conv1"]->Fill(eta, m_weight);
	  if (isFiducial) m_histograms["ph_pt_cont_conv1"]->Fill(p.perp()/GeV, m_weight);

	  if (photon->isPhoton(egammaPID::PhotonLooseAR)) {
	    m_histograms["ph_eta_loose_conv1"]->Fill(eta, m_weight);
	    if (isFiducial) m_histograms["ph_pt_loose_conv1"]->Fill(p.perp()/GeV, m_weight);

	    if (photon->isPhoton(egammaPID::PhotonTightAR)) {
	      m_histograms["ph_eta_tight_conv1"]->Fill(eta, m_weight);
	      if (isFiducial) m_histograms["ph_pt_tight_conv1"]->Fill(p.perp()/GeV, m_weight);
	    }
	  }

	} else {
	  m_histograms["ph_eta_cont_conv2"]->Fill(eta, m_weight);
	  if (isFiducial) m_histograms["ph_pt_cont_conv2"]->Fill(p.perp()/GeV, m_weight);

	  if (photon->isPhoton(egammaPID::PhotonLooseAR)) {
	    m_histograms["ph_eta_loose_conv2"]->Fill(eta, m_weight);
	    if (isFiducial) m_histograms["ph_pt_loose_conv2"]->Fill(p.perp()/GeV, m_weight);

	    if (photon->isPhoton(egammaPID::PhotonTightAR)) {
	      m_histograms["ph_eta_tight_conv2"]->Fill(eta, m_weight);
	      if (isFiducial) m_histograms["ph_pt_tight_conv2"]->Fill(p.perp()/GeV, m_weight);
	    }
	  }

	}
      } else {
	m_histograms["ph_eta_cont_unconv"]->Fill(eta, m_weight);
	if (isFiducial) m_histograms["ph_pt_cont_unconv"]->Fill(p.perp()/GeV, m_weight);

	if (photon->isPhoton(egammaPID::PhotonLooseAR)) {
	  m_histograms["ph_eta_loose_unconv"]->Fill(eta, m_weight);
	  if (isFiducial) m_histograms["ph_pt_loose_unconv"]->Fill(p.perp()/GeV, m_weight);
	  
	  if (photon->isPhoton(egammaPID::PhotonTightAR)) {
	    m_histograms["ph_eta_tight_unconv"]->Fill(eta, m_weight);
	    if (isFiducial) m_histograms["ph_pt_tight_unconv"]->Fill(p.perp()/GeV, m_weight);
	  }
	}
	
      }
    }
  }
}

