# configure athena to read flat n-tuples
import AthenaRootComps.ReadAthenaRoot

#--------------------------------------------------------------
# Templated Parameters
#--------------------------------------------------------------

from glob import glob
#InputList = glob('/data3/jmitrevs/mc12_8TeV.164439.MadGraphPythia_AUET2BCTEQ6L1*/NTUP_SUSY.01183600._000013.root.2')
#InputList = glob('/data3/jmitrevs/mc12_8TeV.147806.PowhegPythia8_AU2CT10_Zee.merge.NTUP_SUSY.e1169_s1469_s1470_r3542_r3549_p1181*/*.root*')
InputList = glob('/data3/jmitrevs/mc12_8TeV.147806.PowhegPythia8_AU2CT10_Zee.merge.NTUP_SUSY.e1169_s1469_s1470_r3542_r3549_p13*/*.root*')
#InputList = glob('/data3/jmitrevs/mc12_8TeV.164439.MadGraphPythia_AUET2BCTEQ6L1*/*root*')

svcMgr.EventSelector.InputCollections = InputList

# the n-tuple name in the input files to read data from
svcMgr.EventSelector.TupleName = "susy"

# ==============================================================================
# Set the number of events that you want to process (-1 means all events) or skip.
# Shown is a handy way how you can use command-line options.
# If EVTMAX is not given on the command line, the default -1 (process all events) is used.
# This works for any command line option that you may need; it is a python feature.
# ==============================================================================
if not vars().has_key('EVTMAX'): EVTMAX = -1
theApp.EvtMax = EVTMAX

# getting a handle on the alg sequence
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()


# add the selection
include ( "gmsbTools/gmsbTools_jobOptions.py" )
include ( "gmsbTools/gmsbTools_MET_jobOptions.py" )

import PyCintex
PyCintex.loadDictionary('egammaEnumsDict')
from ROOT import egammaPID

#if not 'RANDSEED' in dir():
#    RANDSEED = 0

#print "random seed", RANDSEED

gmsbSelectionTool.IsMC = True
gmsbSelectionTool.SmearMC = False
gmsbSelectionTool.ApplyFF = False
#gmsbSelectionTool.OutputLevel = DEBUG
#gmsbSelectionTool.RandomSeed = RANDSEED
#gmsbSelectionTool.MCEtconeShift = 0.0;
gmsbSelectionTool.PhotonIsEM = egammaPID.PhotonLoose
gmsbMETSelectionTool.PhotonIsEM = egammaPID.PhotonLoose

gmsbSelectionTool.PhotonIsEM = egammaPID.PhotonLoose
gmsbMETSelectionTool.PhotonIsEM = egammaPID.PhotonLoose

gmsbFinalSelectionTool.IsMC = True
gmsbFinalSelectionTool.SmearMC = False
gmsbFinalSelectionTool.PhotonPt = 25*GeV
gmsbFinalSelectionTool.ElectronPt = 25*GeV
gmsbFinalSelectionTool.DoElectronIsolation = NONE
gmsbFinalSelectionTool.DoMuonIsolation = NONE
gmsbFinalSelectionTool.DoEDPhotonIsolation = False

# from gmsbTools.gmsbToolsConf import TruthStudies
# truthStudies = TruthStudies(name = "TruthStudies",
#                             PrintDecayTree = False,
#                             UseAnnotated = False,
#                             DumpEntireTree = False,
#                             #Ptcut = 8*GeV,
#                             doDeltaRLepton = False,
#                             #OutputLevel = DEBUG
#                             )
# ToolSvc += truthStudies
# print truthStudies

# # add the MET systematics
# include ( "gmsbAnalysis/METSystematics.py" )

from MissingETUtility.MissingETUtilityConf import METUtilityAthD3PDTool
METUtility = METUtilityAthD3PDTool(name = "gmsbMETUtility",
                                   PreparationTool = gmsbMETPreparationTool,
                                   OverlapRemovalTool = gmsbMETOverlapRemovalTool,
                                   FixOverlap = True,
                                   OutputLevel = DEBUG,
                                   )

ToolSvc += METUtility
print METUtility                   

from gmsbAnalysis.gmsbAnalysisConf import MetStudies
testAlg = MetStudies(name = "MetStudies",
                     isMC = True,
                     PreparationTool = gmsbPreparationTool,
                     FinalSelectionTool = gmsbFinalSelectionTool,
                     OverlapRemovalTool1 = gmsbOverlapRemovalTool1,
                     OverlapRemovalTool2 = gmsbOverlapRemovalTool2,
                     #JetCleaningTool = myJetCleaningTool,
                     applyTrigger = True,
                     NumPhotons = 1,
                     NumElectrons = 1,
                     outputNtuple = True,
                     METUtility = METUtility,
                     useMETUtility = False
                     # doTruthStudies = True,
                     # TruthStudiesTool = truthStudies,
                     # DoEtMissSystematics = False,
                     # DoEtMissMuonSystematics = False,
                     #EtMissSystematicsTool = myEtMissSystematicsTool,
                     #EtMissMuonSystematicsTool = myEtMissMuonSystematicsTool
                     )
from AthenaCommon.AppMgr import ToolSvc
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

ServiceMgr.MessageSvc.OutputLevel = WARNING
ServiceMgr.MessageSvc.defaultLimit = 1000000000

#==============================================================
#==============================================================
# setup TTree registration Service
# save ROOT histograms and Tuple
from GaudiSvc.GaudiSvcConf import THistSvc
ServiceMgr += THistSvc()
ServiceMgr.THistSvc.Output = ["MetStudies DATAFILE='MetStudies.root' OPT='RECREATE'"]

