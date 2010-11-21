#ifndef checkOQ_h
#define checkOQ_h

#include "TROOT.h"
#include "TString.h"
#include "TFile.h"
#include "TH2I.h"
#include <vector>
#include <iostream>

#include <string>
using std::string;

using namespace std;

namespace egammaOQ {
  vector<double> provideCellCenterS2(double myEta, double myPhi, bool verbose=false);
  int checkOQRegion(double myEta, double myPhi, double deltaEta, double deltaPhi, int candidate, bool verbose=false);
  int checkOQCoreRegion(double myEta, double myPhi, double deltaEta, double deltaPhi, int candidate, bool verbose=false);
  int checkOQ(TH2I *histo, double myEta, double myPhi);
  int checkOQCluster(int runnumber, double myEta, double myPhi, int candidate, bool verbose=false);
  int checkOQClusterElectron(int runnumber, double myEta, double myPhi, bool verbose=false);
  int checkOQClusterPhoton(int runnumber, double myEta, double myPhi, bool verbose=false);
  int checkOQCluster(double myEta, double myPhi, int NetaCells, int NphiCells, int candidate, bool verbose=false);
  int checkOQPointTile(double myEta, double myPhi);
  bool checkHistoBound(TH2I* histo, double myEta, double myPhi);
  int checkOQMap(TH2I* histo, double myEta, double myPhi, double deltaEta, double deltaPhi, double granularity);
  int LoadOQMaps(int runnumber);
  int GetMapNumber(int runnumber);

#if !defined(__CINT__) || defined(__MAKECINT__) 
  extern TH2I *thehEMPS;
  extern TH2I *thehEMS1;
  extern TH2I *thehEMS2;
  extern TH2I *thehEMS3;
  extern TH2I *thehTile;
  extern TH2I *thehEMS1onlyDeadFeb;
  extern TH2I *thehEMS2onlyDeadFeb;
  extern TH2I *thehEMPSOnlyHV;
  extern TH2I *thehEMS1S2S3OnlyHV;
  extern TH2I *thehEMPSonlyDeadFeb;
  extern int OQMapInMemory;
  extern TFile* OQMapFile;

#else
  TH2I *thehEMPS;
  TH2I *thehEMS1;
  TH2I *thehEMS2;
  TH2I *thehEMS3;
  TH2I *thehTile;
  TH2I *thehEMS1onlyDeadFeb;
  TH2I *thehEMS2onlyDeadFeb;
  TH2I *thehEMPSOnlyHV;
  TH2I *thehEMS1S2S3OnlyHV;
  TH2I *thehEMPSonlyDeadFeb;
  int OQMapInMemory;
  TFile* OQMapFile;

#endif
}

#endif
