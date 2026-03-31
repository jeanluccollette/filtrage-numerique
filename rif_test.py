# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:06:49 2013

@author: jean-luc
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

nuc1 = 0.2
nuc2 = 0.25
nuc = (nuc1+nuc2)/2
N = 25
Ncal = 10000
fe = 1000.0
T = 1/fe
duree = 10.0
fmin = 0.0
fmax = 500.0

# b = signal.firwin(N, nuc, window=('hanning'),nyq=0.5)
b = signal.remez(N, [0, nuc1, nuc2, 0.5], [1, 0])

NT = np.round(duree/T)

t = T*np.arange(NT)
u = np.sin(2*np.pi*(fmin*t+(fmax-fmin)*(t**2)/(2*duree)))
y = signal.lfilter(b, 1, u)

plt.figure()
plt.title(
    'Reponse chirp fmin={:.1f}Hz,fmax={:.1f}Hz,fe={:.1f}Hz'.format(fmin, fmax, fe))
plt.plot(t, u, 'b')
plt.plot(t, y, 'r')
plt.xlabel('Temps(en s)')
plt.ylabel('Amplitude')
plt.show()
