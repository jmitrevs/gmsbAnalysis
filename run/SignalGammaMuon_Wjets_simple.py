
#--------------------------------------------------------------
# Define your Signal Selection Algorithm and Add Tools
#--------------------------------------------------------------

#---------------------------------------------------------------
# UserDataSvc
#---------------------------------------------------------------
#from AthenaServices.TheUserDataSvc import TheUserDataSvc
#svcMgr += TheUserDataSvc("UserDataSvc")
#svcMgr.UserDataSvc.OutputStream=outStream

# #======================================================================================
# # L u m i B l o c k  j o b  o p t i o n s 
# #=========================================
# # add LumiBlockMetaDataTool to ToolSvc and configure
# from LumiBlockComps.LumiBlockCompsConf import LumiBlockMetaDataTool
# ToolSvc += LumiBlockMetaDataTool( "LumiBlockMetaDataTool" )
# LumiBlockMetaDataTool.calcLumi = False # False by default
# LumiBlockMetaDataTool.storeXMLFiles = True
# LumiBlockMetaDataTool.applyDQCuts = True 
# LumiBlockMetaDataTool.OutputLevel = INFO

# # add ToolSvc.LumiBlockMetaDataTool to MetaDataSvc
# from EventSelectorAthenaPool.EventSelectorAthenaPoolConf import MetaDataSvc
# svcMgr += MetaDataSvc( "MetaDataSvc" )
# svcMgr.MetaDataSvc.MetaDataTools += [ ToolSvc.LumiBlockMetaDataTool ]

# # Configure the goodrunslist selector tool
# from GoodRunsLists.GoodRunsListsConf import *
# ToolSvc += GoodRunsListSelectorTool() 
# GoodRunsListSelectorTool.OutputLevel = INFO
# #GoodRunsListSelectorTool.GoodRunsListVec = [ 'susy_E3toI.xml' ]
# GoodRunsListSelectorTool.PassThrough = True

# ## This Athena job consists of algorithms that loop over events;
# ## here, the (default) top sequence is used:
# from AthenaCommon.AlgSequence import AlgSequence, AthSequencer
# job = AlgSequence()
# seq = AthSequencer("AthFilterSeq")

# from GoodRunsListsUser.GoodRunsListsUserConf import *
# seq += GRLTriggerSelectorAlg('GRLTriggerAlg1')
# ## In the next line, pick up correct name from inside xml file!
# # seq.GRLTriggerAlg1.GoodRunsListArray = ['susy_7TeV']
# seq.GRLTriggerAlg1.TriggerSelection = 'EF_2g20_loose'

# Full job is a list of algorithms
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()

localDataFile = "ilumicalc_histograms_EF_2g20_loose_178044-184169.root"
localMCFile = "mu_mc10b.root"

# ====================================================================
# Load the pileup reweighting algorithm
# ====================================================================
# from PileupReweighting.PileupReweightingConf import PileupReweightingAlg
# topSequence += PileupReweightingAlg( "PileupStream_PileupReweightingAlg",
#                                      OutputLevel      = DEBUG,
#                                      dataROOTFileName = localDataFile,
#                                      dataROOTHistName = "avgintperbx",
#                                      mcROOTFileName   = localMCFile,
#                                      mcROOTHistName   = "mu_mc10b"
#                                      )

# add the fudge factors
include ( "gmsbFudgeFactors/gmsbFudgeFactors.py" )
topSequence += theGmsbFudgeFactors

#theGmsbFudgeFactors.WhichFudgeFactors = 200

# add the selection
include ( "gmsbTools/gmsbTools_jobOptions.py" )

from JetSelectorTools.ConfiguredAthJetCleaningTools import *
myJetCleaningTool = ConfiguredAthJetCleaningTool_VeryLoose("gmsbJetCleaningTool")
ToolSvc += myJetCleaningTool

import PyCintex
PyCintex.loadDictionary('egammaEnumsDict')
from ROOT import egammaPID

#if not 'RANDSEED' in dir():
#    RANDSEED = 0

#print "random seed", RANDSEED

gmsbSelectionTool.IsMC = True
gmsbSelectionTool.SmearMC = True
gmsbSelectionTool.ElectronPt = 25*GeV
gmsbSelectionTool.PhotonPt = 85*GeV
#gmsbSelectionTool.MuonPt = 25*GeV
#gmsbSelectionTool.RandomSeed = RANDSEED
#gmsbSelectionTool.MCEtconeShift = 0.0;
#gmsbSelectionTool.PhotonIsEM = egammaPID.PhotonTight

gmsbFinalSelectionTool.IsMC = True
gmsbFinalSelectionTool.SmearMC = False

from gmsbTools.gmsbToolsConf import TruthStudies
truthStudies = TruthStudies(name = "TruthStudies",
                            PrintDecayTree = False,
                            UseAnnotated = False,
                            DumpEntireTree = False,
                            Ptcut = 40*GeV,
                            doDeltaRLepton = False,
                            OutputLevel = INFO
                            )
ToolSvc += truthStudies
print truthStudies

from gmsbAnalysis.gmsbAnalysisConf import SignalGammaLepton
testAlg = SignalGammaLepton(name = "SignalGammaLepton",
                            isMC = True,
                            PreparationTool = gmsbPreparationTool,
                            FinalSelectionTool = gmsbFinalSelectionTool,
                            OverlapRemovalTool1 = gmsbOverlapRemovalTool1,
                            OverlapRemovalTool2 = gmsbOverlapRemovalTool2,
                            JetCleaningTool = myJetCleaningTool,
                            applyTrigger = False,
                            triggers = "EF_mu18",
                            NumPhotons = 1,
                            NumMuons = 1,
                            outputNtuple = True,
                            doTruthStudies = True,
                            TruthStudiesTool = truthStudies
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

#==============================================================
#==============================================================
# setup TTree registration Service
# save ROOT histograms and Tuple
from GaudiSvc.GaudiSvcConf import THistSvc
ServiceMgr += THistSvc()
ServiceMgr.THistSvc.Output = ["SignalGammaLepton DATAFILE='SignalGammaLepton.root' OPT='RECREATE'"]

