 
# Set up the reading of a file:
from glob import glob

#FNAME = glob('/home/jmitrevs/workarea/mc12_8TeV.110101.AcerMCPythia_P2011CCTEQ6L1_singletop_tchan_l.evgen.EVNT.e1731_tid01147138_00/*')

FNAME = glob('/home/jmitrevs/workarea/AtlasProduction-17.2.11.7/workarea_Whizard_tchanPlus_alt/EVNT*pool.root')
#FNAME = glob('/home/jmitrevs/workarea/AtlasProduction-17.2.11.7/workarea_Whizard_tchanMinus_alt/EVNT*pool.root')
#FNAME = glob('/home/jmitrevs/workarea/AtlasProduction-17.2.11.7/workarea_Whizard_tchanPlusTau_alt/EVNT*pool.root')
#FNAME = glob('/home/jmitrevs/workarea/AtlasProduction-17.2.11.7/workarea_Whizard_tchanMinusTau_alt/EVNT*pool.root')



include( "AthenaPython/iread_file.py" )
 

# Full job is a list of algorithms
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()


from gmsbTools.gmsbToolsConf import TruthStudies
truthStudies = TruthStudies(name = "TruthStudies",
			    McEventCollection = "GEN_EVENT",
                            PrintDecayTree = False,
                            UseAnnotated = False,
                            DumpEntireTree = True,
                            Ptcut = 8*GeV,
                            doMInv = False,
                            OutputLevel = DEBUG
                            )
ToolSvc += truthStudies
print truthStudies

from gmsbAnalysis.gmsbAnalysisConf import TruthPlots
testAlg = TruthPlots(name = "TruthPlots")

#testAlg.OutputLevel = DEBUG
testAlg.OutputLevel = INFO

# Add example to Reader
topSequence += testAlg
print testAlg

#--------------------------------------------------------------
# Add Dictionary for writing out in PoolDPDs
#--------------------------------------------------------------
#AthenaSealSvc = Service( "AthenaSealSvc" )
#include( "AthenaSealSvc/AthenaSealSvc_joboptions.py" )
#include ( "InsituEvent/InsituEventDict_joboptions.py" )

#--------------------------------------------------------------
# Event related parameters
#--------------------------------------------------------------

#==============================================================
#==============================================================
# setup TTree registration Service
# save ROOT histograms and Tuple
from GaudiSvc.GaudiSvcConf import THistSvc
ServiceMgr += THistSvc()
ServiceMgr.THistSvc.Output = ["TruthPlots DATAFILE='TruthPlots.root' OPT='RECREATE'"]


# Do some additional tweaking:
from AthenaCommon.AppMgr import theApp
theApp.EvtMax = 1
ServiceMgr.MessageSvc.OutputLevel = INFO
ServiceMgr.MessageSvc.defaultLimit = 1000000
