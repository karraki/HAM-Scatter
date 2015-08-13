"""Various differential Halo Mass Functions (HMFs) derived from
literature HMFs
"""
#-----------------------------------------------------------------------------
# Kenza Arraki, 2014
#-----------------------------------------------------------------------------

from __future__ import division
import numpy as np

def garrisonkimmel(x, mvir1=1.5e12, mvir2=2.0e12):
    """Garrison-Kimmel 2014 Local Group derived differential mass function.
    
    Keyword arguments:
    x -- array of peak halo masses
    mvir1 -- halo mass of the Milky Way (default 1.5e12)
    mvir2 -- halo mass of M31 (default 2.0e12)
    """
    mw_hmf = -0.9*3.85*(x/0.01/mvir1)**-0.9
    m31_hmf = -0.9*3.85*(x/0.01/mvir2)**-0.9
    out_hmf = -0.9*11.*(x/1.e10)**-0.9
    tr = out_hmf + mw_hmf + m31_hmf
    return tr

def brook(x):
    """Brook 2014 CLUES derived differential subhalo mass function

    Keyword arguments:
    x -- array of subhalo halo masses
    """
    tr = -0.89*((x/1.e10)/38.1)**-0.89
    return tr

def derive_dhmf(x, hmf):
    """Derives differential halo mass function from provided cumulative
    halo mass function.

    Keyword arguments:
    x -- array of peak halo masses
    hmf - array of cumulative halo mass function values
    """
    dhmf_1 = np.zeros_like(hmf)
    for i in range(1,len(hmf)):
        dhmf_1[i] = hmf[i-1]-hmf[i]
    print dhmf_1
    dhmf_1 = np.round(dhmf_1)
    dhmf = np.array([])
    dhmf_x = np.array([])
    for i in range(1,len(hmf)):
        if dhmf_1[i] != dhmf_1[i-1]:
            dhmf = np.append(dhmf,dhmf_1[i])
            dhmf_x = np.append(dhmf_x,x[i])
    return dhmf_x
