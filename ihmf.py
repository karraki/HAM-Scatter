'''

Inverted Halo Mass Function (HMF) from the literature

'''
#-----------------------------------------------------------------------------
# Kenza Arraki, 2014
#-----------------------------------------------------------------------------

from __future__ import division

def brook(x):
    """ Brook 2014 CLUES inverted subhalo mass function """
    tr = 38.1*1.e10/(x**(1./0.89))
    return tr
