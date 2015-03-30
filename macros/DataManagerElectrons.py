#! /usr/bin/env python
'''
Module to store all the source files, yields, etc, for electron channel.
'''

from __future__ import division

import ROOT
# ROOT.gROOT.LoadMacro("AtlasStyle.C") 
# ROOT.SetAtlasStyle()

PRINT_YIELDS = False

#Lumi = 4812.34 # old
#Lumi = 4816.68 # old (but done again)
Lumi = 20300.0

DOSTANDARD = True
DOSYST = True

if 'DOTEST' not in globals():
    DOTEST = False

DOTEST = True

print "Lepton is ELECTRON."


path = "/data/jmitrevs/output/elphoton/v141110/mergedFiles/"

# format is (name, xsec in pb, kfac, eff, dsid)
names = (('Wenugamma', 0.71925, 1.0, 1.0, 126741),
         ('Wtaunugamma', 0.71925, 1.0, 1.0, 158727),
         ('dilep', 22.134, 1.1997, 1.0, 181087), 
         ('ttbargamma', 1.3963, 1.9, 7.0707E-02, 177998),
         ('singletop_tchan', 25.748, 1.1043, 1.0, 110101),
         ('tW', 20.461, 1.0933, 1.0, 110140),
         ('singletop_tchan_gamma', 0.187298, 1.000000, 0.121980, 202621),
         ('singletop_tchan_gammaDec', 0.313866, 1.000000, 0.012927, 202622),
         ('tW_dilep_gamma', 0.012915, 1.000000, 0.164370, 202623),
         ('tW_dilep_gammatDec', 0.014538, 1.000000, 0.028748, 202624),
         ('tW_dilep_gammaWDec', 0.010405, 1.000000, 0.075489, 202625),
         ('tW_tlepWhad_gamma', 0.025825, 1.000000, 0.162440, 202626),
         ('tW_tlepWhad_gammatDec', 0.029084, 1.000000, 0.027609, 202627),
         ('tW_tlepWhad_gammaWDec', 0.011594, 1.000000, 0.064709, 202628),
         ('tW_thadWlep_gamma', 0.025817, 1.000000, 0.161780, 202629),
         ('tW_thadWlep_gammatDec', 0.020127, 1.000000, 0.041977, 202630),
         ('tW_thadWlep_gammaWDec', 0.020788, 1.000000, 0.075740, 202631)
         )

# pathSyst = "/data/jmitrevs/output/elphoton/v141113_truth/mergedFiles/"
# namesSyst = (('Wenugamma_ckkw15', 0.71925, 1.0, 1.0, 204731),
#              ('Wenugamma_ckkw30', 0.71925, 1.0, 1.0, 204732),
#              ('Wenugamma_fac025', 0.71925, 1.0, 1.0, 204733),
#              ('Wenugamma_fac4', 0.71925, 1.0, 1.0, 204734),
#              ('Wenugamma_renorm025', 0.71925, 1.0, 1.0, 204735),
#              ('Wenugamma_renorm4', 0.71925, 1.0, 1.0, 204736),
#              ('ttbargamma_nom', 1.3963, 1.9, 7.0707E-02, 177998),
#              ('ttbargamma_scaleUP', 1.3963, 1.9, 7.0707E-02, 202332),
#              ('ttbargamma_scaleDN', 1.3963, 1.9, 7.0707E-02, 202333),
#              ('ttbargamma_alpsUP', 1.3963, 1.9, 7.0707E-02, 202334),
#              ('ttbargamma_alpsDN', 1.3963, 1.9, 7.0707E-02, 202335),
#              ('ttbargamma_lessFSR', 1.3963, 1.9, 7.0707E-02, 202336),
#              ('ttbargamma_moreFSR', 1.3963, 1.9, 7.0707E-02, 202337)
#              )

pathSyst = "/data/jmitrevs/output/elphoton/v150204_truth/mergedFiles/"
namesSyst = (
    # ('WenuPt70_140_ckkw15', 250.55, 1.11, 0.74456, 183497),
    # ('WenuPt70_140_ckkw30', 250.55, 1.11, 0.75784, 183498),
    # ('WenuPt70_140_fac025', 250.55, 1.11, 0.76846, 183499),
    # ('WenuPt70_140_fac4', 250.55, 1.11, 0.73826, 183500),
    ('WenuPt70_140_renorm025', 250.55, 1.11, 0.73177, 183501),
    ('WenuPt70_140_renorm4', 250.55, 1.11, 0.76347, 183502),
    # ('WenuPt140_280_ckkw15', 31.155, 1.11, 0.70323, 183515),
    # ('WenuPt140_280_ckkw30', 31.155, 1.11, 0.72312, 183516),
    # ('WenuPt140_280_fac025', 31.155, 1.11, 0.73174, 183517),
    # ('WenuPt140_280_fac4', 31.155, 1.11, 0.70092, 183518),
    ('WenuPt140_280_renorm025', 31.155, 1.11, 0.68695, 183519),
    ('WenuPt140_280_renorm4', 31.155, 1.11, 0.73235, 183520),
    ('WenuPt280_500_ckkw15', 1.8413, 1.11, 0.66937, 183533),
    ('WenuPt280_500_ckkw30', 1.8413, 1.11, 0.69556, 183534),
    ('WenuPt280_500_fac025', 1.8413, 1.11, 0.69974, 183535),
    ('WenuPt280_500_fac4', 1.8413, 1.11, 0.66888, 183536),
    ('WenuPt280_500_renorm025', 1.8413, 1.11, 0.65114, 183537),
    ('WenuPt280_500_renorm4', 1.8413, 1.11, 0.70563, 183538),
    ('WenuPt500_ckkw15', 0.10188, 1.11, 0.64323, 183551),
    ('WenuPt500_ckkw30', 0.10188, 1.11, 0.67156, 183552),
    ('WenuPt500_fac025', 0.10188, 1.11, 0.67314, 183553),
    ('WenuPt500_fac4', 0.10188, 1.11, 0.64569, 183554),
    ('WenuPt500_renorm025', 0.10188, 1.11, 0.62521, 183555),
    ('WenuPt500_renorm4', 0.10188, 1.11, 0.68381, 183556)
             )

binToLookAt = 12 #1 more than last Fill value because this count starts at 1

values = {}

if DOTEST:
    # path = "/data/jmitrevs/output/elphoton/v150116/mergedFiles/"

    # # format is (name, xsec in pb, kfac, eff, dsid)
    # names = (('dilep', 22.134, 1.1997, 1.0, 181087), 
    #          ('dilepAlt', 21.806 , 1.217, 1.0, 110001),
    #          ('dilepShLeptLept', 9.1637 , 1.2876, 1.0, 117800),
    #          ('dilepShLeptTaulept', 3.2296 , 1.286, 1.0, 117801),
    #          ('dilepShTauleptTaulept', 0.28 , 1.3053, 1.0, 117802),
    #          ('dilepShLeptTauhad', 6.0007 , 1.2741, 1.0, 117804),
    #          ('Znunugammagamma', 5.6e-3 , 2.0, 1.0, 167479)
    #          )

    path = "/data/jmitrevs/output/elphoton/v150317/mergedFiles/"

    # format is (name, xsec in pb, kfac, eff, dsid)
    names = (('Zeegamma', 0.18606, 1.0, 1.0, 158728), 
             ('Ztautaugamma', 0.18584, 1.0, 1.0, 158730) 
             )
    

if DOSTANDARD:
    for i in range(len(names)):
        name = names[i][0]
        fileName = path + name + ".root"
        fl = ROOT.TFile(fileName)
        cutFlow = fl.Get("Global/CutFlow")
        nOrig = cutFlow.GetBinContent(1)

        xsec = names[i][1]
        kfac = names[i][2]
        eff = names[i][3]
        scale = Lumi * xsec * kfac * eff / nOrig
        nAfterPreselect = cutFlow.GetBinContent(binToLookAt)
        yd = nAfterPreselect * scale

        values[name] = (fl, scale)

        if PRINT_YIELDS:
            print "name: nOrig =", nOrig, "scale =", scale, "yield =", yd

if DOSYST:
    for i in range(len(namesSyst)):
        name = namesSyst[i][0]
        fileName = pathSyst + name + ".root"
        fl = ROOT.TFile(fileName)
        cutFlow = fl.Get("Global/CutFlow")
        nOrig = cutFlow.GetBinContent(1)

        xsec = namesSyst[i][1]
        kfac = namesSyst[i][2]
        eff = namesSyst[i][3]
        scale = Lumi * xsec * kfac * eff / nOrig
        nAfterPreselect = cutFlow.GetBinContent(binToLookAt)
        yd = nAfterPreselect * scale

        values[name] = (fl, scale)

        if PRINT_YIELDS:
            print "name: nOrig =", nOrig, "scale =", scale, "yield =", yd
