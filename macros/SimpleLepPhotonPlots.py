#! /usr/bin/env python

from __future__ import division

# code to make all the plots in a file
import sys
import getopt
import math

import ROOT
ROOT.gROOT.SetBatch()
ROOT.gROOT.LoadMacro("AtlasStyle.C") 
ROOT.SetAtlasStyle()

import histUtils

ELECTRON = 0
MUON = 1

DEFAULTLEPTON = ELECTRON

USE_WGAMMA_SHERPA = False

combineTypes = True

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



def SimpleLepPhotonPlots(lepton, drawLegend, logy, allFormats, addRatio, addSignal):


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

    #
    # errors
    # 3.9
    
    stdErr2 = .039**2   # lumi
    stdErr2 += .046**2  # photon
    stdErr2 += .044**2  # pileup

    if lepton == ELECTRON:
        stdErr2 += 0.019**2
        stdErr2 += 0.02**2
    else:
        stdErr2 += 0.02**2
    
    WgammaErr2 = stdErr2
    WjetsErr2 = stdErr2
    ttbargammaErr2 = stdErr2
    dilepErr2 = stdErr2
    lepjetsErr2 = stdErr2
    stErr2 = stdErr2
    dibosonErr2 = stdErr2
    diphotonErr2 = stdErr2
    ZgammaErr2 = stdErr2
    ZjetsErr2 = stdErr2
    qcdErr2 = stdErr2

    WgammaErr2 += .28**2
    ttbargammaErr2 += .40**2
    ZjetsErr2 += .05**2
    ZgammaErr2 += .15**2
    stErr2 += .08**2
    diphotonErr2 += 1
    lepjetsErr2 += 25

    if lepton == ELECTRON:
        WjetsErr2 += .5**2
        dilepErr2 += .136**2

        WgammaErr2 += .25**2
        ttbargammaErr2 += .15**2
        dilepErr2 += .17**2
        WjetsErr2 += .28**2
        stErr2 += .2**2
        dibosonErr2 += .05**2
        ZgammaErr2 += .164**2
        qcdErr2 += .15**2

    else:
        WjetsErr2 += .97**2
        dilepErr2 += .148**2
        qcdErr2 += .5**2

        WgammaErr2 += .12**2
        ttbargammaErr2 += .13**2
        dilepErr2 += .18**2
        WjetsErr2 += .35**2
        stErr2 += .3**2
        dibosonErr2 += .04**2
        ZgammaErr2 += .1**2

        WgammaErr2 += .027**2
        ttbargammaErr2 += .031**2
        dilepErr2 += .025**2
        dibosonErr2 += .032**2
        ZgammaErr2 += .231**2

    ############################################


    for histName in histNames:

        winoStrong0 = DataManager.winoStrong0File.Get(histName)
        winoWeak0 = DataManager.winoWeak0File.Get(histName)
        winoStrong1 = DataManager.winoStrong1File.Get(histName)
        winoWeak1 = DataManager.winoWeak1File.Get(histName)
        
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
        
        if USE_WGAMMA_SHERPA:
            Wgamma_lepnu = DataManager.Wgamma_lepnu_sherpaFile.Get(histName)
            Wgamma_taunu = DataManager.Wgamma_taunu_sherpaFile.Get(histName)
        else:
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
        ZZ_llll   = DataManager.ZZ_llllFile.Get(histName)
        ZZ_llnunu   = DataManager.ZZ_llnunuFile.Get(histName)
        
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
        ratioHist = data.Clone()

        ############################################

        winoStrong = winoStrong0.Clone()
        winoStrong.Add(winoStrong1)

        print "here1"

        winoWeak = winoWeak0.Clone()
        winoWeak.Add(winoWeak1)

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

        print "here1b"

        Wjets = Wlepnu.Clone()
        Wjets.Add(Wtaunu)

        addUnc(Wjets, WjetsErr2)
 
        print "here1c"

        if USE_WGAMMA_SHERPA:
            Wgamma = Wgamma_lepnu.Clone()
            Wgamma.Add(Wgamma_taunu)
        else:
            Wgamma = Wgamma_Np0.Clone()
            Wgamma.Add(Wgamma_Np1)
            Wgamma.Add(Wgamma_Np2)
            Wgamma.Add(Wgamma_Np3)
            Wgamma.Add(Wgamma_Np4)
            Wgamma.Add(Wgamma_Np5)

        addUnc(Wgamma, WgammaErr2)

        print "here1d"

        print "here2"

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

        addUnc(Zjets, ZjetsErr2)

        Zgamma = Zleplepgamma.Clone()
        Zgamma.Add(Ztautaugamma)

        addUnc(Zgamma, ZgammaErr2)

        Z = Zgamma.Clone()
        Z.Add(Zjets)

        diboson = WW.Clone()
        diboson.Add(WZ)
        diboson.Add(ZZ_llll)
        diboson.Add(ZZ_llnunu)

        addUnc(diboson, dibosonErr2)

        # gamma = gamma_Np1.Clone()
        # gamma.Add(gamma_Np2)
        # gamma.Add(gamma_Np3)
        # gamma.Add(gamma_Np4)
        # gamma.Add(gamma_Np5)


        st = st_tchan_lepnu.Clone()
        st.Add(st_tchan_taunu)
        #st.Add(st_schan_lepnu)
        #st.Add(st_schan_taunu)
        st.Add(st_Wt)

        print "here3"

        addUnc(st, stErr2)

        hn = ttbargamma.GetName()
        if addRatio:
            c_paper = ROOT.TCanvas(hn +"_canvas", hn+"_canvas",700,610,500,600)
            p_ratio = ROOT.TPad(hn +"_ratio", hn +"_ratio", 0,0,1,.35)
            p_ratio.Draw()
            p_plot = ROOT.TPad(hn +"_plot", hn +"_plot", 0,.35,1,1)
            p_plot.Draw()
            if logy:
                p_plot.SetLogy()
            p_plot.cd()
        else:
            c_paper = ROOT.TCanvas(hn +"_canvas", hn+"_canvas",700,410,500,400)
            if logy:
                c_paper.SetLogy()

        bg = ROOT.THStack(hn+"_bg","stacked bg;"+ttbargamma.GetXaxis().GetTitle()+";Events")

        print "here4"

        addUnc(ttbargamma, ttbargammaErr2)
        addUnc(ttbar, dilepErr2)
        addUnc(gj, qcdErr2)

        if lepton == ELECTRON:
            addUnc(diphotons, diphotonErr2)

            if combineTypes:
                gj.Add(diphotons)

        bg.SetMinimum(5e-2)
        #bg.SetMaximum(25)

        gj.SetFillStyle(1001)
        Wjets.SetFillStyle(1001)
        Wgamma.SetFillStyle(1001)
        diboson.SetFillStyle(1001)
        Zgamma.SetFillStyle(1001)
        Z.SetFillStyle(1001)
        ttbar.SetFillStyle(1001)
        ttbargamma.SetFillStyle(1001)
        st.SetFillStyle(1001)

        print "here5"

        gj.SetFillColor(28) # brown
        gj.SetLineColor(28)
        Zjets.SetFillColor(43) # tan
        Zjets.SetLineColor(43)
        Zgamma.SetFillColor(42) # tan
        Zgamma.SetLineColor(42)
        Z.SetFillColor(42) # tan
        Z.SetLineColor(42)
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
        if combineTypes:
            bg.Add(Z)
        else:
            bg.Add(Zjets)
            bg.Add(Zgamma)
        if lepton == ELECTRON and not combineTypes:
            bg.Add(diphotons)
        bg.Add(Wjets)
        bg.Add(Wgamma)
        bg.Add(diboson)
        bg.Add(ttbar)
        bg.Add(ttbargamma)
        bg.Add(st)

        #if winoWeak.GetDimension() == 1 and addRatio:

        suHist = bg.GetStack().Last().Clone()

        # let's try to find the range
        dataMaxBin = data.GetMaximumBin()
        maxData = data.GetBinContent(dataMaxBin) + 1.4 * data.GetBinError(dataMaxBin)
        suMaxBin = suHist.GetMaximumBin()
        maxSu = suHist.GetBinContent(suMaxBin) + 1.4 * suHist.GetBinError(suMaxBin)

        maxVal = max(maxData, maxSu)

        dataGraph = histUtils.MakePoissonConfidenceLevelErrors(data)

        if data.Integral() != 0:
            if not logy:
                data.SetMinimum(0)
                if maxVal > 0:
                    data.SetMaximum(maxVal)

            data.Draw("AXIS")
            bg.Draw("HIST same")
        else:
            bg.Draw("HIST")
        
        suHist.SetMarkerSize(0)
        suHist.SetFillColor(1)
        suHist.SetFillStyle(3245)
        suHist.Draw("E2 same");

        #wino.Rebin(nRebin)
        #wino.Scale(0.5)
        #wino.Scale(10)

        
        winoStrong.SetFillStyle(0)
        winoStrong.SetLineColor(12)
        winoStrong.SetLineWidth(3)

        winoWeak.SetFillStyle(0)
        winoWeak.SetLineColor(50)
        winoWeak.SetLineWidth(3)

        #data.Rebin(nRebin)
        if dataGraph != None:
            dataGraph.SetLineWidth(2)
            dataGraph.Draw("p")
        else:
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
        if addSignal:
            winoWeak.Draw("hist same");
            winoStrong.Draw("hist same");
        # #wino_1000_200.Draw("hist same");
        # wino_1500_300.Draw("hist same");


        if drawLegend:
            ATLASLabel(0.65,0.46,"Internal");

            l = ROOT.TLatex()
            l.SetNDC()
            l.SetTextColor(1);
            l.SetTextFont(42);
            l.SetTextSize(0.038)
            if lepton == ELECTRON:
                l.DrawLatex(0.65,0.39,"#int Ldt = 4.8 fb^{-1}");
                l.DrawLatex(0.65,0.32,"#sqrt{s} = 7 TeV,  e channel");

            else:
                l.DrawLatex(0.65,0.39,"#int Ldt = 4.7 fb^{-1}");
                l.DrawLatex(0.65,0.32,"#sqrt{s} = 7 TeV,  #mu channel");

            legb = ROOT.TLegend(0.65,0.50,0.93,0.92)
            legb.SetFillColor(0)
            legb.SetBorderSize(0)
            legb.SetTextSize(0.038)
            legb.AddEntry(data,"data","l")
            
            if lepton == ELECTRON and combineTypes:
                legb.AddEntry(gj,"#gamma+jets, #gamma#gamma","f")
            else:
                legb.AddEntry(gj,"#gamma+jets","f")
            if combineTypes:
                legb.AddEntry(Z,"Z","f")
            else:
                legb.AddEntry(Zjets,"Z+jets","f")
                legb.AddEntry(Zgamma,"Z#gamma","f")
            if lepton == ELECTRON and not combineTypes:
                legb.AddEntry(diphotons,"#gamma#gamma","f")
            legb.AddEntry(Wjets,"W+jets","f")
            legb.AddEntry(Wgamma,"W#gamma","f")
            legb.AddEntry(diboson,"WW, WZ, ZZ","f")
            legb.AddEntry(ttbar,"ttbar","f")
            legb.AddEntry(ttbargamma,"ttbar#gamma","f")
            legb.AddEntry(st,"singe top","f")
            if addSignal:
                legb.AddEntry(winoWeak,"GGM (1500, 200)", "l");
                legb.AddEntry(winoStrong,"GGM (600, 500)","l");
            #legb.AddEntry(wino_1000_200,"wino (1000, 200)", "l");
            #legb.AddEntry(wino_1500_300,"wino (1500, 400) #times 100","l");

            legb.Draw()
        else:
            ATLASLabel(0.65,0.90,"Internal");
            l = ROOT.TLatex()
            l.SetNDC()
            l.SetTextColor(1);
            l.SetTextFont(42);
            l.SetTextSize(0.038)
            if lepton == ELECTRON:
                l.DrawLatex(0.65,0.80,"#int Ldt = 4.8 fb^{-1}");
            else:
                l.DrawLatex(0.65,0.80,"#int Ldt = 4.7 fb^{-1}");
            l.DrawLatex(0.65,0.70,"#sqrt{s}=7 TeV");


        if winoWeak.GetDimension() == 1 and addRatio:
            p_ratio.cd()
            print "Margin =",p_ratio.GetBottomMargin()
            p_ratio.SetBottomMargin(0.3)
            ratioErrorHist = suHist.Clone()
            ratioErrorHist.GetYaxis().SetTitle("Data/MC")
            ratioErrorHist.GetYaxis().SetLabelSize(0.08)
            ratioErrorHist.GetXaxis().SetLabelSize(0.08)
            print "GetTitleXSize", ratioErrorHist.GetXaxis().GetTitleSize()
            print "GetTitleYSize", ratioErrorHist.GetYaxis().GetTitleSize()
            print "GetTitleXOffset", ratioErrorHist.GetXaxis().GetTitleOffset()
            print "GetTitleYOffset", ratioErrorHist.GetYaxis().GetTitleOffset()
            ratioErrorHist.GetYaxis().SetTitleSize(0.09)
            ratioErrorHist.GetXaxis().SetTitleSize(0.09)
            ratioErrorHist.GetYaxis().SetTitleOffset(0.8)
            ratioErrorHist.GetXaxis().SetTitleOffset(1.2)
            for i in range(ratioErrorHist.GetNbinsX() + 1):
                cont = ratioErrorHist.GetBinContent(i)
                err = ratioErrorHist.GetBinError(i)
                if cont != 0:
                    ratioErrorHist.SetBinError(i,err/cont)
                else:
                    ratioErrorHist.SetBinError(i,0)
                ratioErrorHist.SetBinContent(i,1)
            ratioErrorHist.SetMinimum(-1)
            ratioErrorHist.SetMaximum(3)
            ratioErrorHist.Draw("E2")
            line = ROOT.TF1("line", "1", -1e10, 1e10)
            line.SetLineWidth(1)
            line.Draw("same")
            ratioGraph = histUtils.MakePoissonConfidenceLevelErrors_ratio(data, suHist)
            if ratioGraph != None:
                ratioGraph.SetLineWidth(2)
                ratioGraph.Draw("p")
            else:
                ratioHist.Divide(ratioHist, ratioErrorHist, 1, 1, "B")
                ratioHist.Draw("same")

        if logy:
            if drawLegend:
                if winoWeak.GetDimension() == 1:
                    c_paper.Print(hn+"LogLegPlot.eps")
                    if allFormats: c_paper.Print(hn+"LogLegPlot.png")
                if allFormats: c_paper.Print(hn+"LogLegPlot.root")
            else:
                if winoWeak.GetDimension() == 1:
                    c_paper.Print(hn+"LogPlot.eps")
                    if allFormats: c_paper.Print(hn+"LogPlot.png")
                if allFormats: c_paper.Print(hn+"LogPlot.root")
        else:
            if drawLegend:
                if winoWeak.GetDimension() == 1:
                    c_paper.Print(hn+"LegPlot.eps")
                    if allFormats: c_paper.Print(hn+"LegPlot.png")
                if allFormats: c_paper.Print(hn+"LegPlot.root")
            else:
                if winoWeak.GetDimension() == 1:
                    c_paper.Print(hn+"Plot.eps")
                    if allFormats: c_paper.Print(hn+"Plot.png")
                if allFormats: c_paper.Print(hn+"Plot.root")


def addUnc(hist, unc2):
    for te in range(hist.GetNbinsX()):
        i = te+1
        realUnc = math.hypot(hist.GetBinError(i), hist.GetBinContent(i)*math.sqrt(unc2))
        hist.SetBinError(i, realUnc)

def ATLASLabel(x,y,text = "", color=1):
    l = ROOT.TLatex()
    l.SetNDC()
    l.SetTextFont(72)
    l.SetTextSize(0.038)
    l.SetTextColor(color)


    #delx = 0.115*696*ROOT.gPad.GetWh()/(472*ROOT.gPad.GetWw())
    #print ROOT.gPad.GetWh(),ROOT.gPad.GetWw(),delx
    
    delx = 0.1
                                    
    l.DrawLatex(x,y,"ATLAS")

    if text != "":
        p = ROOT.TLatex()
        p.SetNDC()
        p.SetTextFont(42)
        p.SetTextSize(0.038)
        p.SetTextColor(color)
        p.DrawLatex(x+delx,y,text)
        

    
if __name__ == "__main__":
    try:
        # retrive command line options
        shortopts  = "emgars"
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
    addRatio = False
    addSignal = False
    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)
        elif o in ("-a"):
            formats = True
        elif o in ("-r"):
            addRatio = True
        elif o in ("-s"):
            addSignal = True
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
    
    SimpleLepPhotonPlots(lepton, legend, logy, formats, addRatio, addSignal)


