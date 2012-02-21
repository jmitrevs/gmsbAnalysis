#! /usr/bin/env python

import os
import commands
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing
inDS_test = [
  
    'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    ]

inDS_full = [

    'mc11_7TeV.107680.AlpgenJimmyWenuNp0_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107681.AlpgenJimmyWenuNp1_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107682.AlpgenJimmyWenuNp2_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107683.AlpgenJimmyWenuNp3_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107684.AlpgenJimmyWenuNp4_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107685.AlpgenJimmyWenuNp5_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993'
   
    'mc11_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',

    'mc11_7TeV.117420.AlpgenJimmyWgammaNp0_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117421.AlpgenJimmyWgammaNp1_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117422.AlpgenJimmyWgammaNp2_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117423.AlpgenJimmyWgammaNp3_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117424.AlpgenJimmyWgammaNp4_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117425.AlpgenJimmyWgammaNp5_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',

    'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.AOD.e835_s1272_s1274_r3043_r2993',

    'mc11_7TeV.105985.WW_Herwig.merge.AOD.e825_s1310_s1300_r3043_r2993',
    'mc11_7TeV.105986.ZZ_Herwig.merge.AOD.e825_s1310_s1300_r3043_r2993',
    'mc11_7TeV.105987.WZ_Herwig.merge.AOD.e825_s1310_s1300_r3043_r2993',


    'mc11_7TeV.108323.Pythia_MadGraph_Zeegamma.merge.AOD.e887_s1310_s1300_r3043_r2993',
    'mc11_7TeV.108325.Pythia_MadGraph_Ztautaugamma.merge.AOD.e887_s1310_s1300_r3043_r2993',

    'mc11_7TeV.108340.st_tchan_enu_McAtNlo_Jimmy.merge.AOD.e825_s1310_s1300_r3043_r2993',
    'mc11_7TeV.108342.st_tchan_taunu_McAtNlo_Jimmy.merge.AOD.e835_s1310_s1300_r3043_r2993',
    'mc11_7TeV.108346.st_Wt_McAtNlo_Jimmy.merge.AOD.e835_s1310_s1300_r3043_r2993',

    'mc11_7TeV.107650.AlpgenJimmyZeeNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107651.AlpgenJimmyZeeNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107652.AlpgenJimmyZeeNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107653.AlpgenJimmyZeeNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107654.AlpgenJimmyZeeNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107655.AlpgenJimmyZeeNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',

    'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',

    # 'mc11_7TeV.116390.AlpgenJimmyGamNp1_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r2730_r2780',
    # 'mc11_7TeV.116391.AlpgenJimmyGamNp2_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r2730_r2780',
    # 'mc11_7TeV.116392.AlpgenJimmyGamNp3_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r2730_r2780',
    # 'mc11_7TeV.116393.AlpgenJimmyGamNp4_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r2730_r2780',
    # 'mc11_7TeV.116394.AlpgenJimmyGamNp5_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r2730_r2700',


    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_test):

    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GammaElectron_120220.%s SignalGammaElectron.py " % (inDS, inDS)
    
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammael_120220.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammael_120220.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammael_120220.tar"

    print command
    os.system(command)
    
