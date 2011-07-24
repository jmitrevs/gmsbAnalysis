#ifndef GMSBANALYSIS_BACKGROUNDMODELEE_H
#define GMSBANALYSIS_BACKGROUNDMODELEE_H

#include "AthenaBaseComps/AthAlgorithm.h"
#include "GaudiKernel/ITHistSvc.h"
#include "AthenaKernel/IUserDataSvc.h"

#include "gmsbTools/gmsbPreparationTool.h"
#include "gmsbTools/gmsbOverlapRemovalTool.h"

#include "TRandom3.h"

class Jet;
namespace Reco  { class ITrackToVertex; }
class ISUSYPhotonJetCleaningTool;

/////////////////////////////////////////////////////////////////////////////
class BackgroundModelEE:public AthAlgorithm {
public:
  BackgroundModelEE (const std::string& name, ISvcLocator* pSvcLocator);
  StatusCode initialize();
  StatusCode execute();
  StatusCode finalize();

  enum NUM_CUTS_t {NUM_CUTS = 20};

private:

  bool isBad(const Jet *) const;

  bool m_isMC;

  /** MET selecton */
  std::string m_METContainerName;

  double m_leadElPtCut;

  /** primary vertex container */
  std::string m_vxCandidatesName;

  /// a handle on the Hist/TTree registration service
  ITHistSvc * m_thistSvc;
  std::string m_histFileName;

  std::map<std::string, TH1*> m_histograms;

  // tools for selection

  /** get a handle on the user tool for pre-selection and overlap removal */
  ToolHandle<gmsbPreparationTool>     m_PreparationTool;
  ToolHandle<gmsbPreparationTool>     m_CrackPreparationTool;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool1;
  ToolHandle<gmsbOverlapRemovalTool>  m_OverlapRemovalTool2;

  /** @brief Tool handle for track extrapolation to vertex */
  ToolHandle< Reco::ITrackToVertex > m_trackToVertexTool;
  
  /** @breif Tool handle for jet cleaning */  
  ToolHandle<ISUSYPhotonJetCleaningTool>  m_JetCleaningTool;

  // user data
  ServiceHandle<IUserDataSvc> m_userdatasvc;

  // for bookkeeping
  double numEventsCut[NUM_CUTS];

  // mee (Z) window cut
  double m_windowLow;
  double m_windowHigh;
  
  mutable TRandom3 m_rand3;
};

#endif // GMSBANALYSIS_BACKGROUNDMODELEE_H
