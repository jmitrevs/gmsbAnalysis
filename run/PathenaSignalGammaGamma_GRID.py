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
    # 'mc10_7TeV.118973.Pythia_GGM_Bino800_200.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118976.Pythia_GGM_Bino800_500.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118435.Pythia_GGM_Bino500_200.merge.AOD.e640_s933_s946_r1831_r2040',
    'mc10_7TeV.118970.Pythia_GGM_Bino650_500.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118968.Pythia_GGM_Bino650_300.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118445.Pythia_GGM_Bino700_150.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118430.Pythia_GGM_Bino400_150.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118434.Pythia_GGM_Bino500_150.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118446.Pythia_GGM_Bino700_200.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118447.Pythia_GGM_Bino700_300.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118975.Pythia_GGM_Bino800_400.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118437.Pythia_GGM_Bino500_400.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118977.Pythia_GGM_Bino800_600.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118978.Pythia_GGM_Bino800_700.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118431.Pythia_GGM_Bino400_200.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118440.Pythia_GGM_Bino600_200.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118971.Pythia_GGM_Bino650_600.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118439.Pythia_GGM_Bino600_150.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118979.Pythia_GGM_Bino800_780.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118966.Pythia_GGM_Bino650_150.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118450.Pythia_GGM_Bino700_600.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118448.Pythia_GGM_Bino700_400.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118451.Pythia_GGM_Bino700_680.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118433.Pythia_GGM_Bino400_380.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118972.Pythia_GGM_Bino800_150.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118438.Pythia_GGM_Bino500_480.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118449.Pythia_GGM_Bino700_500.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118969.Pythia_GGM_Bino650_400.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118444.Pythia_GGM_Bino600_580.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118967.Pythia_GGM_Bino650_200.merge.AOD.e715_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118432.Pythia_GGM_Bino400_300.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118443.Pythia_GGM_Bino600_500.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118441.Pythia_GGM_Bino600_300.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118442.Pythia_GGM_Bino600_400.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118436.Pythia_GGM_Bino500_300.merge.AOD.e640_s933_s946_r1831_r2040',
    # 'mc10_7TeV.118974.Pythia_GGM_Bino800_300.merge.AOD.e715_s933_s946_r1831_r2040',

    # # # UED

    # # 'mc10_7TeV.105754.PythiaUED_6_700.merge.AOD.e574_s933_s946_r1831_r2040',
    # # 'mc10_7TeV.105753.PythiaUED_6_500.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115257.PythiaUED_6_1000.merge.AOD.e598_s933_s946_r1831_r2040',
    # # 'mc10_7TeV.115256.PythiaUED_6_900.merge.AOD.e598_s933_s946_r1831_r2040',

    # 'mc10_7TeV.115255.PythiaUED_6_800.merge.AOD.e598_s933_s946_r1831_r2040',

    # 'mc10_7TeV.115255.PythiaUED_6_800.merge.AOD.e734_s1171_s1100_r2053_r2040',
    # 'mc10_7TeV.115257.PythiaUED_6_1000.merge.AOD.e734_s1171_s1100_r2053_r2040',

    # 'mc10_7TeV.115105.PythiaUED_6_480.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115251.PythiaUED_6_600.merge.AOD.e734_s1171_s1100_r1831_r2040',
    # 'mc10_7TeV.115254.PythiaUED_6_675.merge.AOD.e598_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115104.PythiaUED_6_460.merge.AOD.e574_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115250.PythiaUED_6_575.merge.AOD.e598_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115664.PythiaUED_6_975.merge.AOD.e725_s933_s946_r1831_r2040',
    # 'mc10_7TeV.115251.PythiaUED_6_600.merge.AOD.e598_s933_s946_r1831_r2040',
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

inDS_lowBino = [
    # 'mc10_7TeV.123079.Pythia_GGM_Bino_400_75.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123078.Pythia_GGM_Bino_400_50.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123081.Pythia_GGM_Bino_400_125.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123094.Pythia_GGM_Bino_700_50.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123089.Pythia_GGM_Bino_600_125.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123088.Pythia_GGM_Bino_600_100.merge.AOD.e756_s933_s946_r1831_r2040',
    'mc10_7TeV.123093.Pythia_GGM_Bino_650_125.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123083.Pythia_GGM_Bino_500_75.merge.AOD.e756_s933_s946_r1831_r2040',
    'mc10_7TeV.123092.Pythia_GGM_Bino_650_100.merge.AOD.e756_s933_s946_r1831_r2040',
    'mc10_7TeV.123101.Pythia_GGM_Bino_800_125.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123097.Pythia_GGM_Bino_700_125.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123095.Pythia_GGM_Bino_700_75.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123090.Pythia_GGM_Bino_650_50.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123096.Pythia_GGM_Bino_700_100.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123091.Pythia_GGM_Bino_650_75.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123086.Pythia_GGM_Bino_600_50.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123100.Pythia_GGM_Bino_800_100.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123080.Pythia_GGM_Bino_400_100.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123099.Pythia_GGM_Bino_800_75.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123087.Pythia_GGM_Bino_600_75.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123085.Pythia_GGM_Bino_500_125.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123084.Pythia_GGM_Bino_500_100.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123098.Pythia_GGM_Bino_800_50.merge.AOD.e756_s933_s946_r1831_r2040',
    # 'mc10_7TeV.123082.Pythia_GGM_Bino_500_50.merge.AOD.e756_s933_s946_r1831_r2040'
]

inDS_private = [
    'user.ddamiani.myMC10.123078.Pythia_GGM_Bino_400_50.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123079.Pythia_GGM_Bino_400_75.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123080.Pythia_GGM_Bino_400_100.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123081.Pythia_GGM_Bino_400_125.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123082.Pythia_GGM_Bino_500_50.merge.AOD.e715_s933_s946_r1652_v2',
    'user.ddamiani.myMC10.123083.Pythia_GGM_Bino_500_75.merge.AOD.e715_s933_s946_r1652_v2',
    'user.ddamiani.myMC10.123084.Pythia_GGM_Bino_500_100.merge.AOD.e715_s933_s946_r1652_v2',
    'user.ddamiani.myMC10.123085.Pythia_GGM_Bino_500_125.merge.AOD.e715_s933_s946_r1652_v2',
    'user.ddamiani.myMC10.123086.Pythia_GGM_Bino_600_50.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123087.Pythia_GGM_Bino_600_75.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123088.Pythia_GGM_Bino_600_100.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123089.Pythia_GGM_Bino_600_125.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123094.Pythia_GGM_Bino_700_50.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123095.Pythia_GGM_Bino_700_75.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123096.Pythia_GGM_Bino_700_100.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123097.Pythia_GGM_Bino_700_125.merge.AOD.e715_s933_s946_r1652',

    'user.ddamiani.myMC10.123090.Pythia_GGM_Bino_650_50.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123092.Pythia_GGM_Bino_650_100.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123093.Pythia_GGM_Bino_650_125.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123091.Pythia_GGM_Bino_650_75.merge.AOD.e715_s933_s946_r1652',
    
    'user.ddamiani.myMC10.123100.Pythia_GGM_Bino_800_100.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123101.Pythia_GGM_Bino_800_125.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123098.Pythia_GGM_Bino_800_50.merge.AOD.e715_s933_s946_r1652',
    'user.ddamiani.myMC10.123099.Pythia_GGM_Bino_800_75.merge.AOD.e715_s933_s946_r1652'

]

for i,inDS in enumerate(inDS_grid):
#for i,inDS in enumerate(inDS_lowBino):
   
    number = inDS[10:16]
    ######number = inDS[21:27]
    #print number

    command = "pathena -c 'RANDSEED=%s' --excludedSite=ANALY_FZK --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_160411.%s SignalGammaGamma.py " % (number, inDS, inDS)

    #print command
    #os.system(command)

    #command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_120411_altiso.%s SignalGammaGamma_altiso.py " % (number, inDS, inDS)


    #command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_110411_looseFF.%s SignalGammaGamma_looseFF.py " % (number, inDS, inDS)


    # command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_140411_isoShiftDown.%s SignalGammaGamma_isoShiftDown.py " % (number, inDS, inDS)

    #print command
    #os.system(command)

    #command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_130411_isoShiftUp.%s SignalGammaGamma_isoShiftUp.py " % (number, inDS, inDS)

    # print command
    # os.system(command)

    #command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_130411_su.%s SignalGammaGamma_ShiftUp.py " % (number, inDS, inDS)

    #print command
    #os.system(command)

    #command = "pathena -c 'RANDSEED=%s' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_140411_sd.%s SignalGammaGamma_ShiftDown.py " % (number, inDS, inDS)
    
    print command
    os.system(command)
    
