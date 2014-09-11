#! /usr/bin/env python

from __future__ import division
import math
import sys
import getopt


DEF_RELERROR = 0.25

def get_significance(s, b, sb=None):
    """ Get significance taking into account
    the background uncertainty (from Cowan) """
    if s < 0 or b < 0:
        return 0.00
    if b == 0.:
        return 0.00
    if sb is None: sb = 0.25 * b # for now we use 25% of uncertainty for the background
    zaint = 2 * ((s + b) * math.log( ((s + b) * (b + sb**2))/(b**2 + (s + b) * sb**2) ) - \
            (b**2/sb**2) * math.log(1 + (s * sb**2)/(b * (b + sb**2))) )
    if zaint <= 0.:
        return 0
    za = math.sqrt(zaint)
    if za > 0.0:
        za = round(za, 2)
    else:
        za = 0.00
    return za


def usage():
    print " "
    print "Usage: %s [options] signal background [sigma_back]" % sys.argv[0]    
    print "  -? | --usage      : print this help message"
    print "  -h | --help       : print this help message"

def main():
    
    try:
        # retrive command line options
        shortopts  = "h?"
        longopts   = ["help", "usage"]
        opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )

    except getopt.GetoptError:
        # print help information and exit:
        print "ERROR: unknown options in argument %s" % sys.argv[1:]
        usage()
        sys.exit(1)

    if len(args) < 2:
        print "ERROR:  Did not provide enough arguments"
        usage()
        sys.exit(1)
    elif len(args) == 2:
        # using default error
        signal = float(args[0])
        back = float(args[1])
        sigma = DEF_RELERROR * back
    elif len(args) == 3:
        signal = float(args[0])
        back = float(args[1])
        sigma = float(args[2])
    else:
        print "ERROR:  Too many arguments arguments"
        usage()
        sys.exit(1)
        
    for o, a in opts:
        if o in ("-?", "-h", "--help", "--usage"):
            usage()
            sys.exit(0)

    sig = get_significance(signal, back, sigma)
    print "Significance:", sig

if __name__ == "__main__":
    main()

