import numpy as np
import math
import matplotlib.pyplot as plt
import paths


# 绘制不同的路径损耗模型
fc = 2e9
d0 = 100
htx = np.array([30,30])
hrx = np.array([2,10])
distance = np.arange(1,1001)
y_ieee16d = np.zeros([2,distance.size])
y_mieee16d = np.zeros([2,distance.size])

for k in range(0,2):
    y_ieee16d[k,...] = paths.pl_ieee80216d(fc,distance,'A',htx[k],hrx[k],'ATNT')
    y_mieee16d[k,...] = paths.pl_ieee80216d(fc,distance,'A',htx[k],hrx[k],'ATNT','MOD')
fig,ax = plt.subplots(1,2,figsize=(14,7))
ax[0].plot(distance,y_ieee16d[0,...],label='htx=%dm,hrx=%dm'%(htx[0],hrx[0]))
ax[0].plot(distance,y_ieee16d[1,...],label='htx=%dm,hrx=%dm'%(htx[1],hrx[1]))
ax[0].set(xlim=(1,1000),ylim=(10,150))
ax[0].set_xscale('log')
ax[0].set_xlabel('Distance[m]')
ax[0].set_ylabel('Pathloss[dB]')
ax[0].legend()
ax[0].grid(axis='both',which='both')
ax[0].set_title('IEEE 802.16d path loss models,fc=%dMHz'%(fc/1e6))

ax[1].plot(distance,y_mieee16d[0,...],label='htx=%dm,hrx=%dm'%(htx[0],hrx[0]))
ax[1].plot(distance,y_mieee16d[1,...],label='htx=%dm,hrx=%dm'%(htx[1],hrx[1]))
ax[1].set(xlim=(1,1000),ylim=(10,150))
ax[1].set_xscale('log')
ax[1].set_xlabel('Distance[m]')
ax[1].set_ylabel('Pathloss[dB]')
ax[1].legend()
ax[1].grid(axis='both',which='both')
ax[1].set_title('Modified IEEE 802.16d path loss models,fc=%dMHz'%(fc/1e6))
