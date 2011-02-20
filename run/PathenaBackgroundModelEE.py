#! /usr/bin/env python

import os
import commands
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing
inDS_test = [
  
    'data10_7TeV.periodG.physics_Egamma.PhysCont.AOD.repro05_v02'
#    'data10_7TeV.periodB.physics_L1Calo.PhysCont.AOD.repro05_v02'

    ]

inDS_full = [
  
    #'mc10_7TeV.107650.AlpgenJimmyZeeNp0_pt20.merge.AOD.e600_s933_s946_r1831_r1700',
    #'mc10_7TeV.107651.AlpgenJimmyZeeNp1_pt20.merge.AOD.e600_s933_s946_r1831_r1700',
    #'mc10_7TeV.107652.AlpgenJimmyZeeNp2_pt20.merge.AOD.e600_s933_s946_r1831_r1700',
    'mc10_7TeV.107653.AlpgenJimmyZeeNp3_pt20.merge.AOD.e600_s933_s946_r1831_r1700',
    'mc10_7TeV.107654.AlpgenJimmyZeeNp4_pt20.merge.AOD.e600_s933_s946_r1831_r1700',
    'mc10_7TeV.107655.AlpgenJimmyZeeNp5_pt20.merge.AOD.e600_s933_s946_r1831_r1700',
    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_full):
   
   
    command = "pathena --nGBPerJob=MAX --excludedSite=ANALY_TAIWAN,ANALY_TOKYO --inDS %s/ --outDS user.jmitrevs.BackgroundModelEE_170211.%s BackgroundModelEE.py " % (inDS, inDS)
    
    print command
    os.system(command)
    
