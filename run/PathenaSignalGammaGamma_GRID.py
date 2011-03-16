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

inDS_grid_old = [
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

inDS_grid = [
    'mc10_7TeV.118973.Pythia_GGM_Bino800_200.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118976.Pythia_GGM_Bino800_500.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118435.Pythia_GGM_Bino500_200.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118970.Pythia_GGM_Bino650_500.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118968.Pythia_GGM_Bino650_300.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118445.Pythia_GGM_Bino700_150.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118430.Pythia_GGM_Bino400_150.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118434.Pythia_GGM_Bino500_150.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118446.Pythia_GGM_Bino700_200.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118447.Pythia_GGM_Bino700_300.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118975.Pythia_GGM_Bino800_400.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118437.Pythia_GGM_Bino500_400.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118977.Pythia_GGM_Bino800_600.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118978.Pythia_GGM_Bino800_700.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118431.Pythia_GGM_Bino400_200.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118440.Pythia_GGM_Bino600_200.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118971.Pythia_GGM_Bino650_600.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118439.Pythia_GGM_Bino600_150.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118979.Pythia_GGM_Bino800_780.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118966.Pythia_GGM_Bino650_150.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118450.Pythia_GGM_Bino700_600.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118448.Pythia_GGM_Bino700_400.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118451.Pythia_GGM_Bino700_680.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118433.Pythia_GGM_Bino400_380.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118972.Pythia_GGM_Bino800_150.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118438.Pythia_GGM_Bino500_480.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118449.Pythia_GGM_Bino700_500.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118969.Pythia_GGM_Bino650_400.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118444.Pythia_GGM_Bino600_580.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118967.Pythia_GGM_Bino650_200.merge.AOD.e715_s933_s946_r1831_r2040',
    'mc10_7TeV.118432.Pythia_GGM_Bino400_300.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118443.Pythia_GGM_Bino600_500.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118441.Pythia_GGM_Bino600_300.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118442.Pythia_GGM_Bino600_400.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118436.Pythia_GGM_Bino500_300.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118974.Pythia_GGM_Bino800_300.merge.AOD.e715_s933_s946_r1831_r2040',

    # UED

    'mc10_7TeV.105754.PythiaUED_6_700.merge.AOD.e574_s933_s946_r1831_r2040',
    'mc10_7TeV.105753.PythiaUED_6_500.merge.AOD.e574_s933_s946_r1831_r2040',
    'mc10_7TeV.115257.PythiaUED_6_1000.merge.AOD.e598_s933_s946_r1831_r2040',
    'mc10_7TeV.115256.PythiaUED_6_900.merge.AOD.e598_s933_s946_r1831_r2040',

    # 'mc10_7TeV.115105.PythiaUED_6_480.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115251.PythiaUED_6_600.merge.AOD.e734_s1171_s1100_r1831_r2040',
    # 'mc10_7TeV.115254.PythiaUED_6_675.merge.AOD.e598_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115104.PythiaUED_6_460.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115250.PythiaUED_6_575.merge.AOD.e598_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115664.PythiaUED_6_975.merge.AOD.e725_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115251.PythiaUED_6_600.merge.AOD.e598_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115255.PythiaUED_6_800.merge.AOD.e598_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115102.PythiaUED_6_350.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.105339.PythiaUED_6_300.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115106.PythiaUED_6_520.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115101.PythiaUED_6_330.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115662.PythiaUED_6_925.merge.AOD.e725_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115255.PythiaUED_6_800.merge.AOD.e734_s1171_s1100_r1831_r2040',
    # 'mc10_7TeV.115252.PythiaUED_6_625.merge.AOD.e598_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115253.PythiaUED_6_650.merge.AOD.e598_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115268.PythiaUED_6_775.merge.AOD.e660_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115257.PythiaUED_6_1000.merge.AOD.e734_s1171_s1100_r1831_r2040',
    # 'mc10_7TeV.115267.PythiaUED_6_750.merge.AOD.e660_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115103.PythiaUED_6_400.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115107.PythiaUED_6_555.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115266.PythiaUED_6_725.merge.AOD.e660_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115663.PythiaUED_6_950.merge.AOD.e725_s933_s946_r1831_r2040',

    ]

inDS_noPileup = [
    'mc10_7TeV.118441.Pythia_GGM_Bino600_300.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118431.Pythia_GGM_Bino400_200.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118445.Pythia_GGM_Bino700_150.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118433.Pythia_GGM_Bino400_380.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118439.Pythia_GGM_Bino600_150.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118966.Pythia_GGM_Bino650_150.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118976.Pythia_GGM_Bino800_500.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118430.Pythia_GGM_Bino400_150.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118432.Pythia_GGM_Bino400_300.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118451.Pythia_GGM_Bino700_680.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118967.Pythia_GGM_Bino650_200.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118443.Pythia_GGM_Bino600_500.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118437.Pythia_GGM_Bino500_400.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118444.Pythia_GGM_Bino600_580.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118973.Pythia_GGM_Bino800_200.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118979.Pythia_GGM_Bino800_780.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118971.Pythia_GGM_Bino650_600.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118436.Pythia_GGM_Bino500_300.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118970.Pythia_GGM_Bino650_500.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118969.Pythia_GGM_Bino650_400.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118434.Pythia_GGM_Bino500_150.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118438.Pythia_GGM_Bino500_480.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118968.Pythia_GGM_Bino650_300.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118442.Pythia_GGM_Bino600_400.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118977.Pythia_GGM_Bino800_600.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118446.Pythia_GGM_Bino700_200.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118435.Pythia_GGM_Bino500_200.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118450.Pythia_GGM_Bino700_600.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118447.Pythia_GGM_Bino700_300.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118975.Pythia_GGM_Bino800_400.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118972.Pythia_GGM_Bino800_150.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118974.Pythia_GGM_Bino800_300.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118978.Pythia_GGM_Bino800_700.merge.AOD.e715_s933_s946_r1652_r1700',
    'mc10_7TeV.118440.Pythia_GGM_Bino600_200.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118449.Pythia_GGM_Bino700_500.merge.AOD.e640_s933_s946_r1652_r1700',
    'mc10_7TeV.118448.Pythia_GGM_Bino700_400.merge.AOD.e640_s933_s946_r1652_r1700',

    'mc10_7TeV.105754.PythiaUED_6_700.merge.AOD.e574_s933_s946_r1652_r1700',
    'mc10_7TeV.105753.PythiaUED_6_500.merge.AOD.e574_s933_s946_r1652_r1700',
    'mc10_7TeV.115257.PythiaUED_6_1000.merge.AOD.e598_s933_s946_r1652_r1700',
    'mc10_7TeV.115256.PythiaUED_6_900.merge.AOD.e598_s933_s946_r1652_r1700'

    ]

#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_grid):
   
    number = inDS[10:16]
    #print number

    command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_170311.%s SignalGammaGamma.py " % (number, inDS, inDS)

    #command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_140311_looseff.%s SignalGammaGamma_looseFF.py " % (number, inDS, inDS)


    #command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_070311_v2_noIso.%s SignalGammaGamma_noIso.py " % (number, inDS, inDS)

    print command
    os.system(command)

    #command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_140311_su.%s SignalGammaGamma_ShiftUp.py " % (number, inDS, inDS)

    #print command
    #os.system(command)

    #command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_140311_sd.%s SignalGammaGamma_ShiftDown.py " % (number, inDS, inDS)
    
    #print command
    #os.system(command)
    
