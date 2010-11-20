##-----------------------------------------------------------------------------
## Name: D2PD_ExampleSimpleHgamgam.py
##
## Author: Karsten Koeneke (DESY)
## Email:  karsten.koeneke@desy.de
##
## Description: This defines the content of the D2PD after skimmit two loose photons
##
##-----------------------------------------------------------------------------

## Import the module that allows to use named units, e.g. GeV
import AthenaCommon.SystemOfUnits as Units

## Include the job property flags for this package and from RecExCommon
from D2PDMaker.D2PDFlags import D2PDFlags

## This handels multiple output streams
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr 



#====================================================================
# Define the individual particle selections
#====================================================================
# - the electron selector
# Load the actual filter
from D2PDMaker.D2PDMakerConf import D2PDPhotonSelector, D2PDElectronSelector
# Create an instance of this filter, configure it, and add it to the AlgSequence

topSequence += D2PDElectronSelector( "DiElectronSelector",
                                     OutputLevel                      = INFO,
                                     inputCollection                  = 'ElectronAODCollection',
                                     outputLinkCollection             = 'SelectedDiElectronLinkCollection',
                                     minNumberPassed                  = 2,
                                     electronIsEM                     = egammaPID.ElectronMedium_WithTrackMatch,
                                     etMin                            = 20.0*Units.GeV,
                                     electronAuthor       = egammaParameters.AuthorElectron,
                                     clusterEMCaloLayerEtaMin = -2.5,
                                     clusterEMCaloLayerEtaMax = 2.5,
                                     clusterEMCaloLayer   = 2,
                                     )

topSequence += D2PDElectronSelector( "HighPtElectronSelector",
                                     OutputLevel                      = INFO,
                                     inputCollection                  = 'SelectedDiElectronLinkCollection',
                                     outputLinkCollection             = 'SelectedHighPtLinkCollection',
                                     minNumberPassed                  = 1,
                                     etMin                            = 30.0*Units.GeV,
                                     )


#====================================================================
# Define the trigger selection
#====================================================================
include("PrimaryDPDMaker/SetupTrigDecisionTool.py")
from PrimaryDPDMaker.TriggerFilter import TriggerFilter
topSequence += TriggerFilter( "D2PDTriggerFilterGMSB",
                              trigger = "EF_g10_loose"
                              )



#====================================================================
# Define the test DPD output stream
#====================================================================
from D2PDMaker.D2PDHelpers import buildFileName
# This stream HAS TO start with "StreamD2AOD_"! If the input was an (D)ESD(M), this should start with "StreamD2ESD(M)_".
# See this twiki for more information: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/DPDNamingConvention
streamName = "StreamD2AOD_GMSB"
fileName   = D2PDFlags.OutputDirectoryName() + "D2AOD_GMSBee2_g10_loose.pool.root"
SimpleGMSBStream = MSMgr.NewPoolStream( streamName, fileName )

# Only events that pass the filters listed below are written out
# AcceptAlgs  = logical OR of filters
# RequireAlgs = logical AND of filters
SimpleGMSBStream.AcceptAlgs( ["DiElectronSelector", "HighPtElectronSelector", "D2PDTriggerFilterGMSB"] )


#---------------------------------------------------
# Add the containers to the output stream
#---------------------------------------------------
from PrimaryDPDMaker import PrimaryDPD_OutputDefinitions as dpdOutput

# Take all items from the input, except for the ones listed in the excludeList
# If the excludeList is empty, all containers from the input file (e.g. AOD)
# are copied to the output file.
excludeList = []
excludeList = list(set(excludeList)) # This removes dublicates from the list
dpdOutput.addAllItemsFromInputExceptExcludeList( streamName, excludeList )


# You need to add your newly created output containers from above to the output stream
#SimpleGMSBStream.AddItem( ['CompositeParticleContainer#MyHgamgamLooseHgamgamBosonCollection'] )
SimpleGMSBStream.AddItem( ['INav4MomLinkContainer#SelectedDiElectronLinkCollection'] )




#====================================================================
# UserDataSvc
#====================================================================
#from AthenaServices.TheUserDataSvc import TheUserDataSvc
#svcMgr += TheUserDataSvc("UserDataInSimpleGMSBStream")
#svcMgr.UserDataInSimpleGMSBStream.OutputStream = SimpleGMSBStream.Stream
