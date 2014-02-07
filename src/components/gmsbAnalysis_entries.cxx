#include "gmsbAnalysis/BackgroundModelEE.h"
#include "gmsbAnalysis/SignalGammaGamma.h"
#include "gmsbAnalysis/SignalGammaLepton.h"
#include "gmsbAnalysis/TriggerStudies.h"
#include "gmsbAnalysis/PhotonEfficiency.h"
#include "gmsbAnalysis/PhotonIso.h"
#include "gmsbAnalysis/CutFlowHelper.h"
#include "gmsbAnalysis/TruthPlots.h"
#include "GaudiKernel/DeclareFactoryEntries.h"

DECLARE_ALGORITHM_FACTORY( BackgroundModelEE )
DECLARE_ALGORITHM_FACTORY( SignalGammaGamma )
DECLARE_ALGORITHM_FACTORY( SignalGammaLepton )
DECLARE_ALGORITHM_FACTORY( TriggerStudies )
DECLARE_ALGORITHM_FACTORY( PhotonEfficiency )
DECLARE_ALGORITHM_FACTORY( PhotonIso )
DECLARE_ALGORITHM_FACTORY( CutFlowHelper )
DECLARE_ALGORITHM_FACTORY( TruthPlots )

DECLARE_FACTORY_ENTRIES(gmsbAnalysis) {
  DECLARE_ALGORITHM( BackgroundModelEE )
  DECLARE_ALGORITHM( SignalGammaGamma )
  DECLARE_ALGORITHM( SignalGammaLepton )
  DECLARE_ALGORITHM( TriggerStudies )
  DECLARE_ALGORITHM( PhotonEfficiency )
  DECLARE_ALGORITHM( PhotonIso )
  DECLARE_ALGORITHM( CutFlowHelper )
  DECLARE_ALGORITHM( TruthPlots )
}
