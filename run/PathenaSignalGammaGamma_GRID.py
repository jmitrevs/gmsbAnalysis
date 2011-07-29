#! /usr/bin/env python

import os
import commands
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

inDS_diphoton = [
  
    'mc10_7TeV.115038.Pythia_photos_diphotons25.merge.AOD.e574_s933_s946_r1831_r1700'

    ]

inDS_grid = [
    'mc10_7TeV.118430.Pythia_GGM_Bino400_150.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118431.Pythia_GGM_Bino400_200.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118432.Pythia_GGM_Bino400_300.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118433.Pythia_GGM_Bino400_380.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118434.Pythia_GGM_Bino500_150.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118435.Pythia_GGM_Bino500_200.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118436.Pythia_GGM_Bino500_300.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118437.Pythia_GGM_Bino500_400.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118438.Pythia_GGM_Bino500_480.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118439.Pythia_GGM_Bino600_150.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118440.Pythia_GGM_Bino600_200.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118441.Pythia_GGM_Bino600_300.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118442.Pythia_GGM_Bino600_400.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118443.Pythia_GGM_Bino600_500.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118444.Pythia_GGM_Bino600_580.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118445.Pythia_GGM_Bino700_150.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118446.Pythia_GGM_Bino700_200.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118447.Pythia_GGM_Bino700_300.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118448.Pythia_GGM_Bino700_400.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118449.Pythia_GGM_Bino700_500.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118450.Pythia_GGM_Bino700_600.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118451.Pythia_GGM_Bino700_680.merge.AOD.e640_s933_s946_r2302_r2300',
    'mc10_7TeV.118972.Pythia_GGM_Bino800_150.merge.AOD.e715_s933_s946_r2302_r2300',
    'mc10_7TeV.118973.Pythia_GGM_Bino800_200.merge.AOD.e715_s933_s946_r2302_r2300',
    'mc10_7TeV.118974.Pythia_GGM_Bino800_300.merge.AOD.e715_s933_s946_r2302_r2300',
    'mc10_7TeV.118975.Pythia_GGM_Bino800_400.merge.AOD.e715_s933_s946_r2302_r2300',
    'mc10_7TeV.118976.Pythia_GGM_Bino800_500.merge.AOD.e715_s933_s946_r2302_r2300',
    'mc10_7TeV.118977.Pythia_GGM_Bino800_600.merge.AOD.e715_s933_s946_r2302_r2300',
    'mc10_7TeV.118978.Pythia_GGM_Bino800_700.merge.AOD.e715_s933_s946_r2302_r2300',
    'mc10_7TeV.118979.Pythia_GGM_Bino800_780.merge.AOD.e715_s933_s946_r2302_r2300',
    'mc10_7TeV.123078.Pythia_GGM_Bino_400_50.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123079.Pythia_GGM_Bino_400_75.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123080.Pythia_GGM_Bino_400_100.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123081.Pythia_GGM_Bino_400_125.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123082.Pythia_GGM_Bino_500_50.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123083.Pythia_GGM_Bino_500_75.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123084.Pythia_GGM_Bino_500_100.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123085.Pythia_GGM_Bino_500_125.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123086.Pythia_GGM_Bino_600_50.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123087.Pythia_GGM_Bino_600_75.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123088.Pythia_GGM_Bino_600_100.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123089.Pythia_GGM_Bino_600_125.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123094.Pythia_GGM_Bino_700_50.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123095.Pythia_GGM_Bino_700_75.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123096.Pythia_GGM_Bino_700_100.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123097.Pythia_GGM_Bino_700_125.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123098.Pythia_GGM_Bino_800_50.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123099.Pythia_GGM_Bino_800_75.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123100.Pythia_GGM_Bino_800_100.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.123101.Pythia_GGM_Bino_800_125.merge.AOD.e756_s933_s946_r2302_r2300',
    'mc10_7TeV.138568.Pythia_GGM_Bino_900_50.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138569.Pythia_GGM_Bino_900_100.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138570.Pythia_GGM_Bino_900_150.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138571.Pythia_GGM_Bino_900_200.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138572.Pythia_GGM_Bino_900_300.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138573.Pythia_GGM_Bino_900_400.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138574.Pythia_GGM_Bino_900_500.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138575.Pythia_GGM_Bino_900_600.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138576.Pythia_GGM_Bino_900_700.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138577.Pythia_GGM_Bino_900_800.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138578.Pythia_GGM_Bino_900_880.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138579.Pythia_GGM_Bino_1000_50.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138580.Pythia_GGM_Bino_1000_100.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138581.Pythia_GGM_Bino_1000_150.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138582.Pythia_GGM_Bino_1000_200.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138583.Pythia_GGM_Bino_1000_300.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138584.Pythia_GGM_Bino_1000_400.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138585.Pythia_GGM_Bino_1000_500.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138586.Pythia_GGM_Bino_1000_600.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138587.Pythia_GGM_Bino_1000_700.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138588.Pythia_GGM_Bino_1000_800.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138589.Pythia_GGM_Bino_1000_900.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138590.Pythia_GGM_Bino_1000_980.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138591.Pythia_GGM_Bino_1100_50.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138592.Pythia_GGM_Bino_1100_100.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138593.Pythia_GGM_Bino_1100_150.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138594.Pythia_GGM_Bino_1100_200.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138595.Pythia_GGM_Bino_1100_300.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138596.Pythia_GGM_Bino_1100_400.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138597.Pythia_GGM_Bino_1100_500.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138598.Pythia_GGM_Bino_1100_600.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138599.Pythia_GGM_Bino_1100_700.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138600.Pythia_GGM_Bino_1100_800.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138601.Pythia_GGM_Bino_1100_900.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138602.Pythia_GGM_Bino_1100_1000.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138603.Pythia_GGM_Bino_1100_1080.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138604.Pythia_GGM_Bino_1200_50.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138605.Pythia_GGM_Bino_1200_100.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138606.Pythia_GGM_Bino_1200_150.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138607.Pythia_GGM_Bino_1200_200.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138608.Pythia_GGM_Bino_1200_300.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138609.Pythia_GGM_Bino_1200_400.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138610.Pythia_GGM_Bino_1200_500.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138611.Pythia_GGM_Bino_1200_600.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138612.Pythia_GGM_Bino_1200_700.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138613.Pythia_GGM_Bino_1200_800.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138614.Pythia_GGM_Bino_1200_900.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138615.Pythia_GGM_Bino_1200_1000.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138616.Pythia_GGM_Bino_1200_1100.merge.AOD.e804_s933_s946_r2302_r2300',
    'mc10_7TeV.138617.Pythia_GGM_Bino_1200_1180.merge.AOD.e804_s933_s946_r2302_r2300',

    ]

for i,inDS in enumerate(inDS_grid):
   
    number = inDS[10:16]
    ######number = inDS[21:27]
    #print number

    command = "pathena -c 'RANDSEED=%s' '--extFile=ilumicalc_histograms_EF_2g20_loose_178044-184169.root,mu_mc10b.root' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_290711.%s SignalGammaGamma.py " % (number, inDS, inDS)

    #command = "pathena -c 'FFSet=6' '--extFile=ilumicalc_histograms_EF_2g20_loose_178044-184169.root,mu_mc10b.root' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_260711_FFSet6.%s SignalGammaGamma_altFF.py " % (inDS, inDS)


    # command = "pathena -c 'RANDSEED=%s' '--extFile=ilumicalc_histograms_EF_2g20_loose_178044-184169.root,mu_mc10b.root' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_140411_isoShiftDown.%s SignalGammaGamma_isoShiftDown.py " % (number, inDS, inDS)

    #print command
    #os.system(command)

    #command = "pathena -c 'RANDSEED=%s' '--extFile=ilumicalc_histograms_EF_2g20_loose_178044-184169.root,mu_mc10b.root' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_130411_isoShiftUp.%s SignalGammaGamma_isoShiftUp.py " % (number, inDS, inDS)

    # print command
    # os.system(command)

    #command = "pathena -c 'RANDSEED=%s' '--extFile=ilumicalc_histograms_EF_2g20_loose_178044-184169.root,mu_mc10b.root' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_130411_su.%s SignalGammaGamma_ShiftUp.py " % (number, inDS, inDS)

    #print command
    #os.system(command)

    #command = "pathena -c 'RANDSEED=%s' '--extFile=ilumicalc_histograms_EF_2g20_loose_178044-184169.root,mu_mc10b.root' --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.SignalModel_140411_sd.%s SignalGammaGamma_ShiftDown.py " % (number, inDS, inDS)

    if i == 0:
        command += " --outTarBall=/data3/jmitrevs/submission_29.tar"
        print command
        os.system(command)
    else:
        command += " --inTarBall=/data3/jmitrevs/submission_29.tar"
        print command
        os.system(command)
    
