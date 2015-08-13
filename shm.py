""" Various Stellar-Halo-Mass (SHM) functions at redshift zero
from the literature.
"""
#-----------------------------------------------------------------------------
# Kenza Arraki, 2014
#-----------------------------------------------------------------------------

from __future__ import division
import numpy as np

def moster(x):
    """Moster 2013 Stellar-Halo-Mass function redshift zero.

    Keyword arguments:
    x -- array of peak halo masses
    """
    m1 = 10.**11.59
    n = 0.0351
    beta = 1.376
    gamma = 0.608
    tr = x * 2.0 * n
    tr *= ((x/m1)**-beta + (x/m1)**gamma)**-1.
    return tr

def behroozi_f(bx, alpha, delta, gamma):
    """Intermediary function for Behroozi SHM.
    Should not be called by the user.
    """
    tr = np.log10(1.+np.exp(bx))**gamma
    tr *= delta
    tr /= 1. + np.exp(10.**(-bx))
    tr += -np.log10(10.**(alpha*bx) + 1.)
    return tr

def behroozi(x):
    """Behroozi 2013 Stellar-Halo-Mass function at redshift zero.

    Keyword arguments:
    x -- array of peak halo masses
    """
    epsilon = 10.**-1.777
    m1 = 10.**11.514
    alpha = -1.412
    delta = 3.508
    gamma = 0.316 
    bx = np.log10(x/m1)
    f = behroozi_f(bx, alpha, delta, gamma) 
    f0 = behroozi_f(0., alpha, delta, gamma)
    tr = 10.**(np.log10(epsilon*m1) + f - f0)
    return tr

def garrisonkimmel(x):
    """Garrison-Kimmel 2014 Stellar-Halo-Mass function at redshift zero.
    MNRAS 438, 2578–2596 (2014)
    Equation 4

    Keyword arguments:
    x -- array of peak halo masses
    """
    tr = 3.0e6 * (x/1.0e10)**1.92
    return tr

def brook(x):
    """Brook 2014 Stellar-Halo-Mass function at redshift zero.

    Keyword arguments:
    x -- array of peak halo masses
    """
    tr = (x/(63.1e6))**3.1
    return tr
