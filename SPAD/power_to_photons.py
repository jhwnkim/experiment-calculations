# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:44:23 2020

@author: Jaehwan Kim

Functions to calculate input power to average photon rate and vice versa
"""

import numpy as np
import pint
from pint import UnitRegistry
from pint import Quantity as Q_
from scipy.constants import *

u = UnitRegistry()

power = 100e-6*u.watt
color = 470*u.nanometer

photonE = h*u.joule*u.second *c*u.meter/u.second/color

photonRate = power/photonE


print('{}'.format(photonRate.to_base_units()))
# def to_photons(power, color):
    


photonRate = 1e6/ u.second
power = photonRate*photonE

print('{}'.format(power.to_compact()))

