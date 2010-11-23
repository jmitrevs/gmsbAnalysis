
#--------------------------------------------------------------
# Define your Signal Selection Algorithm and Add Tools
#--------------------------------------------------------------

# Full job is a list of algorithms
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()

include ( "gmsbTools/gmsbTools_jobOptions.py" )

from ROOT import egammaPID
gmsbSelectionTool.PhotonIsEM = egammaPID.PhotonLoose
gmsbSelectionTool.ElectronPt = 0.0

from gmsbAnalysis.gmsbAnalysisConf import TriggerStudies
testAlg = TriggerStudies(name = "TriggerStudies",
                            OQRunNum = 167521,
                            PreparationTool = gmsbPreparationTool,
                            CrackPreparationTool = gmsbCrackPreparationTool,
                            OverlapRemovalTool1 = gmsbOverlapRemovalTool1,
                            OverlapRemovalTool2 = gmsbOverlapRemovalTool2
                            )
from AthenaCommon.AppMgr import ToolSvc
testAlg.OutputLevel = DEBUG

# Add example to Reader
topSequence += testAlg

#--------------------------------------------------------------
# Add Dictionary for writing out in PoolDPDs
#--------------------------------------------------------------
#AthenaSealSvc = Service( "AthenaSealSvc" )
#include( "AthenaSealSvc/AthenaSealSvc_joboptions.py" )
#include ( "InsituEvent/InsituEventDict_joboptions.py" )

#--------------------------------------------------------------
# Event related parameters
#--------------------------------------------------------------

ServiceMgr.MessageSvc.OutputLevel = WARNING

#==============================================================
#==============================================================
# setup TTree registration Service
# save ROOT histograms and Tuple
from GaudiSvc.GaudiSvcConf import THistSvc
ServiceMgr += THistSvc()
ServiceMgr.THistSvc.Output = ["TriggerStudies DATAFILE='TriggerStudies.root' OPT='RECREATE'"]

