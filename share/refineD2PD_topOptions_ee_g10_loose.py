##=============================================================================
## Name:        D2PD_topOptions.py
##
## Author:      Karsten Koeneke (DESY)
## Created:     April 2009

## Description: job options for all AOD->D2PD and D1PD->D2PD.
##
## Usage: Here, all neccessary job options for the D2PDs can be set.
##        To run, type:
##             athena D2PDMaker/D2PD_topOptions.py 2>&1 | tee log.txt
##=============================================================================


#==============================================================================
## Include the job property flags for this package 
#==============================================================================
from D2PDMaker.D2PDFlags import D2PDFlags


#==============================================================================
# If you have your own DPD Maker scripts
# (see:
#                    share/D2PD_ExampleSimple*.py
# for examples),
# then just append your script (wherever it is) to this list:
#
#       D2PDFlags.DPDMakerScripts.append("MyPackage/MyScript")
#
# The example scripts are appended below, so you can see how it works!
#==============================================================================
#D2PDFlags.DPDMakerScripts.append("D2PDMaker/D2PD_Test.py")
#D2PDFlags.DPDMakerScripts.append("D2PDMaker/D2PD_ExampleSimpleZee.py")
#D2PDFlags.DPDMakerScripts.append("D2PDMaker/D2PD_ExampleSimpleZtautau.py")
#D2PDFlags.DPDMakerScripts.append("D2PDMaker/D2PD_ExampleSimpleHgamgam.py")
#D2PDFlags.DPDMakerScripts.append("D2PDMaker/D2PD_ExampleSimpleWmunu.py")
#D2PDFlags.DPDMakerScripts.append("D2PDMaker/D2PD_ZeeStream.py")
#D2PDFlags.DPDMakerScripts.append("D2PDMaker/D2PD_WenuStream.py")
#D2PDFlags.DPDMakerScripts.append("myFirstD2PD.py")
#D2PDFlags.DPDMakerScripts.append("eeSkim.py")
D2PDFlags.DPDMakerScripts.append("gmsbAnalysis/refine_ee_g10_looseSkim.py")

#==============================================================================
# Load your input file
#==============================================================================
from glob import glob

from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
#athenaCommonFlags.FilesInput=glob("/data3/jmitrevs/mc09_7TeV.114007.SPS8_110_jimmy_susy.merge.AOD.e530_s765_s767_r1302_r1306_tid140030_00/AOD.*1.pool.*")

inputList = glob("/data3/jmitrevs/dataskims/ee/user.jmitrevs*periodE[12]*/*pool.root*")
inputList.extend(glob("/data3/jmitrevs/dataskims/ee/user.jmitrevs*period[ABCD]*/*pool.root*"))

## for messaging
from AthenaCommon.Logging import logging
my_msg = logging.getLogger( 'myTopLogger' )
my_msg.info( 'running over the following files:\n' )
my_msg.info( inputList )

athenaCommonFlags.FilesInput=inputList


#==============================================================================
# You can change the location and name of your output file with
# these three flags:
#==============================================================================
#D2PDFlags.OutputDirectoryName = "/my/directory/with/enough/space/"


#==============================================================================
# Set the number of events that you want to process
#==============================================================================
#athenaCommonFlags.SkipEvents.set_Value_and_Lock(0)
#athenaCommonFlags.EvtMax.set_Value_and_Lock(2)
if not vars().has_key('EvtMax'): EvtMax = -1
athenaCommonFlags.EvtMax=EvtMax


#==============================================================================
# Execute the dpd maker
#==============================================================================
from RecExConfig.RecFlags import rec
# Turn off most of RecExCommon... (optional)
rec.doCBNT       = False
rec.doWriteESD   = False
rec.doWriteAOD   = False
rec.doAOD        = False
rec.doWriteTAG   = False 
rec.doPerfMon    = False
rec.doHist       = False
rec.doTruth      = False
#rec.LoadGeometry = False

# Mandatory for ESD->DPD
rec.doDPD   = True
rec.DPDMakerScripts.append("D2PDMaker/D2PDMaker.py")

# The job starts here!
include ("RecExCommon/RecExCommon_topOptions.py")


