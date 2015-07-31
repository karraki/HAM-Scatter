'''

Various Halo Mass Functions (HMFs) from the literature

'''
#-----------------------------------------------------------------------------
# Kenza Arraki, 2014
#-----------------------------------------------------------------------------

from __future__ import division

def garrisonkimmel(x, mvir1=1.5e12, mvir2=2.e12):
    """ Garrison-Kimmel 2014 LG mass function """
    mw_hmf = 3.85*(x/0.01/mvir1)**-0.9 #MW HMF
    m31_hmf = 3.85*(x/0.01/mvir2)**-0.9 #M31 HMF
    out_hmf = 11.*(x/1.e10)**-0.9 #outsize MW & M31
    tr = out_hmf + mw_hmf + m31_hmf
    return tr

def brook(x):
    """ Brook 2014 CLUES subhalo mass function """
    tr = ((x/1.e10)/38.1)**-0.89
    return tr

def klypin(x, mvir=1.5e12):
    """ Klypin 2011 Bolshoi subhalo mass function """
    mvir = 1.5e12 #depends on host halo mass
    tr = 1.7e-3*(mvir)**0.5*(x)**-3
    return tr
