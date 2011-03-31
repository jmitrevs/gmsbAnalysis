
#--------------------------------------------------------------
# Define your Signal Selection Algorithm and Add Tools
#--------------------------------------------------------------

#---------------------------------------------------------------
# UserDataSvc
#---------------------------------------------------------------
from AthenaServices.TheUserDataSvc import TheUserDataSvc
svcMgr += TheUserDataSvc("UserDataSvc")
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
# seq.GRLTriggerAlg1.TriggerSelection = 'EF_2g15_loose'

# Full job is a list of algorithms
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()

# # add the fudge factors
# include ( "gmsbFudgeFactors/gmsbFudgeFactors.py" )
# topSequence += theGmsbFudgeFactors

from gmsbAnalysis.gmsbAnalysisConf import PhotonIso
testAlg = PhotonIso(name = "PhotonIso",
                    PAUcaloIsolationTool = None)
from AthenaCommon.AppMgr import ToolSvc
#testAlg.OutputLevel = DEBUG

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
ServiceMgr.THistSvc.Output = ["PhotonIso DATAFILE='PhotonIso.root' OPT='RECREATE'"]

