#define IsoSelector_cxx
// The class definition in IsoSelector.h has been generated automatically
// by the ROOT utility TTree::MakeSelector(). This class is derived
// from the ROOT class TSelector. For more information on the TSelector
// framework see $ROOTSYS/README/README.SELECTOR or the ROOT User Manual.

// The following methods are defined in this file:
//    Begin():        called every time a loop on the tree starts,
//                    a convenient place to create your histograms.
//    SlaveBegin():   called after Begin(), when on PROOF called only on the
//                    slave servers.
//    Process():      called for each event, in this function you decide what
//                    to read and fill your histograms.
//    SlaveTerminate: called at the end of the loop on the tree, when on PROOF
//                    called only on the slave servers.
//    Terminate():    called at the end of the loop on the tree,
//                    a convenient place to draw/fit your histograms.
//
// To use this file, try the following session on your Tree T:
//
// Root > T->Process("IsoSelector.C")
// Root > T->Process("IsoSelector.C","some options")
// Root > T->Process("IsoSelector.C+")
//

#include "IsoSelector.h"
#include <TH2.h>
#include <TStyle.h>
#include <iostream>


void IsoSelector::Begin(TTree * /*tree*/)
{
   // The Begin() function is called at the start of the query.
   // When running with PROOF Begin() is only called on the client.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

   fileOut = TFile::Open("IsoOut.root","recreate");

   Int_t numBins = 8;
   Double_t bins[10] = {20000, 35000, 45000, 55000, 70000, 105000, 140000, 280000, 1000000};

   hetcone20 = new TH1D("hetcone20", "etcone20;Etleak [MeV]", 100, 0, 20000);
   het = new TH1D("het", "et;Etleak [MeV]", 200, 0, 100000);

   hetcone20ovet = new TH1D("hetcone20ovet", "etcone20/et vs et;etcone20/et", 100, 0, 1);
   

   hetcone20_0p6 = new TH2D("hetcone20_0p6", "etcone20 vs et;Etleak [MeV];Et [MeV]", 100, 0, 20000, numBins, bins);
   hetcone20_1p37 = new TH2D("hetcone20_1p37", "etcone20 vs et;Etleak [MeV];Et [MeV]", 100, 0, 20000, numBins, bins);
   hetcone20_1p81 = new TH2D("hetcone20_1p81", "etcone20 vs et;Etleak [MeV];Et [MeV]", 100, 0, 20000, numBins, bins);

   hetcone20ovet_0p6 = new TH2D("hetcone20ovet_0p6", "etcone20/et vs et;etcone20/et;Et [MeV]", 200, 0, 1, numBins, bins);
   hetcone20ovet_1p37 = new TH2D("hetcone20ovet_1p37", "etcone20/et vs et;etcone20/et;Et [MeV]", 200, 0, 1, numBins, bins);
   hetcone20ovet_1p81 = new TH2D("hetcone20ovet_1p81", "etcone20/et vs et;etcone20/et;Et [MeV]", 200, 0, 1, numBins, bins);

}

void IsoSelector::SlaveBegin(TTree * /*tree*/)
{
   // The SlaveBegin() function is called after the Begin() function.
   // When running with PROOF SlaveBegin() is called on each slave server.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

}

Bool_t IsoSelector::Process(Long64_t entry)
{
   // The Process() function is called for each entry in the tree (or possibly
   // keyed object in the case of PROOF) to be processed. The entry argument
   // specifies which entry in the currently loaded tree is to be processed.
   // It can be passed to either IsoSelector::GetEntry() or TBranch::GetEntry()
   // to read either all or the required parts of the data. When processing
   // keyed objects with PROOF, the object is already loaded and is available
   // via the fObject pointer.
   //
   // This function should contain the "body" of the analysis. It can contain
   // simple or elaborate selection criteria, run algorithms on the data
   // of the event and typically fill histograms.
   //
   // The processing can be stopped by calling Abort().
   //
   // Use fStatus to set the return value of TTree::Process().
   //
   // The return value is currently not used.

  GetEntry(entry);
  
  // b_PhotonN->GetEntry(entry);
  // PhotonEtcone20->clear();
  // b_PhotonEtcone20->GetEntry(entry);

  // cout << "Size = " << PhotonN << endl;

  for (int i = 0; i < PhotonN ; i++) {
    const Double_t et = PhotonEt->at(i);
    const Double_t eta = PhotonEta->at(i);

    Double_t etcone = 0;
    if (eta < 0.6) {
      etcone = PhotonEtcone20->at(i) + 0.007 * et;
      hetcone20_0p6->Fill(etcone, et);
      hetcone20ovet_0p6->Fill(etcone/et, et);
    } else if (eta < 1.37) {
      etcone = PhotonEtcone20->at(i) + 0.009 * et;
      hetcone20_1p37->Fill(etcone, et);
      hetcone20ovet_1p37->Fill(etcone/et, et);
    } else if (eta < 1.81) {
      etcone = PhotonEtcone20->at(i) + 0.008 * et;
      hetcone20_1p81->Fill(etcone, et);
      hetcone20ovet_1p81->Fill(etcone/et, et);
    }
    hetcone20->Fill(etcone);
    het->Fill(et);
    hetcone20ovet->Fill(etcone/et);

  }


   return kTRUE;
}

void IsoSelector::SlaveTerminate()
{
   // The SlaveTerminate() function is called after all entries or objects
   // have been processed. When running with PROOF SlaveTerminate() is called
   // on each slave server.

}

void IsoSelector::Terminate()
{
   // The Terminate() function is the last function to be called during
   // a query. It always runs on the client, it can be used to present
   // the results graphically or save the results to file.

   fileOut->Write();

}
