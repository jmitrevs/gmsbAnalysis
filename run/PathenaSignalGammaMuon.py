#! /usr/bin/env python

import os
import commands
import sys
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing
inDS_test = [
   
    #'mc11_7TeV.117402.Whizard_CTEQL1Jimmy_TTbarPhoton_SM_NoFullHad.merge.AOD.e1086_s1372_s1370_r3043_r2993',
    'mc11_7TeV.126855.Sherpa_tautaugammaPt40.merge.AOD.e1181_s1372_s1370_r3108_r3109',
    ]

inDS_full = [

    'mc11_7TeV.117420.AlpgenJimmyWgammaNp0_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117421.AlpgenJimmyWgammaNp1_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117422.AlpgenJimmyWgammaNp2_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117423.AlpgenJimmyWgammaNp3_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117424.AlpgenJimmyWgammaNp4_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',
    'mc11_7TeV.117425.AlpgenJimmyWgammaNp5_pt20.merge.AOD.e873_s1310_s1300_r3043_r2993',

    # 'mc11_7TeV.105985.WW_Herwig.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.105986.ZZ_Herwig.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.105987.WZ_Herwig.merge.AOD.e825_s1310_s1300_r3043_r2993',

    # #'mc11_7TeV.108325.Pythia_MadGraph_Ztautaugamma.merge.AOD.e887_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.126855.Sherpa_tautaugammaPt40.merge.AOD.e1181_s1372_s1370_r3108_r3109',
    # 'mc11_7TeV.145164.Sherpa_Zmumugamma_highpt.merge.AOD.e923_s1310_s1300_r3043_r2993', 

    # 'mc11_7TeV.108341.st_tchan_munu_McAtNlo_Jimmy.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.108342.st_tchan_taunu_McAtNlo_Jimmy.merge.AOD.e835_s1310_s1300_r3043_r2993',
    # 'mc11_7TeV.108346.st_Wt_McAtNlo_Jimmy.merge.AOD.e835_s1310_s1300_r3043_r2993',

    # # 'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    # # 'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    # # 'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    # # 'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    # # 'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    # # 'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',

    # # 'mc11_7TeV.116394.AlpgenJimmyGamNp5_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.116392.AlpgenJimmyGamNp3_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.116393.AlpgenJimmyGamNp4_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.116390.AlpgenJimmyGamNp1_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',
    # # 'mc11_7TeV.116391.AlpgenJimmyGamNp2_JetFilter_Nj2Et20.merge.AOD.e825_s1310_s1300_r3043_r2993',

    # 'mc11_7TeV.117402.Whizard_CTEQL1Jimmy_TTbarPhoton_SM_NoFullHad.merge.AOD.e1086_s1372_s1370_r3043_r2993',

    # # # 'mc11_7TeV.126022.Sherpa_Znunugamma_highpt.merge.AOD.e931_s1310_s1300_r3043_r2993',
    # # # 'mc11_7TeV.118619.Pythia_MadGraph_Znunugammagamma.merge.AOD.e887_s1372_s1370_r3043_r2993',
    # # # 'mc11_7TeV.107710.AlpgenJimmyZnunuNp0_pt20_filt1jet.merge.AOD.e859_s1310_s1300_r3043_r2993',
    # # # 'mc11_7TeV.107711.AlpgenJimmyZnunuNp1_pt20_filt1jet.merge.AOD.e859_s1310_s1300_r3043_r2993',
    # # # 'mc11_7TeV.107712.AlpgenJimmyZnunuNp2_pt20_filt1jet.merge.AOD.e887_s1310_s1300_r3043_r2993',
    # # # 'mc11_7TeV.107713.AlpgenJimmyZnunuNp3_pt20_filt1jet.merge.AOD.e859_s1310_s1300_r3043_r2993',
    # # # 'mc11_7TeV.107714.AlpgenJimmyZnunuNp4_pt20_filt1jet.merge.AOD.e859_s1310_s1300_r3043_r2993',
    # # # 'mc11_7TeV.107715.AlpgenJimmyZnunuNp5_pt20_filt1jet.merge.AOD.e1004_s1372_s1370_r3043_r2993',

    # # # 'mc11_7TeV.115040.Pythia_photos_diphotons100.merge.AOD.e997_s1372_s1370_r3043_r2993',
    # # # 'mc11_7TeV.115039.Pythia_photos_diphotons50.merge.AOD.e997_s1372_s1370_r3043_r2993',
]

#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_full):
   
    outName = inDS[:95] # make sure the name is not too long
   
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GM_120705.%s SignalGammaMuon.py " % (inDS, outName)
    
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammamu_120705.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120705.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120705.tar"

    print command
    sys.stdout.flush()
    os.system(command)
    

inDS_ttbar = [
    'mc11_7TeV.105200.T1_McAtNlo_Jimmy.merge.AOD.e835_s1272_s1274_r3043_r2993',
    ]

    
for i,inDS in enumerate(inDS_ttbar):
 
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GM_120625.%s SignalGammaMuon_ttbar.py " % (inDS, inDS)
   
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammamu_120418.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120418.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120625.tar"

    # print command
    # sys.stdout.flush()
    # os.system(command)
    

inDS_Wjets = [

    #'mc11_7TeV.107690.AlpgenJimmyWmunuNp0_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107691.AlpgenJimmyWmunuNp1_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107692.AlpgenJimmyWmunuNp2_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107693.AlpgenJimmyWmunuNp3_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107694.AlpgenJimmyWmunuNp4_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107695.AlpgenJimmyWmunuNp5_pt20.merge.AOD.e825_s1299_s1300_r3043_r2993',
    
    #'mc11_7TeV.107700.AlpgenJimmyWtaunuNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107701.AlpgenJimmyWtaunuNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107702.AlpgenJimmyWtaunuNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107703.AlpgenJimmyWtaunuNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107704.AlpgenJimmyWtaunuNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107705.AlpgenJimmyWtaunuNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
]

for i,inDS in enumerate(inDS_Wjets):
   
    outName = inDS[:95] # make sure the name is not too long
   
    command = "pathena --mergeOutput --excludedSite=ANALY_GRIF-LAL --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GML_120705.%s SignalGammaMuon_WjetsLoose.py " % (inDS, inDS)
    
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammamu_120601.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120601.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120705.tar"

    print command
    sys.stdout.flush()
    os.system(command)

inDS_Zjets = [

    'mc11_7TeV.107660.AlpgenJimmyZmumuNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107661.AlpgenJimmyZmumuNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107662.AlpgenJimmyZmumuNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107663.AlpgenJimmyZmumuNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107664.AlpgenJimmyZmumuNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107665.AlpgenJimmyZmumuNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    
]

for i,inDS in enumerate(inDS_Zjets):
   
    outName = inDS[:95] # make sure the name is not too long
   
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GM_120625.%s SignalGammaMuon_Zjets.py " % (inDS, inDS)
    
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammamu_120520Zjets.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120520Zjets.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120625.tar"

    # print command
    # sys.stdout.flush()
    # os.system(command)

inDS_Zjets = [

    #'mc11_7TeV.107670.AlpgenJimmyZtautauNp0_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107671.AlpgenJimmyZtautauNp1_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107672.AlpgenJimmyZtautauNp2_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107673.AlpgenJimmyZtautauNp3_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107674.AlpgenJimmyZtautauNp4_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
    'mc11_7TeV.107675.AlpgenJimmyZtautauNp5_pt20.merge.AOD.e835_s1299_s1300_r3043_r2993',
]

for i,inDS in enumerate(inDS_Zjets):
   
    outName = inDS[:95] # make sure the name is not too long
   
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GM_120625.%s SignalGammaMuon_Ztaujets.py " % (inDS, inDS)
    
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammamu_120520Zjets.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120520Zjets.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammamu_120625.tar"

    # print command
    # sys.stdout.flush()
    # os.system(command)

