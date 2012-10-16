

from getPoissonConfidenceLevels import calcPoissonCLLower, calcPoissonCLUpper
from array import array
from ROOT import TGraphAsymmErrors

def MakePoissonConfidenceLevelErrors( hist ):
    x_val = array('f')
    y_val = array('f')
    x_errU = array('f')
    x_errL = array('f')
    y_errU = array('f')
    y_errL = array('f')
    for b in xrange( 1, hist.GetNbinsX()+1 ):
        binEntries = hist.GetBinContent( b )
        if binEntries > 0.:
            binErrUp   = calcPoissonCLUpper( binEntries ) - binEntries
            binErrLow  = binEntries - calcPoissonCLLower( binEntries )
            x_val.append( hist.GetXaxis().GetBinCenter( b ) )
            y_val.append( binEntries )
            y_errU.append( binErrUp )
            y_errL.append( binErrLow )
            x_errU.append( 0. ) #hist.GetXaxis().GetBinWidth( b )/2.0  )
            x_errL.append( 0. ) #hist.GetXaxis().GetBinWidth( b )/2.0  )
            pass
        pass
    #print len(x_val), x_val, y_val, x_errL, x_errU, y_errL, y_errU
    if len(x_val) > 0 :
        dataGraph = TGraphAsymmErrors( len(x_val), x_val, y_val, x_errL, x_errU, y_errL, y_errU)
        return dataGraph
    else:
        return None

def MakePoissonConfidenceLevelErrors_ratio( hist, hden ):
    x_val = array('f')
    y_val = array('f')
    x_errU = array('f')
    x_errL = array('f')
    y_errU = array('f')
    y_errL = array('f')
    if hist.GetNbinsX() != hden.GetNbinsX():
        print "error: hist and hden have different number of bins"
        return None
    for b in xrange( 1, hist.GetNbinsX()+1 ):
        binEntries = hist.GetBinContent( b )
        den = hden.GetBinContent( b )
        if binEntries > 0. and den != 0.0 :
            binErrUp   = (calcPoissonCLUpper( binEntries ) - binEntries)/den
            binErrLow  = (binEntries - calcPoissonCLLower( binEntries ))/den
            x_val.append( hist.GetXaxis().GetBinCenter( b ) )
            y_val.append( binEntries/den )
            y_errU.append( binErrUp )
            y_errL.append( binErrLow )
            x_errU.append( hist.GetXaxis().GetBinWidth( b )/2.0 )
            x_errL.append( hist.GetXaxis().GetBinWidth( b )/2.0 )
            #print "ratio:",hist.GetXaxis().GetBinCenter( b ), binEntries/den, binErrUp, binErrLow
            pass
        pass
    #print len(x_val), x_val, y_val, x_errL, x_errU, y_errL, y_errU
    if len(x_val) > 0 :
        dataGraph = TGraphAsymmErrors( len(x_val), x_val, y_val, x_errL, x_errU, y_errL, y_errU)
        return dataGraph
    else:
        return None

def MakePoissonConfidenceLevelErrors_ratio_lowErr( hist, hden, minRatio ):
    res = hist.Clone()
    res.Reset()
    #
    if hist.GetNbinsX() != hden.GetNbinsX():
        print "error: hist and hden have different number of bins"
        return None
    for b in xrange( 1, hist.GetNbinsX()+1 ):
        binEntries = hist.GetBinContent( b )
        den = hden.GetBinContent( b )
        if binEntries > 0. and den != 0.0 :
            y = binEntries / den
            if y < minRatio:
                res.SetBinContent( b, -50. )
                res.SetBinError( b, 0. )
            else:
                binErrLow  = (binEntries - calcPoissonCLLower( binEntries ))/den
                res.SetBinContent( b, y )
                res.SetBinError( b, binErrLow )
                #print "lowErr h:",hist.GetXaxis().GetBinCenter( b ), y,binErrLow
                pass
            pass
        else:
            res.SetBinContent( b, -50. )
            res.SetBinError( b, 0. )
        pass
    #print len(x_val), x_val, y_val, x_errL, x_errU, y_errL, y_errU
    return res


def GetHistArrays( hist ):
    x_val = array('f')
    y_val = array('f')
    x_err = array('f')
    y_err = array('f')
    for bin in xrange( 1, hist.GetNbinsX()+1 ):
        binEntries = hist.GetBinContent( bin )
        binError   = hist.GetBinError  ( bin )
        x_val.append( hist.GetXaxis().GetBinCenter( bin ) )
        x_err.append( (hist.GetXaxis().GetBinUpEdge( bin ) - hist.GetXaxis().GetBinLowEdge( bin ) )/2. )
        y_val.append( binEntries )
        y_err.append( binError )
        pass

    return [ x_val, y_val, x_err, y_err ]


def GetHistDiff( hist1, hist2 ):
    diff = array('f')
    for bin in xrange( 1, hist1.GetNbinsX()+1 ):
        diff.append( hist1.GetBinContent( bin ) - hist2.GetBinContent( bin ) )
        pass
    return diff
