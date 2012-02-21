#--------------------------------------------------------------
# Templated Parameters
#--------------------------------------------------------------

from glob import glob
#InputList = glob('/data3/jmitrevs/mcskims/mc10_7TeV.115038.Pythia_photos_diphotons25.merge.AOD.e574_s933_s946_r1831_r1700*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/mc10_7TeV.115038.Pythia_photos_diphotons25.merge.AOD.e574_s933_s946_r1831_r1700*/*1.pool.root.8')
#InputList = glob('/data3/jmitrevs/dataskims/gg_rel16/user.*periodH*/*.pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/mc10*Wpluslepgammagamma*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/sps8/D2AOD_GMSBgg2.pool.root')
#InputList = glob('/data3/jmitrevs/mcskims/rel_15/user.jmitrevs.20101120.76.mc09_7TeV.115038.Pythia_photos_diphotons25.ANALY_RALPP/*pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/user.jmitrevs.*.mc09_7TeV.10765*.AlpgenJimmyZee*/*pool.root*')
#InputList = glob('/data3/jmitrevs/AtlasProduction-16.0.2.5/run/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc10_7TeV.139433.SPS8_160_herwigpp_susy.merge.AOD.e818_s933_s946_r2302_r2300_tid422579_00/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc10_7TeV*GGM_Bino_1000_300*_r2300*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc10_7TeV*GGM_Bino800_400*_r2300*/*pool.root*')
#InputList = glob('/data3/jmitrevs/suspect_data/wino_600_500/*pool.root*')
#InputList = glob('/data3/jmitrevs/suspect_data/wino_600_200/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.106046.PythiaZee_no_filter.merge.AOD.e815_s1272_s1274_r2730_r2700_tid519072_00/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.144716.GGM_gl_wino_1500_300_gfilter_herwigpp_susy.merge.AOD.e1004_s1372_s1370_r3043_r2993*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.14*.GGM_gl_wino_700_680_gfilter_herwigpp_susy.merge.AOD.e1004_s1372_s1370_r3043_r2993*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.14*.GGM_gl_wino_600_500_unf_herwigpp_susy.merge.AOD.*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.14*.GGM_gl_wino_600_200_unf_herwigpp_susy.merge.AOD.*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.14*.GGM_gl_wino_600_500_gfilter_herwigpp_susy.merge.AOD.*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.14*.GGM_gl_wino_600_200_gfilter_herwigpp_susy.merge.AOD.e1004_s1372_s1370_r3043_r2993*/*pool.root*')
#InputList = glob('/data3/jmitrevs/suspect_data/wino_600_500_ucsc/*pool.root*')
InputList = glob('/data3/jmitrevs/mc11_7TeV.152627.GGM_gl_wino_900_200_newgfilter_herwigpp_susy.merge.AOD*/*pool.root*')

from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
athenaCommonFlags.FilesInput = InputList
#athenaCommonFlags.SkipEvents=2
athenaCommonFlags.EvtMax=-1
#athenaCommonFlags.EvtMax=100


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

rec.UserAlgs.set_Value_and_Lock("SignalGammaMuon_simple.py")
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

#### jOs from Thijs for spacepoints from ESDs:
#from AthenaCommon.BeamFlags import jobproperties
#from InDetRecExample.InDetJobProperties import InDetFlags
#jobproperties.InDetJobProperties.Enabled.set_Value_and_Lock(True)
#InDetFlags.preProcessing.set_Value_and_Lock(True)
#InDetFlags.doSpacePointFormation.set_Value_and_Lock(True)

# main jobOption - must always be included
include ("RecExCommon/RecExCommon_topOptions.py")
