#include "gmsbAnalysis/BackgroundModelEE.h"
#include "gmsbAnalysis/SignalGammaGamma.h"
#include "gmsbAnalysis/TriggerStudies.h"
#include "gmsbAnalysis/PhotonEfficiency.h"
#include "GaudiKernel/DeclareFactoryEntries.h"

DECLARE_ALGORITHM_FACTORY( BackgroundModelEE )
DECLARE_ALGORITHM_FACTORY( SignalGammaGamma )
DECLARE_ALGORITHM_FACTORY( TriggerStudies )
DECLARE_ALGORITHM_FACTORY( PhotonEfficiency )

DECLARE_FACTORY_ENTRIES(gmsbAnalysis) {
  DECLARE_ALGORITHM( BackgroundModelEE )
  DECLARE_ALGORITHM( SignalGammaGamma )
  DECLARE_ALGORITHM( TriggerStudies )
  DECLARE_ALGORITHM( PhotonEfficiency )
}
