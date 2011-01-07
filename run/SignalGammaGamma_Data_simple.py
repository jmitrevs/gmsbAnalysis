
#--------------------------------------------------------------
# Define your Signal Selection Algorithm and Add Tools
#--------------------------------------------------------------

#from TriggerJobOpts.TriggerFlags import TriggerFlags
#TriggerFlags.configurationSourceList = ['ds']

#======================================================================================
# L u m i B l o c k  j o b  o p t i o n s 
#=========================================
# add LumiBlockMetaDataTool to ToolSvc and configure
from LumiBlockComps.LumiBlockCompsConf import LumiBlockMetaDataTool
ToolSvc += LumiBlockMetaDataTool( "LumiBlockMetaDataTool" )
LumiBlockMetaDataTool.calcLumi = False # False by default
LumiBlockMetaDataTool.storeXMLFiles = True
LumiBlockMetaDataTool.applyDQCuts = True 
LumiBlockMetaDataTool.OutputLevel = INFO

# add ToolSvc.LumiBlockMetaDataTool to MetaDataSvc
from EventSelectorAthenaPool.EventSelectorAthenaPoolConf import MetaDataSvc
svcMgr += MetaDataSvc( "MetaDataSvc" )
svcMgr.MetaDataSvc.MetaDataTools += [ ToolSvc.LumiBlockMetaDataTool ]

# Configure the goodrunslist selector tool
from GoodRunsLists.GoodRunsListsConf import *
ToolSvc += GoodRunsListSelectorTool() 
GoodRunsListSelectorTool.OutputLevel = INFO
GoodRunsListSelectorTool.GoodRunsListVec = [ 'susyH.26oct.xml' ]  # <<<<--- Edit this line!
GoodRunsListSelectorTool.PassThrough = False

## This Athena job consists of algorithms that loop over events;
## here, the (default) top sequence is used:
from AthenaCommon.AlgSequence import AlgSequence, AthSequencer
job = AlgSequence()
seq = AthSequencer("AthFilterSeq")

from GoodRunsListsUser.GoodRunsListsUserConf import *
seq += GRLTriggerSelectorAlg('GRLTriggerAlg1')
## In the next line, pick up correct name from inside xml file!
seq.GRLTriggerAlg1.GoodRunsListArray = ['susy_7TeV']
seq.GRLTriggerAlg1.TriggerSelection = 'EF_2g15_loose'

#======================================================================================

# Full job is a list of algorithms
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()

# from MissingET.METRefGetter_new import *

# my_alg4 = make_METRefAlg(_suffix='_EMJES_CellOutEM_PhotonTight')
# my_alg4.jet_JetInputCollectionKey   ='AntiKt4TopoEMJESJets'
# my_alg4.jet_JetPtCut                = 20.0*GeV
# my_alg4.jet_ApplyJetScale           = "Yes"
# my_alg4.jet_UseJetMomentForScale    = True
# my_alg4.jet_JetMomentForScale       = "EMJES"
# my_alg4.jet_RunSoftJetsTool         = False
# my_alg4.jet_SoftJetsPtCut           = 7.0*GeV
# my_alg4.jet_SoftJetsMaxPtCut        = 20.0*GeV
# my_alg4.photon_doPhotonTool         = True
# my_alg4.tau_doTauTool               = False
# my_alg4.jet_SoftJetsCalibType       = "EmScale"
# my_alg4.jet_ApplySoftJetsScale      = "No"
# my_alg4.jet_calibType               ='EmScale'
# my_alg4.ele_calibType               ='RefCalib'
# my_alg4.gamma_calibType             ='EmScale'
# my_alg4.cellout_calibType           ='EmScale'
# my_alg4.tau_calibType               ='EmScale'
# my_alg4.cryo_ApplyCorrection        = "Off"
# my_alg4.muon_algorithm              = "Staco"
# my_alg4.muon_isolationAlg           = "dRJet"
# my_alg4()


# def jetMaker( ):
    
#     def specialMomentTool():
#         from JetCalibTools.SetupJetCalibrators import doJetOriginCorrection
#         from JetCalibTools.MakeCalibSequences import makeCalibSequence
#         calibSeq = makeCalibSequence("JetOriginCorr",
#                                      [ doJetOriginCorrection('AntiKt',0.4,'Topo',numInvBase='EM')] )
        
#         l = getStandardPostProcessTool('Topo',True)
#         # remove JetOriginCorrectionTool and JetCalibrationTool in moment-mode
#         return l[:-3] +l[-2:-1]+ [getJetCalibrationTool( calibSeq, "OriginCorr",True)]

include ( "gmsbTools/gmsbTools_jobOptions.py" )


from gmsbAnalysis.gmsbAnalysisConf import SignalGammaGamma
testAlg = SignalGammaGamma(name = "SignalGammaGamma",
                            OQRunNum = -1,
                            PreparationTool = gmsbPreparationTool,
                            CrackPreparationTool = gmsbCrackPreparationTool,
                            OverlapRemovalTool1 = gmsbOverlapRemovalTool1,
                            OverlapRemovalTool2 = gmsbOverlapRemovalTool2,
                            METContainerName = "MET_RefFinal"
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
ServiceMgr.THistSvc.Output = ["SignalGammaGamma DATAFILE='SignalGammaGamma.root' OPT='RECREATE'"]

