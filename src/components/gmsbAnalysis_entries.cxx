#include "gmsbAnalysis/SignalGammaLepton.h"
#include "gmsbAnalysis/MetStudies.h"
#include "gmsbAnalysis/Testing.h"
#include "gmsbAnalysis/PhotonEfficiency.h"
#include "gmsbAnalysis/PhotonIso.h"
#include "gmsbAnalysis/CutFlowHelper.h"
#include "GaudiKernel/DeclareFactoryEntries.h"

DECLARE_ALGORITHM_FACTORY( SignalGammaLepton )
DECLARE_ALGORITHM_FACTORY( MetStudies )
DECLARE_ALGORITHM_FACTORY( Testing )
DECLARE_ALGORITHM_FACTORY( PhotonEfficiency )
DECLARE_ALGORITHM_FACTORY( PhotonIso )
DECLARE_ALGORITHM_FACTORY( CutFlowHelper )

DECLARE_FACTORY_ENTRIES(gmsbAnalysis) {
  DECLARE_ALGORITHM( SignalGammaLepton )
  DECLARE_ALGORITHM( MetStudies )
  DECLARE_ALGORITHM( Testing )
  DECLARE_ALGORITHM( PhotonEfficiency )
  DECLARE_ALGORITHM( PhotonIso )
  DECLARE_ALGORITHM( CutFlowHelper )
}
