#include "gmsbAnalysis/BackgroundModelEE.h"
#include "gmsbAnalysis/checkOQ.h"

#include "TH1.h"

#include "EventInfo/EventInfo.h"
#include "EventInfo/EventID.h"

#include "egammaEvent/ElectronContainer.h"
#include "egammaEvent/Electron.h"
#include "egammaEvent/PhotonContainer.h"
#include "egammaEvent/Photon.h"
#include "egammaEvent/egammaPIDdefs.h"

#include "JetEvent/JetCollection.h"

#include "MissingETEvent/MissingET.h"

/////////////////////////////////////////////////////////////////////////////
BackgroundModelEE::BackgroundModelEE(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator)
{
  declareProperty("HistFileName", m_histFileName = "BackgroundModelEE");

  /** Electron selection */
  declareProperty("ElectronContainerName", m_ElectronContainerName = "ElectronAODCollection");
  declareProperty("ElectronIsEM", m_electronIsEM = egammaPID::ElectronMedium_WithTrackMatch);

  declareProperty("PhotonContainerName", m_PhotonContainerName = "PhotonAODCollection");
  declareProperty("PhotonIsEM", m_photonIsEM = egammaPID::PhotonTight);

  declareProperty("METContainerName", m_METContainerName = "MET_LocHadTopo");
  declareProperty("JetContainerName", m_JetContainerName = "AntiKt4TopoJets");

  declareProperty("OQRunNum", m_OQRunNum = -1);

  declareProperty("MinPtCrack", m_minPtForCrack = 10.0*GeV);

  declareProperty("AnalysisPreparationTool",     m_analysisPreparationTool);
  declareProperty("AnalysisCrackPreparationTool", m_analysisCrackPreparationTool);
  declareProperty("AnalysisOverlapRemovalTool1",  m_analysisOverlapRemovalTool1);
  declareProperty("AnalysisOverlapRemovalTool2",  m_analysisOverlapRemovalTool2);

}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::initialize(){

  ATH_MSG_DEBUG("initialize()");
 
  StatusCode sc = m_analysisPreparationTool.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on analysis preparation tool");
    return sc;
  }

  StatusCode sc = m_analysisCrackPreparationTool.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on crack preparation tool");
    return sc;
  }

  sc = m_analysisOverlapRemovalTool1.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on first analysis overlap removal tool");
    return sc;
  }

  sc = m_analysisOverlapRemovalTool2.retrieve();
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on secnd analysis overlap removal tool");
    return sc;
  }
 
  /// histogram location
  StatusCode sc = service("THistSvc", m_thistSvc);
  if(sc.isFailure()) {
    ATH_MSG_ERROR("Unable to retrieve pointer to THistSvc");
    return sc;
  }

  m_histograms["eta1"] = new TH1F("eta1","Psuedorapidity of the leading electrons;#eta_{reco}", 100, -3,3);
  m_histograms["pt1"] = new TH1F("pt1","Transvers momentum of the leading electrons;#p_{T} [MeV]", 100, 0*GeV, 250*GeV);
  m_histograms["eta2"] = new TH1F("eta2","Psuedorapidity of the second electrons;#eta_{reco}", 100, -3,3);
  m_histograms["pt2"] = new TH1F("pt2","Transvers momentum of the second electrons;#p_{T} [MeV]", 100, 0*GeV, 250*GeV);

  m_histograms["minv"] = new TH1F("minv", "The invariante mass of the two leading electrons;M_{inv} [MeV]", 120, 0*GeV, 120*GeV);
  m_histograms["numEl"] = new TH1F("numEl", "The number of electrons that pass cuts;N_{electrons}", 9, -0.5, 8.5);
  m_histograms["numJets"] = new TH1F("numJets", "The number of jets that pass cuts;N_{jets}", 9, -0.5, 8.5);

  // MET
  m_histograms["met"] = new TH1F("met", "The MET distribution of Z events;Etmiss [MeV]", 100, 0*GeV, 250*GeV);
  m_histograms["met0J"] = new TH1F("met0J", "The MET distribution of Z events with zero jets;Etmiss [MeV]", 100, 0*GeV, 250*GeV);
  m_histograms["met1J"] = new TH1F("met1J", "The MET distribution of Z events with one jet;Etmiss [MeV]", 100, 0*GeV, 250*GeV);
  m_histograms["met2J"] = new TH1F("met2J", "The MET distribution of Z events with two jets;Etmiss [MeV]", 100, 0*GeV, 250*GeV);
  m_histograms["met3J"] = new TH1F("met3J", "The MET distribution of Z events with three jets;Etmiss [MeV]", 100, 0*GeV, 250*GeV);
  m_histograms["met4J"] = new TH1F("met4J", "The MET distribution of Z events with four jets;Etmiss [MeV]", 100, 0*GeV, 250*GeV);


  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta1" , m_histograms["eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt1" , m_histograms["pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/eta2" , m_histograms["eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/pt2" , m_histograms["pt2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/minv" , m_histograms["minv"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Electron/numEl" , m_histograms["numEl"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/Jets/numJets" , m_histograms["numJets"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met" , m_histograms["met"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met0J" , m_histograms["met0J"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met1J" , m_histograms["met1J"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met2J" , m_histograms["met2J"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met3J" , m_histograms["met3J"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/MET/met4J" , m_histograms["met4J"]).ignore();

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::execute() 
{
  ATH_MSG_DEBUG("execute");


  double weight = 1.0;

  const ElectronContainer* electrons;
  StatusCode sc=evtStore()->retrieve( electrons, m_ElectronContainerName);
  if( sc.isFailure()  ||  !electrons ) {
    ATH_MSG_ERROR("No continer "<< m_ElectronContainerName <<" container found in TDS");
    return StatusCode::FAILURE;
  }

  // ATH_MSG_DEBUG("Photon container name: " << m_PhotonContainerName);

  const PhotonContainer* photons;
  sc=evtStore()->retrieve( photons, m_PhotonContainerName);
  if( sc.isFailure()  ||  !photons ) {
    ATH_MSG_ERROR("No continer "<< m_PhotonContainerName <<" container found in TDS");
    return StatusCode::RECOVERABLE;
  }

  // The missing ET object
  const MissingET* met(0);
  sc = evtStore()->retrieve( met, m_METContainerName );
  if( sc.isFailure()  ||  !met ) {
    ATH_MSG_ERROR("No continer "<< m_METContainerName <<" container found in TDS");
    return StatusCode::RECOVERABLE;
  }
  
  const JetCollection* jets = 0;
  sc = evtStore()->retrieve( jets, m_JetContainerName);
  if( sc.isFailure()  ||  !jets ) {
    ATH_MSG_ERROR("No Jet Collection  "<< m_JetContainerName);
    return StatusCode::RECOVERABLE;
  }
  
  const EventInfo*  evtInfo = 0;
  sc = evtStore()->retrieve(evtInfo);
  if(sc.isFailure() || !evtInfo) {
    ATH_MSG_ERROR("could not retrieve event info");
    return StatusCode::RECOVERABLE;
  }

  const unsigned runNum = evtInfo->event_ID()->run_number();


  if (m_OQRunNum < 0) {
    m_OQRunNum = runNum;
  }

  bool rejectEvent = false;


  // veto events if they have a tight photon

  // loop over photons
  for (PhotonContainer::const_iterator ph  = photons->begin();
       ph != photons->end();
       ph++) {

    if ((*ph)->isPhoton(egammaPID::PhotonTight)) {
      const double pt = (*ph)->pt();

      if (pt > 20*GeV) {
	rejectEvent = true;
	break;
      }
      const double absClusEta = fabs((*ph)->cluster()->eta());

      const bool badOQ = egammaOQ::checkOQClusterPhoton(m_OQRunNum, (*ph)->cluster()->eta(), (*ph)->cluster()->phi())==3;
      const bool isCrack = absClusEta > 1.37 && absClusEta < 1.52; 
      if (pt > m_minPtForCrack && isCrack && !badOQ) {
	rejectEvent = true;
	break;
      }
    }      
  }

  if (rejectEvent) return StatusCode::SUCCESS;

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

    if ((*el)->author(egammaParameters::AuthorElectron) && (*el)->isElectron(egammaPID::ElectronMedium_WithTrackMatch)) {
      numElPass++;
      
      const double pt = (*el)->pt();
      const double absClusEta = fabs((*el)->cluster()->eta());

      const bool badOQ = egammaOQ::checkOQClusterElectron(m_OQRunNum, (*el)->cluster()->eta(), (*el)->cluster()->phi())==3;
      const bool isCrack = absClusEta > 1.37 && absClusEta < 1.52; 

      if (pt > m_minPtForCrack && isCrack && !badOQ) {
	rejectEvent = true;
	break;
      }

      if (pt > leadingElPt) {
	secondEl = leadingEl;
	leadingEl = *el;
	secondElPt = leadingElPt;
	leadingElPt = pt;
      } else if (pt > secondElPt) {
	secondEl = *el;
	secondElPt = pt;
      }


    }
  }

  if (rejectEvent) return StatusCode::SUCCESS;

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::finalize() {
    
    ATH_MSG_INFO ("finalize()");
    
    return StatusCode::SUCCESS;
}
