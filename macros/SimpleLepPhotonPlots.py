#! /usr/bin/env python

# code to make all the plots in a file
import sys
import getopt

import ROOT
ROOT.gROOT.SetBatch()
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



def SimpleLepPhotonPlots(lepton, drawLegend, logy, allFormats):


    if lepton == ELECTRON:
        import DataManagerElectronsSimple as DataManager
    elif lepton == MUON:
        import DataManagerMuonsSimple as DataManager
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
        ttbargamma = DataManager.ttbargammaFile.Get(histName)
        
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

        if lepton == ELECTRON:
            diphotons = DataManager.diphotonsFile.Get(histName)

        data = DataManager.dataFile.Get(histName)
        gj = DataManager.gjFile.Get(histName)
        #gj.Add(data, -1.0);
        data.Sumw2()

        ############################################


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
 
        Wgamma = Wgamma_Np0.Clone()
        Wgamma.Add(Wgamma_Np1)
        Wgamma.Add(Wgamma_Np2)
        Wgamma.Add(Wgamma_Np3)
        Wgamma.Add(Wgamma_Np4)
        Wgamma.Add(Wgamma_Np5)

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

        Zgamma = Zleplepgamma.Clone()
        Zgamma.Add(Ztautaugamma)

        diboson = WW.Clone()
        diboson.Add(WZ)
        diboson.Add(ZZ)

        gamma = gamma_Np1.Clone()
        gamma.Add(gamma_Np2)
        gamma.Add(gamma_Np3)
        gamma.Add(gamma_Np4)
        gamma.Add(gamma_Np5)


        st = st_tchan_lepnu.Clone()
        st.Add(st_tchan_taunu)
        #st.Add(st_schan_lepnu)
        #st.Add(st_schan_taunu)
        st.Add(st_Wt)

        hn = ttbargamma.GetName()
        c_paper = ROOT.TCanvas(hn +"_canvas", hn+"_canvas",700,410,500,400)
        if logy:
            c_paper.SetLogy()

        bg = ROOT.THStack(hn+"_bg","stacked bg;"+ttbargamma.GetXaxis().GetTitle()+";Events")

        bg.SetMinimum(5e-2)
        #bg.SetMaximum(25)

        gj.SetFillStyle(1001)
        Wjets.SetFillStyle(1001)
        Wgamma.SetFillStyle(1001)
        diboson.SetFillStyle(1001)
        Zgamma.SetFillStyle(1001)
        ttbar.SetFillStyle(1001)
        ttbargamma.SetFillStyle(1001)
        st.SetFillStyle(1001)

        gj.SetFillColor(28) # brown
        gj.SetLineColor(28)
        Zjets.SetFillColor(43) # tan
        Zjets.SetLineColor(43)
        Zgamma.SetFillColor(42) # tan
        Zgamma.SetLineColor(42)
        if lepton == ELECTRON:
            diphotons.SetFillColor(39) # 
            diphotons.SetLineColor(39)            
        Wjets.SetFillColor(3) # green
        Wjets.SetLineColor(3)
        Wgamma.SetFillColor(7) # cyan
        Wgamma.SetLineColor(7)
        diboson.SetFillColor(8) # dark green
        diboson.SetLineColor(8)
        ttbar.SetFillColor(2) # red
        ttbar.SetLineColor(2)
        ttbargamma.SetFillColor(46) # brick
        ttbargamma.SetLineColor(46)
        st.SetFillColor(9) # purple
        st.SetLineColor(9)

        bg.Add(gj)
        bg.Add(Zjets)
        bg.Add(Zgamma)
        if lepton == ELECTRON:
            bg.Add(diphotons)
        bg.Add(Wjets)
        bg.Add(Wgamma)
        bg.Add(diboson)
        bg.Add(ttbar)
        bg.Add(ttbargamma)
        bg.Add(st)

        if data.Integral() != 0:
            if not logy:
                data.SetMinimum(0)
            data.Draw()
            bg.Draw("HIST same")
        else:
            bg.Draw("HIST")
        
        #wino.Rebin(nRebin)
        #wino.Scale(0.5)
        #wino.Scale(10)

        
        wino.SetFillStyle(0)
        wino.SetLineColor(12)
        wino.SetLineWidth(3)

        #data.Rebin(nRebin)
        data.Draw("same")

        #gj.Rebin(nRebin)
        #gj.SetFillStyle(0)
        #gj.SetLineColor(41)
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
        # wino.Draw("hist same");
        # #wino_700_680.Draw("hist same");
        # #wino_1000_200.Draw("hist same");
        # wino_1500_300.Draw("hist same");

        if drawLegend:
            legb = ROOT.TLegend(0.65,0.55,0.93,0.92)
            legb.SetFillColor(0)
            legb.SetBorderSize(0)
            legb.SetTextSize(0.045)
            legb.AddEntry(data,"data","l")
            legb.AddEntry(gj,"#gamma+jets","f")
            legb.AddEntry(Zjets,"Z+jets","f")
            legb.AddEntry(Zgamma,"Z#gamma","f")
            if lepton == ELECTRON:
                legb.AddEntry(diphotons,"#gamma#gamma","f")
            legb.AddEntry(Wjets,"W+jets","f")
            legb.AddEntry(Wgamma,"W#gamma","f")
            legb.AddEntry(diboson,"WW, WZ, ZZ","f")
            legb.AddEntry(ttbar,"ttbar","f")
            legb.AddEntry(ttbargamma,"ttbar#gamma","f")
            legb.AddEntry(st,"singe top","f")
            #legb.AddEntry(wino,"wino (600, 200)", "l");
            #legb.AddEntry(wino_700_680,"wino (600, 500)","l");
            #legb.AddEntry(wino_1000_200,"wino (1000, 200)", "l");
            #legb.AddEntry(wino_1500_300,"wino (1500, 400) #times 100","l");

            legb.Draw()

        if logy:
            if drawLegend:
                if wino.GetDimension() == 1:
                    c_paper.Print(hn+"LogLegPlot.eps")
                    if allFormats: c_paper.Print(hn+"LogLegPlot.png")
                if allFormats: c_paper.Print(hn+"LogLegPlot.root")
            else:
                if wino.GetDimension() == 1:
                    c_paper.Print(hn+"LogPlot.eps")
                    if allFormats: c_paper.Print(hn+"LogPlot.png")
                if allFormats: c_paper.Print(hn+"LogPlot.root")
        else:
            if drawLegend:
                if wino.GetDimension() == 1:
                    c_paper.Print(hn+"LegPlot.eps")
                    if allFormats: c_paper.Print(hn+"LegPlot.png")
                if allFormats: c_paper.Print(hn+"LegPlot.root")
            else:
                if wino.GetDimension() == 1:
                    c_paper.Print(hn+"Plot.eps")
                    if allFormats: c_paper.Print(hn+"Plot.png")
                if allFormats: c_paper.Print(hn+"Plot.root")

    
if __name__ == "__main__":
    try:
        # retrive command line options
        shortopts  = "emga"
        longopts   = ["lepton=", "log"]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )
    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        sys.exit(1)

    lepton = DEFAULTLEPTON
    legend = False
    logy = False
    formats = False
    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-a"):
            formats = True
        elif o in ("-m"):
            lepton = MUON
        elif o in ("-e"):
            lepton = ELECTRON
        elif o in ("-g"):
            legend = True
        elif o in ("--log"):
            logy = True
        elif o in ("--lepton"):
            if a == "electron":
                lepton = ELECTRON
            elif a == "muon":
                lepton = MUON
            else:
                print "*** Lepton must be 'electron' or 'muon ****"
                sys.exit(1)
    
    SimpleLepPhotonPlots(lepton, legend, logy, formats)
