# This is a code for creating fourier-transforms our time-dependent dipole, largely inspired by Lukas Medisauskas from the Max-Born Institute of Berlin
# August 8, 2016
# Written by: Clayton Blythe, Vanderbilt university: email: blythec1@central.edu
###################################################################################
import numpy as np
from numpy import fft
import math
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.colors import LinearSegmentedColormap
import os
cwd = os.getcwd()

matplotlib.rcParams.update({'font.size': 8})
cMap = plt.get_cmap('RdYlBu')

filename = 'dipoleXY'
ld = np.loadtxt(filename)

filename2 = 'laser_manual.dat'
laser = np.loadtxt(filename2)

time = laser[:,1]
laserx = laser[:,2]
lasery = laser[:,3]

###converting to atomic units from time in femtoseconds and eV* Angstrom/V
t = ld[:, 0] * 1e-15 / 2.418884326505e-17
n = len(t)
window = np.hamming(n)

dx = np.multiply(window, ld[:, 1])# / .529177
dy = np.multiply(window, ld[:, 2])# / .529177
sample_spacing = t[1] - t[0]
##

fourierx = np.abs(np.fft.rfft(dx))
fouriery = np.abs(np.fft.rfft(dy))

freq = (np.fft.rfftfreq(n, d=sample_spacing)) * (2 * math.pi / .056939228)

##

plt.figure(1, figsize=(14,12),dpi=128)

plt.subplot(331)
plt.plot(time,laserx)
plt.title('X Component of Laser vs Time')
plt.xlabel('Time in Femtoseconds')
plt.ylabel('Amplitude (a.u.)')

plt.subplot(332)
plt.plot(time,lasery)
plt.title('Y Component of Laser vs Time')
plt.xlabel('Time in Femtoseconds')
plt.ylabel('Amplitude (a.u.)')

plt.subplot(333)
plt.plot(laserx,lasery)
plt.title('Y vs X Component of Laser')
plt.xlabel('X Component (a.u)')
plt.ylabel('Y Component (a.u)')

plt.subplot(334)
plt.plot(ld[:,0],dx)
plt.title('Dipole in X')
plt.xlabel('Time in fs')
plt.ylabel('Amplitude')

plt.subplot(335)
plt.plot(ld[:,0],dy)
plt.title('Dipole in Y')
plt.xlabel('Time in fs')
plt.ylabel('Amplitude')

plt.subplot(336)
plt.plot(dx,dy)
plt.title('Dipole Y vs Dipole X')
plt.xlabel('Dipole X (a.u)')
plt.ylabel('Dipole Y (a.u)')


plt.subplot(337)
plt.plot(freq,fourierx)
plt.title('|Y| for X Transform')
plt.xlabel('Multiples of Fundamental')
plt.ylabel('abs |Y|')
plt.xlim(0,70)
plt.yscale('log')

plt.subplot(338)
plt.plot(freq,fouriery)
plt.title('|Y| for Y Transform')
plt.xlabel('Multiples of Fundamental')
plt.ylabel('abs |Y|')
plt.xlim(0,70)
plt.yscale('log')

plt.subplot(339)
plt.plot(freq,fourierx + fouriery)
plt.title('Summed Transforms')
plt.xlabel('Multiples of Fundamental')
plt.ylabel('abs |Y|')
plt.xlim(0,70)
plt.yscale('log')

##plt.subplot(4310)
##plt.plot(freq,(fourierx + fouriery)**2)
##plt.title('Power of Summed Transform')
##plt.xlabel('Multiples of Fundamental')
##plt.ylabel('abs |Y|^2')
##plt.xlim(0,70)
##plt.yscale('log')

current_dir = os.path.basename(cwd)

plt.savefig('clay_spectra_'+current_dir + '_.pdf', dpi=1200, Transparent=True)
print(current_dir +'  completed')
