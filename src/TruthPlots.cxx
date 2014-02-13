#include "gmsbAnalysis/TruthPlots.h"
#include "AthenaKernel/errorcheck.h"

#include "TH1.h"

#include "GeneratorObjects/McEventCollection.h"
#include "HepMC/GenEvent.h"
#include "HepMC/GenParticle.h"

#include "GaudiKernel/SystemOfUnits.h"

#include <climits>

using Gaudi::Units::GeV;

/////////////////////////////////////////////////////////////////////////////
TruthPlots::TruthPlots(const std::string& name, ISvcLocator* pSvcLocator) :
  AthAlgorithm(name, pSvcLocator)
{
  // Name of the McEventCollection Container
  declareProperty("McEventContainerName",
		  m_McEventContainerName="GEN_EVENT",
		  "Name of the McEventCollection container");
  declareProperty("HistFileName", m_histFileName = "TruthPlots");

  declareProperty("TruthStudiesTool", m_truth);

}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode TruthPlots::initialize(){

  ATH_MSG_DEBUG("initialize()");
 
  CHECK(m_truth.retrieve());
  CHECK(service("THistSvc", m_thistSvc));

  TH1::SetDefaultSumw2(true);

  m_histograms["top_eta1"] = new TH1F("top_eta1","Psuedorapidity of the leading top;#eta", 50, -5,5);
  m_histograms["top_pt1"] = new TH1F("top_pt1","Transverse momentum of the leading top;p_{T} [GeV]", 50, 0, 250);
  m_histograms["top_m1"] = new TH1F("top_m1","Mass of the leading top;p_{T} [GeV]", 40, 160, 180);
  m_histograms["top_eta2"] = new TH1F("top_eta2","Psuedorapidity of the second top;#eta", 50, -5,5);
  m_histograms["top_pt2"] = new TH1F("top_pt2","Transverse momentum of the second top;p_{T} [GeV]", 50, 0, 250);
  m_histograms["top_m2"] = new TH1F("top_m2","Mass of the second top;p_{T} [GeV]", 40, 160, 180);

  m_histograms["W_eta1"] = new TH1F("W_eta1","Psuedorapidity of the leading W;#eta", 50, -5,5);
  m_histograms["W_pt1"] = new TH1F("W_pt1","Transverse momentum of the leading W;p_{T} [GeV]", 50, 0, 250);
  m_histograms["W_eta2"] = new TH1F("W_eta2","Psuedorapidity of the second W;#eta", 50, -5,5);
  m_histograms["W_pt2"] = new TH1F("W_pt2","Transverse momentum of the second W;p_{T} [GeV]", 50, 0, 250);

  m_histograms["bFromTop_eta1"] = new TH1F("bFromTop_eta1","Psuedorapidity of the leading bFromTop;#eta", 50, -5,5);
  m_histograms["bFromTop_pt1"] = new TH1F("bFromTop_pt1","Transverse momentum of the leading bFromTop;p_{T} [GeV]", 50, 0, 250);
  m_histograms["bFromTop_eta2"] = new TH1F("bFromTop_eta2","Psuedorapidity of the second bFromTop;#eta", 50, -5,5);
  m_histograms["bFromTop_pt2"] = new TH1F("bFromTop_pt2","Transverse momentum of the second bFromTop;p_{T} [GeV]", 50, 0, 250);

  m_histograms["otherB_eta1"] = new TH1F("otherB_eta1","Psuedorapidity of the leading otherB;#eta", 50, -5,5);
  m_histograms["otherB_pt1"] = new TH1F("otherB_pt1","Transverse momentum of the leading otherB;p_{T} [GeV]", 50, 0, 250);
  m_histograms["otherB_eta2"] = new TH1F("otherB_eta2","Psuedorapidity of the second otherB;#eta", 50, -5,5);
  m_histograms["otherB_pt2"] = new TH1F("otherB_pt2","Transverse momentum of the second otherB;p_{T} [GeV]", 50, 0, 250);

  m_histograms["lightQ_eta1"] = new TH1F("lightQ_eta1","Psuedorapidity of the leading lightQ;#eta", 50, -5,5);
  m_histograms["lightQ_pt1"] = new TH1F("lightQ_pt1","Transverse momentum of the leading lightQ;p_{T} [GeV]", 50, 0, 250);
  m_histograms["lightQ_eta2"] = new TH1F("lightQ_eta2","Psuedorapidity of the second lightQ;#eta", 50, -5,5);
  m_histograms["lightQ_pt2"] = new TH1F("lightQ_pt2","Transverse momentum of the second lightQ;p_{T} [GeV]", 50, 0, 250);


  m_thistSvc->regHist(std::string("/")+m_histFileName+"/top_eta1" , m_histograms["top_eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/top_pt1" , m_histograms["top_pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/top_m1" , m_histograms["top_m1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/top_eta2" , m_histograms["top_eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/top_pt2" , m_histograms["top_pt2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/top_m2" , m_histograms["top_m2"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/W_eta1" , m_histograms["W_eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/W_pt1" , m_histograms["W_pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/W_eta2" , m_histograms["W_eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/W_pt2" , m_histograms["W_pt2"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/bFromTop_eta1" , m_histograms["bFromTop_eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/bFromTop_pt1" , m_histograms["bFromTop_pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/bFromTop_eta2" , m_histograms["bFromTop_eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/bFromTop_pt2" , m_histograms["bFromTop_pt2"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/otherB_eta1" , m_histograms["otherB_eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/otherB_pt1" , m_histograms["otherB_pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/otherB_eta2" , m_histograms["otherB_eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/otherB_pt2" , m_histograms["otherB_pt2"]).ignore();

  m_thistSvc->regHist(std::string("/")+m_histFileName+"/lightQ_eta1" , m_histograms["lightQ_eta1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/lightQ_pt1" , m_histograms["lightQ_pt1"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/lightQ_eta2" , m_histograms["lightQ_eta2"]).ignore();
  m_thistSvc->regHist(std::string("/")+m_histFileName+"/lightQ_pt2" , m_histograms["lightQ_pt2"]).ignore();


  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode TruthPlots::execute() 
{
  ATH_MSG_DEBUG("execute");

  double weight = 1.0;

  const McEventCollection * aMcEventContainer;
  CHECK(evtStore()->retrieve(aMcEventContainer, m_McEventContainerName));

  const HepMC::GenEvent * aGenEvent = *(aMcEventContainer->begin());
  const HepMC::WeightContainer& weightContainer = aGenEvent->weights();
      
  if(weightContainer.size() > 0) weight = weightContainer[0];
  
  CHECK(m_truth->execute());

  const std::vector<const HepMC::GenParticle *>& tops = m_truth->tops();
  if (tops.size() > 0) {
    const HepMC::GenParticle *top = tops[0];
    m_histograms["top_m1"]->Fill(top->generated_mass()/GeV, weight);
    const HepMC::FourVector& p = top->momentum();
    m_histograms["top_pt1"]->Fill(p.perp()/GeV, weight);
    m_histograms["top_eta1"]->Fill(p.eta(), weight);
  }
  if (tops.size() > 1) {
    const HepMC::GenParticle *top = tops[1];
    m_histograms["top_m2"]->Fill(top->generated_mass()/GeV, weight);
    const HepMC::FourVector& p = top->momentum();
    m_histograms["top_pt2"]->Fill(p.perp()/GeV, weight);
    m_histograms["top_eta2"]->Fill(p.eta(), weight);
  }

  const std::vector<const HepMC::GenParticle *>& Ws = m_truth->Ws();
  if (Ws.size() > 0) {
    const HepMC::FourVector& p = Ws[0]->momentum();
    m_histograms["W_pt1"]->Fill(p.perp()/GeV, weight);
    m_histograms["W_eta1"]->Fill(p.eta(), weight);
    if (Ws.size() > 1) {
      const HepMC::FourVector& p = Ws[1]->momentum();
      m_histograms["W_pt2"]->Fill(p.perp()/GeV, weight);
      m_histograms["W_eta2"]->Fill(p.eta(), weight);
    }
  } else {
    const std::vector<ROOT::Math::PxPyPzEVector>& WsAlt = m_truth->WsAlt();
    if (WsAlt.size() > 0) {
      const ROOT::Math::PxPyPzEVector& p = WsAlt[0];
      m_histograms["W_pt1"]->Fill(p.Pt()/GeV, weight);
      m_histograms["W_eta1"]->Fill(p.Eta(), weight);
      if (WsAlt.size() > 1) {
	const ROOT::Math::PxPyPzEVector& p = WsAlt[1];
	m_histograms["W_pt2"]->Fill(p.Pt()/GeV, weight);
	m_histograms["W_eta2"]->Fill(p.Eta(), weight);
      }
    }
  }
    

  const std::vector<const HepMC::GenParticle *>& bFromTops = m_truth->bsFromTops();
  if (bFromTops.size() > 0) {
    const HepMC::FourVector& p = bFromTops[0]->momentum();
    m_histograms["bFromTop_pt1"]->Fill(p.perp()/GeV, weight);
    m_histograms["bFromTop_eta1"]->Fill(p.eta(), weight);
  }
  if (bFromTops.size() > 1) {
    const HepMC::FourVector& p = bFromTops[1]->momentum();
    m_histograms["bFromTop_pt2"]->Fill(p.perp()/GeV, weight);
    m_histograms["bFromTop_eta2"]->Fill(p.eta(), weight);
  }

  const std::vector<const HepMC::GenParticle *>& otherBs = m_truth->otherBs();
  if (otherBs.size() > 0) {
    const HepMC::FourVector& p = otherBs[0]->momentum();
    m_histograms["otherB_pt1"]->Fill(p.perp()/GeV, weight);
    m_histograms["otherB_eta1"]->Fill(p.eta(), weight);
  }
  if (otherBs.size() > 1) {
    const HepMC::FourVector& p = otherBs[1]->momentum();
    m_histograms["otherB_pt2"]->Fill(p.perp()/GeV, weight);
    m_histograms["otherB_eta2"]->Fill(p.eta(), weight);
  }

  const std::vector<const HepMC::GenParticle *>& lightQs = m_truth->lightQuarks();
  if (lightQs.size() > 0) {
    const HepMC::FourVector& p = lightQs[0]->momentum();
    m_histograms["lightQ_pt1"]->Fill(p.perp()/GeV, weight);
    m_histograms["lightQ_eta1"]->Fill(p.eta(), weight);
  }
  if (lightQs.size() > 1) {
    const HepMC::FourVector& p = lightQs[1]->momentum();
    m_histograms["lightQ_pt2"]->Fill(p.perp()/GeV, weight);
    m_histograms["lightQ_eta2"]->Fill(p.eta(), weight);
  }

  return StatusCode::SUCCESS;
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
StatusCode TruthPlots::finalize() {
    
  ATH_MSG_DEBUG ("finalize()");
  
  return StatusCode::SUCCESS;
}
