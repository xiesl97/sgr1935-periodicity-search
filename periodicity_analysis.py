"""
Periodicity Analysis Module for SGR 1935+2154

This module provides core functions for analyzing periodicities in burst time series data
using various statistical methods including Lomb-Scargle periodograms, Pearson chi-square,
and C-statistic analysis.

Reference: Xie et al. 2022, MNRAS 517, 3854-3863
"Revisit the periodicity of SGR J1935+2154 bursts with updated sample"
https://arxiv.org/abs/2205.08003
DOI: 10.1093/mnras/stac2918
"""

import numpy as np
from numba import njit
from scipy.special import gammaln


# ===========================
# Phase Folding Functions
# ===========================

@njit(nogil=True)
def FoldPhase(T, T0, P):
    """
    Fold time series to phase space.
    
    Parameters
    ----------
    T : ndarray
        Array of times (MJD)
    T0 : float
        Reference epoch (MJD)
    P : float
        Period (days)
    
    Returns
    -------
    phi : ndarray
        Array of phases in range [0, 1)
    """
    phi = (T - T0) / P - np.floor((T - T0) / P)
    return phi


# ===========================
# Exposure Calculation
# ===========================

def Exposure(mjd_ot, observe_time, index0, index1, T0, phasebins, period):
    """
    Calculate exposure time in each phase bin.
    
    Parameters
    ----------
    mjd_ot : ndarray
        Array of MJD times with observation data
    observe_time : ndarray
        Array of observation times for each mjd_ot entry
    index0, index1 : int
        Index range to consider
    T0 : float
        Reference epoch (MJD)
    phasebins : int
        Number of phase bins
    period : float
        Period for phase folding (days)
    
    Returns
    -------
    exposures : ndarray
        Exposure time in each phase bin
    """
    Times = mjd_ot[index0:index1+1]
    observe_times = observe_time[index0:index1+1]
    phis = FoldPhase(Times, T0, period)
    sortindex = np.argsort(phis)
    phis = phis[sortindex]
    observe_times = observe_times[sortindex]
    
    exposures = np.zeros(phasebins)
    phasebin_size = 1.0 / phasebins
    
    for i in range(phasebins):
        phase_start = i * phasebin_size
        phase_end = (i + 1) * phasebin_size
        index = np.where((phase_start < phis) & (phis < phase_end) & (observe_times != 1))[0]
        
        if len(index) > 0:
            exposures[i] = np.sum(observe_times[index]) / len(index)
    
    return exposures


# ===========================
# Chi-Square Statistic
# ===========================

def PearsonChiSquare(phasebins, phi, period, exposures):
    """
    Calculate Pearson chi-square statistic for phase-folded data.
    
    Parameters
    ----------
    phasebins : int
        Number of phase bins
    phi : ndarray
        Array of phases
    period : float
        Period (days)
    exposures : ndarray
        Exposure time in each phase bin
    
    Returns
    -------
    chi2 : float
        Reduced chi-square statistic
    """
    phasebin = 1.0 / phasebins
    Ni, bins = np.histogram(phi, bins=np.arange(0., 1. + phasebin, phasebin))
    p = np.sum(Ni) / np.sum(exposures)
    
    chi2 = np.zeros(phasebins)
    for i in range(phasebins):
        chi2[i] = (Ni[i] - p * exposures[i])**2 / (p * exposures[i] + 1e-10)
    
    chi2_reduced = np.sum(chi2) / (phasebins - 1)
    return chi2_reduced


# ===========================
# C-Statistic Functions
# ===========================

def Poissonk(miu, k):
    """Calculate Poisson probability P(k; μ)."""
    return np.exp(-miu) * miu**k / np.math.factorial(k)


def Cexpeted(miu):
    """
    Calculate expected C statistic value.
    
    Uses piecewise polynomial approximations for different μ ranges.
    Reference: Cash (1979) and subsequent approximations.
    
    Parameters
    ----------
    miu : float
        Mean value (μ)
    
    Returns
    -------
    Ce : float
        Expected C statistic
    """
    epsilon = 1e-6
    
    if (0 <= miu) & (miu <= 0.5):
        Ce = -0.25*miu**3 + 1.38*miu**2 - 2*miu*np.log(miu + epsilon)
    elif (0.5 < miu) & (miu <= 2):
        Ce = -0.00335*miu**5 + 0.04259*miu**4 - 0.27331*miu**3 + 1.381*miu**2 - 2*miu*np.log(miu + epsilon)
    elif (2 < miu) & (miu <= 5):
        Ce = 1.019275 + 0.1345*miu**(0.461 - 0.9*np.log(miu + epsilon))
    elif (5 < miu) & (miu <= 10):
        Ce = 1.00624 + 0.604/(miu**1.68)
    else:  # miu > 10
        Ce = 1 + 0.1649/miu + 0.226/(miu**2)
    
    return Ce


def Cvariance(miu):
    """
    Calculate variance of C statistic.
    
    Uses piecewise polynomial approximations for different μ ranges.
    
    Parameters
    ----------
    miu : float
        Mean value (μ)
    
    Returns
    -------
    Cv : float
        Variance of C statistic
    """
    epsilon = 1e-6
    
    if (0 <= miu) & (miu <= 0.1):
        Sv = 4 * np.sum([Poissonk(miu, k) * (miu - k + k*np.log(k/miu + epsilon))**2 for k in range(1, 5)])
        Cv = Sv - Cexpeted(miu)**2
    elif (0.1 < miu) & (miu <= 0.2):
        Cv = -262*miu**4 + 195*miu**3 - 51.24*miu**2 + 4.34*miu + 0.77005
    elif (0.2 < miu) & (miu <= 0.3):
        Cv = 4.23*miu**2 - 2.8254*miu + 1.12522
    elif (0.3 < miu) & (miu <= 0.5):
        Cv = -3.7*miu**3 + 7.328*miu**2 - 3.6926*miu + 1.20641
    elif (0.5 < miu) & (miu <= 1):
        Cv = 1.28*miu**4 - 5.191*miu**3 + 7.666*miu**2 - 3.5446*miu + 1.15431
    elif (1 < miu) & (miu <= 2):
        Cv = 0.1125*miu**4 - 0.641*miu**3 + 0.859*miu**2 + 1.0914*miu - 0.05748
    elif (2 < miu) & (miu <= 3):
        Cv = 0.089*miu**3 - 0.872*miu**2 + 2.8422*miu - 0.67539
    elif (3 < miu) & (miu <= 5):
        Cv = 2.12336 + 0.012202*miu**(5.717 - 2.6*np.log(miu + epsilon))
    elif (5 < miu) & (miu <= 10):
        Cv = 2.05159 + 0.331*miu**(1.343 - np.log(miu + epsilon))
    else:  # miu > 10
        Cv = 12/(miu**3) + 0.79/(miu**2) + 0.6747/miu + 2
    
    return Cv


def Cstat(phasebins, phi, period, exposures):
    """
    Calculate normalized C statistic.
    
    C = 2 * Σ[c_i] - Σ[C_e,i] / √(Σ[C_v,i])
    
    where c_i is Cash statistic for bin i, C_e,i is expected value, C_v,i is variance.
    
    Parameters
    ----------
    phasebins : int
        Number of phase bins
    phi : ndarray
        Array of phases
    period : float
        Period (days)
    exposures : ndarray
        Exposure time in each phase bin
    
    Returns
    -------
    C_Ce_Cv : float
        Normalized C statistic value
    """
    epsilon = 1e-6
    phasebin = 1.0 / phasebins
    Ni, bins = np.histogram(phi, bins=np.arange(0., 1. + phasebin, phasebin))
    p = np.sum(Ni) / np.sum(exposures)
    
    cstat = np.zeros(phasebins)
    Ce = np.zeros(phasebins)
    Cv = np.zeros(phasebins)
    
    for i in range(phasebins):
        if Ni[i] == 0:
            cstat[i] = p * exposures[i]
        else:
            cstat[i] = p * exposures[i] - Ni[i] + Ni[i] * np.log(epsilon + Ni[i] / (p * exposures[i]))
        
        Ce[i] = Cexpeted(p * exposures[i])
        Cv[i] = Cvariance(p * exposures[i])
    
    C_Ce_Cv = (2 * np.sum(cstat) - np.sum(Ce)) / np.sqrt(np.sum(Cv))
    return C_Ce_Cv
