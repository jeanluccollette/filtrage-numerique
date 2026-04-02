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
N = 42
Ncal = 10000

b = signal.remez(N, [0, nuc1, nuc2, 0.5], [1, 0])
w, h = signal.freqz(b, worN=Ncal)

gabarit_min = np.zeros(Ncal)
gabarit_min[w <= 2*np.pi*nuc1] = np.min(np.abs(h[w <= 2*np.pi*nuc1]))
gabarit_min[w > 2*np.pi*nuc1] = np.min(np.abs(h[w > 2*np.pi*nuc2]))
gabarit_max = np.zeros(Ncal)
gabarit_max[w <= 2*np.pi*nuc2] = np.max(np.abs(h[w <= 2*np.pi*nuc1]))
delta = np.max(np.abs(h[w >= 2*np.pi*nuc2]))
gabarit_max[w > 2*np.pi*nuc2] = delta

plt.figure()
plt.title('Filtre numerique : gain')
plt.plot(w/(2*np.pi), 20*np.log10(np.abs(h)), 'b')
plt.xlabel('Frequence reduite, nuc1={:.2f}, nuc2={:.2f}'.format(nuc1, nuc2))
plt.ylabel('Gain (dB), delta={:.2f}'.format(20*np.log10(delta)), color='b')
plt.grid()
plt.axis('tight')
plt.plot(w/(2*np.pi), 20*np.log10(gabarit_min), 'k--')
plt.plot(w/(2*np.pi), 20*np.log10(gabarit_max), 'k--')
plt.savefig('rif_gain_db.png')

plt.figure()
plt.title('Filtre numerique : gain')
plt.plot(w/(2*np.pi), np.abs(h), 'b')
plt.xlabel('Frequence reduite, nuc1={:.2f}, nuc2={:.2f}'.format(nuc1, nuc2))
plt.ylabel('Gain (lin), delta={:.3f}'.format(delta), color='b')
plt.grid()
plt.axis('tight')
plt.plot(w/(2*np.pi), gabarit_min, 'k--')
plt.plot(w/(2*np.pi), gabarit_max, 'k--')
plt.savefig('rif_gain_lin.png')

plt.figure()
angles = np.unwrap(np.angle(h))
plt.plot(w/(2*np.pi), 180*angles/np.pi, 'g')
plt.title('Filtre numerique : phase')
plt.xlabel('Frequence reduite')
plt.ylabel('Phase (degre)', color='g')
plt.grid()
plt.axis('tight')
plt.savefig('rif_phase.png')

plt.show()
