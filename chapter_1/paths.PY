import numpy as np
import math


def pl_free(fc, dist, gt=0, gr=0):
    # 自由空间路径损耗模型
    # 输入
    # fc:载波频率
    # dist:基站和移动台之间的距离(m)
    # Gt:发射机天线增益
    # Gr:接收机天线增益
    # 输出
    # PL:路径损耗(dB)
    pl = np.zeros(shape=dist.shape)
    lamda = 3e8/fc  # 波长
    tmp = lamda / (4*math.pi * dist)
    if gt != 0:
        tmp = tmp*math.sqrt(gt)
    if gr != 0:
        tmp = tmp*math.sqrt(gr)
    for k in range(0, dist.size):
        pl[k] = -20 * math.log10(tmp[k])
    return pl


def pl_logdist_or_norm(fc, d, d0, n, sigma=0):
    # 对数距离或对数阴影路径损耗模型
    # 输入
    # fc:载波频率
    # d:基站与移动台之间的距离
    # d0:参考距离
    # n:路径损耗指数
    # sigma:方差
    # 输出
    # pl:路径损耗
    pl = np.zeros(shape=d.shape)
    lamda = 3e8/fc
    for k in range(0, d.size):
        pl[k] = -20*math.log10(lamda/(4*math.pi*d0)) + 10*n*math.log10(d[k]/d0)
    if sigma != 0:
        pl = pl + sigma*np.random.normal(size=d.shape)
    return pl


def pl_hata(fc,d,htx,hrx,etype='URBAN'):
    # etype:环境类型，‘urban’,'suburban','open'
    pl = np.zeros(d.shape)
    fc=fc/1e6
    for k in range(0,d.size):
        pl[k] = 69.55 + 26.16*math.log10(fc) - 13.82*math.log10(htx) + (44.9-6.55*math.log10(htx))*math.log10(d[k])
    if etype == 'URBAN':
        if fc>=150 and fc <=200:
            C = 8.29*math.log10(1.54*hrx)**2 - 1.1
        elif fc>=200 and fc<=1500:
            C = 3.2*math.log10(11.75*hrx)**2 - 4.97
        pl = pl - C
    else:
        C = 0.8 + (1.1*math.log10(fc)-0.7)*hrx - 1.56*math.log10(fc)
        pl = pl -C
        if etype == 'SUBURBAN':
            pl = pl - 2*math.log10(fc/28)**2 - 5.4
        elif etype == 'OPEN':
            pl = pl - 4.78*math.log10(fc)**2 + 18.33*math.log10(fc) - 40.97
    return pl


def pl_ieee80216d(fc,d,type,htx,hrx,corr_fact,mod='UNMOD'):
    # corr_fact:如果存在阴影，那么设置为‘ATnT’或‘Okumura'，否则设置为No
    d0 = 100
    d0_new = 100
    lammda = 3e8/fc
    fc = fc/1e6
    Cf = 6*math.log10(fc/2e3)
    pl = np.zeros(d.shape)

    if corr_fact == 'ATNT':
        if type == 'A' or type == 'B':
            Crx = -10.8*math.log10(hrx/2)
        elif type == 'C':
            Crx = -20*math.log10(hrx/2)
    elif corr_fact == 'OKUMURA':
        if hrx <= 3:
            Crx = -10*math.log10(hrx/3)
        elif hrx >3:
            Crx = -20*math.log10(hrx/3)
    if type == 'A':#这段判断语句感觉可以优化
        a=4.6
        b=0.0075
        c=12.6
    elif type == 'B':
        a=4
        b=0.065
        c=17.1
    elif type == 'C':
        a=3.6
        b=0.005
        c=20
    gamma = a - b*htx +c/htx
    if mod == 'MOD':
        d0_new = d0*10**(-(Cf+Crx)/(10*gamma))
    for k in range(0,d.size):
        if d[k] <= d0_new:
            pl[k] = 20*math.log10(4*math.pi*d[k]/lammda)
        elif d[k] > d0_new:
            pl[k] = 20*math.log10(4*math.pi*d0_new/lammda) + 10*gamma*math.log10(d[k]/d0) + Cf + Crx
    return pl
