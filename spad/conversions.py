# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:44:23 2020

@author: Jaehwan Kim

Functions to convert SPAD experiment related quantities
"""

import pint
from pint import Quantity as Q_
from scipy.constants import *

def power_to_cps(power, wavelength):
    """
    Function to convert optical power to count per second

    Parameters
    ----------
    power : float
        Optical power in watts
    wavelength : float
        wavelength of light in nanometers

    Returns
    -------
    cps : int
        counts per second of photons

    """

    power = Q_(power, 'watt')
    color = Q_(wavelength, 'nm')

    photonE = Q_(h, 'joule*second') * Q_(c, 'm/s') / color

    cps = (power/photonE).to('Hz')

    # print('{:e}'.format(cps))

    return cps


def cps_to_power(cps, wavelength):
    """
    Function to convert count per second to optical power

    Parameters
    ----------
    cps : float
        Photon counts per second
    wavelength : float
        wavelength of light in nanometers

    Returns
    -------
    power : float
        Optical power in watts

    """

    count = Q_(cps, '1/s')
    color = Q_(wavelength, 'nm')

    photonE = Q_(h, 'joule*second') * Q_(c, 'meter/second') / color

    power = (count*photonE).to('watt')

    # print('{:e}'.format(power))

    return power

def resp_to_qe(responsivity, wavelength):
    """
    Function to convert responsivity to quantum efficiency

    Parameters
    ----------
    responsivity : float
        Responsivity in A/W
    wavelength : float
        wavelength of light in nanometers

    Returns
    -------
    qe : float
        Quantum efficiency in %
    """
    resp = Q_(responsivity, 'A/W')
    color = Q_(wavelength, 'nm')

    photonE = Q_(h, 'joule*second') * Q_(c, 'meter/second') / color
    qe = resp / Q_(e, 'coulomb')*photonE*100
    print(qe)

    return qe
