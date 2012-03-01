#! /usr/bin/env python

# code to make all the plots in a file

import ROOT
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

ELECTRON = 0
MUON = 1

DEFAULTLEPTON = ELECTRON

def GetHistNames(inFile):
    
    histNames = []

    for key in inFile.GetListOfKeys():
        h = key.ReadObj()
        #dirItem = [key.ReadObj().ClassName(), key.GetName(), key.GetTitle()]
        #print dirItem
        if h.InheritsFrom("TDirectory"):
            newList = [key.GetName() + "/" + x for x in GetHistNames(key.ReadObj())]
            #print newList
            histNames.extend(newList)
        elif h.InheritsFrom("TH1"):
            histNames.append(key.GetName())

    return histNames



def LepPhotonPlots(lepton):


    if lepton == ELECTRON:
        import DataManagerElectrons as DataManager
    elif lepton == MUON:
        import DataManagerMuons as DataManager
    else:
        raise ValueError("Lepton has to be ELECTRON or MUON.")

    ##########################################################
    #   Now make a list of histogram names

    #   Take the ttbar as the input that defines what should be in every file
    histNames = GetHistNames(DataManager.ttbarFile)
    
    #print histNames

    ##########################################################

    for histName in histNames:

        wino = DataManager.winoFile.Get(histName)
        
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
        
        ttbar = DataManager.ttbarFile.Get(histName)
        
        st_tchan_lepnu = DataManager.st_tchan_lepnuFile.Get(histName)
        st_tchan_taunu = DataManager.st_tchan_taunuFile.Get(histName)
        
        #st_schan_lepnu = st_schan_lepnuFile.Get(histName)
        #st_schan_taunu = st_schan_taunuFile.Get(histName)
        
        st_Wt   = DataManager.st_WtFile.Get(histName)
        
        WW   = DataManager.WWFile.Get(histName)
        WZ   = DataManager.WZFile.Get(histName)
        ZZ   = DataManager.ZZFile.Get(histName)
        
        Zleplepgamma = DataManager.ZleplepgammaFile.Get(histName)
        Ztautaugamma = DataManager.ZtautaugammaFile.Get(histName)
        
        gamma_Np1 = DataManager.gammaFile_Np1.Get(histName)
        gamma_Np2 = DataManager.gammaFile_Np2.Get(histName)
        gamma_Np3 = DataManager.gammaFile_Np3.Get(histName)
        gamma_Np4 = DataManager.gammaFile_Np4.Get(histName)
        gamma_Np5 = DataManager.gammaFile_Np5.Get(histName)

        data = DataManager.dataFile.Get(histName)
        gj = DataManager.gjFile.Get(histName)
        gj.Add(data, -1.0);
        data.Sumw2()

        #######################################

        wino.Scale(DataManager.wino_scale)

        Wlepnu_Np0.Scale(DataManager.Wlepnu_Np0_scale)
        Wlepnu_Np1.Scale(DataManager.Wlepnu_Np1_scale)
        Wlepnu_Np2.Scale(DataManager.Wlepnu_Np2_scale)
        Wlepnu_Np3.Scale(DataManager.Wlepnu_Np3_scale)
        Wlepnu_Np4.Scale(DataManager.Wlepnu_Np4_scale)
        Wlepnu_Np5.Scale(DataManager.Wlepnu_Np5_scale)

        Wtaunu_Np0.Scale(DataManager.Wtaunu_Np0_scale)
        Wtaunu_Np1.Scale(DataManager.Wtaunu_Np1_scale)
        Wtaunu_Np2.Scale(DataManager.Wtaunu_Np2_scale)
        Wtaunu_Np3.Scale(DataManager.Wtaunu_Np3_scale)
        Wtaunu_Np4.Scale(DataManager.Wtaunu_Np4_scale)
        Wtaunu_Np5.Scale(DataManager.Wtaunu_Np5_scale)

        Zleplep_Np0.Scale(DataManager.Zleplep_Np0_scale)
        Zleplep_Np1.Scale(DataManager.Zleplep_Np1_scale)
        Zleplep_Np2.Scale(DataManager.Zleplep_Np2_scale)
        Zleplep_Np3.Scale(DataManager.Zleplep_Np3_scale)
        Zleplep_Np4.Scale(DataManager.Zleplep_Np4_scale)
        Zleplep_Np5.Scale(DataManager.Zleplep_Np5_scale)

        Ztautau_Np0.Scale(DataManager.Ztautau_Np0_scale)
        Ztautau_Np1.Scale(DataManager.Ztautau_Np1_scale)
        Ztautau_Np2.Scale(DataManager.Ztautau_Np2_scale)
        Ztautau_Np3.Scale(DataManager.Ztautau_Np3_scale)
        Ztautau_Np4.Scale(DataManager.Ztautau_Np4_scale)
        Ztautau_Np5.Scale(DataManager.Ztautau_Np5_scale)
        
        Wgamma_Np0.Scale(DataManager.Wgamma_Np0_scale)
        Wgamma_Np1.Scale(DataManager.Wgamma_Np1_scale)
        Wgamma_Np2.Scale(DataManager.Wgamma_Np2_scale)
        Wgamma_Np3.Scale(DataManager.Wgamma_Np3_scale)
        Wgamma_Np4.Scale(DataManager.Wgamma_Np4_scale)
        Wgamma_Np5.Scale(DataManager.Wgamma_Np5_scale)
        
        ttbar.Scale(DataManager.ttbar_scale)
        
        st_tchan_lepnu.Scale(DataManager.st_tchan_lepnu_scale)
        st_tchan_taunu.Scale(DataManager.st_tchan_taunu_scale)
        
        #st_schan_lepnu.Scale(st_schan_lepnu_scale)
        #st_schan_taunu.Scale(st_schan_taunu_scale)

        st_Wt.Scale(DataManager.st_Wt_scale)

        WW.Scale(DataManager.WW_scale)
        WZ.Scale(DataManager.WZ_scale)
        ZZ.Scale(DataManager.ZZ_scale)
        
        Zleplepgamma.Scale(DataManager.Zleplepgamma_scale)
        Ztautaugamma.Scale(DataManager.Ztautaugamma_scale)
        
        gamma_Np1.Scale(DataManager.gamma_Np1_scale)
        gamma_Np2.Scale(DataManager.gamma_Np2_scale)
        gamma_Np3.Scale(DataManager.gamma_Np3_scale)
        gamma_Np4.Scale(DataManager.gamma_Np4_scale)
        gamma_Np5.Scale(DataManager.gamma_Np5_scale)

        ############################################

        nRebin = 5

        Wlepnu = Wlepnu_Np0.Clone()
        Wlepnu.Add(Wlepnu_Np1)
        Wlepnu.Add(Wlepnu_Np2)
        Wlepnu.Add(Wlepnu_Np3)
        Wlepnu.Add(Wlepnu_Np4)
        Wlepnu.Add(Wlepnu_Np5)

        Wtaunu = Wtaunu_Np0.Clone()
        Wtaunu.Add(Wtaunu_Np1)
        Wtaunu.Add(Wtaunu_Np2)
        Wtaunu.Add(Wtaunu_Np3)
        Wtaunu.Add(Wtaunu_Np4)
        Wtaunu.Add(Wtaunu_Np5)

        Wjets = Wlepnu.Clone()
        Wjets.Add(Wtaunu)
        Wjets.Rebin(nRebin)
 
        Wgamma = Wgamma_Np0.Clone()
        Wgamma.Add(Wgamma_Np1)
        Wgamma.Add(Wgamma_Np2)
        Wgamma.Add(Wgamma_Np3)
        Wgamma.Add(Wgamma_Np4)
        Wgamma.Add(Wgamma_Np5)
        Wgamma.Rebin(nRebin)

        Zleplep = Zleplep_Np0.Clone()
        Zleplep.Add(Zleplep_Np1)
        Zleplep.Add(Zleplep_Np2)
        Zleplep.Add(Zleplep_Np3)
        Zleplep.Add(Zleplep_Np4)
        Zleplep.Add(Zleplep_Np5)

        Ztautau = Ztautau_Np0.Clone()
        Ztautau.Add(Ztautau_Np1)
        Ztautau.Add(Ztautau_Np2)
        Ztautau.Add(Ztautau_Np3)
        Ztautau.Add(Ztautau_Np4)
        Ztautau.Add(Ztautau_Np5)

        Zjets = Zleplep.Clone()
        Zjets.Add(Ztautau)
        Zjets.Rebin(nRebin)

        Zgamma = Zleplepgamma.Clone()
        Zgamma.Add(Ztautaugamma)
        Zgamma.Rebin(nRebin)

        diboson = WW.Clone()
        diboson.Add(WZ)
        diboson.Add(ZZ)
        diboson.Rebin(nRebin)

        gamma = gamma_Np1.Clone()
        gamma.Add(gamma_Np2)
        gamma.Add(gamma_Np3)
        gamma.Add(gamma_Np4)
        gamma.Add(gamma_Np5)
        gamma.Rebin(nRebin)


        st = st_tchan_lepnu.Clone()
        st.Add(st_tchan_taunu)
        #st.Add(st_schan_lepnu)
        #st.Add(st_schan_taunu)
        st.Add(st_Wt)
        st.Rebin(nRebin)

        ttbar.Rebin(nRebin)

        hn = ttbar.GetName()
        c_paper = ROOT.TCanvas(hn +"_canvas", hn+"_canvas",700,410,500,400)
        #c_paper.SetLogy()

        bg = ROOT.THStack(hn+"_bg","stacked bg;"+ttbar.GetXaxis().GetTitle()+";Events")

        bg.SetMinimum(5e-2)
        bg.SetMaximum(200)

        gamma.SetFillStyle(1001)
        Wjets.SetFillStyle(1001)
        Wgamma.SetFillStyle(1001)
        diboson.SetFillStyle(1001)
        Zgamma.SetFillStyle(1001)
        ttbar.SetFillStyle(1001)
        st.SetFillStyle(1001)

        gamma.SetFillColor(28) # brown
        gamma.SetLineColor(28)
        Zjets.SetFillColor(43) # tan
        Zjets.SetLineColor(43)
        Zgamma.SetFillColor(42) # tan
        Zgamma.SetLineColor(42)
        Wjets.SetFillColor(3) # green
        Wjets.SetLineColor(3)
        Wgamma.SetFillColor(7) # cyan
        Wgamma.SetLineColor(7)
        diboson.SetFillColor(8) # dark green
        diboson.SetLineColor(8)
        ttbar.SetFillColor(2) # red
        ttbar.SetLineColor(2)
        st.SetFillColor(9) # purple
        st.SetLineColor(9)

        bg.Add(gamma)
        bg.Add(Zjets)
        bg.Add(Zgamma)
        bg.Add(Wjets)
        bg.Add(Wgamma)
        bg.Add(diboson)
        bg.Add(ttbar)
        bg.Add(st)
        
        bg.Draw()
        
        wino.Rebin(nRebin)
        #wino.Scale(0.5)
        #wino.Scale(10)

        
        wino.SetFillStyle(0)
        wino.SetLineColor(12)
        wino.SetLineWidth(3)

        data.Rebin(nRebin)
        data.Draw("same")

        gj.Rebin(nRebin)
        gj.SetFillStyle(0)
        gj.SetLineColor(41)
        #gj.Draw("hist same")

        # wino_700_680.SetFillStyle(0)
        # wino_700_680.SetLineColor(46)
        # wino_700_680.SetLineWidth(3)
        # wino_1000_200.SetFillStyle(0)
        # wino_1000_200.SetLineColor(41)
        # wino_1000_200.SetLineWidth(3)
        # wino_1500_300.SetFillStyle(0)
        # wino_1500_300.SetLineColor(43)
        # wino_1500_300.SetLineWidth(3)
        wino.Draw("hist same");
        # #wino_700_680.Draw("hist same");
        # #wino_1000_200.Draw("hist same");
        # wino_1500_300.Draw("hist same");


        legb = ROOT.TLegend(0.5,0.55,0.93,0.92)
        legb.SetFillColor(0)
        legb.SetBorderSize(0)
        legb.SetTextSize(0.045)
        legb.AddEntry(data,"data","l")
        legb.AddEntry(gamma,"#gamma+jets","f")
        legb.AddEntry(Zjets,"Z+jets","f")
        legb.AddEntry(Zgamma,"Z#gamma","f")
        legb.AddEntry(Wjets,"W+jets","f")
        legb.AddEntry(Wgamma,"W#gamma","f")
        legb.AddEntry(diboson,"WW, WZ, ZZ","f")
        legb.AddEntry(ttbar,"ttbar","f")
        legb.AddEntry(st,"singe top","f")
        legb.AddEntry(wino,"wino (600, 200)", "l");
        #legb.AddEntry(wino_700_680,"wino (600, 500)","l");
        #legb.AddEntry(wino_1000_200,"wino (1000, 200)", "l");
        #legb.AddEntry(wino_1500_300,"wino (1500, 400) #times 100","l");

        legb.Draw()

        c_paper.Print(hn+"Plot.eps")
        c_paper.Print(hn+"Plot.png")
        c_paper.Print(hn+"Plot.root")
  

    
if __name__ == "__main__":
    LepPhotonPlots(DEFAULTLEPTON)
