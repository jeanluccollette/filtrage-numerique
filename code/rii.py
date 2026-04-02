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
Rp = 1
Rs = 60
Ncal = 10000

b, a = signal.iirfilter(ordre, 2*nuc1, Rp, Rs,
                        analog=False, ftype=methode, btype='lowpass')
w, h = signal.freqz(b, a, worN=np.linspace(0, np.pi, Ncal))

gabarit_min = np.zeros(Ncal)
gabarit_min[w <= 2*np.pi*nuc1] = 10**(-Rp/20)
gabarit_min[w > 2*np.pi*nuc1] = np.min(np.abs(h[w > 2*np.pi*nuc1]))
nuc2 = w[np.abs(h) <= 10**(-Rs/20)][0]/(2*np.pi)

gabarit_max = np.zeros(Ncal)
gabarit_max[w <= 2*np.pi*nuc2] = 1
gabarit_max[w > 2*np.pi*nuc2] = 10**(-Rs/20)

plt.figure()
plt.title('Filtre numerique : gain')
plt.plot(w/(2*np.pi), 20*np.log10(np.abs(h)), 'b')
plt.xlabel('Frequence reduite, nuc1={:.3f}, nuc2={:.3f}'.format(nuc1, nuc2))
plt.ylabel('Gain (dB)', color='b')
plt.grid()
plt.axis('tight')
plt.plot(w/(2*np.pi), 20*np.log10(gabarit_min), 'k--')
plt.plot(w/(2*np.pi), 20*np.log10(gabarit_max), 'k--')
plt.savefig('rii_gain_db.png')

plt.figure()
plt.title('Filtre numerique : gain')
plt.plot(w/(2*np.pi), np.abs(h), 'b')
plt.xlabel('Frequence reduite, nuc1={:.3f}, nuc2={:.3f}'.format(nuc1, nuc2))
plt.ylabel('Gain (lin)', color='b')
plt.grid()
plt.axis('tight')
plt.plot(w/(2*np.pi), gabarit_min, 'k--')
plt.plot(w/(2*np.pi), gabarit_max, 'k--')
plt.savefig('rii_gain_lin.png')

plt.figure()
angles = np.unwrap(np.angle(h))
plt.plot(w/(2*np.pi), 180*angles/np.pi, 'g')
plt.title('Filtre numerique : phase')
plt.xlabel('Frequence (Hz)')
plt.ylabel('Phase (degre)', color='g')
plt.grid()
plt.axis('tight')
plt.savefig('rii_phase.png')

plt.show()

