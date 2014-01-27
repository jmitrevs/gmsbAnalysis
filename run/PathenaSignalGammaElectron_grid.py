#! /usr/bin/env python

import os
import commands
import sys
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing
inDS_test = [
    'mc12_8TeV.175052.Herwigpp_UEEE3CTEQ6L1_GGM_wino_300_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',
    ]


inDS_full = [
'mc12_8TeV.174988.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_600_100_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174989.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_600_150_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174990.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_600_200_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174991.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_600_350_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174992.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_600_500_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174993.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_600_580_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174994.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_650_100_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174995.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_650_150_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174996.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_650_200_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174997.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_650_350_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174998.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_650_500_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.174999.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_650_630_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175000.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_700_100_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175001.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_700_150_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175002.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_700_200_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175003.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_700_350_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175004.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_700_500_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175005.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_700_680_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175006.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_750_100_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175007.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_750_150_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175008.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_750_200_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175009.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_750_350_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175010.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_750_500_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175011.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_750_730_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175012.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_800_100_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175013.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_800_150_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175014.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_800_200_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175015.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_800_350_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175016.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_800_500_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175017.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_800_700_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175018.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_800_780_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175019.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_850_100_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175020.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_850_150_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175021.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_850_200_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175022.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_850_350_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175023.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_850_500_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175024.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_850_700_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175025.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_850_830_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175026.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_900_100_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175027.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_900_150_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175028.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_900_200_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175029.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_900_350_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175030.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_900_500_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175031.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_900_700_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175032.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_900_880_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175033.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_950_100_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175034.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_950_150_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175035.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_950_200_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175036.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_950_350_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175037.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_950_500_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175038.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_950_700_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175039.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_950_930_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175040.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_1000_100_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175041.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_1000_150_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175042.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_1000_200_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175043.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_1000_350_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175044.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_1000_500_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175045.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_1000_700_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175046.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_1000_900_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175047.Herwigpp_UEEE3CTEQ6L1_GGM_gl_wino_1000_980_egfilter.merge.NTUP_SUSY.e1639_a159_a171_r3549_p1328',
'mc12_8TeV.175048.Herwigpp_UEEE3CTEQ6L1_GGM_wino_100_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',
'mc12_8TeV.175049.Herwigpp_UEEE3CTEQ6L1_GGM_wino_150_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',
'mc12_8TeV.175050.Herwigpp_UEEE3CTEQ6L1_GGM_wino_200_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',
'mc12_8TeV.175051.Herwigpp_UEEE3CTEQ6L1_GGM_wino_250_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',
'mc12_8TeV.175052.Herwigpp_UEEE3CTEQ6L1_GGM_wino_300_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',
'mc12_8TeV.175053.Herwigpp_UEEE3CTEQ6L1_GGM_wino_350_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',
'mc12_8TeV.175054.Herwigpp_UEEE3CTEQ6L1_GGM_wino_400_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',
'mc12_8TeV.175055.Herwigpp_UEEE3CTEQ6L1_GGM_wino_450_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',
'mc12_8TeV.175056.Herwigpp_UEEE3CTEQ6L1_GGM_wino_500_egfilter.merge.NTUP_SUSY.e1754_a159_a171_r3549_p1328',

    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_test):

    outName = inDS[:90] # make sure the name is not too long
 
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_131010.%s newSignalGammaElectron_afast.py " % (inDS, outName)

    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.PU_120828.%s --extOutFile=gmsbPileupTool.prw.root  PileupHelper.py " % (inDS, outName)
   
    # if i == 0:
    #     command += " --outTarBall=/tmp/jmitrevs/submission_gammael_131010.tar"
    # else:
    #     command += " --inTarBall=/tmp/jmitrevs/submission_gammael_131010.tar"

    #command += " --inTarBall=/data3/jmitrevs/submission_gammael_130318.tar"

    print command
    sys.stdout.flush()
    os.system(command)
    
