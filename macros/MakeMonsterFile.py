#! /usr/bin/env python

# code to make all the plots in a file
import sys
import getopt
from glob import glob

import ROOT
ROOT.gROOT.SetBatch()
#ROOT.gROOT.LoadMacro("AtlasStyle.C") 
#ROOT.SetAtlasStyle()

from signalXsecsCombined import signalXsecsCombined



Blind = True

SIGMA = -1.0
#DEFAULTNAME = "LepPhoton.root"
#DEFAULTNAME = "LepPhoton_AllUncertsXsecPlus1Sigma.root"
DEFAULTNAME = "LepPhoton_AllUncertsXsecMinus1Sigma.root"

def MakeMonsterFile(outfile=DEFAULTNAME):

    f = ROOT.TFile("output_gl_wino.root")
    ttree = f.Get("SignalUncertainties")
    xsecs = signalXsecsCombined(ttree)

    f = ROOT.TFile(outfile, 'RECREATE')

    for lepton in ('El', 'Mu'):
        if lepton == 'El':
            import DataManagerElectronsSimple as DataManager
            sigpath = "input/signal/El/"
        else:
            import DataManagerMuonsSimple as DataManager
            sigpath = "input/signal/Mu/"

        for region in ('SR', 'WCR'):
            suffix = region + lepton + "_obs_cuts"
            if region == 'SR':
                histName = 'nSIG'
            else:
                histName = 'nWCR'
        
            Wlepnu_Np0 = DataManager.WlepnuFile_Np0.Get(histName)
            Wlepnu_Np1 = DataManager.WlepnuFile_Np1.Get(histName)
            Wlepnu_Np2 = DataManager.WlepnuFile_Np2.Get(histName)
            Wlepnu_Np3 = DataManager.WlepnuFile_Np3.Get(histName)
            Wlepnu_Np4 = DataManager.WlepnuFile_Np4.Get(histName)
            Wlepnu_Np5 = DataManager.WlepnuFile_Np5.Get(histName)
            
            Wtaunu_Np0 = DataManager.WtaunuFile_Np0.Get(histName)
            Wtaunu_Np1 = DataManager.WtaunuFile_Np1.Get(histName)
            Wtaunu_Np2 = DataManager.WtaunuFile_Np2.Get(histName)
            Wtaunu_Np3 = DataManager.WtaunuFile_Np3.Get(histName)
            Wtaunu_Np4 = DataManager.WtaunuFile_Np4.Get(histName)
            Wtaunu_Np5 = DataManager.WtaunuFile_Np5.Get(histName)
            
            Zleplep_Np0 = DataManager.ZleplepFile_Np0.Get(histName)
            Zleplep_Np1 = DataManager.ZleplepFile_Np1.Get(histName)
            Zleplep_Np2 = DataManager.ZleplepFile_Np2.Get(histName)
            Zleplep_Np3 = DataManager.ZleplepFile_Np3.Get(histName)
            Zleplep_Np4 = DataManager.ZleplepFile_Np4.Get(histName)
            Zleplep_Np5 = DataManager.ZleplepFile_Np5.Get(histName)
            
            Ztautau_Np0 = DataManager.ZtautauFile_Np0.Get(histName)
            Ztautau_Np1 = DataManager.ZtautauFile_Np1.Get(histName)
            Ztautau_Np2 = DataManager.ZtautauFile_Np2.Get(histName)
            Ztautau_Np3 = DataManager.ZtautauFile_Np3.Get(histName)
            Ztautau_Np4 = DataManager.ZtautauFile_Np4.Get(histName)
            Ztautau_Np5 = DataManager.ZtautauFile_Np5.Get(histName)
            
            Wgamma_Np0 = DataManager.WgammaFile_Np0.Get(histName)
            Wgamma_Np1 = DataManager.WgammaFile_Np1.Get(histName)
            Wgamma_Np2 = DataManager.WgammaFile_Np2.Get(histName)
            Wgamma_Np3 = DataManager.WgammaFile_Np3.Get(histName)
            Wgamma_Np4 = DataManager.WgammaFile_Np4.Get(histName)
            Wgamma_Np5 = DataManager.WgammaFile_Np5.Get(histName)
            
            ttbarLepjets = DataManager.ttbarLepjetsFile.Get(histName)
            ttbarDilep = DataManager.ttbarDilepFile.Get(histName)
            ttbargamma = DataManager.ttbargammaFile.Get(histName)
            
            st_tchan_lepnu = DataManager.st_tchan_lepnuFile.Get(histName)
            st_tchan_taunu = DataManager.st_tchan_taunuFile.Get(histName)
            
            st_Wt   = DataManager.st_WtFile.Get(histName)
            
            WW   = DataManager.WWFile.Get(histName)
            WZ   = DataManager.WZFile.Get(histName)
            ZZ_llll   = DataManager.ZZ_llllFile.Get(histName)
            ZZ_llnunu = DataManager.ZZ_llnunuFile.Get(histName)
            
            Zleplepgamma = DataManager.ZleplepgammaFile.Get(histName)
            Ztautaugamma = DataManager.ZtautaugammaFile.Get(histName)
            
            if lepton == 'El':
                diphotons = DataManager.diphotonsFile.Get(histName)
                
            if Blind and region == 'SR':
                data = DataManager.totalFile.Get(histName)
            else:
                data = DataManager.dataFile.Get(histName)
            gj = DataManager.gjFile.Get(histName)
                
            ############################################
            f.cd()
            httbargamma = ttbargamma.Clone("httbargammaNom_" + suffix)
            httbarDilep = ttbarDilep.Clone("httbarDilepNom_" + suffix)
            httbarLepjets = ttbarLepjets.Clone("httbarLepjetsNom_" + suffix)

            hWlepnu = Wlepnu_Np0.Clone("hWjetsNom_" + suffix)
            hWlepnu.Add(Wlepnu_Np1)
            hWlepnu.Add(Wlepnu_Np2)
            hWlepnu.Add(Wlepnu_Np3)
            hWlepnu.Add(Wlepnu_Np4)
            hWlepnu.Add(Wlepnu_Np5)
            
            hWlepnu.Add(Wtaunu_Np1)
            hWlepnu.Add(Wtaunu_Np2)
            hWlepnu.Add(Wtaunu_Np3)
            hWlepnu.Add(Wtaunu_Np4)
            hWlepnu.Add(Wtaunu_Np5)

            hWgamma = Wgamma_Np0.Clone("hWgammaNom_" + suffix)
            hWgamma.Add(Wgamma_Np1)
            hWgamma.Add(Wgamma_Np2)
            hWgamma.Add(Wgamma_Np3)
            hWgamma.Add(Wgamma_Np4)
            hWgamma.Add(Wgamma_Np5)

            hZleplep = Zleplep_Np0.Clone("hZleplepNom_" + suffix)
            hZleplep.Add(Zleplep_Np1)
            hZleplep.Add(Zleplep_Np2)
            hZleplep.Add(Zleplep_Np3)
            hZleplep.Add(Zleplep_Np4)
            hZleplep.Add(Zleplep_Np5)
            
            #hZtautau = Ztautau_Np0.Clone("hZtautauNom_" + suffix)
            hZleplep.Add(Ztautau_Np1)
            hZleplep.Add(Ztautau_Np2)
            hZleplep.Add(Ztautau_Np3)
            hZleplep.Add(Ztautau_Np4)
            hZleplep.Add(Ztautau_Np5)

            hZgamma = Zleplepgamma.Clone("hZgammaNom_" + suffix)
            hZgamma.Add(Ztautaugamma)

            hdiboson = WW.Clone("hdibosonNom_"+suffix)
            hdiboson.Add(WZ)
            hdiboson.Add(ZZ_llll)
            hdiboson.Add(ZZ_llnunu)

            hst = st_tchan_lepnu.Clone("hstNom_"+suffix)
            hst.Add(st_tchan_taunu)
            hst.Add(st_Wt)

            if lepton == 'El':
                hdiphotons = gj.Clone("hdiphotonsNom_"+suffix)

            hgj = gj.Clone("hgjNom_"+suffix)
            hdata = data.Clone("hdata_"+suffix)

            # this is because of stupid root"
            wino = []
            for mgl in range(0, 1600, 100):
                for mC1 in range(0, mgl, 50) + [mgl-20]:
                    filelist = glob(sigpath + 'wino_%d_%d_[01]_Hist.root' % (mgl, mC1))
                    if len(filelist) == 2:
                        winoFileName0 = filelist[0]
                        winoFile0 = ROOT.TFile(winoFileName0)
                        wino0 = winoFile0.Get(histName)
                        winoFileName1 = filelist[1]
                        winoFile1 = ROOT.TFile(winoFileName1)
                        wino1 = winoFile1.Get(histName)
                        f.cd()
                        hwino = wino0.Clone('hwino_%d_%dNom_%s' % (mgl, mC1, suffix))
                        hwino.Add(wino1)
                        if SIGMA:
                            hwino.Scale(1.0 + SIGMA * xsecs.getXsecRelError(mgl, mC1))
                        wino.append(hwino)
            f.Write()
    
if __name__ == "__main__":
    MakeMonsterFile()
