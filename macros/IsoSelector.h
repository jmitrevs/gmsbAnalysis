//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Mar 25 09:52:18 2011 by ROOT version 5.26/00e
// from TTree PhotonTree/TTree for photon isolation
// found on file: user.jmitrevs.004638.PhotonIso._00185.root
//////////////////////////////////////////////////////////

#ifndef IsoSelector_h
#define IsoSelector_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TH1.h>
#include <TH2.h>

class IsoSelector : public TSelector {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain

   // Declaration of leaf types
   Int_t           Run;
   Int_t           Event;
   Int_t           LumiBlock;
   Double_t        Weight;
   Int_t           PhotonN;
   vector<int>     *PhotonConv;
   vector<double>  *PhotonEt;
   vector<double>  *PhotonE;
   vector<double>  *PhotonEta;
   vector<double>  *PhotonClusterEta;
   vector<double>  *PhotonPhi;
   vector<double>  *PhotonEtcone20;
   vector<double>  *PhotonEtcone40;
   vector<double>  *PhotonEtcone20_corr;
   vector<double>  *PhotonEtcone40_corr;

   // List of branches
   TBranch        *b_Run;   //!
   TBranch        *b_Event;   //!
   TBranch        *b_LumiBlock;   //!
   TBranch        *b_Weight;   //!
   TBranch        *b_PhotonN;   //!
   TBranch        *b_PhotonConv;   //!
   TBranch        *b_PhotonEt;   //!
   TBranch        *b_PhotonE;   //!
   TBranch        *b_PhotonEta;   //!
   TBranch        *b_PhotonClusterEta;   //!
   TBranch        *b_PhotonPhi;   //!
   TBranch        *b_PhotonEtcone20;   //!
   TBranch        *b_PhotonEtcone40;   //!
   TBranch        *b_PhotonEtcone20_corr;   //!
   TBranch        *b_PhotonEtcone40_corr;   //!

   IsoSelector(TTree * /*tree*/ =0) { }
   virtual ~IsoSelector() { }
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual Int_t   GetEntry(Long64_t entry, Int_t getall = 0) { return fChain ? fChain->GetTree()->GetEntry(entry, getall) : 0; }
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();

  TFile *fileOut;

  TH1D *hetcone20;
  TH1D *het;

  TH1D *hetcone20ovet;

  TH2D *hetcone20_0p6;
  TH2D *hetcone20_1p37;
  TH2D *hetcone20_1p81;

  TH2D *hetcone20ovet_0p6;
  TH2D *hetcone20ovet_1p37;
  TH2D *hetcone20ovet_1p81;

   ClassDef(IsoSelector,0);
};

#endif

#ifdef IsoSelector_cxx
void IsoSelector::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   PhotonConv = 0;
   PhotonEt = 0;
   PhotonE = 0;
   PhotonEta = 0;
   PhotonClusterEta = 0;
   PhotonPhi = 0;
   PhotonEtcone20 = 0;
   PhotonEtcone40 = 0;
   PhotonEtcone20_corr = 0;
   PhotonEtcone40_corr = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("Run", &Run, &b_Run);
   fChain->SetBranchAddress("Event", &Event, &b_Event);
   fChain->SetBranchAddress("LumiBlock", &LumiBlock, &b_LumiBlock);
   fChain->SetBranchAddress("Weight", &Weight, &b_Weight);
   fChain->SetBranchAddress("PhotonN", &PhotonN, &b_PhotonN);
   fChain->SetBranchAddress("PhotonConv", &PhotonConv, &b_PhotonConv);
   fChain->SetBranchAddress("PhotonEt", &PhotonEt, &b_PhotonEt);
   fChain->SetBranchAddress("PhotonE", &PhotonE, &b_PhotonE);
   fChain->SetBranchAddress("PhotonEta", &PhotonEta, &b_PhotonEta);
   fChain->SetBranchAddress("PhotonClusterEta", &PhotonClusterEta, &b_PhotonClusterEta);
   fChain->SetBranchAddress("PhotonPhi", &PhotonPhi, &b_PhotonPhi);
   fChain->SetBranchAddress("PhotonEtcone20", &PhotonEtcone20, &b_PhotonEtcone20);
   fChain->SetBranchAddress("PhotonEtcone40", &PhotonEtcone40, &b_PhotonEtcone40);
   fChain->SetBranchAddress("PhotonEtcone20_corr", &PhotonEtcone20_corr, &b_PhotonEtcone20_corr);
   fChain->SetBranchAddress("PhotonEtcone40_corr", &PhotonEtcone40_corr, &b_PhotonEtcone40_corr);
}

Bool_t IsoSelector::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

#endif // #ifdef IsoSelector_cxx
