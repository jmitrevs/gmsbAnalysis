#! /usr/bin/env python

import os
import commands
import sys
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing
inDS_test = [
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodL.physics_Egamma.PhysCont.AOD.pro10_v01'

    ]

inDS_full = [
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodM.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodL.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodK.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodJ.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodI.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodH.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodG.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodF.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodE.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodD.physics_Egamma.PhysCont.AOD.pro10_v01',
    'user.jmitrevs.eLgSkim_120419.data11_7TeV.periodB.physics_Egamma.PhysCont.AOD.pro10_v01',
    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_full):

    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.1205621a.%s SignalGammaElectron_Data.py " % (inDS, inDS)
    
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammael_data_120621a.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammael_data_120621a.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammael_data_120621a.tar"

    print command
    sys.stdout.flush()
    os.system(command)

    command = "pathena --mergeOutput --excludedSite=ANALY_GOEGRID --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.120522_gej.%s SignalGammaElectron_Data_gjets.py " % (inDS, inDS)
    
    # if i == 0:
    #     command += " --outTarBall=/data3/jmitrevs/submission_gammael_data_120522.tar"
    # else:
    #     command += " --inTarBall=/data3/jmitrevs/submission_gammael_data_120522.tar"

    command += " --inTarBall=/data3/jmitrevs/submission_gammael_data_120522.tar"

    # print command
    # sys.stdout.flush()
    # os.system(command)
    
