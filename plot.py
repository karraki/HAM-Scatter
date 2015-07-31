# Kenza Arraki (karraki@gmail.com)
# Written September 2014
# Predict Stellar Mass Function including scatter in SHM relation

import os.path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import hmf
import dhmf
import ihmf
import shm


# Create array of input halo masses 
Mhx = 10.**np.arange(8.,11.6,0.01)

# Start plots
pp = PdfPages('HaloMassFunctions.pdf')

# 1. Plot LG mass functions
fig, ax = plt.subplots()
plt.plot(Mhx, hmf.brook(Mhx),'r-',zorder=-1)
plt.plot(Mhx, hmf.garrisonkimmel(Mhx,0.7e12,1.2e12),'g-',zorder=-2)
plt.plot(Mhx, hmf.garrisonkimmel(Mhx,1.2e12,2.2e12),'b--',zorder=-3)
ax.semilogx()
ax.semilogy()
plt.xlim(1.e8,1.e12)
plt.ylim(ymin=1)
plt.xlabel(r'M$_\mathregular{vir}$ (M$_{\odot})$')
plt.ylabel('N(>M)')
plt.title('Halo Mass Functions')
plt.savefig(pp, format='pdf', bbox_inches='tight')


# 2. Plot differential mass functions
fig, ax = plt.subplots()
plt.plot(Mhx, hmf.brook(Mhx),'c-',zorder=-1)
Mhm = ihmf.brook(np.arange(1e3)+1.)
NMhm = np.zeros_like(Mhm)
for i in range(len(Mhm)):
    NMhm[i] = len(Mhm[:i])
plt.plot(Mhm, NMhm,'r.')
ax.semilogx()
ax.semilogy()
plt.xlim(1.e8,1.e12)
plt.ylim(1,3e3)
plt.xlabel(r'M$_\mathregular{vir}$ (M$_{\odot})$')
plt.ylabel('N(>M)')
plt.plot(hmf.brook(Mhx), Mhx,'r-',zorder=-1)
plt.title('Differential Mass Functions')
plt.savefig(pp, format='pdf', bbox_inches='tight')


# 3. Plot SHM relation
Mst_garrisonkimmel = shm.garrisonkimmel(Mhm)
Mst_brook = shm.brook(Mhm)
fig, ax = plt.subplots()
plt.plot(Mhx, shm.garrisonkimmel(Mhx),'r-.',zorder=-2)
plt.plot(Mhx, shm.brook(Mhx),'c--',zorder=-1)
plt.plot(Mhm, Mst_garrisonkimmel,'k.')
plt.plot(Mhm, Mst_brook,'k.')
ax.semilogx()
ax.semilogy()
plt.xlim(1e8,1e12)
plt.ylim(1e1,1e12)
plt.xlabel(r'M$_\mathregular{vir}$ (M$_{\odot})$')
plt.ylabel(r'M$_{*}$ (M$_{\odot})$')
plt.title('Stellar Halo Mass Relations')
plt.savefig(pp, format='pdf', bbox_inches='tight')

# Add scatter to halo mass values
Mhm_new = np.zeros_like(Mhm)
for i in range(len(Mhm_new)):
    Mhm_new[i] = np.random.normal(Mhm[i], 1.5*Mhm[i], 1)
Mhm_new[Mhm_new < 0.] = 0. 
Mst_garrisonkimmel_new = shm.garrisonkimmel(Mhm_new)
Mst_brook_new = shm.brook(Mhm_new)

# Write out file with the scatter values
with open('estimated_mstar.txt','w') as f:
    f.write('# orig_Mh scatter_Mh orig_garrisonkimmel_M*'+
        ' scatter_garrisonkimmel_M* orig_brook_M* scatter_brook_M*\n')
    for i in range(len(Mhm_new)):
        f.write('{:e} '.format(Mhm[i])+
            '{:e} '.format(Mhm_new[i])+
            '{:e} '.format(Mst_garrisonkimmel[i])+
            '{:e} '.format(Mst_garrisonkimmel_new[i])+
            '{:e} '.format(Mst_brook[i])+
            '{:e} '.format(Mst_brook_new[i])+'\n')

# 4. Plot stellar halo mass function with scatter
fig, ax = plt.subplots()
plt.plot(Mhm, Mst_garrisonkimmel_new, 'r.', zorder=-1)
plt.plot(Mhm, Mst_brook_new, 'c.', zorder=-1)
plt.plot(Mhm, Mst_garrisonkimmel, 'k-')
plt.plot(Mhm, Mst_brook, 'k-')
ax.semilogx()
ax.semilogy()
plt.xlim(1.e8,1.e12)
plt.ylim(1.e1,1.e12)
plt.xlabel(r'M$_\mathregular{vir}$ (M$_{\odot})$')
plt.ylabel(r'M$_{*}$ (M$_{\odot})$')
plt.title('Stellar Halo Mass Function with Scatter')
plt.savefig(pp, format='pdf', bbox_inches='tight')

# 5. Plot stellar halo mass function with scatter zoomed in
fig, ax = plt.subplots()
plt.plot(Mhm, Mst_garrisonkimmel_new, 'r.', zorder=1, mfc='none')
plt.plot(Mhm, Mst_brook_new, 'c.', zorder=-1, mfc='none')
plt.plot(Mhm, Mst_garrisonkimmel, 'k-', zorder=2, mfc='none')
plt.plot(Mhm, Mst_brook, 'k-', zorder=2, mfc='none')
ax.semilogx()
ax.semilogy()
plt.xlim(1.5e8,3.e9)
plt.ylim(1.e-2,3.e5)
plt.xlabel(r'M$_\mathregular{vir}$ (M$_{\odot})$')
plt.ylabel(r'M$_{*}$ (M$_{\odot})$')
plt.title('Stellar Halo Mass Function with Scatter, Zoomed In')
plt.savefig(pp, format='pdf', bbox_inches='tight')

# 6. Plot halo masses to check scatter
fig, ax = plt.subplots()
plt.plot([1.e1,1.e12],[1.e1,1.e12],'k-',zorder=10)
plt.plot(Mhm, Mhm_new, 'g.')
ax.semilogx()
ax.semilogy()
plt.xlim(1.e8,1.e12)
plt.ylim(1.e8,1.e12)
plt.xlabel(r'M$_\mathregular{vir}$ (M$_{\odot})$')
plt.ylabel(r'M$_\mathregular{vir, scatter}$ (M$_{\odot})$')
plt.title('Halo Mass Versus Self with Scatter')
plt.savefig(pp, format='pdf', bbox_inches='tight')

# 7. Plot stellar masses to check scatter
fig, ax = plt.subplots()
plt.plot([1.e1,1.e12],[1.e1,1.e12],'k-',zorder=10)
plt.plot(Mst_garrisonkimmel, Mst_garrisonkimmel_new, 'r.')
plt.plot(Mst_brook, Mst_brook_new, 'c.')
ax.semilogx()
ax.semilogy()
plt.xlim(1.e1,1.e12)
plt.ylim(1.e1,1.e12)
plt.xlabel(r'M$_\mathregular{*}$ (M$_{\odot})$')
plt.ylabel(r'M$_\mathregular{*, scatter}$ (M$_{\odot})$')
plt.title('Stellar Mass Versus Self with Scatter')
plt.savefig(pp, format='pdf', bbox_inches='tight')


# 8. Plot Stellar Mass Function predicted with scatter
fig, ax = plt.subplots()

# Read in observational data
if os.path.isfile('mcconnachie.dat'):
    f = 'mcconnachie.dat'
    dtypes = ['S4','S15','S9','f','f','f','f','f','f','f']
    grp = np.loadtxt(f,comments='#',dtype=dtypes[0],usecols=[0])
    name = np.loadtxt(f,comments='#',dtype=dtypes[1],usecols=[1])
    mtype = np.loadtxt(f,comments='#',dtype=dtypes[2],usecols=[2])
    dmw = np.loadtxt(f,comments='#',dtype=dtypes[3],usecols=[3])
    dm31 = np.loadtxt(f,comments='#',dtype=dtypes[4],usecols=[4])
    dlg = np.loadtxt(f,comments='#',dtype=dtypes[5],usecols=[5])
    r12 = np.loadtxt(f,comments='#',dtype=dtypes[6],usecols=[6])
    obs_mst0 = np.loadtxt(f,comments='#',dtype=dtypes[7],usecols=[7])*1.e6
    obs_mhi = np.loadtxt(f,comments='#',dtype=dtypes[8],usecols=[8])*1.e6
    obs_mdyn = np.loadtxt(f,comments='#',dtype=dtypes[9],usecols=[9])*1.e6
    obs_mst = obs_mst0[dlg < 1800.]
    obs_mst = obs_mst[np.isnan(obs_mst) == False]

    nobs_mst = np.zeros(len(obs_mst))
    sort_ind = sorted(range(len(obs_mst)), key=obs_mst.__getitem__)
    sort_obs_mst = obs_mst[sort_ind]
    for i in range(len(obs_mst)):
        nobs_mst[i] = len(sort_obs_mst[i:])
    plt.plot(sort_obs_mst, nobs_mst, 'g:')

NMhm = np.zeros_like(Mhm)
sort_ind = sorted(range(len(Mhm)), key=Mhm.__getitem__)
sort_Mhm = Mhm[sort_ind]
for i in range(len(Mhm)):
    NMhm[i] = len(sort_Mhm[i:])
plt.plot(sort_Mhm,NMhm,'k--')

NMhm_new = np.zeros_like(Mhm_new)
sort_ind = sorted(range(len(Mhm_new)), key=Mhm_new.__getitem__)
sort_Mhm_new = Mhm_new[sort_ind]
for i in range(len(Mhm_new)):
    NMhm_new[i] = len(sort_Mhm_new[i:])
plt.plot(sort_Mhm_new,NMhm_new,'k-')

NMst_garrisonkimmel = np.zeros_like(Mst_garrisonkimmel)
sort_ind = sorted(range(len(Mst_garrisonkimmel)),
                  key=Mst_garrisonkimmel.__getitem__)
sort_Mst_garrisonkimmel = Mst_garrisonkimmel[sort_ind]
for i in range(len(Mst_garrisonkimmel)):
    NMst_garrisonkimmel[i] = len(sort_Mst_garrisonkimmel[i:])
plt.plot(sort_Mst_garrisonkimmel,NMst_garrisonkimmel,'r--')

NMst_brook = np.zeros_like(Mst_brook)
sort_ind = sorted(range(len(Mst_brook)), key=Mst_brook.__getitem__)
sort_Mst_brook = Mst_brook[sort_ind]
for i in range(len(Mst_brook)):
    NMst_brook[i] = len(sort_Mst_brook[i:])
plt.plot(sort_Mst_brook,NMst_brook,'c--')

NMst_garrisonkimmel_new = np.zeros_like(Mst_garrisonkimmel_new)
sort_ind = sorted(range(len(Mst_garrisonkimmel_new)),
                  key=Mst_garrisonkimmel_new.__getitem__)
sort_Mst_garrisonkimmel_new = Mst_garrisonkimmel_new[sort_ind]
for i in range(len(Mst_garrisonkimmel_new)):
    NMst_garrisonkimmel_new[i] = len(sort_Mst_garrisonkimmel_new[i:])
plt.plot(sort_Mst_garrisonkimmel_new,NMst_garrisonkimmel_new,'r-')

NMst_brook_new = np.zeros_like(Mst_brook_new)
sort_ind = sorted(range(len(Mst_brook_new)),
                  key=Mst_brook_new.__getitem__)
sort_Mst_brook_new = Mst_brook_new[sort_ind]
for i in range(len(Mst_brook_new)):
    NMst_brook_new[i] = len(sort_Mst_brook_new[i:])
plt.plot(sort_Mst_brook_new,NMst_brook_new,'c-')

plt.scatter(1.e3, 82., marker='*', c='b', s=100, edgecolor='none')
plt.scatter(1.e3, 160., marker='*', c='gray', s=100, edgecolor='none')
plt.scatter(1.e3, 240., marker='*', c='gray', s=100, edgecolor='none')
#plt.scatter(1.e3, 82., marker='>', c='b', s=100, edgecolor='none')
plt.plot([3e6,3e6],[1,1e3],'k:')

ax.semilogx()
ax.semilogy()
plt.xlim(1.e1,1.e11)
plt.ylim(1,1e3)
plt.xlabel(r'M$_{*}$ (M$_{\odot})$')
plt.ylabel('N(>M)')
plt.title('Stellar Mass Function with Scatter')
plt.savefig(pp, format='pdf', bbox_inches='tight')

pp.close()
