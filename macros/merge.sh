#
ln -s ../*GamNp1*/*root* gamma_Np1.root
ln -s ../*GamNp2*/*root* gamma_Np2.root
hadd  gamma_Np3.root ../*GamNp3*/*root*
ln -s ../*GamNp4*/*root* gamma_Np4.root
ln -s ../*GamNp5*/*root* gamma_Np5.root

hadd Wenu_Np0.root ../*WenuNp0*/*root*
hadd Wenu_Np1.root ../*WenuNp1*/*root*
hadd Wenu_Np2.root ../*WenuNp2*/*root*
hadd Wenu_Np3.root ../*WenuNp3*/*root*
ln -s ../*WenuNp4*/*root* Wenu_Np4.root
ln -s ../*WenuNp5*/*root* Wenu_Np5.root

ln -s ../*WtaunuNp0*/*root* Wtaunu_Np0.root
ln -s ../*WtaunuNp1*/*root* Wtaunu_Np1.root
ln -s ../*WtaunuNp2*/*root* Wtaunu_Np2.root
ln -s ../*WtaunuNp3*/*root* Wtaunu_Np3.root
ln -s ../*WtaunuNp4*/*root* Wtaunu_Np4.root
ln -s ../*WtaunuNp5*/*root* Wtaunu_Np5.root

hadd Wgamma_Np0.root ../*WgammaNp0*/*root*
hadd Wgamma_Np1.root ../*WgammaNp1*/*root*
ln -s ../*WgammaNp2*/*root* Wgamma_Np2.root 
ln -s ../*WgammaNp3*/*root* Wgamma_Np3.root
ln -s ../*WgammaNp4*/*root* Wgamma_Np4.root
ln -s ../*WgammaNp5*/*root* Wgamma_Np5.root

hadd ttbar.root ../*T1_McAtNlo_Jimmy*/*root*
hadd WW.root ../*WW*/*root*
ln -s ../*ZZ*/*root* ZZ.root
hadd WZ.root ../*WZ*/*root*
ln -s ../*st_tchan_taunu*/*root* st_tchan_taunu.root
ln -s ../*st_tchan_enu*/*root* st_tchan_enu.root
ln -s ../*st_Wt*/*root* st_Wt.root

ln -s ../*ZnunuNp0*/*root* Znunu_Np0.root
ln -s ../*ZnunuNp1*/*root* Znunu_Np1.root
ln -s ../*ZnunuNp2*/*root* Znunu_Np2.root
ln -s ../*ZnunuNp3*/*root* Znunu_Np3.root
ln -s ../*ZnunuNp4*/*root* Znunu_Np4.root
ln -s ../*ZnunuNp5*/*root* Znunu_Np5.root

hadd Zee_Np0.root ../*ZeeNp0*/*root*
hadd Zee_Np1.root ../*ZeeNp1*/*root*
hadd Zee_Np2.root ../*ZeeNp2*/*root*
hadd Zee_Np3.root ../*ZeeNp3*/*root*
hadd Zee_Np4.root ../*ZeeNp4*/*root*
hadd Zee_Np5.root ../*ZeeNp5*/*root*

hadd Ztautau_Np0.root ../*ZtautauNp0*/*root*
hadd Ztautau_Np1.root ../*ZtautauNp1*/*root*
hadd Ztautau_Np2.root ../*ZtautauNp2*/*root*
hadd Ztautau_Np3.root ../*ZtautauNp3*/*root*
hadd Ztautau_Np4.root ../*ZtautauNp4*/*root*
hadd Ztautau_Np5.root ../*ZtautauNp5*/*root*

hadd Zeegamma.root ../*Sherpa_Zeegamma*/*root*
ln -s ../*Ztautaugamma*/*root* Ztautaugamma.root

ln -s ../*Znunugammagamma*/*root* Znunugammagamma.root
ln -s ../*Znunugamma_highpt*/*root* Znunugamma.root

ln -s ../*Whizard_Jimmy_TTbarPhoton_SM_NoFullHad*/*root* ttbargamma.root
