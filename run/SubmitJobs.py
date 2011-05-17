#! /usr/bin/env python

import os
import commands
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here, without user.jmitrevs, and remove the '/' from the end. 

inDS_ee = [
    'eeSkim_090511.data11_7TeV.PeriodB2.physics_Egamma.PhysCont.AOD.repro08_v01',
    'eeSkim_090511.data11_7TeV.periodD.physics_Egamma.PhysCont.AOD.t0pro08_v01'
    ]

inDS_gg = [
    'ggSkim_290111.data10_7TeV.periodA.physics_L1Calo.PhysCont.AOD.repro05_v02',
    'ggSkim_290111.data10_7TeV.periodB.physics_L1Calo.PhysCont.AOD.repro05_v02',
    'ggSkim_290111.data10_7TeV.periodC.physics_L1Calo.PhysCont.AOD.repro05_v02',
    'ggSkim_290111.data10_7TeV.periodD.physics_L1Calo.PhysCont.AOD.repro05_v02',
    'ggSkim_290111_v2.data10_7TeV.periodE.physics_Egamma.PhysCont.AOD.repro05_v02',
    'ggSkim_290111.data10_7TeV.periodF.physics_Egamma.PhysCont.AOD.repro05_v02',
    'ggSkim_290111_v2.data10_7TeV.periodG.physics_Egamma.PhysCont.AOD.repro05_v02',
    'ggSkim_290111.data10_7TeV.periodI.physics_Egamma.PhysCont.AOD.repro05_v02',
     
    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_ee):

    command = 'pathena BackgroundModelEE_Data.py --inDS=user.jmitrevs.{0}/ --outDS=user.jmitrevs.eeResult_180511.{0} --nGBPerJob=MAX --excludeFile="*.tgz*"'.format(inDS)

    print command
    os.system(command)
