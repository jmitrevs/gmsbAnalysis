#include "gmsbAnalysis/BackgroundModelEE.h"
//#include "GaudiKernel/MsgStream.h"
/////////////////////////////////////////////////////////////////////////////
BackgroundModelEE::BackgroundModelEE(const std::string& name, ISvcLocator* pSvcLocator) :
AthAlgorithm(name, pSvcLocator)
{
  // Properties go here
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::initialize(){

    ATH_MSG_INFO ("initialize()");

    return StatusCode::SUCCESS;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::execute() {

   ATH_MSG_INFO ("Your new package and algorithm are successfully executing");

    return StatusCode::SUCCESS;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode BackgroundModelEE::finalize() {
    
    ATH_MSG_INFO ("finalize()");
    
    return StatusCode::SUCCESS;
}
