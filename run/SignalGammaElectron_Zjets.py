#--------------------------------------------------------------
# Templated Parameters
#--------------------------------------------------------------

from glob import glob
#InputList = glob('/data3/jmitrevs/dataskims/gg_rel16/user.*periodH*/*.pool.root*')
#InputList = glob('/data3/jmitrevs/mcskims/mc10*Wpluslepgammagamma*/*pool.root*')
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
#InputList = glob('/data3/jmitrevs/mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.AOD.e835_s1272_s1274_r3043_r2993_tid645402_00/*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.152627.GGM_gl_wino_900_200_newgfilter_herwigpp_susy.merge.AOD*/*pool.root*')
InputList = glob('/data3/jmitrevs/mc11_7TeV.*.GGM_gl_wino_600_200_newgfilter_herwigpp_susy.merge.AOD*/*pool.root*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.117421.AlpgenJimmyWgammaNp1_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993*/*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.107681.AlpgenJimmyWenuNp1_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993*/*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.145163.Sherpa_Zeegamma_highpt.merge.AOD.e923_s1310_s1300_r3043_r2993*/*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.107650.AlpgenJimmyZeeNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993*/*')
#InputList = glob('/data3/jmitrevs/mc11_7TeV.117402.Whizard_CTEQL1Jimmy_TTbarPhoton_SM_NoFullHad.merge.AOD.e1086_s1372_s1370_r3043_r2993*/*')

from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
athenaCommonFlags.FilesInput = InputList
##athenaCommonFlags.SkipEvents=34262
##athenaCommonFlags.SkipEvents=47940
#athenaCommonFlags.SkipEvents=50293
#athenaCommonFlags.EvtMax=2
athenaCommonFlags.EvtMax=-1
##athenaCommonFlags.EvtMax=1000

# # use closest DB replica
# from AthenaCommon.AppMgr import ServiceMgr
# from PoolSvc.PoolSvcConf import PoolSvc
# ServiceMgr+=PoolSvc(SortReplicas=True)
# from DBReplicaSvc.DBReplicaSvcConf import DBReplicaSvc
# ServiceMgr+=DBReplicaSvc(UseCOOLSQLite=False)


from RecExConfig.RecFlags import rec

rec.doTrigger.set_Value_and_Lock(True)

#--------------------------------------------------------------
# ANALYSIS
#--------------------------------------------------------------

rec.UserAlgs.set_Value_and_Lock("SignalGammaElectron_Zjets_simple.py")
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

include ("RecExCond/RecExCommon_flags.py")
DetFlags.ID_setOn()
DetFlags.geometry.Calo_setOn()

# import TrigDecisionTool.TrigDecisionToolConf 
# tdt = TrigDecisionTool.TrigDecisionToolConf.Trig__TrigDecisionTool("TrigDecisionTool") 
# ToolSvc += tdt 
# ToolSvc.TrigDecisionTool.Navigation.Dlls = ['TrigTopoEvent'] 

# main jobOption - must always be included
include ("RecExCommon/RecExCommon_topOptions.py")

# if not hasattr(svcMgr, theApp.EventLoop):
#    svcMgr += getattr(CfgMgr, theApp.EventLoop)() 
# evtloop = getattr(svcMgr, theApp.EventLoop)
# evtloop.EventPrintoutInterval = 1
