# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:42:43 2021

@author: Wiebke.Timm
"""

import matplotlib.pyplot as plt
import numpy as np

number_of_pasef_ramps = 10
target_intensity = 20000
cutoff = 500

plotrange = range(cutoff,25000)
intensity = [i for i in plotrange]
repetition = [min(number_of_pasef_ramps, round(float(target_intensity)/float(i)) for i in plotrange]


fig, ax = plt.subplots()
ax.set_ylabel('Repetitions')
ax.set_xlabel('Precursor Intensity (counts)')
ax.set_title('PASEF Repetitions vs Precursor Intensity')

ax.plot(intensity, repetition)
ax.vlines(cutoff, -1, number_of_pasef_ramps + 1, linestyles='dashed')
