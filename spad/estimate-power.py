# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:04:24 2020

@author: Jaehwan Kim

Script to estimate power on sample based on Alexandra's ND filter and system optical throughput data'
"""


import numpy as np
from pint import Quantity as Q_
from conversions import *

power_at_sample = Q_('20 uW')

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

wavelength =650

attenuated_power = power_at_sample * nd_filter["NE50A-A"] * nd_filter["NE30A-A"] * nd_filter["NE10A-A"]

print("Attenuated power: {:e} --> {:e} cps".format(attenuated_power.to_compact(), power_to_cps(attenuated_power.to('watt').magnitude, wavelength).to('Hz').magnitude))