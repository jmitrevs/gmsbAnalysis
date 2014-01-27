# configure athena to read flat n-tuples
import AthenaRootComps.ReadAthenaRoot

#--------------------------------------------------------------
# Templated Parameters
#--------------------------------------------------------------

from glob import glob
InputList = glob('/data3/jmitrevs/mc12_8TeV.164439.MadGraphPythia_AUET2BCTEQ6L1*/*root*')

svcMgr.EventSelector.InputCollections = InputList

# the n-tuple name in the input files to read data from
svcMgr.EventSelector.TupleName = "susy"

# ==============================================================================
# Set the number of events that you want to process (-1 means all events) or skip.
# Shown is a handy way how you can use command-line options.
# If EVTMAX is not given on the command line, the default -1 (process all events) is used.
# This works for any command line option that you may need; it is a python feature.
# ==============================================================================
if not vars().has_key('EVTMAX'): EVTMAX = -1
theApp.EvtMax = EVTMAX
#theApp.EvtMax = 3

#svcMgr.EventSelector.SkipEvents = 5000


# getting a handle on the alg sequence
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()


# add the selection
include ( "gmsbTools/gmsbTools_jobOptions.py" )

import PyCintex
PyCintex.loadDictionary('egammaEnumsDict')
from ROOT import egammaPID

#if not 'RANDSEED' in dir():
#    RANDSEED = 0

#print "random seed", RANDSEED

gmsbSelectionTool.IsMC = True
gmsbSelectionTool.SmearMC = True
#gmsbSelectionTool.ElectronPt = 25*GeV
#gmsbSelectionTool.PhotonPt = 100*GeV
#gmsbSelectionTool.MuonPt = 25*GeV
#gmsbSelectionTool.OutputLevel = DEBUG
#gmsbSelectionTool.RandomSeed = RANDSEED
#gmsbSelectionTool.MCEtconeShift = 0.0;
#gmsbSelectionTool.PhotonIsEM = egammaPID.PhotonTight

gmsbFinalSelectionTool.IsMC = True
gmsbFinalSelectionTool.SmearMC = False

# from gmsbTools.gmsbToolsConf import TruthStudies
# truthStudies = TruthStudies(name = "TruthStudies",
#                             PrintDecayTree = False,
#                             UseAnnotated = False,
#                             DumpEntireTree = False,
#                             #Ptcut = 8*GeV,
#                             doDeltaRLepton = False,
#                             #OutputLevel = DEBUG
#                             )
# ToolSvc += truthStudies
# print truthStudies

# # add the MET systematics
# include ( "gmsbAnalysis/METSystematics.py" )

from gmsbAnalysis.gmsbAnalysisConf import Testing
testAlg = Testing(name = "Testing",
                            isMC = True,
                            PreparationTool = gmsbPreparationTool,
                            FinalSelectionTool = gmsbFinalSelectionTool,
                            OverlapRemovalTool1 = gmsbOverlapRemovalTool1,
                            OverlapRemovalTool2 = gmsbOverlapRemovalTool2,
                            #JetCleaningTool = myJetCleaningTool,
                            applyTrigger = True,
                            NumPhotons = 1,
                            NumElectrons = 1,
                            outputNtuple = True,
                            # doTruthStudies = True,
                            # TruthStudiesTool = truthStudies,
                            # DoEtMissSystematics = False,
                            # DoEtMissMuonSystematics = False,
                            #EtMissSystematicsTool = myEtMissSystematicsTool,
                            #EtMissMuonSystematicsTool = myEtMissMuonSystematicsTool,
                  printEvents = [1756,
1780,
2425,
2521,
8052,
8770,
10971,
11366,
16328,
16622,
16656,
16857,
17365,
18457,
19047,
19510,
19743,
23466,
23543,
24222,
26280,
29157,
31803,
33217,
35053,
37295,
37995,
38553,
40611,
42085,
42802,
42809,
49718,
49907,
49974,
49975,
50862,
56640,
61192,
62356,
64956,
66446,
67024,
67336,
68727,
69426,
70848,
72532,
72611,
73671,
73765,
75112,
77511,
81646,
84457,
86695,
87073,
87969,
88955,
89759,
89835,
89943,
90991,
92646,
93049,
94264,
94638,
96065,
98609,
99689,
102108,
106711,
107850,
108368,
108474,
109239,
109451,
110348,
112951,
113690,
114163,
114199,
114200,
119444,
119864,
120388,
120640,
120643,
122715,
127191,
127461,
128946,
133111,
133342,
134916,
137254,
140424,
151575,
153167,
155613,
155730,
156986,
159880,
161428,
167390,
169773,
170730,
171509,
172050,
175921,
176699,
179225,
181123,
181337,
181727,
182016,
183228,
185102,
185114,
185437,
185686,
192790]

                            )
from AthenaCommon.AppMgr import ToolSvc
#testAlg.OutputLevel = DEBUG
testAlg.OutputLevel = INFO

# Add example to Reader
topSequence += testAlg
print testAlg

#--------------------------------------------------------------
# Add Dictionary for writing out in PoolDPDs
#--------------------------------------------------------------
#AthenaSealSvc = Service( "AthenaSealSvc" )
#include( "AthenaSealSvc/AthenaSealSvc_joboptions.py" )
#include ( "InsituEvent/InsituEventDict_joboptions.py" )

#--------------------------------------------------------------
# Event related parameters
#--------------------------------------------------------------

ServiceMgr.MessageSvc.OutputLevel = WARNING

#==============================================================
#==============================================================
# setup TTree registration Service
# save ROOT histograms and Tuple
from GaudiSvc.GaudiSvcConf import THistSvc
ServiceMgr += THistSvc()
ServiceMgr.THistSvc.Output = ["Testing DATAFILE='Testing.root' OPT='RECREATE'"]

