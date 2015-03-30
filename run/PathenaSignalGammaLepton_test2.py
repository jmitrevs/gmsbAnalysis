#! /usr/bin/env python

import os
import commands
import sys
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing
inDS_test = [ 
    #'mc12_8TeV.177998.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_fixed.merge.NTUP_SUSY.e2189_a188_a205_r4540_p1328',
    #'mc12_8TeV.181087.PowhegPythia_P2011C_ttbar_dilepton.merge.NTUP_SUSY.e2091_a188_a205_r4540_p1328',
    #'mc12_8TeV.126741.Sherpa_CT10_enugammaPt80.merge.NTUP_SUSY.e1533_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.126744.Sherpa_CT10_munugammaPt80.merge.NTUP_SUSY.e1533_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.158727.Sherpa_CT10_WtaunugammaPt80.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.146436.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp0_LeptonPhotonFilter.merge.NTUP_SUSY.e1601_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.146437.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp1_LeptonPhotonFilter.merge.NTUP_SUSY.e1601_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.146438.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp2_LeptonPhotonFilter.merge.NTUP_SUSY.e1601_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.146439.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp3_LeptonPhotonFilter.merge.NTUP_SUSY.e1601_s1499_s1504_r3658_r3549_p1328',

    # 'mc12_8TeV.158728.Sherpa_CT10_ZeegammaPt70.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',
    # 'mc12_8TeV.158730.Sherpa_CT10_ZtautaugammaPt70.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',

# 'mc12_8TeV.202621.WhizardPythia_P2011CCTEQ6L1_singletop_tchan_gamma.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202622.WhizardPythia_P2011CCTEQ6L1_singletop_tchan_gammaDec.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202623.WhizardPythia_P2011CCTEQ6L1_tW_dilep_gamma.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202624.WhizardPythia_P2011CCTEQ6L1_tW_dilep_gammatDec.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202625.WhizardPythia_P2011CCTEQ6L1_tW_dilep_gammaWDec.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202626.WhizardPythia_P2011CCTEQ6L1_tW_tlepWhad_gamma.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202627.WhizardPythia_P2011CCTEQ6L1_tW_tlepWhad_gammatDec.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202628.WhizardPythia_P2011CCTEQ6L1_tW_tlepWhad_gammaWDec.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202629.WhizardPythia_P2011CCTEQ6L1_tW_thadWlep_gamma.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202630.WhizardPythia_P2011CCTEQ6L1_tW_thadWlep_gammatDec.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.202631.WhizardPythia_P2011CCTEQ6L1_tW_thadWlep_gammaWDec.merge.NTUP_SUSY.e2807_a220_a205_r4540_p1328',
# 'mc12_8TeV.110140.PowhegPythia_P2011C_st_Wtchan_incl_DR.merge.NTUP_SUSY.e1743_a188_a171_r3549_p1328',
# 'mc12_8TeV.110101.AcerMCPythia_P2011CCTEQ6L1_singletop_tchan_l.merge.NTUP_SUSY.e1720_a188_a171_r3549_p1328',

    #'mc12_8TeV.110001.McAtNloJimmy_CT10_ttbar_dilepton.merge.NTUP_SUSY.e1576_a159_a171_r3549_p1328',
    #'mc12_8TeV.110001.McAtNloJimmy_CT10_ttbar_dilepton.merge.NTUP_SUSY.e1576_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.117800.Sherpa_CT10_TtbarLeptLept.merge.NTUP_SUSY.e1434_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.117801.Sherpa_CT10_TtbarLeptTaulept.merge.NTUP_SUSY.e1434_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.117802.Sherpa_CT10_TtbarTauleptTaulept.merge.NTUP_SUSY.e1434_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.117804.Sherpa_CT10_TtbarLeptTauhad.merge.NTUP_SUSY.e1434_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.167479.Sherpa_CT10_Znunugammagamma.merge.NTUP_SUSY.e1531_s1499_s1504_r3658_r3549_p1328'
    #'mc12_8TeV.167763.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto.merge.NTUP_SUSY.e1620_a159_a171_r3549_p1328',
    #'mc12_8TeV.167772.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto.merge.NTUP_SUSY.e1620_a159_a171_r3549_p1328',
    'mc12_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.NTUP_SUSY.e1727_a188_a171_r3549_p1328',
    # 'mc12_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.NTUP_SUSY.e1728_s1773_s1776_r3658_r3549_p1328',
    # 'mc12_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.NTUP_SUSY.e1728_s1581_s1586_r3658_r3549_p1328',
  ]

# this is for testing
inDS_test_mu = [ 
    #'mc12_8TeV.177998.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_fixed.merge.NTUP_SUSY.e2189_a188_a205_r4540_p1328',
    #'mc12_8TeV.181087.PowhegPythia_P2011C_ttbar_dilepton.merge.NTUP_SUSY.e2091_a188_a205_r4540_p1328',
    #'mc12_8TeV.126741.Sherpa_CT10_enugammaPt80.merge.NTUP_SUSY.e1533_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.126744.Sherpa_CT10_munugammaPt80.merge.NTUP_SUSY.e1533_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.158727.Sherpa_CT10_WtaunugammaPt80.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',
# 'mc12_8TeV.146436.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp0_LeptonPhotonFilter.merge.NTUP_SUSY.e1260_s1469_s1470_r3542_r3549_p1328',
#'mc12_8TeV.146436.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp0_LeptonPhotonFilter.merge.NTUP_SUSY.e1601_s1499_s1504_r3658_r3549_p1328',
# 'mc12_8TeV.146437.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp1_LeptonPhotonFilter.merge.NTUP_SUSY.e1260_s1469_s1470_r3752_r3549_p1328',
#'mc12_8TeV.146437.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp1_LeptonPhotonFilter.merge.NTUP_SUSY.e1601_s1499_s1504_r3658_r3549_p1328',
# 'mc12_8TeV.146438.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp2_LeptonPhotonFilter.merge.NTUP_SUSY.e1260_s1469_s1470_r3542_r3549_p1328',
#'mc12_8TeV.146438.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp2_LeptonPhotonFilter.merge.NTUP_SUSY.e1601_s1499_s1504_r3658_r3549_p1328',
# 'mc12_8TeV.146439.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp3_LeptonPhotonFilter.merge.NTUP_SUSY.e1293_s1469_s1470_r3752_r3549_p1328',
#'mc12_8TeV.146439.AlpgenJimmy_AUET2CTEQ6L1_WgammaNp3_LeptonPhotonFilter.merge.NTUP_SUSY.e1601_s1499_s1504_r3658_r3549_p1328',
    # 'mc12_8TeV.158729.Sherpa_CT10_ZmumugammaPt70.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.158730.Sherpa_CT10_ZtautaugammaPt70.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.110001.McAtNloJimmy_CT10_ttbar_dilepton.merge.NTUP_SUSY.e1576_a159_a171_r3549_p1328',
    # 'mc12_8TeV.110001.McAtNloJimmy_CT10_ttbar_dilepton.merge.NTUP_SUSY.e1576_s1499_s1504_r3658_r3549_p1328',
    # 'mc12_8TeV.117800.Sherpa_CT10_TtbarLeptLept.merge.NTUP_SUSY.e1434_s1499_s1504_r3658_r3549_p1328',
    # 'mc12_8TeV.117801.Sherpa_CT10_TtbarLeptTaulept.merge.NTUP_SUSY.e1434_s1499_s1504_r3658_r3549_p1328'
    #'mc12_8TeV.117802.Sherpa_CT10_TtbarTauleptTaulept.merge.NTUP_SUSY.e1434_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.117804.Sherpa_CT10_TtbarLeptTauhad.merge.NTUP_SUSY.e1434_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.167479.Sherpa_CT10_Znunugammagamma.merge.NTUP_SUSY.e1531_s1499_s1504_r3658_r3549_p1328',
    #'mc12_8TeV.167766.Sherpa_CT10_WmunuMassiveCBPt70_140_CJetVetoBVeto.merge.NTUP_SUSY.e1714_a159_a171_r3549_p1328',
    #'mc12_8TeV.167775.Sherpa_CT10_WmunuMassiveCBPt140_280_CJetVetoBVeto.merge.NTUP_SUSY.e1714_a159_a171_r3549_p1328',

    'mc12_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.NTUP_SUSY.e1727_a188_a171_r3549_p1328',
    # 'mc12_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.NTUP_SUSY.e1728_s1773_s1776_r3658_r3549_p1328',
    # 'mc12_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.NTUP_SUSY.e1728_s1581_s1586_r3658_r3549_p1328',

  ]
    
tarfile = "/data/jmitrevs/scratch/submission_150330.tar"

for i,inDS in enumerate(inDS_test):

    outName = inDS[:88] # make sure the name is not too long
 
    print outName

    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_150317b.%s newSignalGammaElectron.py " % (inDS, outName)
    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_150308.%s newSignalGammaElectron_afast.py " % (inDS, outName)

    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.PU_120828.%s --extOutFile=gmsbPileupTool.prw.root  PileupHelper.py " % (inDS, outName)
   
    if not os.path.exists(tarfile):
        command += " --outTarBall="+tarfile
    else:
        command += " --inTarBall="+tarfile

    # print command
    # sys.stdout.flush()
    # os.system(command)
    
for i,inDS in enumerate(inDS_test_mu):

    outName = inDS[:88] # make sure the name is not too long

    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GM_150317b%s newSignalGammaMuon.py " % (inDS, outName)
    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GM_150317.%s newSignalGammaMuon_afast.py " % (inDS, outName)

    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.PU_120828.%s --extOutFile=gmsbPileupTool.prw.root  PileupHelper.py " % (inDS, outName)
   
    if not os.path.exists(tarfile):
        command += " --outTarBall="+tarfile
    else:
        command += " --inTarBall="+tarfile

    # print command
    # sys.stdout.flush()
    # os.system(command)
