# Set options for EtMissSystematicsTool
from DanGMSBAnaTools.DanGMSBAnaToolsConf import TopoSystematicsTool as ConfiguredTopoSystematicsTool
myEtMissSystematicsTool = ConfiguredTopoSystematicsTool(

    UsePrimaryVertex = True,
    UncertaintyBounds = 1.0,
    TopoClusterPtCut = -1.0E+30*MeV,
    UseEtaParametrization = True

)

ToolSvc += myEtMissSystematicsTool
print      myEtMissSystematicsTool

# Set options for EtMissMuonSystematicsTool
from DanGMSBAnaTools.DanGMSBAnaToolsConf import EtMissMuonSystematicsTool as ConfiguredEtMissMuonSystematicsTool
myEtMissMuonSystematicsTool = ConfiguredEtMissMuonSystematicsTool(

    IsoDeltaR = 0.3

)

ToolSvc += myEtMissMuonSystematicsTool
print      myEtMissMuonSystematicsTool
