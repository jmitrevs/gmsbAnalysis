#! /usr/bin/env python

import math

from ROOT import gSystem
gSystem.Load('libRooFit')

from ROOT import *

###################################################################
### NOTE: THIS FILE DOES EVERYTHING IN GEV!!!!!!!
###################################################################

MINV_WINDOW_LO = 81.0
MINV_WINDOW_HI = 101.0

#if the fitting LO and HI are equal, then the fit is made over the whole range
FIT_LO = 40.0
FIT_HI = 120.0

minv_low = 0
minv_high = 150

ZMASS = 91.1876
ZWIDTH = 2.4952
STR_ZMASS = "91.1876"
STR_ZWIDTH = "2.4952"

def calcEff(h_eff, h_num, h_den, subBack):
    '''Calculate the efficiency given the numerator and denominator histograms, and fill the eff histogram.
     The first dimension must be the invariant mass distribution'''
    if (h_num.GetDimension() != h_den.GetDimension() or
        h_num.GetDimension() == 1 and h_eff.GetDimension() != 1 or
        h_num.GetDimension() > 1 and h_eff.GetDimension() != h_num.GetDimension() - 1):
        raise TypeError("Histograms of incompatible dimensions passed")
    
    if h_num.GetDimension() == 1:
        eff, err = calcEff1D(h_num, h_den, subBack)
        h_eff.SetBinContent(1, eff)
        h_eff.SetBinError(1, err)
    elif h_num.GetDimension() == 2:
        nbinsx = h_eff.GetNbinsX()
        if nbinsx != h_num.GetNbinsY() or nbinsx != h_den.GetNbinsY():
            raise TypeError("Histograms of incompatible number of bins passed")
        for b in range(nbinsx+2):
            proj_num = h_num.ProjectionX(h_num.GetName() + "proj_" + str(b), b, b)
            proj_den = h_den.ProjectionX(h_den.GetName() + "proj_" + str(b), b, b)
            eff, err = calcEff1D(proj_num, proj_den, subBack)
            h_eff.SetBinContent(b, eff)
            h_eff.SetBinError(b, err)
    else:
        raise NotImplementedError("Currently only support 1D and 2D histograms as input (0D and 1D output)")
        
    
def calcEff1D(h_num, h_den, subBack):
    '''Calculate the efficiency given the 1D numerator and denominator histograms, and return (eff, err).
     NOT MEANT TO BE USED DIRECTLY. ONLY CALLED FROM calcEff'''
    if subBack:
        raise NotImplementedError("Background subtraction is not yet implemented")
        # a variable repesenting the invariant mass
        minv = RooRealVar("minv","invariant mass", minv_low, minv_high)

        # the signal -- Voigtian
        mean = RooRealVar("mean", "mean (the Z mass)", ZMASS, ZMASS-5.0, ZMASS+5.0)
        #width = RooFormulaVar("width", "@0 * " + STR_ZWIDTH + "/" + STR_ZMASS, RooArgList(mean))
        width = RooRealVar("width", "width", ZWIDTH)
        sigma = RooRealVar("sigma","sigma (the sigma of the gaussian)",2.0 , 0.05, 3.0);

        sigPDF = RooVoigtian("sigPDF", "sigPDF", minv, mean, width, sigma)

        # # the signal -- CB
        # mean = RooRealVar("mean", "mean (the Z mass)", ZMASS, ZMASS-0.5, ZMASS+0.5)
        # sigma = RooRealVar("sigma","sigma (the sigma of the gaussian)",1.0 , 0.05, 4.0);
        # alpha = RooRealVar("alph","alpha", 0.01, 300.0);
        # n = RooRealVar("n","n", 0.01, 3.0);
        # sigPDF = RooCBShape("sigPDF", "sigPDF", minv, mean, sigma, alpha, n)

        # the background
        expScale = RooRealVar("expScale", "expScale", 0.0, -2.0, 0.0)
        backPDF = RooExponential("backPDF", "backPDF", minv, expScale)
        #turnon = RooRealVar("turnon", "turnon", 0., 0., 200.)
        #steepness = RooRealVar("steepness", "steepness of turnon", 0., 0., 2.)
        
        #erfcPDF = RooGenericPDF("erfcPDF", "The turnon part of the pdf", "erfc((@1 - @0) * @2)", RooArgList(minv, turnon, steepness))

        nsig = RooRealVar("nsig","numuber of signal events",50000,0.,1e10)
        nbkg = RooRealVar("nbkg","number of background events",10000,0.,1e10) 
        totPDF = RooAddPdf("totPDF", "sum of signal and background", RooArgList(sigPDF, backPDF), RooArgList(nsig, nbkg)) 

        rh_num = RooDataHist("rh_num", "numerator histogram", RooArgList(minv), h_num)
        rh_den = RooDataHist("rh_deb", "denominaot histogram", RooArgList(minv), h_den)

        canvas = TCanvas("myCanvas")
        frame = minv.frame()
        rh_den.plotOn(frame)
        frame.Draw()
        totPDF.fitTo(rh_den, RooFit.Extended(True), RooFit.Range(FIT_LO, FIT_HI))
        totPDF.plotOn(frame,  RooFit.LineColor(kRed))
        frame.Draw()
        canvas.SaveAs("myframe.png")


        return (0.0, 0.0)

    else:
        num = 0.0
        den = 0.0
        for b in range(1, h_num.GetNbinsX() + 1):
            if MINV_WINDOW_LO <= h_num.GetBinLowEdge(b) < MINV_WINDOW_HI:
                num += h_num.GetBinContent(b)
                den += h_den.GetBinContent(b)
        if den != 0:
            return (num / den, EfficiencyError(num, den))
        else:
            return (0.0, 0.0)

def EfficiencyError(a, b):
    'Returns the error when not doing background subtracion. From D0'
    return math.sqrt((a+1.0)*(b-a+1.0)/(b+2.0)/(b+2.0)/(b+3.0))
