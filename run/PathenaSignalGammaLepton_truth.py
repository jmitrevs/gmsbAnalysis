#! /usr/bin/env python

import os
import commands
import sys
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing
inDS_test = [ 
# 'mc12_8TeV.204731.Sherpa_CT10_enugammaPt80_ckkw15.merge.NTUP_TRUTH.e3140_p1605_tid04400102_00',
# 'mc12_8TeV.204732.Sherpa_CT10_enugammaPt80_ckkw30.merge.NTUP_TRUTH.e3140_p1605_tid04400103_00',
# 'mc12_8TeV.204733.Sherpa_CT10_enugammaPt80_fac025.merge.NTUP_TRUTH.e3140_p1605_tid04400104_00',
# 'mc12_8TeV.204734.Sherpa_CT10_enugammaPt80_fac4.merge.NTUP_TRUTH.e3140_p1605_tid04400105_00',
# 'mc12_8TeV.204735.Sherpa_CT10_enugammaPt80_renorm025.merge.NTUP_TRUTH.e3140_p1605_tid04400106_00',
# 'mc12_8TeV.204736.Sherpa_CT10_enugammaPt80_renorm4.merge.NTUP_TRUTH.e3140_p1605_tid04400107_00',
# 'mc12_8TeV.202336.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_moreFSR.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202335.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_alpsDN.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202332.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_scaleUP.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202337.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_lessFSR.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202334.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_alpsUP.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202333.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_scaleDN.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.177998.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_fixed.merge.NTUP_TRUTH.e2189_p1605',

# 'mc12_8TeV.183497.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto_ckkw15.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183498.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto_ckkw30.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183499.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto_fac025.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183500.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto_fac4.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183501.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto_renorm025.merge.NTUP_TRUTH.e2465_p1605',
# 'mc12_8TeV.183501.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto_renorm025.merge.NTUP_TRUTH.e2648_p1605',
# 'mc12_8TeV.183502.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto_renorm4.merge.NTUP_TRUTH.e2465_p1605',
# 'mc12_8TeV.183502.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto_renorm4.merge.NTUP_TRUTH.e2648_p1605',
# 'mc12_8TeV.183515.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto_ckkw15.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183516.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto_ckkw30.merge.NTUP_TRUTH.e2369_p1605',
# 'mc12_8TeV.183517.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto_fac025.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183518.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto_fac4.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183519.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto_renorm025.merge.NTUP_TRUTH.e2465_p1605',
# 'mc12_8TeV.183519.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto_renorm025.merge.NTUP_TRUTH.e2648_p1605',
# 'mc12_8TeV.183520.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto_renorm4.merge.NTUP_TRUTH.e2465_p1605',
'mc12_8TeV.183520.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto_renorm4.merge.NTUP_TRUTH.e2648_p1605',
# 'mc12_8TeV.183533.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto_ckkw15.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183534.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto_ckkw30.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183535.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto_fac025.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183536.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto_fac4.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183537.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto_renorm025.merge.NTUP_TRUTH.e2465_p1605',
# 'mc12_8TeV.183537.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto_renorm025.merge.NTUP_TRUTH.e2648_p1605',
# 'mc12_8TeV.183538.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto_renorm4.merge.NTUP_TRUTH.e2465_p1605',
# 'mc12_8TeV.183538.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto_renorm4.merge.NTUP_TRUTH.e2648_p1605',
# 'mc12_8TeV.183551.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto_ckkw15.merge.NTUP_TRUTH.e2489_p1605',
# 'mc12_8TeV.183552.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto_ckkw30.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183553.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto_fac025.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183554.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto_fac4.merge.NTUP_TRUTH.e2391_p1605',
# 'mc12_8TeV.183555.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto_renorm025.merge.NTUP_TRUTH.e2465_p1605',
# 'mc12_8TeV.183555.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto_renorm025.merge.NTUP_TRUTH.e2648_p1605',
# 'mc12_8TeV.183556.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto_renorm4.merge.NTUP_TRUTH.e2465_p1605',
# 'mc12_8TeV.183556.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto_renorm4.merge.NTUP_TRUTH.e2648_p1605'
  ]

# this is for testing
inDS_test_mu = [ 
# 'mc12_8TeV.204737.Sherpa_CT10_munugammaPt80_ckkw15.merge.NTUP_TRUTH.e3140_p1605_tid04400108_00',
# 'mc12_8TeV.204738.Sherpa_CT10_munugammaPt80_ckkw30.merge.NTUP_TRUTH.e3140_p1605_tid04400109_00',
# 'mc12_8TeV.204739.Sherpa_CT10_munugammaPt80_fac025.merge.NTUP_TRUTH.e3140_p1605_tid04400110_00',
# 'mc12_8TeV.204740.Sherpa_CT10_munugammaPt80_fac4.merge.NTUP_TRUTH.e3140_p1605_tid04400111_00',
# 'mc12_8TeV.204741.Sherpa_CT10_munugammaPt80_renorm025.merge.NTUP_TRUTH.e3140_p1605_tid04400112_00',
# 'mc12_8TeV.204742.Sherpa_CT10_munugammaPt80_renorm4.merge.NTUP_TRUTH.e3140_p1605_tid04400113_00',
# 'mc12_8TeV.202336.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_moreFSR.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202335.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_alpsDN.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202332.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_scaleUP.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202337.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_lessFSR.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202334.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_alpsUP.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.202333.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_scaleDN.merge.NTUP_TRUTH.e2894_p1605',
# 'mc12_8TeV.177998.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_fixed.merge.NTUP_TRUTH.e2189_p1605',
  ]

    
for i,inDS in enumerate(inDS_test):

    outName = inDS[:88] # make sure the name is not too long
 
    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_141113.%s newSignalGammaElectron_truth.py " % (inDS, outName)
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s --outDS user.jmitrevs.GE_150212b.%s newSignalGammaElectron_truth.py " % (inDS, outName)

    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.PU_120828.%s --extOutFile=gmsbPileupTool.prw.root  PileupHelper.py " % (inDS, outName)
   
    # if i == 0:
    #     command += " --outTarBall=/data/jmitrevs/scratch/submission_150204.tar"
    # else:
    #     command += " --inTarBall=/data/jmitrevs/scratch/submission_150204.tar"

    command += " --inTarBall=/data/jmitrevs/scratch/submission_150204.tar"

    print command
    sys.stdout.flush()
    os.system(command)
    
for i,inDS in enumerate(inDS_test_mu):

    outName = inDS[:88] # make sure the name is not too long

    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GM_141113.%s newSignalGammaMuon_truth.py " % (inDS, outName)
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s --outDS user.jmitrevs.GM_141119.%s newSignalGammaMuon_truth.py " % (inDS, outName)

    # if i == 0:
    #     command += " --outTarBall=/data/jmitrevs/scratch/submission_141110.tar"
    # else:
    #     command += " --inTarBall=/data/jmitrevs/scratch/submission_141110.tar"

    command += " --inTarBall=/data/jmitrevs/scratch/submission_141113.tar"

    print command
    sys.stdout.flush()
    os.system(command)
