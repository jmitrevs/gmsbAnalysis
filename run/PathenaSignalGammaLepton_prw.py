#! /usr/bin/env python

import os
import commands
import sys
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing

inDS_test = [
]

inDS_full = [ 
#     'mc12_8TeV.177998.MadGraphPythia_AUET2BCTEQ6L1_ttbargammaPt80_noAllHad_fixed.merge.NTUP_SUSY.e2189_a188_a205_r4540_p1328',
#     'mc12_8TeV.181087.PowhegPythia_P2011C_ttbar_dilepton.merge.NTUP_SUSY.e2091_a188_a205_r4540_p1328',
#     'mc12_8TeV.126741.Sherpa_CT10_enugammaPt80.merge.NTUP_SUSY.e1533_s1499_s1504_r3658_r3549_p1328',
#     'mc12_8TeV.126744.Sherpa_CT10_munugammaPt80.merge.NTUP_SUSY.e1533_s1499_s1504_r3658_r3549_p1328',
    'mc12_8TeV.158727.Sherpa_CT10_WtaunugammaPt80.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',
# 'mc12_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.NTUP_SUSY.e1727_a188_a171_r3549_p1328',
# #'mc12_8TeV.107680.AlpgenJimmy_AUET2CTEQ6L1_WenuNp0.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
'mc12_8TeV.107680.AlpgenJimmy_AUET2CTEQ6L1_WenuNp0.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107681.AlpgenJimmy_AUET2CTEQ6L1_WenuNp1.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
'mc12_8TeV.107681.AlpgenJimmy_AUET2CTEQ6L1_WenuNp1.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107682.AlpgenJimmy_AUET2CTEQ6L1_WenuNp2.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
'mc12_8TeV.107682.AlpgenJimmy_AUET2CTEQ6L1_WenuNp2.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107683.AlpgenJimmy_AUET2CTEQ6L1_WenuNp3.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
'mc12_8TeV.107683.AlpgenJimmy_AUET2CTEQ6L1_WenuNp3.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107684.AlpgenJimmy_AUET2CTEQ6L1_WenuNp4.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107684.AlpgenJimmy_AUET2CTEQ6L1_WenuNp4.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107685.AlpgenJimmy_AUET2CTEQ6L1_WenuNp5.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
'mc12_8TeV.107685.AlpgenJimmy_AUET2CTEQ6L1_WenuNp5.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# 'mc12_8TeV.126928.PowhegPythia8_AU2CT10_WpWm_ee.merge.NTUP_SUSY.e1280_a159_a171_r3549_p1328',
# #'mc12_8TeV.126928.PowhegPythia8_AU2CT10_WpWm_ee.merge.NTUP_SUSY.e1280_s1469_s1470_r3542_r3549_p1328',
# #'mc12_8TeV.126928.PowhegPythia8_AU2CT10_WpWm_ee.merge.NTUP_SUSY.e1280_s1469_s1470_r3752_r3549_p1328',
# 'mc12_8TeV.126929.PowhegPythia8_AU2CT10_WpWm_me.merge.NTUP_SUSY.e1280_a159_a171_r3549_p1328',
# #'mc12_8TeV.126929.PowhegPythia8_AU2CT10_WpWm_me.merge.NTUP_SUSY.e1280_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.126930.PowhegPythia8_AU2CT10_WpWm_te.merge.NTUP_SUSY.e1280_a159_a171_r3549_p1328',
# #'mc12_8TeV.126930.PowhegPythia8_AU2CT10_WpWm_te.merge.NTUP_SUSY.e1280_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.126931.PowhegPythia8_AU2CT10_WpWm_em.merge.NTUP_SUSY.e1280_a159_a171_r3549_p1328',
# #'mc12_8TeV.126931.PowhegPythia8_AU2CT10_WpWm_em.merge.NTUP_SUSY.e1280_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.126932.PowhegPythia8_AU2CT10_WpWm_mm.merge.NTUP_SUSY.e1280_a159_a171_r3549_p1328',
# #'mc12_8TeV.126932.PowhegPythia8_AU2CT10_WpWm_mm.merge.NTUP_SUSY.e1280_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.126933.PowhegPythia8_AU2CT10_WpWm_tm.merge.NTUP_SUSY.e1280_a159_a171_r3549_p1328',
# #'mc12_8TeV.126933.PowhegPythia8_AU2CT10_WpWm_tm.merge.NTUP_SUSY.e1280_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.126934.PowhegPythia8_AU2CT10_WpWm_et.merge.NTUP_SUSY.e1280_a159_a171_r3549_p1328',
# #'mc12_8TeV.126934.PowhegPythia8_AU2CT10_WpWm_et.merge.NTUP_SUSY.e1280_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.126935.PowhegPythia8_AU2CT10_WpWm_mt.merge.NTUP_SUSY.e1280_a159_a171_r3549_p1328',
# #'mc12_8TeV.126935.PowhegPythia8_AU2CT10_WpWm_mt.merge.NTUP_SUSY.e1280_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.126936.PowhegPythia8_AU2CT10_WpWm_tt.merge.NTUP_SUSY.e1280_a159_a171_r3549_p1328',
# #'mc12_8TeV.126936.PowhegPythia8_AU2CT10_WpWm_tt.merge.NTUP_SUSY.e1280_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129477.PowhegPythia8_AU2CT10_WZ_Wm11Z11_mll0p250d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129478.PowhegPythia8_AU2CT10_WZ_Wm11Z13_mll0p4614d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129479.PowhegPythia8_AU2CT10_WZ_Wm11Z15_mll3p804d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129480.PowhegPythia8_AU2CT10_WZ_Wm13Z11_mll0p250d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129481.PowhegPythia8_AU2CT10_WZ_Wm13Z13_mll0p4614d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129482.PowhegPythia8_AU2CT10_WZ_Wm13Z15_mll3p804d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129483.PowhegPythia8_AU2CT10_WZ_Wm15Z11_mll0p250d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129484.PowhegPythia8_AU2CT10_WZ_Wm15Z13_mll0p4614d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129485.PowhegPythia8_AU2CT10_WZ_Wm15Z15_mll3p804d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129486.PowhegPythia8_AU2CT10_WZ_W11Z11_mll0p250d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129487.PowhegPythia8_AU2CT10_WZ_W11Z13_mll0p4614d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129488.PowhegPythia8_AU2CT10_WZ_W11Z15_mll3p804d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129489.PowhegPythia8_AU2CT10_WZ_W13Z11_mll0p250d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129490.PowhegPythia8_AU2CT10_WZ_W13Z13_mll0p4614d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129491.PowhegPythia8_AU2CT10_WZ_W13Z15_mll3p804d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129492.PowhegPythia8_AU2CT10_WZ_W15Z11_mll0p250d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129493.PowhegPythia8_AU2CT10_WZ_W15Z13_mll0p4614d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.129494.PowhegPythia8_AU2CT10_WZ_W15Z15_mll3p804d0_2LeptonFilter5.merge.NTUP_SUSY.e1300_s1469_s1470_r3542_r3549_p1328',
#'mc12_8TeV.179385.PowhegPythia8_AU2CT10_WZ_Wm11Z15_mll3p80d40_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# # 'mc12_8TeV.179385.PowhegPythia8_AU2CT10_WZ_Wm11Z15_mll3p80d40_taufilter.merge.NTUP_SUSY.e2236_s1581_s1586_r4485_r4540_p1328',
# #'mc12_8TeV.179386.PowhegPythia8_AU2CT10_WZ_Wm13Z15_mll3p80d40_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# #'mc12_8TeV.179387.PowhegPythia8_AU2CT10_WZ_Wm15Z11_mll0p250d0_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# 'mc12_8TeV.179387.PowhegPythia8_AU2CT10_WZ_Wm15Z11_mll0p250d0_taufilter.merge.NTUP_SUSY.e2236_s1581_s1586_r4485_r4540_p1328',
# #'mc12_8TeV.179388.PowhegPythia8_AU2CT10_WZ_Wm15Z13_mll0p4614d0_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# #'mc12_8TeV.179389.PowhegPythia8_AU2CT10_WZ_Wm15Z15_mll3p804d0_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# 'mc12_8TeV.179389.PowhegPythia8_AU2CT10_WZ_Wm15Z15_mll3p804d0_taufilter.merge.NTUP_SUSY.e2236_s1581_s1586_r4485_r4540_p1328',
# #'mc12_8TeV.179390.PowhegPythia8_AU2CT10_WZ_W11Z15_mll3p80d40_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# #'mc12_8TeV.179391.PowhegPythia8_AU2CT10_WZ_W13Z15_mll3p80d40_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# 'mc12_8TeV.179391.PowhegPythia8_AU2CT10_WZ_W13Z15_mll3p80d40_taufilter.merge.NTUP_SUSY.e2236_s1581_s1586_r4485_r4540_p1328',
# #'mc12_8TeV.179392.PowhegPythia8_AU2CT10_WZ_W15Z11_mll0p250d0_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# 'mc12_8TeV.179392.PowhegPythia8_AU2CT10_WZ_W15Z11_mll0p250d0_taufilter.merge.NTUP_SUSY.e2236_s1581_s1586_r4485_r4540_p1328',
# #'mc12_8TeV.179393.PowhegPythia8_AU2CT10_WZ_W15Z13_mll0p4614d0_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# 'mc12_8TeV.179393.PowhegPythia8_AU2CT10_WZ_W15Z13_mll0p4614d0_taufilter.merge.NTUP_SUSY.e2236_s1581_s1586_r4485_r4540_p1328',
#'mc12_8TeV.179394.PowhegPythia8_AU2CT10_WZ_W15Z15_mll3p804d0_taufilter.merge.NTUP_SUSY.e2098_s1581_s1586_r4485_r4540_p1328',
# # 'mc12_8TeV.179394.PowhegPythia8_AU2CT10_WZ_W15Z15_mll3p804d0_taufilter.merge.NTUP_SUSY.e2236_s1581_s1586_r4485_r4540_p1328',
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
# 'mc12_8TeV.126389.Sherpa_CT10_2DP20_DirectPhotonFilter.merge.NTUP_SUSY.e1434_s1499_s1504_r3658_r3549_p1328',
# 'mc12_8TeV.158728.Sherpa_CT10_ZeegammaPt70.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',
# 'mc12_8TeV.158729.Sherpa_CT10_ZmumugammaPt70.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',
# 'mc12_8TeV.158730.Sherpa_CT10_ZtautaugammaPt70.merge.NTUP_SUSY.e1518_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107650.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp0.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107650.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp0.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107651.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp1.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107651.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp1.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107652.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp2.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107652.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp2.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107653.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp3.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107653.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp3.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107654.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp4.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107654.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp4.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107655.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp5.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107655.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp5.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107660.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp0.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107660.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp0.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107661.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp1.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107661.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp1.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107662.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp2.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107662.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp2.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107663.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp3.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107663.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp3.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107664.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp4.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107664.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp4.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107665.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp5.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107665.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp5.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107670.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp0.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107670.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp0.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107671.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp1.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107671.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp1.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107672.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp2.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107672.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp2.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107673.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp3.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107673.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp3.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107674.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp4.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107674.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp4.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',
# #'mc12_8TeV.107675.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp5.merge.NTUP_SUSY.e1218_s1469_s1470_r3542_r3549_p1328',
# 'mc12_8TeV.107675.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp5.merge.NTUP_SUSY.e1571_s1499_s1504_r3658_r3549_p1328',

  ]


for i,inDS in enumerate(inDS_full):

    outName = inDS[:89] # make sure the name is not too long
 
    #command = "pathena myJobOptions.py --inDS=%s/ --outDS=user.jmitrevs.prw141022.%s --extOutFile=MC12ab_MyPRW.prw.root --nGBPerJob=MAX --notSkipMissing" % (inDS, outName)
    command = "pathena myJobOptions.py --inDS=%s/ --outDS=user.jmitrevs.prw141022a.%s --extOutFile=MC12ab_MyPRW.prw.root --nGBPerJob=MAX --notSkipMissing" % (inDS, outName)

   
    # if i == 0:
    #     command += " --outTarBall=/data/jmitrevs/scratch/submission_prw_141022.tar"
    # else:
    #     command += " --inTarBall=/data/jmitrevs/scratch/submission_prw_141022.tar"

    command += " --inTarBall=/data/jmitrevs/scratch/submission_prw_141022.tar"

    print command
    sys.stdout.flush()
    os.system(command)
