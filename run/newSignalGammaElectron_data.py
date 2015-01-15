# configure athena to read flat n-tuples
import AthenaRootComps.ReadAthenaRoot

#--------------------------------------------------------------
# Templated Parameters
#--------------------------------------------------------------

from glob import glob
#InputList = glob('/data3/jmitrevs/mc12_8TeV.164439.MadGraphPythia_AUET2BCTEQ6L1*/NTUP_SUSY.01183600._000013.root.2')
#InputList = glob('/data3/jmitrevs/mc12_8TeV.164439.MadGraphPythia_AUET2BCTEQ6L1*/*root*')
#InputList = glob('/data3/jmitrevs/mc12_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.NTUP_SUSY.e1727_a188_a171_r3549_p1328*/*root*')
#InputList = glob('/data3/jmitrevs/mc12_8TeV.105200.McAtNloJimmy_CT10_ttbar_LeptonFilter.merge.NTUP_SUSY.e1513_s1499_s1504_r3945_r3549_p1328*/*root*')
#InputList = glob('/data/jmitrevs/input/mc12_8TeV.*GGM_wino_300_egfilter*/*root*')
InputList = glob('/data/jmitrevs/input/data12_8TeV.*NTUP_SUSY*/*root*')
# InputList = ['root://eosatlas//eos/atlas/user/j/jmitrevs/wino_300/NTUP_SUSY.01185684._000001.root.1',
#              'root://eosatlas//eos/atlas/user/j/jmitrevs/wino_300/NTUP_SUSY.01185684._000002.root.1',
#              'root://eosatlas//eos/atlas/user/j/jmitrevs/wino_300/NTUP_SUSY.01185684._000003.root.1']

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

import PyCintex
PyCintex.loadDictionary('egammaEnumsDict')
from ROOT import egammaPID

#if not 'RANDSEED' in dir():
#    RANDSEED = 0

#print "random seed", RANDSEED

gmsbSelectionTool.IsMC = False
gmsbSelectionTool.Atlfast = False
gmsbSelectionTool.SmearMC = True
#gmsbSelectionTool.RandomSeed = RANDSEED
#gmsbSelectionTool.MCEtconeShift = 0.0;
#gmsbSelectionTool.PhotonIsEM = egammaPID.PhotonTight

gmsbFinalSelectionTool.IsMC = False
gmsbFinalSelectionTool.Atlfast = False
gmsbFinalSelectionTool.SmearMC = False
gmsbFinalSelectionTool.PhotonPt = 125*GeV

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

from gmsbAnalysis.gmsbAnalysisConf import SignalGammaLepton
testAlg = SignalGammaLepton(name = "SignalGammaLepton",
                            isMC = False,
                            PrePreparationTool = gmsbPrePreparationTool,
                            PreparationTool = gmsbPreparationTool,
                            FinalSelectionTool = gmsbFinalSelectionTool,
                            OverlapRemovalTool1 = gmsbOverlapRemovalTool1,
                            OverlapRemovalTool2 = gmsbOverlapRemovalTool2,
                            #JetCleaningTool = myJetCleaningTool,
                            applyTrigger = True,
                            NumPhotons = 1,
                            NumElectrons = 1,
                            outputNtuple = True,
                            # doTruthStudies = True,
                            # TruthStudiesTool = truthStudies,
                            # DoEtMissSystematics = False,
                            # DoEtMissMuonSystematics = False,
                            #EtMissSystematicsTool = myEtMissSystematicsTool,
                            #EtMissMuonSystematicsTool = myEtMissMuonSystematicsTool
                            useMETUtility=False
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
ServiceMgr.THistSvc.Output = ["SignalGammaLepton DATAFILE='SignalGammaLepton.root' OPT='RECREATE'"]

