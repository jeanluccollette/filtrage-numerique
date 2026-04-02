# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:09:10 2013

@author: jean-luc
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

nuc1 = 0.25
ordre = 6
methode = 'ellip'
# methode='cheby1';
Rp = 1.0
Rs = 60.0
Ncal = 10000
fe = 1000.0
T = 1/fe
duree = 10.0
fmin = 0.0
fmax = 500.0

b, a = signal.iirfilter(ordre, 2*nuc1, Rp, Rs,
                        analog=False, ftype=methode, btype='lowpass')

NT = np.round(duree/T)

t = T*np.arange(NT)
u = np.sin(2*np.pi*(fmin*t+(fmax-fmin)*(t**2)/(2*duree)))
y = signal.lfilter(b, a, u)

plt.figure()
plt.title(
    'Reponse chirp fmin={:.1f}Hz,fmax={:.1f}Hz,fe={:.1f}Hz'.format(fmin, fmax, fe))
plt.plot(t, u, 'b')
plt.plot(t, y, 'r')
plt.xlabel('Temps(en s)')
plt.ylabel('Amplitude')
plt.savefig('rii_chirp.png')

plt.show()
