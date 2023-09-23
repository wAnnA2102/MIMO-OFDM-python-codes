import numpy as np
import math
import matplotlib.pyplot as plt
import paths


# 1.1.1 free path-loss model and log distance path model
fc = 1.5e9
d0 = 100
sigma = 3
distance = np.arange(1,33,2)**2  #好像比matlab里的少个数,arange不包括初始值

Gt = np.array([1,1,0.5])
Gr = np.array([1,0.5,0.5])
Exp = np.array([2,3,6])
y_Free = np.zeros([3,16])
y_logdist = np.zeros([3,16])
y_lognorm = np.zeros([3,16])
# 计算和绘图函数
for k in range(0,3):
    y_Free[k,...] = paths.pl_free(fc,distance,Gt[k],Gr[k])
    y_logdist[k,...] = paths.pl_logdist_or_norm(fc,distance,d0,Exp[k])
    y_lognorm[k,...] = paths.pl_logdist_or_norm(fc,distance,d0,Exp[0],sigma)


fig, ax = plt.subplots(1,3,figsize=(14,7))
ax[0].plot(distance,y_Free[0,...],label='Gt=1,Gr=1')
ax[0].plot(distance,y_Free[1,...],label='Gt=1,Gr=0.5')
ax[0].plot(distance,y_Free[2,...],label='Gt=0.5,Gr=0.5')
ax[0].set_xscale('log')
ax[0].set_title('Free PL-loss Model,fc=%d MHz'%fc)
ax[0].set_xlabel('Distance[m]')
ax[0].set_ylabel('Path loss[dB]')
ax[0].set(xlim=(1,1000),ylim=(40,110))
ax[0].legend()
ax[0].grid(which='both',axis='both')


ax[1].plot(distance,y_logdist[0,...],label='n=2')
ax[1].plot(distance,y_logdist[1,...],label='n=3')
ax[1].plot(distance,y_logdist[2,...],label='n=6')
ax[1].set_xscale('log')
ax[1].set_title('Log-distance Path-loss Model,fc=%d'%fc)
ax[1].set_xlabel('Distance[m]')
ax[1].set_ylabel('Path loss[dB]')
ax[1].set(xlim=(1,1000),ylim=(40,110))
ax[1].legend()
ax[1].grid(which='both',axis='both')


ax[2].plot(distance,y_lognorm[0,...],label='path 1')
ax[2].plot(distance,y_lognorm[1,...],label='path 2')
ax[2].plot(distance,y_lognorm[2,...],label='path 3')
ax[2].set_xscale('log')
ax[2].set_title('Log-norm Path-loss Model,fc=%d,sigma=%ddB'%(fc,sigma))
ax[2].set_xlabel('Distance[m]')
ax[2].set_ylabel('Path loss[dB]')
ax[2].set(xlim=(1,1000),ylim=(40,110))
ax[2].legend()
ax[2].grid(which='both',axis='both')








#1.1.2 Okumura/Hata model

# fc = 1.5e9
# d0 = 100
# sigma = 3
# distance = np.arange(1,33,2)**2  #好像比matlab里的少个数,arange不包括初始值

# htx = 70
# hrx = 1.5

# y_urban = paths.pl_hata(fc,distance,htx,hrx,'URBAN')
# y_suburban = paths.pl_hata(fc,distance,htx,hrx,'SUBURBAN')
# y_open = paths.pl_hata(fc,distance,htx,hrx,'OPEN')

# fig,ax = plt.subplots(figsize=(14,7))
# ax.plot(distance,y_urban,label='urban')
# ax.plot(distance,y_suburban,label='suburban')
# ax.plot(distance,y_open,label='open area')
# ax.set_xscale('log')
# ax.set_title('Hata PL model,fc=%dMHz'%(fc/1e6))
# ax.set_xlabel('Distance[Km]')
# ax.set_ylabel('Path loss[dB]')
# ax.grid(which='both',axis='both')
# ax.legend()




# # 1.1.3 IEEE 802.16d model
# fc = 2e9
# d0 = 100
# htx = np.array([30,30])
# hrx = np.array([2,10])
# distance = np.arange(1,1001)
# y_ieee16d = np.zeros([2,distance.size])
# y_mieee16d = np.zeros([2,distance.size])

# for k in range(0,2):
#     y_ieee16d[k,...] = paths.pl_ieee80216d(fc,distance,'A',htx[k],hrx[k],'ATNT')
#     y_mieee16d[k,...] = paths.pl_ieee80216d(fc,distance,'A',htx[k],hrx[k],'ATNT','MOD')
# fig,ax = plt.subplots(1,2,figsize=(14,7))
# ax[0].plot(distance,y_ieee16d[0,...],label='htx=%dm,hrx=%dm'%(htx[0],hrx[0]))
# ax[0].plot(distance,y_ieee16d[1,...],label='htx=%dm,hrx=%dm'%(htx[1],hrx[1]))
# ax[0].set(xlim=(1,1000),ylim=(10,150))
# ax[0].set_xscale('log')
# ax[0].set_xlabel('Distance[m]')
# ax[0].set_ylabel('Pathloss[dB]')
# ax[0].legend()
# ax[0].grid(axis='both',which='both')
# ax[0].set_title('IEEE 802.16d path loss models,fc=%dMHz'%(fc/1e6))

# ax[1].plot(distance,y_mieee16d[0,...],label='htx=%dm,hrx=%dm'%(htx[0],hrx[0]))
# ax[1].plot(distance,y_mieee16d[1,...],label='htx=%dm,hrx=%dm'%(htx[1],hrx[1]))
# ax[1].set(xlim=(1,1000),ylim=(10,150))
# ax[1].set_xscale('log')
# ax[1].set_xlabel('Distance[m]')
# ax[1].set_ylabel('Pathloss[dB]')
# ax[1].legend()
# ax[1].grid(axis='both',which='both')
# ax[1].set_title('Modified IEEE 802.16d path loss models,fc=%dMHz'%(fc/1e6))
