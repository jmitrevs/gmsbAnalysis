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

inDS_diphoton = [
  
    'mc10_7TeV.115038.Pythia_photos_diphotons25.merge.AOD.e574_s933_s946_r1831_r1700'

    ]

inDS_grid = [
    'mc10_7TeV.118441.Pythia_GGM_Bino600_300.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118437.Pythia_GGM_Bino500_400.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118449.Pythia_GGM_Bino700_500.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118440.Pythia_GGM_Bino600_200.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118447.Pythia_GGM_Bino700_300.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118439.Pythia_GGM_Bino600_150.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118443.Pythia_GGM_Bino600_500.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118438.Pythia_GGM_Bino500_480.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118451.Pythia_GGM_Bino700_680.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118450.Pythia_GGM_Bino700_600.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118435.Pythia_GGM_Bino500_200.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118432.Pythia_GGM_Bino400_300.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118444.Pythia_GGM_Bino600_580.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118446.Pythia_GGM_Bino700_200.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118434.Pythia_GGM_Bino500_150.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118436.Pythia_GGM_Bino500_300.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118448.Pythia_GGM_Bino700_400.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118433.Pythia_GGM_Bino400_380.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118442.Pythia_GGM_Bino600_400.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118431.Pythia_GGM_Bino400_200.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118430.Pythia_GGM_Bino400_150.merge.AOD.e640_s933_s946_r1831_r1700',
    'mc10_7TeV.118445.Pythia_GGM_Bino700_150.merge.AOD.e640_s933_s946_r1831_r1700'
    ]


#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_grid):
   
    number = inDS[10:16]
    #print number

    command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_210211.%s SignalGammaGamma.py " % (number, inDS, inDS)
    
    print command
    os.system(command)
    
