#! /usr/bin/env python

import math
import ROOT
ROOT.gROOT.SetBatch()
#ROOT.gROOT.LoadMacro("AtlasStyle.C") 
#ROOT.SetAtlasStyle()

INPUT_FILE = "/data/jmitrevs/SignalUncertaintiesUtils/output_strong.root"

dataSetID = {}

dataSetID['600_100'] = 174988
dataSetID['600_150'] = 174989
dataSetID['600_200'] = 174990
dataSetID['600_350'] = 174991
dataSetID['600_500'] = 174992
dataSetID['600_580'] = 174993
dataSetID['650_100'] = 174994
dataSetID['650_150'] = 174995
dataSetID['650_200'] = 174996
dataSetID['650_350'] = 174997
dataSetID['650_500'] = 174998
dataSetID['650_630'] = 174999
dataSetID['700_100'] = 175000
dataSetID['700_150'] = 175001
dataSetID['700_200'] = 175002
dataSetID['700_350'] = 175003
dataSetID['700_500'] = 175004
dataSetID['700_680'] = 175005
dataSetID['750_100'] = 175006
dataSetID['750_150'] = 175007
dataSetID['750_200'] = 175008
dataSetID['750_350'] = 175009
dataSetID['750_500'] = 175010
dataSetID['750_730'] = 175011
dataSetID['800_100'] = 175012
dataSetID['800_150'] = 175013
dataSetID['800_200'] = 175014
dataSetID['800_350'] = 175015
dataSetID['800_500'] = 175016
dataSetID['800_700'] = 175017
dataSetID['800_780'] = 175018
dataSetID['850_100'] = 175019
dataSetID['850_150'] = 175020
dataSetID['850_200'] = 175021
dataSetID['850_350'] = 175022
dataSetID['850_500'] = 175023
dataSetID['850_700'] = 175024
dataSetID['850_830'] = 175025
dataSetID['900_100'] = 175026
dataSetID['900_150'] = 175027
dataSetID['900_200'] = 175028
dataSetID['900_350'] = 175029
dataSetID['900_500'] = 175030
dataSetID['900_700'] = 175031
dataSetID['900_880'] = 175032
dataSetID['950_100'] = 175033
dataSetID['950_150'] = 175034
dataSetID['950_200'] = 175035
dataSetID['950_350'] = 175036
dataSetID['950_500'] = 175037
dataSetID['950_700'] = 175038
dataSetID['950_930'] = 175039
dataSetID['1000_100'] = 175040
dataSetID['1000_150'] = 175041
dataSetID['1000_200'] = 175042
dataSetID['1000_350'] = 175043
dataSetID['1000_500'] = 175044
dataSetID['1000_700'] = 175045
dataSetID['1000_900'] = 175046
dataSetID['1000_980'] = 175047

filterEff = {}
filterEff['600_100'] = 4.0933E-01
filterEff['600_150'] = 3.3899E-01
filterEff['600_200'] = 2.8805E-01 
filterEff['600_350'] = 2.8329E-01 
filterEff['600_500'] = 3.0108E-01 
filterEff['600_580'] = 3.2665E-01 
filterEff['650_100'] = 4.3529E-01 
filterEff['650_150'] = 3.6195E-01 
filterEff['650_200'] = 3.0288E-01 
filterEff['650_350'] = 2.8631E-01 
filterEff['650_500'] = 3.0387E-01 
filterEff['650_630'] = 3.3650E-01 
filterEff['700_100'] = 4.5990E-01 
filterEff['700_150'] = 3.8045E-01 
filterEff['700_200'] = 3.2007E-01 
filterEff['700_350'] = 2.9210E-01 
filterEff['700_500'] = 3.0610E-01 
filterEff['700_680'] = 3.4715E-01 
filterEff['750_100'] = 4.8177E-01
filterEff['750_150'] = 4.0229E-01 
filterEff['750_200'] = 3.3558E-01 
filterEff['750_350'] = 3.0285E-01 
filterEff['750_500'] = 3.1184E-01 
filterEff['750_730'] = 3.6320E-01 
filterEff['800_100'] = 5.0374E-01 
filterEff['800_150'] = 4.1712E-01 
filterEff['800_200'] = 3.5205E-01 
filterEff['800_350'] = 3.1297E-01 
filterEff['800_500'] = 3.1321E-01 
filterEff['800_700'] = 3.1321E-01 
filterEff['800_780'] = 3.7112E-01 
filterEff['850_100'] = 5.2802E-01 
filterEff['850_150'] = 4.3537E-01 
filterEff['850_200'] = 3.6936E-01 
filterEff['850_350'] = 3.2719E-01 
filterEff['850_500'] = 3.2021E-01 
filterEff['850_700'] = 3.4556E-01 
filterEff['850_830'] = 3.8473E-01 
filterEff['900_100'] = 5.4897E-01 
filterEff['900_150'] = 4.5486E-01 
filterEff['900_200'] = 3.8715E-01 
filterEff['900_350'] = 3.3959E-01 
filterEff['900_500'] = 3.2812E-01 
filterEff['900_700'] = 3.4766E-01 
filterEff['900_880'] = 3.9339E-01 
filterEff['950_100'] = 5.6675E-01 
filterEff['950_150'] = 4.7325E-01 
filterEff['950_200'] = 4.0427E-01 
filterEff['950_350'] = 3.5508E-01 
filterEff['950_500'] = 3.3909E-01 
filterEff['950_700'] = 3.5100E-01 
filterEff['950_930'] = 4.0490E-01 
filterEff['1000_100'] = 5.8360E-01 
filterEff['1000_150'] = 4.9142E-01 
filterEff['1000_200'] = 4.2361E-01 
filterEff['1000_350'] = 3.7261E-01 
filterEff['1000_500'] = 3.5405E-01 
filterEff['1000_700'] = 3.5594E-01 
filterEff['1000_900'] = 3.9216E-01 
filterEff['1000_980'] = 4.1815E-01 


class signalXsecsStrong:
    def __init__(self):
        'This function returns the cross sections seprated between weak and strong'
        f = ROOT.TFile(INPUT_FILE)
        ttree = f.Get("SignalUncertainties")

        self.xsec = {}
        for ev in ttree:
            key = "%.0f_%.0f" % (ev.m3, ev.m2)
            if key in self.xsec:
                self.xsec[key][0] += ev.crossSection
                self.xsec[key][1] += (ev.crossSection*ev.Tot_error)**2
            else:
                self.xsec[key] = [ev.crossSection, (ev.crossSection*ev.Tot_error)**2]
                
        # for key, item in self.xsec.items():
        #     print "%s & %.3f & %.3f \\\\" % (key, item[0], math.sqrt(item[1])/item[0])

    def getXsec(self, m3, m2):
        key = "%.0f_%.0f" % (m3, m2)
        return self.xsec[key][0]

    def getXsecRelError(self, m3, m2):
        key = "%.0f_%.0f" % (m3, m2)
        return math.sqrt(self.xsec[key][1])/self.xsec[key][0]

    def getXsecK(self, key):
        return self.xsec[key][0]

    def getXsecRelErrorK(self, key):
        return math.sqrt(self.xsec[key][1])/self.xsec[key][0]

    def geteff(self, m3, m2):
        key = "%.0f_%.0f" % (m3, m2)
        return filterEff[key]

if __name__ == "__main__":
    printSignalXsecs(INPUT_FILE)
