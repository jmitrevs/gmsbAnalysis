#! /usr/bin/env python

import os
import commands
import sys
sfg="date '+%y%m%d%H%M'"
Dates=os.system(sfg)

# Put the list of datasets you want to run over here (remove the '/' from the end). 

# this is for testing
inDS_test = [ 
  ]


inDS_full = [
'group.phys-susy.data12_8TeV.periodA.physics_Egamma.PhysCont.NTUP_SUSYSKIM.repro14_v01_p1328_p1329',
'group.phys-susy.data12_8TeV.periodB.physics_Egamma.PhysCont.NTUP_SUSYSKIM.repro14_v01_p1328_p1329',
'group.phys-susy.data12_8TeV.periodC.physics_Egamma.PhysCont.NTUP_SUSYSKIM.repro14_v01_p1328_p1329',
'group.phys-susy.data12_8TeV.periodD.physics_Egamma.PhysCont.NTUP_SUSYSKIM.repro14_v01_p1328_p1329',
'group.phys-susy.data12_8TeV.periodE.physics_Egamma.PhysCont.NTUP_SUSYSKIM.repro14_v01_p1328_p1329',
'group.phys-susy.data12_8TeV.periodG.physics_Egamma.PhysCont.NTUP_SUSYSKIM.repro14_v01_p1328_p1329',
'group.phys-susy.data12_8TeV.periodH.physics_Egamma.PhysCont.NTUP_SUSYSKIM.repro14_v01_p1328_p1329',
'group.phys-susy.data12_8TeV.periodI.physics_Egamma.PhysCont.NTUP_SUSYSKIM.t0pro14_v01_p1328_p1329',
'group.phys-susy.data12_8TeV.periodJ.physics_Egamma.PhysCont.NTUP_SUSYSKIM.t0pro14_v01_p1328_p1329',
'group.phys-susy.data12_8TeV.periodL.physics_Egamma.PhysCont.NTUP_SUSYSKIM.t0pro14_v01_p1328_p1329',

    ]
#how to automatically configure GRL ?


    
for i,inDS in enumerate(inDS_test):

    outName = inDS[:88] # make sure the name is not too long
 
    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_140912.%s newSignalGammaElectron.py " % (inDS, outName)
    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_140612r.%s newSignalGammaElectron_afast_looser.py " % (inDS, outName)

    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.PU_120828.%s --extOutFile=gmsbPileupTool.prw.root  PileupHelper.py " % (inDS, outName)
   
    # if i == 0:
    #     command += " --outTarBall=/data/jmitrevs/scratch/submission_gammael_140905b.tar"
    # else:
    #     command += " --inTarBall=/data/jmitrevs/scratch/submission_gammael_140905b.tar"

    command += " --inTarBall=/data/jmitrevs/scratch/submission_gammael_140912.tar"

    print command
    sys.stdout.flush()
    #os.system(command)
    
for i,inDS in enumerate(inDS_test_mu):

    outName = inDS[:88] # make sure the name is not too long

    command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GM_140912b.%s newSignalGammaMuon.py " % (inDS, outName)
    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.GE_140612r.%s newSignalGammaElectron_afast_looser.py " % (inDS, outName)

    #command = "pathena --mergeOutput --nGBPerJob=MAX --inDS %s/ --outDS user.jmitrevs.PU_120828.%s --extOutFile=gmsbPileupTool.prw.root  PileupHelper.py " % (inDS, outName)
   
    # if i == 0:
    #     command += " --outTarBall=/data/jmitrevs/scratch/submission_gammael_140905.tar"
    # else:
    #     command += " --inTarBall=/data/jmitrevs/scratch/submission_gammael_140905.tar"

    command += " --inTarBall=/data/jmitrevs/scratch/submission_gammael_140912.tar"

    print command
    sys.stdout.flush()
    os.system(command)
