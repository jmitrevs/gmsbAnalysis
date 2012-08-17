#include "gmsbAnalysis/CutFlowHelper.h"

#include "GeneratorObjects/McEventCollection.h"
#include "HepMC/GenEvent.h"

#include "TH1.h"

/////////////////////////////////////////////////////////////////////////////
CutFlowHelper::CutFlowHelper(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator)
{
  declareProperty("HistFileName", m_histName = "/SignalGammaLepton/Global/CutFlow");
  declareProperty("isMC", m_isMC = false);
  // Name of the McEventCollection Container
  declareProperty("McEventContainerName",
		  m_McEventContainerName="GEN_AOD",
		  "Name of the McEventCollection container");

}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode CutFlowHelper::initialize(){

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
StatusCode CutFlowHelper::execute() 
{
  ATH_MSG_DEBUG("execute");

  StatusCode sc = StatusCode::SUCCESS;

  float weight = 1.0;

  if (m_isMC) {
    
    const McEventCollection * aMcEventContainer;
    sc = evtStore()->retrieve(aMcEventContainer, m_McEventContainerName);
    
    if(sc.isSuccess()) {
      ATH_MSG_DEBUG("Found aMcEventContainer, m_McEventContainerName = " << m_McEventContainerName);
      const HepMC::GenEvent * aGenEvent = *(aMcEventContainer->begin());
      const HepMC::WeightContainer& weightContainer = aGenEvent->weights();
      
      unsigned int Size = weightContainer.size();
      if(Size > 0) weight = weightContainer[0];
    } else {
      ATH_MSG_WARNING("did not find aMcEventContainer, m_McEventContainerName = " << m_McEventContainerName);
    }

  }

  TH1 *hCutFlow;
  sc = m_thistSvc->getHist(m_histName, hCutFlow);
  if ( sc.isFailure() ) {
    ATH_MSG_ERROR("Can't get handle on the cut flow histogram");
    return sc;
  }

  hCutFlow->Fill(0.0, weight);

  setFilterPassed(true);

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode CutFlowHelper::finalize() {
    
    ATH_MSG_DEBUG("finalize()");

    return StatusCode::SUCCESS;
}
