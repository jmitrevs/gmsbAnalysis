#!/usr/bin/env python
# File to choose optimal cuts for the lepton+photon analysi

from __future__ import division

# --------------------------------------------
# Standard python import
import sys    # exit
import time   # time accounting
import getopt # command line parser

# --------------------------------------------

ELECTRON = 0
MUON = 1

# Default settings for command line arguments
DEFAULT_OUTFNAME = "TMVA.root"
DEFAULT_METHODS  = "Cuts"
DEFAULT_LEPTONNAME   = "electron"
DEFAULT_LEPTON   = ELECTRON
DEFAULT_SIGNAL   = "600_200"


# Print usage help
def usage():
    print " "
    print "Usage: python %s [options]" % sys.argv[0]
    print "  -m | --methods    : gives methods to be run (default: all methods)"
    print "  -o | --outputfile : name of output ROOT file containing results (default: '%s')" % DEFAULT_OUTFNAME
    print "  -l | --lepton     : which lepton (default: '%s')" % DEFAULT_LEPTONNAME
    print "  -s | --signal     : which gluino_wino combination to choose (default: '%s')" % DEFAULT_SIGNAL
    print "  -v | --verbose"
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"
    print " "

# Main routine
def main():

    try:
        # retrive command line options
        shortopts  = "m:o:l:s:vh?"
        longopts   = ["methods=", "outputfile=", "lepton=", "signal=", "verbose", "help", "usage"]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )

    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        usage()
        sys.exit(1)

    lepton = DEFAULT_LEPTON
    outfname    = DEFAULT_OUTFNAME
    methods     = DEFAULT_METHODS
    verbose     = False
    signal      = DEFAULT_SIGNAL
    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-m", "--methods"):
            methods = a
        elif o in ("-o", "--outputfile"):
            outfname = a
        elif o in ("-s", "--signal"):
            signal = a
        elif o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-l", "--lepton"):
            if a == "electron":
                lepton = ELECTRON
            elif a == "muon":
                lepton = MUON
            else:
                print "*** Lepton must be 'electron' or 'muon ****"
                sys.exit(1)


    # Print methods
    mlist = methods.replace(' ',',').split(',')
    print "=== TMVAClassification: use method(s)..."
    for m in mlist:
        if m.strip() != '':
            print "=== - <%s>" % m.strip()

    # Import ROOT classes
    from ROOT import gSystem, gROOT, gApplication, TFile, TTree, TCut
    
    # check ROOT version, give alarm if 5.18 
    if gROOT.GetVersionCode() >= 332288 and gROOT.GetVersionCode() < 332544:
        print "*** You are running ROOT version 5.18, which has problems in PyROOT such that TMVA"
        print "*** does not run properly (function calls with enums in the argument are ignored)."
        print "*** Solution: either use CINT or a C++ compiled version (see TMVA/macros or TMVA/examples),"
        print "*** or use another ROOT version (e.g., ROOT 5.19)."
        sys.exit(1)
    
    # Logon not automatically loaded through PyROOT (logon loads TMVA library) load also GUI
    gROOT.SetMacroPath( "./" )
    gROOT.Macro       ( "./TMVAlogon.C" )    
    gROOT.LoadMacro   ( "./TMVAGui.C" )
    
    # Import TMVA classes from ROOT
    from ROOT import TMVA

    # Output file
    outputFile = TFile( outfname, 'RECREATE' )
    
    # Create instance of TMVA factory (see TMVA/macros/TMVAClassification.C for more factory options)
    # All TMVA output can be suppressed by removing the "!" (not) in 
    # front of the "Silent" argument in the option string
    factory = TMVA.Factory( "TMVAClassification", outputFile, 
                            "!V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification" )

    # Set verbosity
    factory.SetVerbose( verbose )
    
    # let's open the input files
    if lepton == ELECTRON:

        print "Lepton is ELECTRON."
        sigpath = "/data3/jmitrevs/lepphoton_optimize/elphoton_grid/mergedFiles/"
        backpath = "/data3/jmitrevs/lepphoton_optimize/elphoton_ntuple/mergedFiles/"

        winoFileName = sigpath + "wino_800_500.root"
        
        WgammaFileName = backpath + "Wgamma_enu_sherpa.root"
        ttbarFileName = backpath + "ttbar.root"
        ttbargammaFileName = backpath + "ttbargamma.root"


    elif lepton == MUON:

        raise ValueError("Muon not yet implemented.")


    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")

        
    ###########################################

    
    winoFile = TFile(winoFileName)

    WgammaFile = TFile(WgammaFileName)
    ttbarFile = TFile(ttbarFileName)
    ttbargammaFile = TFile(ttbargammaFileName)
    

    ###########################################

    
    cutFlowwino = winoFile.Get("Global/CutFlow")
    cutFlowWgamma = WgammaFile.Get("Global/CutFlow")
    cutFlowttbar = ttbarFile.Get("Global/CutFlow")
    cutFlowttbargamma = ttbargammaFile.Get("Global/CutFlow")

    nOrigwino = cutFlowwino.GetBinContent(1)
    nOrigWgamma = cutFlowWgamma.GetBinContent(1)
    nOrigttbar = cutFlowttbar.GetBinContent(1)
    nOrigttbargamma = cutFlowttbargamma.GetBinContent(1)

    ##############################

    winoTree = winoFile.Get("GammaLepton")
    WgammaTree = WgammaFile.Get("GammaLepton")
    ttbarTree = ttbarFile.Get("GammaLepton")
    ttbargammaTree = ttbargammaFile.Get("GammaLepton")

    ##############################################
    #   scale is lumi * xsec * kfact * filter / numEvents

    Lumi = 21000.0

    #wino_scale = Lumi * 18.72 * 0.23765 / nOrigwino # 100 weak
    #wino_scale = Lumi * 1.192 * 0.23765 / nOrigwino # 200 weak
    #wino_scale = Lumi * 0.205 * 0.23765 / nOrigwino # 300 weak
    #wino_scale = Lumi * 0.0992 * 0.23765 / nOrigwino # 350 weak
    #wino_scale = Lumi * 0.0507 * 0.23765 / nOrigwino # 400 weak
    wino_scale = Lumi * 0.157 * 0.23765 / nOrigwino # 800_500 strong

    Wgamma_scale = Lumi * 5.5810E-01 * 1.43 / nOrigWgamma
    ttbar_scale          =  Lumi  *  79.01 * 1.146 * 1.43 / nOrigttbar
    ttbargamma_scale     =  Lumi  *  0.84 * 2.55 * 1.43 / nOrigttbargamma

    
    factory.AddSignalTree(winoTree, wino_scale)

    
    factory.AddBackgroundTree(WgammaTree, Wgamma_scale)
    factory.AddBackgroundTree(ttbarTree, ttbar_scale)
    factory.AddBackgroundTree(ttbargammaTree, ttbargamma_scale)
    

    # note that you may also use variable expressions, such as: "3*var1/var2*abs(var3)"
    # [all types of expressions that can also be parsed by TTree::Draw( "expression" )]
    factory.AddVariable( "MET := sqrt(Metx*Metx+Mety*Mety)", 'F' )
    # factory.AddVariable( "HT", 'F' )
    factory.AddVariable( "PhotonPt[0]", 'F' )
    #factory.AddVariable( "ElectronPt[0]", 'F' )
    if lepton == ELECTRON:
        factory.AddVariable( "mTel", 'F' )
    else:
        factory.AddVariable( "mTmu", 'F' )
    #factory.AddVariable( "abs(PhotonEta[0])", 'F' )
    #factory.AddVariable( "abs(ElectronEta[0])", 'F' )

    # Apply additional cuts on the signal and background sample. 
    # example for cut: mycut = TCut( "abs(var1)<0.5 && abs(var2-0.5)<1" )
    #mycutSig = TCut( "abs(PhotonEta[0]) < 2.01 && abs(ElectronEta[0]) < 2.01" ) 

    if lepton == ELECTRON:
        mycutSig = TCut( "sqrt((PhotonEta[0]-ElectronEta[0])*(PhotonEta[0]-ElectronEta[0]) + (PhotonPhi[0]-ElectronPhi[0])*(PhotonPhi[0]-ElectronPhi[0])) > 0.7")
        #mycutSig += TCut( "mTel > 110000" ) 
    else:
        mycutSig = TCut( "sqrt((PhotonEta[0]-MuonEta[0])*(PhotonEta[0]-MuonEta[0]) + (PhotonPhi[0]-MuonPhi[0])*(PhotonPhi[0]-MuonPhi[0])) > 0.7")
        #mycutSig += TCut( "mTmu > 110000" ) 
    mycutBkg = mycutSig 
    
    # Here, the relevant variables are copied over in new, slim trees that are
    # used for TMVA training and testing
    # "SplitMode=Random" means that the input events are randomly shuffled before
    # splitting them into training and test samples
    factory.PrepareTrainingAndTestTree( mycutSig, mycutBkg,
                                        "nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V" )

    # --------------------------------------------------------------------------------------------------

    # ---- Book MVA methods
    #
    # please lookup the various method configuration options in the corresponding cxx files, eg:
    # src/MethoCuts.cxx, etc, or here: http://tmva.sourceforge.net/optionRef.html
    # it is possible to preset ranges in the option string in which the cut optimisation should be done:
    # "...:CutRangeMin[2]=-1:CutRangeMax[2]=1"...", where [2] is the third input variable

    # Cut optimisation
    if "Cuts" in mlist:
        factory.BookMethod( TMVA.Types.kCuts, "Cuts",
                            "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart" )

    if "CutsD" in mlist:
        factory.BookMethod( TMVA.Types.kCuts, "CutsD",
                            "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=Decorrelate" )

    if "CutsPCA" in mlist:
        factory.BookMethod( TMVA.Types.kCuts, "CutsPCA",
                            "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=PCA" )

    # if "CutsGA" in mlist:
    #     factory.BookMethod( TMVA.Types.kCuts, "CutsGA",
    #                         "H:!V:FitMethod=GA:CutRangeMin[0]=-10:CutRangeMax[0]=10:VarProp[1]=FMax:EffSel:Steps=30:Cycles=3:PopSize=400:SC_steps=10:SC_rate=5:SC_factor=0.95" )

    # if "CutsSA" in mlist:
    #     factory.BookMethod( TMVA.Types.kCuts, "CutsSA",
    #                         "!H:!V:FitMethod=SA:EffSel:MaxCalls=150000:KernelTemp=IncAdaptive:InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" )


    # --------------------------------------------------------------------------------------------------
            
    # ---- Now you can tell the factory to train, test, and evaluate the MVAs. 

    # Train MVAs
    factory.TrainAllMethods()
    
    # Test MVAs
    factory.TestAllMethods()
    
    # Evaluate MVAs
    factory.EvaluateAllMethods()    
    
    # Save the output.
    outputFile.Close()
    
    print "=== wrote root file %s\n" % outfname
    print "=== TMVAClassification is done!\n"
    
    # open the GUI for the result macros    
    gROOT.ProcessLine( "TMVAGui(\"%s\")" % outfname )
    
    # keep the ROOT thread running
    gApplication.Run() 

# ----------------------------------------------------------

if __name__ == "__main__":
    main()
