#! /usr/bin/env python

import os
import commands
import sys
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing
inDS_test = [  
    'mc11_7TeV.115039.Pythia_photos_diphotons50.merge.AOD.e997_s1372_s1370_r3043_r2993'
    ]

inDS_full = [

    # 'mc11_7TeV.117402.Whizard_CTEQL1Jimmy_TTbarPhoton_SM_NoFullHad.merge.AOD.e1086_s1372_s1370_r3043_r2993',

    # 'mc11_7TeV.117420.AlpgenJimmyWgammaNp0_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.117421.AlpgenJimmyWgammaNp1_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.117422.AlpgenJimmyWgammaNp2_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.117423.AlpgenJimmyWgammaNp3_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.117424.AlpgenJimmyWgammaNp4_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.117425.AlpgenJimmyWgammaNp5_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',

    # 'mc11_7TeV.105985.WW_Herwig.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.105986.ZZ_Herwig.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.105987.WZ_Herwig.merge.AOD.e825_s1310_s1300_r3043_r2993',


    # #'mc11_7TeV.108323.Pythia_MadGraph_Zeegamma.merge.AOD.e887_s1310_s1300_r3043_r2993',
    # #'mc11_7TeV.108325.Pythia_MadGraph_Ztautaugamma.merge.AOD.e887_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.126855.Sherpa_tautaugammaPt40.merge.AOD.e1181_s1372_s1370_r3108_r3109',
    # 'mc11_7TeV.108340.st_tchan_enu_McAtNlo_Jimmy.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.108342.st_tchan_taunu_McAtNlo_Jimmy.merge.AOD.e835_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.108346.st_Wt_McAtNlo_Jimmy.merge.AOD.e835_s1310_s1300_r3043_r2993',

    # # 'mc11_7TeV.116394.AlpgenJimmyGamNp5_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.116392.AlpgenJimmyGamNp3_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.116393.AlpgenJimmyGamNp4_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.116390.AlpgenJimmyGamNp1_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.116391.AlpgenJimmyGamNp2_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',

    # 'mc11_7TeV.145163.Sherpa_Zeegamma_highpt.merge.AOD.e923_s1310_s1300_r3043_r2993',

    # # 'mc11_7TeV.126022.Sherpa_Znunugamma_highpt.merge.AOD.e931_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.118619.Pythia_MadGraph_Znunugammagamma.merge.AOD.e887_s1372_s1370_r3043_r2993',
    # # 'mc11_7TeV.107710.AlpgenJimmyZnunuNp0_pt20_filt1jet.merge.AOD.e859_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.107711.AlpgenJimmyZnunuNp1_pt20_filt1jet.merge.AOD.e859_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.107712.AlpgenJimmyZnunuNp2_pt20_filt1jet.merge.AOD.e887_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.107713.AlpgenJimmyZnunuNp3_pt20_filt1jet.merge.AOD.e859_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.107714.AlpgenJimmyZnunuNp4_pt20_filt1jet.merge.AOD.e859_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.107715.AlpgenJimmyZnunuNp5_pt20_filt1jet.merge.AOD.e1004_s1372_s1370_r3043_r2993',

    # # 'mc11_7TeV.115040.Pythia_photos_diphotons100.merge.AOD.e997_s1372_s1370_r3043_r2993',
    # 'mc11_7TeV.115039.Pythia_photos_diphotons50.merge.AOD.e997_s1372_s1370_r3043_r2993',

    # 'mc11_7TeV.119081.2DP20_GamJetGamGam_pythia_photon_filter.merge.AOD.e825_s1310_s1300_r3044_r2993',
    # 'mc11_7TeV.126389.Sherpa2DP20.merge.AOD.e1028_s1310_s1300_r3108_r3109',

    'mc11_7TeV.117360.st_tchan_enu_AcerMC.merge.AOD.e835_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117362.st_tchan_taunu_AcerMC.merge.AOD.e825_s1310_s1300_r3043_r2993',
    'mc11_7TeV.126892.Sherpa_CT10_llnunu_WW.merge.AOD.e1255_s1372_s1370_r3108_r3109',
    'mc11_7TeV.126893.Sherpa_CT10_lllnu_WZ.merge.AOD.e1228_s1372_s1370_r3108_r3109',
    'mc11_7TeV.126894.Sherpa_CT10_llll_ZZ.merge.AOD.e1228_s1372_s1370_r3108_r3109',
    'mc11_7TeV.126895.Sherpa_CT10_llnunu_ZZ.merge.AOD.e1228_s1372_s1370_r3108_r3109', 
    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_full):

    outName = inDS[:90] # make sure the name is not too long
 
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_120726.%s SignalGammaElectron.py " % (inDS, outName)
   
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammael_120726.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammael_120726.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammael_120726.tar"

    # print command
    # sys.stdout.flush()
    # os.system(command)
    

inDS_ttbar = [
    'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.AOD.e835_s1272_s1274_r3043_r2993',
    ]

    
for i,inDS in enumerate(inDS_ttbar):
 
    # command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.37.%s SignalGammaElectron.py " % (inDS, inDS)
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_120625.%s SignalGammaElectron_ttbar.py " % (inDS, inDS)
   
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammael_120519.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammael_120519.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammael_120625.tar"

    # print command
    # sys.stdout.flush()
    # os.system(command)


inDS_Wjets = [

    'mc11_7TeV.107680.AlpgenJimmyWenuNp0_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    # 'mc11_7TeV.107681.AlpgenJimmyWenuNp1_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    # 'mc11_7TeV.107682.AlpgenJimmyWenuNp2_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    # 'mc11_7TeV.107683.AlpgenJimmyWenuNp3_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    # 'mc11_7TeV.107684.AlpgenJimmyWenuNp4_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    # 'mc11_7TeV.107685.AlpgenJimmyWenuNp5_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
   
    # 'mc11_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    # 'mc11_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    # 'mc11_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    # 'mc11_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    # 'mc11_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',

    # 'mc11_7TeV.107280.AlpgenJimmyWbbFullNp0_pt20.merge.AOD.e887_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.107281.AlpgenJimmyWbbFullNp1_pt20.merge.AOD.e887_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.107282.AlpgenJimmyWbbFullNp2_pt20.merge.AOD.e887_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.107283.AlpgenJimmyWbbFullNp3_pt20.merge.AOD.e887_s1310_s1300_r3043_r2993',

    ]


for i,inDS in enumerate(inDS_Wjets):
 
    # command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.37.%s SignalGammaElectron.py " % (inDS, inDS)
    command = "pathena --mergeOutput --excludedSite=ANALY_GRIF-LAL --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GEL_120705a.%s SignalGammaElectron_WjetsLoose.py " % (inDS, inDS)
   
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammael_120601.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammael_120601.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammael_120705.tar"

    # print command
    # sys.stdout.flush()
    # os.system(command)
    
inDS_Zjets = [

    'mc11_7TeV.107650.AlpgenJimmyZeeNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107651.AlpgenJimmyZeeNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107652.AlpgenJimmyZeeNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107653.AlpgenJimmyZeeNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107654.AlpgenJimmyZeeNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107655.AlpgenJimmyZeeNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',

    # 'mc11_7TeV.106046.PythiaZee_no_filter.merge.AOD.e815_s1356_s1353_r3043_r2993',
    # 'mc11_7TeV.106087.McAtNloZee_no_filter.merge.AOD.e1096_s1372_s1370_r3043_r2993',

    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_Zjets):
 
    command = "pathena --mergeOutput --excludedSite=ANALY_QMUL --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_120731.%s SignalGammaElectron_Zjets.py " % (inDS, inDS)
   
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammael_120731Zjets.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammael_120731Zjets.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammael_120731Zjets.tar"

    print command
    sys.stdout.flush()
    os.system(command)

inDS_Ztau = [
    'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',

    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_Ztau):
 
    command = "pathena --mergeOutput --excludedSite=ANALY_QMUL --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_120801.%s SignalGammaElectron_Ztaujets.py " % (inDS, inDS)
   
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammael_120801.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammael_120801.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammael_120801.tar"

    # print command
    # sys.stdout.flush()
    # os.system(command)
    
    
