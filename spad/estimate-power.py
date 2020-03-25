# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:04:24 2020

@author: Jaehwan Kim

Script to estimate power on sample based on Alexandra's ND filter and system optical throughput data.
Given a measured count rate from the SPAD it will also output a PDP
"""


import numpy as np
from pint import Quantity as Q_
from conversions import *

power_at_sample = Q_('138 uW')
wavelength = 650 # nm

print("Power at sample: {:e} --> {:e} cps".format(power_at_sample.to_compact(), power_to_cps(power_at_sample.to('watt').magnitude, wavelength).to('Hz').magnitude))

nd_input = 0.320
nd_output = np.array([3.30E-02,
                      3.60E-03,
                      8.00E-06,
                      0.18,
                      4.00E-02,
                      4.70E-04])

nd_filter= {
    "NE10A": nd_output[0]/nd_input,
    "NE20A": nd_output[1]/nd_input,
    "NE50A-A": nd_output[2]/nd_input,
    "NE03A-A": nd_output[3]/nd_input,
    "NE10A-A": nd_output[4]/nd_input,
    "NE30A-A": nd_output[5]/nd_input
    }

"""
Kramnik's configuration
NE10A + NE50A
NE20A + NE20A (NE30A+NE10A)
"""

attenuated_power = power_at_sample * nd_filter["NE50A-A"] * nd_filter["NE30A-A"] * nd_filter["NE10A-A"] * nd_filter["NE10A"]
"""
Our candidate configurations:
    0. NE50A-A + NE30A-A + NE10A-A
    1. NE50A-A + NE30A-A + NE10A-A + NE20A --> 23.3 kcps
    2. NE50A-A + NE30A-A + NE10A-A + NE10A --> 213 kcps
"""

incident_cps = power_to_cps(attenuated_power.to('watt').magnitude, wavelength).to('Hz')
print("Attenuated power: {:e} --> {:e} cps".format(attenuated_power.to_compact(), incident_cps.magnitude) )

measured_cps = 5000 # cps

print('PDP is {} %'.format(100.0*measured_cps/incident_cps.magnitude))