#include "gmsbAnalysis/BackgroundModelEE.h"
#include "gmsbAnalysis/SignalGammaGamma.h"
#include "GaudiKernel/DeclareFactoryEntries.h"

DECLARE_ALGORITHM_FACTORY( BackgroundModelEE )
DECLARE_ALGORITHM_FACTORY( SignalGammaGamma )

DECLARE_FACTORY_ENTRIES(gmsbAnalysis) {
  DECLARE_ALGORITHM( BackgroundModelEE )
  DECLARE_ALGORITHM( SignalGammaGamma )
}
