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
    'mc11_7TeV.108288.Pythia_MadGraph_Wminusenugamma.merge.AOD.e887_s1310_s1300_r2730_r2700',
    'mc11_7TeV.106001.Pythia_MadGraph_Wplusenugamma.merge.AOD.e887_s1310_s1300_r2730_r2700'
    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_full):
   
   
    command = "pathena --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GammaLepton_011111.%s SignalGammaLepton.py " % (inDS, inDS)
    
    print command
    os.system(command)
    
