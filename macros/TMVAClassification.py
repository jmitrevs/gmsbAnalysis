#!/usr/bin/env python
# File to choose optimal cuts for the lepton+photon analysi

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
        path = "/data3/jmitrevs/lepphoton/elphoton_ntuple2/mergedFiles/"

        wino_600_200FileName = path + "wino_600_200_el.root"
        wino_600_500FileName = path + "wino_600_500_el.root"
        wino_1000_200FileName = path + "wino_1000_200_el.root"
        wino_1500_300FileName = path + "wino_1500_300_el.root"
        
        WlepnuFileName_Np0 = path + "Wenu_Np0.root"
        WlepnuFileName_Np1 = path + "Wenu_Np1.root"
        WlepnuFileName_Np2 = path + "Wenu_Np2.root"
        WlepnuFileName_Np3 = path + "Wenu_Np3.root"
        WlepnuFileName_Np4 = path + "Wenu_Np4.root"
        WlepnuFileName_Np5 = path + "Wenu_Np5.root"

        ZleplepFileName_Np0 = path + "Zee_Np0.root"
        ZleplepFileName_Np1 = path + "Zee_Np1.root"
        ZleplepFileName_Np2 = path + "Zee_Np2.root"
        ZleplepFileName_Np3 = path + "Zee_Np3.root"
        ZleplepFileName_Np4 = path + "Zee_Np4.root"
        ZleplepFileName_Np5 = path + "Zee_Np5.root"

        st_tchan_lepnuFileName   = path + "st_tchan_enu.root"
        st_schan_lepnuFileName   = path + "st_schan_enu.root"
        ZleplepgammaFileName = path + "Zeegamma.root"

    elif lepton == MUON:

        print "Lepton is MUON."
        path = "/data3/jmitrevs/lepphoton/old/mergedFiles/"

        wino_600_200FileName = path + "wino_600_200_mu.root"
        wino_600_500FileName = path + "wino_600_500_mu.root"
        wino_1000_200FileName = path + "wino_1000_200_mu.root"
        wino_1500_300FileName = path + "wino_1500_300_mu.root"

        WlepnuFileName_Np0 = path + "Wmunu_Np0.root"
        WlepnuFileName_Np1 = path + "Wmunu_Np1.root"
        WlepnuFileName_Np2 = path + "Wmunu_Np2.root"
        WlepnuFileName_Np3 = path + "Wmunu_Np3.root"
        WlepnuFileName_Np4 = path + "Wmunu_Np4.root"
        WlepnuFileName_Np5 = path + "Wmunu_Np5.root"

        ZleplepFileName_Np0 = path + "Zmumu_Np0.root"
        ZleplepFileName_Np1 = path + "Zmumu_Np1.root"
        ZleplepFileName_Np2 = path + "Zmumu_Np2.root"
        ZleplepFileName_Np3 = path + "Zmumu_Np3.root"
        ZleplepFileName_Np4 = path + "Zmumu_Np4.root"
        ZleplepFileName_Np5 = path + "Zmumu_Np5.root"

        st_tchan_lepnuFileName   = path + "st_tchan_munu.root"
        st_schan_lepnuFileName   = path + "st_schan_munu.root"
        ZleplepgammaFileName = path + "Zeegamma.root"

    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")

    
    WtaunuFileName_Np0 = path + "Wtaunu_Np0.root"
    WtaunuFileName_Np1 = path + "Wtaunu_Np1.root"
    WtaunuFileName_Np2 = path + "Wtaunu_Np2.root"
    WtaunuFileName_Np3 = path + "Wtaunu_Np3.root"
    WtaunuFileName_Np4 = path + "Wtaunu_Np4.root"
    WtaunuFileName_Np5 = path + "Wtaunu_Np5.root"

    ZtautauFileName_Np0 = path + "Ztautau_Np0.root"
    ZtautauFileName_Np1 = path + "Ztautau_Np1.root"
    ZtautauFileName_Np2 = path + "Ztautau_Np2.root"
    ZtautauFileName_Np3 = path + "Ztautau_Np3.root"
    ZtautauFileName_Np4 = path + "Ztautau_Np4.root"
    ZtautauFileName_Np5 = path + "Ztautau_Np5.root"

    st_tchan_taunuFileName = path + "st_tchan_taunu.root"    
    st_schan_taunuFileName = path + "st_schan_taunu.root"
    st_WtFileName   = path + "st_Wt.root"    
    
    WgammaFileName_Np0 = path + "Wgamma_Np0.root"
    WgammaFileName_Np1 = path + "Wgamma_Np1.root"
    WgammaFileName_Np2 = path + "Wgamma_Np2.root"
    WgammaFileName_Np3 = path + "Wgamma_Np3.root"
    WgammaFileName_Np4 = path + "Wgamma_Np4.root"
    WgammaFileName_Np5 = path + "Wgamma_Np5.root"
    
    ttbarFileName = path + "ttbar.root"

    WWFileName = path + "WW.root"
    WZFileName = path + "WZ.root"
    ZZFileName = path + "ZZ.root"

    ZtautaugammaFileName = path + "Ztautaugamma.root"

    
    ###########################################

    
    wino_600_200File = TFile(wino_600_200FileName)
    wino_600_500File = TFile(wino_600_500FileName)
    wino_1000_200File = TFile(wino_1000_200FileName)
    wino_1500_300File = TFile(wino_1500_300FileName)

    WlepnuFile_Np0 = TFile(WlepnuFileName_Np0)
    WlepnuFile_Np1 = TFile(WlepnuFileName_Np1)
    WlepnuFile_Np2 = TFile(WlepnuFileName_Np2)
    WlepnuFile_Np3 = TFile(WlepnuFileName_Np3)
    WlepnuFile_Np4 = TFile(WlepnuFileName_Np4)
    WlepnuFile_Np5 = TFile(WlepnuFileName_Np5)
    
    WtaunuFile_Np0 = TFile(WtaunuFileName_Np0)
    WtaunuFile_Np1 = TFile(WtaunuFileName_Np1)
    WtaunuFile_Np2 = TFile(WtaunuFileName_Np2)
    WtaunuFile_Np3 = TFile(WtaunuFileName_Np3)
    WtaunuFile_Np4 = TFile(WtaunuFileName_Np4)
    WtaunuFile_Np5 = TFile(WtaunuFileName_Np5)

    ZleplepFile_Np0 = TFile(ZleplepFileName_Np0)
    ZleplepFile_Np1 = TFile(ZleplepFileName_Np1)
    ZleplepFile_Np2 = TFile(ZleplepFileName_Np2)
    ZleplepFile_Np3 = TFile(ZleplepFileName_Np3)
    ZleplepFile_Np4 = TFile(ZleplepFileName_Np4)
    ZleplepFile_Np5 = TFile(ZleplepFileName_Np5)
    
    ZtautauFile_Np0 = TFile(ZtautauFileName_Np0)
    ZtautauFile_Np1 = TFile(ZtautauFileName_Np1)
    ZtautauFile_Np2 = TFile(ZtautauFileName_Np2)
    ZtautauFile_Np3 = TFile(ZtautauFileName_Np3)
    ZtautauFile_Np4 = TFile(ZtautauFileName_Np4)
    ZtautauFile_Np5 = TFile(ZtautauFileName_Np5)
    
    WgammaFile_Np0 = TFile(WgammaFileName_Np0)
    WgammaFile_Np1 = TFile(WgammaFileName_Np1)
    WgammaFile_Np2 = TFile(WgammaFileName_Np2)
    WgammaFile_Np3 = TFile(WgammaFileName_Np3)
    WgammaFile_Np4 = TFile(WgammaFileName_Np4)
    WgammaFile_Np5 = TFile(WgammaFileName_Np5)
    
    ttbarFile = TFile(ttbarFileName)
    
    st_tchan_lepnuFile   = TFile(st_tchan_lepnuFileName)
    st_tchan_taunuFile = TFile(st_tchan_taunuFileName)
    
    st_schan_lepnuFile   = TFile(st_schan_lepnuFileName)
    st_schan_taunuFile = TFile(st_schan_taunuFileName)
    
    st_WtFile   = TFile(st_WtFileName)

    WWFile = TFile(WWFileName)
    WZFile = TFile(WZFileName)
    ZZFile = TFile(ZZFileName)
    
    ZleplepgammaFile = TFile(ZleplepgammaFileName)
    ZtautaugammaFile = TFile(ZtautaugammaFileName)

    ###########################################

    
    wino_600_200Tree = wino_600_200File.Get("GammaLepton")
    wino_600_500Tree = wino_600_500File.Get("GammaLepton")
    wino_1000_200Tree = wino_1000_200File.Get("GammaLepton")
    wino_1500_300Tree = wino_1500_300File.Get("GammaLepton")

    WlepnuTree_Np0 = WlepnuFile_Np0.Get("GammaLepton")
    WlepnuTree_Np1 = WlepnuFile_Np1.Get("GammaLepton")
    WlepnuTree_Np2 = WlepnuFile_Np2.Get("GammaLepton")
    WlepnuTree_Np3 = WlepnuFile_Np3.Get("GammaLepton")
    WlepnuTree_Np4 = WlepnuFile_Np4.Get("GammaLepton")
    WlepnuTree_Np5 = WlepnuFile_Np5.Get("GammaLepton")
    
    WtaunuTree_Np0 = WtaunuFile_Np0.Get("GammaLepton")
    WtaunuTree_Np1 = WtaunuFile_Np1.Get("GammaLepton")
    WtaunuTree_Np2 = WtaunuFile_Np2.Get("GammaLepton")
    WtaunuTree_Np3 = WtaunuFile_Np3.Get("GammaLepton")
    WtaunuTree_Np4 = WtaunuFile_Np4.Get("GammaLepton")
    WtaunuTree_Np5 = WtaunuFile_Np5.Get("GammaLepton")

    ZleplepTree_Np0 = ZleplepFile_Np0.Get("GammaLepton")
    ZleplepTree_Np1 = ZleplepFile_Np1.Get("GammaLepton")
    ZleplepTree_Np2 = ZleplepFile_Np2.Get("GammaLepton")
    ZleplepTree_Np3 = ZleplepFile_Np3.Get("GammaLepton")
    ZleplepTree_Np4 = ZleplepFile_Np4.Get("GammaLepton")
    ZleplepTree_Np5 = ZleplepFile_Np5.Get("GammaLepton")
    
    ZtautauTree_Np0 = ZtautauFile_Np0.Get("GammaLepton")
    ZtautauTree_Np1 = ZtautauFile_Np1.Get("GammaLepton")
    ZtautauTree_Np2 = ZtautauFile_Np2.Get("GammaLepton")
    ZtautauTree_Np3 = ZtautauFile_Np3.Get("GammaLepton")
    ZtautauTree_Np4 = ZtautauFile_Np4.Get("GammaLepton")
    ZtautauTree_Np5 = ZtautauFile_Np5.Get("GammaLepton")
    
    WgammaTree_Np0 = WgammaFile_Np0.Get("GammaLepton")
    WgammaTree_Np1 = WgammaFile_Np1.Get("GammaLepton")
    WgammaTree_Np2 = WgammaFile_Np2.Get("GammaLepton")
    WgammaTree_Np3 = WgammaFile_Np3.Get("GammaLepton")
    WgammaTree_Np4 = WgammaFile_Np4.Get("GammaLepton")
    WgammaTree_Np5 = WgammaFile_Np5.Get("GammaLepton")
    
    ttbarTree = ttbarFile.Get("GammaLepton")
    
    st_tchan_lepnuTree   = st_tchan_lepnuFile.Get("GammaLepton")
    st_tchan_taunuTree = st_tchan_taunuFile.Get("GammaLepton")
    
    st_schan_lepnuTree   = st_schan_lepnuFile.Get("GammaLepton")
    st_schan_taunuTree = st_schan_taunuFile.Get("GammaLepton")
    
    st_WtTree   = st_WtFile.Get("GammaLepton")

    WWTree = WWFile.Get("GammaLepton")
    WZTree = WZFile.Get("GammaLepton")
    ZZTree = ZZFile.Get("GammaLepton")
    
    ZleplepgammaTree = ZleplepgammaFile.Get("GammaLepton")
    ZtautaugammaTree = ZtautaugammaFile.Get("GammaLepton")
    
    ##############################
    # and now the weights

    # wino_600_200_scale = 7.005
    # wino_600_500_scale = 3.03021
    # wino_1000_200_scale = 4.1325
    # wino_1500_300_scale = 0.16
    # Wlepnu_Np0_scale = 12.0052623622
    # Wlepnu_Np1_scale = 3.13076456857
    # Wlepnu_Np2_scale = 0.60296853897
    # Wlepnu_Np3_scale = 0.603183318846
    # Wlepnu_Np4_scale = 0.62088
    # Wlepnu_Np5_scale = 0.600008571551
    # Wtaunu_Np0_scale = 12.1457006649
    # Wtaunu_Np1_scale = 3.12868868923
    # Wtaunu_Np2_scale = 0.602359552172
    # Wtaunu_Np3_scale = 0.602586672951
    # Wtaunu_Np4_scale = 0.62088496708
    # Wtaunu_Np5_scale = 0.638769230769
    # Zleplep_Np0_scale = 0.631361988532
    # Zleplep_Np1_scale = 0.629541167757
    # Zleplep_Np2_scale = 0.625618828688
    # Zleplep_Np3_scale = 0.634090909091
    # Zleplep_Np4_scale = 0.6
    # Zleplep_Np5_scale = 0.51875
    # Ztautau_Np0_scale = 0.631228327261
    # Ztautau_Np1_scale = 0.631347664299
    # Ztautau_Np2_scale = 0.622916409433
    # Ztautau_Np3_scale = 0.640077378243
    # Ztautau_Np4_scale = 0.581269375646
    # Ztautau_Np5_scale = 0.48125
    # Wgamma_Np0_scale = 0.0129441737417
    # Wgamma_Np1_scale = 0.0635170304401
    # Wgamma_Np2_scale = 0.140920227273
    # Wgamma_Np3_scale = 0.140622611111
    # Wgamma_Np4_scale = 0.134589
    # Wgamma_Np5_scale = 0.123308
    # ttbar_scale = 0.0384505023442
    # st_tchan_lepnu_scale = 0.200916540624
    # st_tchan_taunu_scale = 0.201132004918
    # st_schan_lepnu_scale = 0.0092735093327
    # st_schan_taunu_scale = 0.00926981472204
    # st_Wt_scale = 0.0916407781992
    # WW_scale = 0.0342151663714
    # WZ_scale = 0.110873818259
    # ZZ_scale = 0.0252773011092
    # Zleplepgamma_scale = 0.963
    # Ztautaugamma_scale = 0.941960800016

    #################ntuple_pt25
    # wino_600_200_scale = 1.401
    # wino_600_500_scale = 3.03021
    # wino_1000_200_scale = 4.1325
    # wino_1500_300_scale = 0.16
    # Wlepnu_Np0_scale = 12.0052623622
    # Wlepnu_Np1_scale = 3.13076456857
    # Wlepnu_Np2_scale = 0.60296853897
    # Wlepnu_Np3_scale = 0.603183318846
    # Wlepnu_Np4_scale = 0.62088
    # Wlepnu_Np5_scale = 0.600008571551
    # Wtaunu_Np0_scale = 12.1457006649
    # Wtaunu_Np1_scale = 3.12868868923
    # Wtaunu_Np2_scale = 0.602359552172
    # Wtaunu_Np3_scale = 0.602586672951
    # Wtaunu_Np4_scale = 0.62088496708
    # Wtaunu_Np5_scale = 0.638769230769
    # Zleplep_Np0_scale = 0.631361988532
    # Zleplep_Np1_scale = 0.629541167757
    # Zleplep_Np2_scale = 0.625618828688
    # Zleplep_Np3_scale = 0.634090909091
    # Zleplep_Np4_scale = 0.6
    # Zleplep_Np5_scale = 0.51875
    # Ztautau_Np0_scale = 0.631228327261
    # Ztautau_Np1_scale = 0.631347664299
    # Ztautau_Np2_scale = 0.622916409433
    # Ztautau_Np3_scale = 0.640077378243
    # Ztautau_Np4_scale = 0.581269375646
    # Ztautau_Np5_scale = 0.48125
    # Wgamma_Np0_scale = 1.08706263428
    # Wgamma_Np1_scale = 0.734676952566
    # Wgamma_Np2_scale = 0.733754057143
    # Wgamma_Np3_scale = 0.149752323594
    # Wgamma_Np4_scale = 0.157524392683
    # Wgamma_Np5_scale = 0.1281354
    # ttbar_scale = 0.0384505023442
    # st_tchan_lepnu_scale = 0.200916540624
    # st_tchan_taunu_scale = 0.201132004918
    # st_Wt_scale = 0.0916407781992
    # WW_scale = 0.0342151663714
    # WZ_scale = 0.110873818259
    # ZZ_scale = 0.0252773011092
    # Zleplepgamma_scale = 0.963
    # Ztautaugamma_scale = 0.941960800016
    # gamma_Np1_scale = 4.06453310851
    # gamma_Np2_scale = 3.3709968686
    # gamma_Np3_scale = 1.38728943513
    # gamma_Np4_scale = 1.41464077802
    # gamma_Np5_scale = 1.23661096137

    wino_600_200_scale = 1.1675
    wino_600_500_scale = 2.69352
    wino_1000_200_scale = 4.1325
    wino_1500_300_scale = 0.0093269
    wino_1000_100_scale = 69.5
    wino_800_700_scale = 0.2328
    Wlepnu_Np0_scale = 12.0052623622
    Wlepnu_Np1_scale = 3.13076456857
    Wlepnu_Np2_scale = 0.60296853897
    Wlepnu_Np3_scale = 0.603183318846
    Wlepnu_Np4_scale = 0.62088
    Wlepnu_Np5_scale = 0.600008571551
    Wtaunu_Np0_scale = 12.1457006649
    Wtaunu_Np1_scale = 3.12868868923
    Wtaunu_Np2_scale = 0.602359552172
    Wtaunu_Np3_scale = 0.602586672951
    Wtaunu_Np4_scale = 0.62088496708
    Wtaunu_Np5_scale = 0.638769230769
    Zleplep_Np0_scale = 0.631361988532
    Zleplep_Np1_scale = 0.629541167757
    Zleplep_Np2_scale = 0.625618828688
    Zleplep_Np3_scale = 0.634090909091
    Zleplep_Np4_scale = 0.6
    Zleplep_Np5_scale = 0.51875
    Ztautau_Np0_scale = 0.631228327261
    Ztautau_Np1_scale = 0.631347664299
    Ztautau_Np2_scale = 0.622916409433
    Ztautau_Np3_scale = 0.640077378243
    Ztautau_Np4_scale = 0.581269375646
    Ztautau_Np5_scale = 0.48125
    Wgamma_Np0_scale = 0.0132834003639
    Wgamma_Np1_scale = 0.0651816146862
    Wgamma_Np2_scale = 0.144613309091
    Wgamma_Np3_scale = 0.144307893333
    Wgamma_Np4_scale = 0.13811616
    Wgamma_Np5_scale = 0.12653952
    ttbar_scale = 0.0384505023442
    st_tchan_lepnu_scale = 0.200916540624
    st_tchan_taunu_scale = 0.201132004918
    st_Wt_scale = 0.0916407781992
    WW_scale = 0.0342151663714
    WZ_scale = 0.110873818259
    ZZ_scale = 0.0252773011092
    Zleplepgamma_scale = 0.963
    Ztautaugamma_scale = 0.941960800016
    gamma_Np1_scale = 4.17064063358
    gamma_Np2_scale = 3.35244054801
    gamma_Np3_scale = 1.36994217452
    gamma_Np4_scale = 1.41464077802
    gamma_Np5_scale = 1.23661096137


    if signal == "600_200":
        factory.AddSignalTree(wino_600_200Tree, wino_600_200_scale)
    elif signal == "600_500":
        factory.AddSignalTree(wino_600_500Tree, wino_600_500_scale)
    elif signal == "1000_200":
        factory.AddSignalTree(wino_1000_200Tree, wino_1000_200_scale)
    elif signal == "1500_300":
        factory.AddSignalTree(wino_1500_300Tree, wino_1500_300_scale)
    else:
        print "*** signal designation not supported: %s ****" % signal
        sys.exit(1)

    factory.AddBackgroundTree(WlepnuTree_Np0, Wlepnu_Np0_scale)
    factory.AddBackgroundTree(WlepnuTree_Np1, Wlepnu_Np1_scale)
    factory.AddBackgroundTree(WlepnuTree_Np2, Wlepnu_Np2_scale)
    factory.AddBackgroundTree(WlepnuTree_Np3, Wlepnu_Np3_scale)
    factory.AddBackgroundTree(WlepnuTree_Np4, Wlepnu_Np4_scale)
    factory.AddBackgroundTree(WlepnuTree_Np5, Wlepnu_Np5_scale)
    
    #factory.AddBackgroundTree(WtaunuTree_Np0, Wtaunu_Np0_scale)
    factory.AddBackgroundTree(WtaunuTree_Np1, Wtaunu_Np1_scale)
    factory.AddBackgroundTree(WtaunuTree_Np2, Wtaunu_Np2_scale)
    factory.AddBackgroundTree(WtaunuTree_Np3, Wtaunu_Np3_scale)
    factory.AddBackgroundTree(WtaunuTree_Np4, Wtaunu_Np4_scale)
    factory.AddBackgroundTree(WtaunuTree_Np5, Wtaunu_Np5_scale)

    factory.AddBackgroundTree(ZleplepTree_Np0, Zleplep_Np0_scale)
    factory.AddBackgroundTree(ZleplepTree_Np1, Zleplep_Np1_scale)
    factory.AddBackgroundTree(ZleplepTree_Np2, Zleplep_Np2_scale)
    factory.AddBackgroundTree(ZleplepTree_Np3, Zleplep_Np3_scale)
    factory.AddBackgroundTree(ZleplepTree_Np4, Zleplep_Np4_scale)
    factory.AddBackgroundTree(ZleplepTree_Np5, Zleplep_Np5_scale)
    
    factory.AddBackgroundTree(ZtautauTree_Np0, Ztautau_Np0_scale)
    factory.AddBackgroundTree(ZtautauTree_Np1, Ztautau_Np1_scale)
    factory.AddBackgroundTree(ZtautauTree_Np2, Ztautau_Np2_scale)
    factory.AddBackgroundTree(ZtautauTree_Np3, Ztautau_Np3_scale)
    factory.AddBackgroundTree(ZtautauTree_Np4, Ztautau_Np4_scale)
    factory.AddBackgroundTree(ZtautauTree_Np5, Ztautau_Np5_scale)
    
    factory.AddBackgroundTree(WgammaTree_Np0, Wgamma_Np0_scale)
    factory.AddBackgroundTree(WgammaTree_Np1, Wgamma_Np1_scale)
    factory.AddBackgroundTree(WgammaTree_Np2, Wgamma_Np2_scale)
    factory.AddBackgroundTree(WgammaTree_Np3, Wgamma_Np3_scale)
    factory.AddBackgroundTree(WgammaTree_Np4, Wgamma_Np4_scale)
    factory.AddBackgroundTree(WgammaTree_Np5, Wgamma_Np5_scale)
    
    factory.AddBackgroundTree(ttbarTree, ttbar_scale)
    
    factory.AddBackgroundTree(st_tchan_lepnuTree, st_tchan_lepnu_scale)
    factory.AddBackgroundTree(st_tchan_taunuTree, st_tchan_taunu_scale)
    
    # factory.AddBackgroundTree(st_schan_lepnuTree, st_schan_lepnu_scale)
    # factory.AddBackgroundTree(st_schan_taunuTree, st_schan_taunu_scale)
    
    factory.AddBackgroundTree(st_WtTree, st_Wt_scale)

    factory.AddBackgroundTree(WWTree, WW_scale)
    factory.AddBackgroundTree(WZTree, WZ_scale)
    factory.AddBackgroundTree(ZZTree, ZZ_scale)
    
    factory.AddBackgroundTree(ZleplepgammaTree, Zleplepgamma_scale)
    factory.AddBackgroundTree(ZtautaugammaTree, Ztautaugamma_scale)
    


    # note that you may also use variable expressions, such as: "3*var1/var2*abs(var3)"
    # [all types of expressions that can also be parsed by TTree::Draw( "expression" )]
    factory.AddVariable( "MET := sqrt(Metx*Metx+Mety*Mety)", 'F' )
    factory.AddVariable( "HT", 'F' )
    factory.AddVariable( "PhotonPt[0]", 'F' )
    #factory.AddVariable( "ElectronPt[0]", 'F' )
    factory.AddVariable( "mTel", 'F' )
    #factory.AddVariable( "abs(PhotonEta[0])", 'F' )
    #factory.AddVariable( "abs(ElectronEta[0])", 'F' )

    # Apply additional cuts on the signal and background sample. 
    # example for cut: mycut = TCut( "abs(var1)<0.5 && abs(var2-0.5)<1" )
    mycutSig = TCut( "abs(PhotonEta[0]) < 2.01 && abs(ElectronEta[0]) < 2.01" ) 
    #mycutSig = TCut( "sqrt(Metx*Metx+Mety*Mety) > 115000" ) 
    mycutBkg = TCut( "" ) 
    
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
