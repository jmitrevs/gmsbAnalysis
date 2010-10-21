#ifndef GMSBANALYSIS_BACKGROUNDMODELEE_H
#define GMSBANALYSIS_BACKGROUNDMODELEE_H

#include "AthenaBaseComps/AthAlgorithm.h"
/////////////////////////////////////////////////////////////////////////////
class BackgroundModelEE:public AthAlgorithm {
    public:
    BackgroundModelEE (const std::string& name, ISvcLocator* pSvcLocator);
    StatusCode initialize();
    StatusCode execute();
    StatusCode finalize();
};

#endif // GMSBANALYSIS_BACKGROUNDMODELEE_H
