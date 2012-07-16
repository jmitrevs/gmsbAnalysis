#
rm ZjetsHist.root ZgammaHist.root total.root
hadd ZjetsHist.root Zee_Np* Ztautau_Np*
hadd ZgammaHist.root ZeegammaHist.root ZtautaugammaHist.root
hadd total.root ZjetsHist.root ZgammaHist.root diphotonsHist.root
