#include "gmsbAnalysis/BackgroundModelEE.h"

#include "TH1.h"

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

}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::initialize(){

  ATH_MSG_DEBUG("initialize()");
  
  /// histogram location
  StatusCode sc = service("THistSvc", m_thistSvc);
  if(sc.isFailure()) {
    ATH_MSG_ERROR("Unable to retrieve pointer to THistSvc");
    return sc;
  }
	
  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::execute() 
{
  ATH_MSG_DEBUG("execute");
  
  const JetCollection* jetColl = 0;
  StatusCode sc = evtStore()->retrieve( jetColl, m_JetContainerName);
  if( sc.isFailure()  ||  !jetColl ) {
    ATH_MSG_ERROR("No Jet Collection  "<< m_JetContainerName);
    return StatusCode::RECOVERABLE;
  }
  
  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::finalize() {
    
    ATH_MSG_INFO ("finalize()");
    
    return StatusCode::SUCCESS;
}
