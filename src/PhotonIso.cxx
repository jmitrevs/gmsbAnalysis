#include "gmsbAnalysis/PhotonIso.h"

#include "TH1.h"

#include "EventInfo/EventInfo.h"
#include "EventInfo/EventID.h"

#include "egammaEvent/ElectronContainer.h"
#include "egammaEvent/Electron.h"
#include "egammaEvent/PhotonContainer.h"
#include "egammaEvent/Photon.h"
#include "egammaEvent/egammaPIDdefs.h"
#include "egammaEvent/EMShower.h"

#include "FourMomUtils/P4Helpers.h"

#include "PhotonAnalysisUtils/IPAUcaloIsolationTool.h"

/////////////////////////////////////////////////////////////////////////////
PhotonIso::PhotonIso(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator),
  m_PAUcaloIsolationTool(0)
{
  declareProperty("PhotonContainerName", m_photonContainerName = "PhotonAODCollection");
  declareProperty("HistFileName", m_histFileName = "PhotonIso");

  declareProperty("PtCut", m_ptCut = 20*GeV);
  declareProperty("EtaCut", m_etaCut = 1.81);
  declareProperty("isEMReq", m_isEMReq = egammaPID::PhotonTightAR);
  declareProperty("ApplyVeto", m_applyVeto = false);
  declareProperty("isEMVeto", m_isEMVeto = 0);

  // for the OQ
  declareProperty("OQRunNum", m_OQRunNum = 167521);
  declareProperty("PAUcaloIsolationTool", m_PAUcaloIsolationTool);

}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonIso::initialize(){

  ATH_MSG_DEBUG("initialize()");
 
  // initialize the OQ 
  m_OQ.initialize();

  ATH_MSG_DEBUG("here");
  /// histogram location
  StatusCode sc = service("THistSvc", m_thistSvc);
  if(sc.isFailure()) {
    ATH_MSG_ERROR("Unable to retrieve pointer to THistSvc");
    return sc;
  }

  ATH_MSG_DEBUG("here2");

  if(!m_PAUcaloIsolationTool.empty()) {
    if(m_PAUcaloIsolationTool.retrieve().isFailure()) {
      ATH_MSG_ERROR("Failed to retrieve " << m_PAUcaloIsolationTool);
      return StatusCode::FAILURE; // why success?
    }
    else {
      ATH_MSG_DEBUG("Retrieved PAUcaloIsolationTool " << m_PAUcaloIsolationTool); 
    }
  }

  ATH_MSG_DEBUG("here3");

  m_photon_conv = new std::vector<int>;

  m_photon_et = new std::vector<double>;
  m_photon_e = new std::vector<double>;
  m_photon_eta = new std::vector<double>;
  m_photon_cluseta = new std::vector<double>;
  m_photon_phi = new std::vector<double>;
  
  m_photon_etcone20 = new std::vector<double>;
  m_photon_etcone40 = new std::vector<double>;
  
  // only filled in if tool passed.
  m_photon_etcone20_corrected = new std::vector<double>;
  m_photon_etcone40_corrected = new std::vector<double>;

  ATH_MSG_DEBUG("here4");

  // the TTree
  m_tree = new TTree("PhotonTree","TTree for photon isolation");
  sc = m_thistSvc->regTree(std::string("/")+m_histFileName+"/PhotonTree", m_tree);
  if(sc.isFailure()) {
    ATH_MSG_ERROR("Unable to register tree to THistSvc");
    return sc;
  }


  // first add Event info stuff
  m_tree->Branch("Run",  &m_runNumber,   "Run/I");    // run number
  m_tree->Branch("Event",&m_eventNumber, "Event/I");  // event number
  m_tree->Branch("LumiBlock", &m_lumiBlock,"LumiBlock/I"); // lum block num
  m_tree->Branch("Weight", &m_weight, "Weight/D"); // weight
  m_tree->Branch("PhotonN",  &m_numPhotons, "PhotonN/I");    // num photons

  ATH_MSG_DEBUG("here4a");
  m_tree->Branch("PhotonConv", &m_photon_conv);
  m_tree->Branch("PhotonEt", &m_photon_et);
  m_tree->Branch("PhotonE", &m_photon_e);
  m_tree->Branch("PhotonEta", &m_photon_eta);
  m_tree->Branch("PhotonClusterEta", &m_photon_cluseta);
  ATH_MSG_DEBUG("here4b");
  m_tree->Branch("PhotonPhi", &m_photon_phi);
  m_tree->Branch("PhotonEtcone20", &m_photon_etcone20);
  m_tree->Branch("PhotonEtcone40", &m_photon_etcone40);
  m_tree->Branch("PhotonEtcone20_corr", &m_photon_etcone20_corrected);
  m_tree->Branch("PhotonEtcone40_corr", &m_photon_etcone40_corrected);

  ATH_MSG_DEBUG("here5");
  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonIso::initEvent() 
{
  ATH_MSG_DEBUG("initEvent");

  m_photon_conv->clear(); // 0 unconv, or num tracks

  m_photon_et->clear(); // redundant, but easier
  m_photon_e->clear();
  m_photon_eta->clear();
  m_photon_cluseta->clear();
  m_photon_phi->clear();

  m_photon_etcone20->clear();
  m_photon_etcone40->clear();
  
  // only filled in if tool passed.
  m_photon_etcone20_corrected->clear();
  m_photon_etcone40_corrected->clear();

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonIso::execute() 
{
  ATH_MSG_DEBUG("execute");


  m_weight = 1.0;

  const PhotonContainer* photons = 0;
  StatusCode sc=evtStore()->retrieve( photons, m_photonContainerName);
  if( sc.isFailure()  ||  !photons ) {
    ATH_MSG_ERROR("could not retrieve photons container");
    return StatusCode::RECOVERABLE;
  }

  const EventInfo*  evtInfo = 0;
  sc = evtStore()->retrieve(evtInfo);
  if(sc.isFailure() || !evtInfo) {
    ATH_MSG_ERROR("could not retrieve event info");
    return StatusCode::RECOVERABLE;
  }

  m_runNumber = evtInfo->event_ID()->run_number();
  m_lumiBlock = evtInfo->event_ID()->lumi_block();
  m_eventNumber = evtInfo->event_ID()->event_number();


  // rewiegh for the Z sample and W sample
  switch (m_runNumber) {
  case 107650:
    m_weight = 661.9/303405.0;
    break;
  case 107651:
    m_weight = 133.3/63484.0;
    break;
  case 107652:
    m_weight = 40.3/19496.0; 
    break;
  case 107653:
    m_weight = 11.2/5500.0;
    break;
  case 107654:
    m_weight = 2.7/1500.0;
    break;
  case 107655:
    m_weight = 0.8/500.0;
    break;
  case 107680:
    m_weight = 6913.3/1382306.0;
    break;
  case 107681:
    m_weight = 1293.0/641361.0;
    break;
  case 107682:
    m_weight = 377.1/188956.0;
    break;
  case 107683:
    m_weight = 100.9/50476.0;
    break;
  case 107684:
    m_weight = 25.3/12990.0;
    break;
  case 107685:
    m_weight = 6.9/3497.0;
    break;
  case 118619:
    m_weight = 1.4597e-2/9998 * 35;
    break;
  case 118618:
    m_weight = 4.0558e-2/9998 * 35;
    break;
  case 118617:
    m_weight = 3.9128e-2/9999 * 35;
    break;
  case 118616:
    m_weight = 2.9366e-2/9998 * 35;
    break;
  case 118615:
    m_weight = 3.9201e-2/9994 * 35;
    break;
  }

  m_numPhotons = 0;
  
  for (PhotonContainer::const_iterator ph  = photons->begin();
       ph != photons->end();
       ph++) {
    if ((*ph)->pt() > m_ptCut && 
	fabs((*ph)->cluster()->etaBE(2)) < m_etaCut &&
	(*ph)->isPhoton(m_isEMReq) &&
	(!m_applyVeto || !(*ph)->isPhoton(m_isEMVeto)) &&
	!(m_OQ.checkOQClusterPhoton(m_OQRunNum, (*ph)->cluster()->eta(), 
				    (*ph)->cluster()->phi()) == 3)) {
      m_numPhotons++;
      
      m_photon_e->push_back((*ph)->e());
      m_photon_et->push_back((*ph)->et());
      m_photon_eta->push_back((*ph)->eta());
      m_photon_cluseta->push_back((*ph)->cluster()->eta());
      m_photon_phi->push_back((*ph)->phi());

      const Trk::VxCandidate*  convVtx = (*ph)->conversion();
      if (convVtx) {
	const std::vector<Trk::VxTrackAtVertex*> *trkAtVxPtr = 
	  convVtx->vxTrackAtVertex();
	m_photon_conv->push_back(trkAtVxPtr->size());
      } else {
	m_photon_conv->push_back(0);
      }

      const EMShower *shower = (*ph)->detail<EMShower>();
      m_photon_etcone20->push_back(shower->etcone20());
      m_photon_etcone40->push_back(shower->etcone40());

      double etcone20_corrected = 100*GeV;
      double etcone40_corrected = 100*GeV;


      if (!m_PAUcaloIsolationTool.empty()) {
	const double pt_correction_20 = m_PAUcaloIsolationTool->EtConeCorrectionPt(*ph, .20) ;
	const double ED_correction_20 = m_PAUcaloIsolationTool->EtConeCorrectionJetAreas(*ph, .20, 0);

	etcone20_corrected = shower->etcone20() 
	  - pt_correction_20 
	  - ED_correction_20;

	const double pt_correction_40 = m_PAUcaloIsolationTool->EtConeCorrectionPt(*ph, .40) ;
	const double ED_correction_40 = m_PAUcaloIsolationTool->EtConeCorrectionJetAreas(*ph, .40, 0);

	etcone40_corrected = shower->etcone40() 
	  - pt_correction_40 
	  - ED_correction_40;
      }

      m_photon_etcone20_corrected->push_back(etcone20_corrected);
      m_photon_etcone40_corrected->push_back(etcone40_corrected);

    }
  }	

  ATH_MSG_DEBUG("Number of photons = " << m_numPhotons);

  if (m_numPhotons > 0) {
    m_tree->Fill();  
  }

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode PhotonIso::finalize() {
    
    ATH_MSG_DEBUG ("finalize()");
    return StatusCode::SUCCESS;
}
