# based on piece of C code from Jan Erik Sundermann
# see 1-lepton SUSY sharepoint

from ROOT import TMath
from math import sqrt


  
def calcPoissonCLLower( obs, q=0.68269 ) :
    """
    Calculate lower confidence limit
    e.g. to calculate the 68% lower limit for 2 observed events:
    calcPoissonCLLower(2.)
    """
    LL = 0.

    if q==0.68269 and obs > 1000 : 
        LL = obs - sqrt(obs+0.25) + 0.5
        return LL
    
    if obs >= 0. :
        a = (1. - q) / 2. # = 0.025 for 95% confidence interval
        LL = TMath.ChisquareQuantile(a, 2.*obs) / 2.
        pass
    return LL



def calcPoissonCLUpper( obs, q=0.68269 ):
    """
    Calculate upper confidence limit
    e.g. to calculate the 68% upper limit for 2 observed events:
    calcPoissonCLUpper(2.)
    """
    UL = 0.

    if q==0.68269 and obs > 1000 : 
        UL = obs + sqrt(obs+0.25) + 0.5
        return UL

    if obs >= 0. :
        a = 1. - (1. - q) / 2. # = 0.025 for 95% confidence interval
        UL = TMath.ChisquareQuantile(a, 2.* (obs + 1.)) / 2.
        pass

    return UL




def findExpForProb( q, obs, oneSided=True, tol=0.01 ):
    """
    q = confidence level, e.g. 68%
    """

    if oneSided : fac = 1.
    else : fac = 2.

    step = 0.01
    
    exp = 0.0
    res = 1.0
    while (abs(res) > tol):
        p = 0.
        for evt in xrange( obs +1 ):
            p += TMath.Poisson( evt, exp )

        res = p - ( 1.0 - q)/fac
        if res < 0.: exp -= step
        else: exp += step

    
    return exp


def UpErr(q, obs):
    if obs == 0.:
        return findExpForProb(q, obs, oneSided=True) - obs
    else:
        return findExpForProb(q, obs, oneSided=False) - obs
#    else:
#        return calcPoissonCLUpper(q, obs) - obs

    


def getup(n,cl):
    import ROOT
    import math
    # Upper statistical uncertainty on poisson distribution
    # Vary poisson expectation value x till cumulative density function < limit
    # limit depend on confidence level
    limit = (1. - cl)/2. # 2-sided confidence interval => divide by 2
    if n == 0.: limit = 1. - cl # 1-sided confidence interval because only upper limit is valid
    sigma = math.sqrt(n) if n > 1. else 1.
    nit = 1000
    nn = int(n)
    xup = n
    success = False
    for i in range(nit):
        x = float(n) + float(i)/float(nit)*5.*sigma
        cdf = ROOT.Math.poisson_cdf(nn,x)
        if cdf > limit: continue
        success = True
        xup = x
        break
    if not success: print "Warning: getdown has not succeed to find a lower bound"
    return xup
