#! /usr/bin/env python

base = "plots"

import os
import os.path

for lepton in ("electron", "muon"):
    for i in ("PRESEL", "SR", "WCR", "HMET", "HMT"):
        path = base+"/"+lepton+"/"+i
        if not os.path.exists(path):
            os.makedirs(path)

        os.system("./RunAnalysis.py -l " + lepton + " -p " + i + " > /dev/null")
        if lepton == "electron":
            os.system("./mergeOutput.sh")
        else:
            os.system("./mergeOutput_mu.sh")
        os.system("./SimpleLepPhotonPlots.py --lepton=" + lepton + " > /dev/null")
        os.system("./SimpleLepPhotonPlots.py --lepton=" + lepton + " -g > /dev/null")
        os.system("./SimpleLepPhotonPlots.py --lepton=" + lepton + " --log > /dev/null")
        os.system("./SimpleLepPhotonPlots.py --lepton=" + lepton + " -g --log > /dev/null")
        os.system("mv *Plot.eps " + path)


        
