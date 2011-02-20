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
  
    'mc10_7TeV.115038.Pythia_photos_diphotons25.merge.AOD.e574_s933_s946_r1831_r1700'

    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_full):
   
   
    command = "pathena --nGBPerJob=MAX --excludedSite=ANALY_RAL,ANALY_LONG_BNL_ATLAS --inDS %s/ --outDS user.jmitrevs.SignalModel_170211_v3.%s SignalGammaGamma.py " % (inDS, inDS)
    
    print command
    os.system(command)
    
