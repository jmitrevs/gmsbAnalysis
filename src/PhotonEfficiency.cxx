#include "gmsbAnalysis/PhotonEfficiency.h"

#include "TH1.h"

#include "EventInfo/EventInfo.h"
#include "EventInfo/EventID.h"

#include "egammaEvent/ElectronContainer.h"
#include "egammaEvent/Electron.h"
#include "egammaEvent/PhotonContainer.h"
#include "egammaEvent/Photon.h"
#include "egammaEvent/egammaPIDdefs.h"

#include "McParticleEvent/TruthParticleContainer.h"


/////////////////////////////////////////////////////////////////////////////
PhotonEfficiency::PhotonEfficiency(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator)
{
  declareProperty("HistFileName", m_histFileName = "PhotonEfficiency");


}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonEfficiency::initialize(){

  ATH_MSG_DEBUG("initialize()");
 

  /// histogram location
  sc = service("THistSvc", m_thistSvc);
  if(sc.isFailure()) {
    ATH_MSG_ERROR("Unable to retrieve pointer to THistSvc");
    return sc;
  }

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

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonEfficiency::execute() 
{
  ATH_MSG_DEBUG("execute");


  double weight = 1.0;


  /** get the MC truth particle AOD container from StoreGate */
  const TruthParticleContainer*  mcpartTES = 0;
  StatusCode sc=m_storeGate->retrieve( mcpartTES, m_truthParticleContainerName);
  if( sc.isFailure()  ||  !mcpartTES ) {
    ATH_MSG_ERROR("could not retrieve MC truth container");
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

  const HepMC::GenEvent *ge=mcpartTES->genEvent();

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
      for (HepMC::GenVertex::particles_in_const_iterator init = pvtx->particles_in_const_begin();
	   init != pvtx->particles_in_const_end();
	   init++) {
	mLog << MSG::INFO;
	mLog << std::setw(7) << std::left <<  m_pdg->GetParticle((*init)->pdg_id())->GetName();
      }
      mLog << " ->\t";
      
      
      PrintDecayTreeAnnotated(mLog, pvtx);
    }

  }

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonEfficiency::finalize() {
    
    ATH_MSG_DEBUG ("finalize()");
    return StatusCode::SUCCESS;
}
