"""Various Halo Mass Functions (HMFs) from the literature
"""
#-----------------------------------------------------------------------------
# Kenza Arraki, 2014
#-----------------------------------------------------------------------------

from __future__ import division

def garrisonkimmel(x, mvir1=1.5e12, mvir2=2.0e12):
    """Garrison-Kimmel 2014 Local Group mass function.

    Keyword arguments:
    x -- array of peak halo masses
    mvir1 -- halo mass of the Milky Way (default 1.5e12)
    mvir2 -- halo mass of M31 (default 2.0e12)
    """
    mw_hmf = 3.85*(x/0.01/mvir1)**-0.9
    m31_hmf = 3.85*(x/0.01/mvir2)**-0.9
    out_hmf = 11.*(x/1.e10)**-0.9
    tr = out_hmf + mw_hmf + m31_hmf
    return tr

def brook(x):
    """Brook 2014 CLUES subhalo mass function.
    
    Keyword arguments:
    x -- array of peak subhalo halo masses
    """
    tr = ((x/1.e10)/38.1)**-0.89
    return tr

def klypin(x, mvir=1.5e12):
    """Klypin 2011 Bolshoi subhalo mass function.

    Keyword arguments:
    x -- array of peak subhalo halo masses
    mvir -- halo mass of host halo (default 1.5e12)
    """
    tr = 1.7e-3*(mvir)**0.5*(x)**-3
    return tr
