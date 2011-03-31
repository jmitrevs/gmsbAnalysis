#--------------------------------------------------------------
# Templated Parameters
#--------------------------------------------------------------

from glob import glob
#InputList = glob('/data3/jmitrevs/mc09_7TeV.106050.PythiaZee_1Lepton.merge.AOD.e468_s765_s767_r1250_r1260_tid129729_00/AOD.129729._000001.pool.root.1')
#InputList = glob('/data3/jmitrevs/data10_7TeV.00155073.physics_L1Calo.merge.DESDM_EGAMMA.r1299_p161_p165_tid143766_00/*')
#InputList = glob('/data3/jmitrevs/mc09_7TeV.114007.SPS8_110_jimmy_susy.merge.AOD.e530_s765_s767_r1302_r1306_tid140030_00/AOD*')
#InputList = glob('../../run/ESD.pool.root')
#InputList = glob('../../run_*/copy_AOD*.pool.root')
#InputList = glob('../../run/AOD.pool.root')
#InputList = glob('/data/jmitrevs/AtlasProduction-15.8.0.2/run/ESD.pool.root')
#InputList = glob('/data3/jmitrevs/AtlasOffline-rel_3/run/ESD.pool.root')
#InputList = glob('/data3/jmitrevs/mc09_7TeV.108085.PythiaPhotonJet_Unbinned7.recon.ESD.e534_s765_s767_r1305_tid137093_00/ESD.137093._000011.pool.root.1')
#InputList = glob('/data3/jmitrevs/dataskims/ee/*/*.pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/mc10*Znunugammagamma*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/mc10_7TeV.*.Pythia_GGM_Bino600_300.merge.AOD.e640_s933_s946_r1831_r1700*/*pool.root*')
InputList = glob('/data3/jmitrevs/isostudy/mc_input/*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/mc10_7TeV.*.Pythia_GGM_Bino800_700.merge.AOD.*_r1831_r2040*/*pool.root*')
#InputList = ['root://castoratlas//castor/cern.ch/user/d/ddamiani/GGM_grid/rel_16/bino_400_200_UEplus/AOD/AOD.merged.bino_400_200_UEplus._000001.pool.root.1']
#InputList = glob('/data3/jmitrevs/mcskims/mc10_7TeV.115038.Pythia_photos_diphotons25.merge.AOD.e574_s933_s946_r1831_r1700*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/mc10_7TeV.115038.Pythia_photos_diphotons25.merge.AOD.e574_s933_s946_r1831_r1700*/*1.pool.root.8')
#InputList = glob('/data3/jmitrevs/dataskims/gg_rel16/user.*periodH*/*.pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/mc10*Wpluslepgammagamma*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/sps8/D2AOD_GMSBgg2.pool.root')
#InputList = glob('/data3/jmitrevs/mcskims/rel_15/user.jmitrevs.20101120.76.mc09_7TeV.115038.Pythia_photos_diphotons25.ANALY_RALPP/*pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/user.jmitrevs.*.mc09_7TeV.10765*.AlpgenJimmyZee*/*pool.root*')
#InputList = glob('/data3/jmitrevs/AtlasProduction-16.0.2.5/run/*pool.root*')

from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
athenaCommonFlags.FilesInput = InputList
#athenaCommonFlags.SkipEvents=2
athenaCommonFlags.EvtMax=-1
#athenaCommonFlags.EvtMax=10


# # use closest DB replica
# from AthenaCommon.AppMgr import ServiceMgr
# from PoolSvc.PoolSvcConf import PoolSvc
# ServiceMgr+=PoolSvc(SortReplicas=True)
# from DBReplicaSvc.DBReplicaSvcConf import DBReplicaSvc
# ServiceMgr+=DBReplicaSvc(UseCOOLSQLite=False)


from RecExConfig.RecFlags import rec

rec.doTrigger.set_Value_and_Lock(False)

#--------------------------------------------------------------
# ANALYSIS
#--------------------------------------------------------------

rec.UserAlgs.set_Value_and_Lock("PhotonIso_simple.py")
#UserExecsList = ["ToolSvc.PhotonProcessingTool.PhotonisEMKey = 'PhotonTight'","ToolSvc.PhotonProcessingTool.ElectronisEMKey = 'ElectronTight'"]
#UserExecsList = ["ToolSvc.PhotonProcessingTool.excludeCrackRegion = False"]
#UserExecsList = ["NtupleDumper.SUSY_ProductionVeto = True","NtupleDumper.SUSY_ProductionTypeAccepted = 2","NtupleDumper.isMC = True"]
#UserExecsList = ["PhotonTrace.FillSPHist = True"]
#rec.UserExecs.set_Value_and_Lock(UserExecsList)

#--------------------------------------------------------------
# General Configuration
#--------------------------------------------------------------

OutputLevel = INFO

rec.readRDO.set_Value_and_Lock(False)
rec.readESD.set_Value_and_Lock(False)
rec.readAOD.set_Value_and_Lock(True)

rec.doAOD.set_Value_and_Lock(False)
rec.doAODCaloCells.set_Value_and_Lock(False)
rec.doCBNT.set_Value_and_Lock(False)
rec.doESD.set_Value_and_Lock(False)
rec.doHist.set_Value_and_Lock(False)
rec.doWriteAOD.set_Value_and_Lock(False)
rec.doWriteESD.set_Value_and_Lock(False)
rec.doWriteTAG.set_Value_and_Lock(False)
rec.doFileMetaData.set_Value_and_Lock(False)
rec.doJiveXML.set_Value_and_Lock(False)

rec.doPerfMon.set_Value_and_Lock(False)

rec.doApplyAODFix.set_Value_and_Lock(False)

#### jOs from Thijs for spacepoints from ESDs:
#from AthenaCommon.BeamFlags import jobproperties
#from InDetRecExample.InDetJobProperties import InDetFlags
#jobproperties.InDetJobProperties.Enabled.set_Value_and_Lock(True)
#InDetFlags.preProcessing.set_Value_and_Lock(True)
#InDetFlags.doSpacePointFormation.set_Value_and_Lock(True)

# main jobOption - must always be included
include ("RecExCommon/RecExCommon_topOptions.py")
