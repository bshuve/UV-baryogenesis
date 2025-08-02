from classy import Class
import matplotlib.pyplot as plt
from math import pi
import numpy as np
from scipy.interpolate import interp1d
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad

kmin = 0.335
kmax = 13.4
klim = 0.804e3
kmaxplot = klim
h = 0.6727
kk = np.logspace(np.log10(kmin),np.log10(klim),1000)

chi1=24.2e3
omegancdm = 0.1198
Tncdm = 0.332      # FIMP
Twdm = 0.0919    # WDM

LambdaCDM = Class()
# pass input parameters
LambdaCDM.set({'omega_b':0.02233,
               'omega_cdm':0.1198,
               'h':0.6737,
               'n_s':0.9652,
               'sigma8':0.8101,
               'z_reio':7.64})
LambdaCDM.set({'output':'mPk','P_k_max_1/Mpc':klim})
# run class
LambdaCDM.compute()

WDMsetting = {'N_ur':3.046,
              'N_ncdm':1,
              'T_ncdm':Tncdm,
              'm_ncdm':chi1,
              'omega_cdm':0.0,
              'omega_b':0.02233,
              'use_ncdm_psd_files':1,
              'omega_ncdm':omegancdm,
#              'ncdm_psd_filenames':"NCDM_distribution.dat",
              'ncdm_psd_filenames':"DMspectrum-for-CLASS-UV.dat",
              'h':0.6737,
              'n_s':0.9652,
              'sigma8':0.8101,
              'z_reio':7.64}
LambdaWDM = Class()
LambdaWDM.set(WDMsetting)
LambdaWDM.set({'output':'mPk','P_k_max_1/Mpc':klim})
LambdaWDM.compute()

Tkncdm = []

for k in kk:
    if k > kmaxplot:
        break

    Tkncdm.append(LambdaWDM.pk(k,0)/LambdaCDM.pk(k,0))

last = 1
new = 1
result = 0
for k in kk:
    new = LambdaWDM.pk(k,0)/LambdaCDM.pk(k,0)
    if last >= 0.5 and new < 0.5:
        result = k
        break

    last = new

print(result)

def kpowerspectrumNCDM( k ):
    return k * LambdaWDM.pk(k,0)

def kpowerspectrumCDM( k ):
    return k * LambdaCDM.pk(k,0)

def R2( k ):
    return ( integrate.quad( kpowerspectrumNCDM, k, klim )[0] / 2 / np.pi ) / ( integrate.quad( kpowerspectrumCDM, k, klim )[0] / 2 / np.pi )

dA = 1. - integrate.quad( R2, kmin, kmax )[0] / (kmax - kmin)

print(dA)

chi1 = 15.7e3
WDMsetting = {'N_ur':3.046,
              'N_ncdm':1,
              'T_ncdm':Tncdm,
              'm_ncdm':chi1,
              'omega_cdm':0.0,
              'omega_b':0.02233,
              'use_ncdm_psd_files':1,
              'omega_ncdm':omegancdm,
#              'ncdm_psd_filenames':"NCDM_distribution.dat",
              'ncdm_psd_filenames':"DMspectrum-for-CLASS-IR.dat",
              'h':0.6737,
              'n_s':0.9652,
              'sigma8':0.8101,
              'z_reio':7.64}
LambdaWDM = Class()
LambdaWDM.set(WDMsetting)
LambdaWDM.set({'output':'mPk','P_k_max_1/Mpc':klim})
LambdaWDM.compute()

TkncdmIR = []
for k in kk:
    if k > kmaxplot:
        break

    TkncdmIR.append(LambdaWDM.pk(k,0)/LambdaCDM.pk(k,0))

chi1 = 5.3e3
WDMsetting = {'N_ur':3.046,
              'N_ncdm':1,
              'T_ncdm':Twdm,
              'm_ncdm':chi1,
              'omega_cdm':0.0,
              'omega_b':0.02233,
              'use_ncdm_psd_files':0,
              'omega_ncdm':omegancdm,
              'h':0.6737,
              'n_s':0.9652,
              'sigma8':0.8101,
              'z_reio':7.64}
LambdaWDM = Class()
LambdaWDM.set(WDMsetting)
LambdaWDM.set({'output':'mPk','P_k_max_1/Mpc':klim})
LambdaWDM.compute()

Tkwdm = []
for k in kk:
    if k > kmaxplot:
        break

    Tkwdm.append(LambdaWDM.pk(k,0)/LambdaCDM.pk(k,0))

kkplot = []
for k in kk:
    if k > kmaxplot:
        break

    kkplot.append(k)

filename = "transfer_UV.txt"
filename2 = "transfer_IR.txt"
filename3 = "transfer_WDM.txt"

outfile = open(filename, 'w')
outfile2 = open(filename2, 'w')
outfile3 = open(filename3, 'w')

for ii in range(len(kkplot)):
    outfile.write(str(kkplot[ii]) + '\t' + str(Tkncdm[ii]) + '\n')
    outfile2.write(str(kkplot[ii]) + '\t' + str(TkncdmIR[ii]) + '\n')
    outfile3.write(str(kkplot[ii]) + '\t' + str(Tkwdm[ii]) + '\n')

outfile.close()
outfile2.close()
outfile3.close()

plt.figure(4)
plt.xscale('log');plt.yscale('linear');plt.xlim(kkplot[0],kkplot[-1])
plt.xlabel(r'$k \,\,\,\, [1/\mathrm{Mpc}]$')
plt.ylabel(r'$T(k)^2$')
plt.plot(kkplot,Tkncdm,'r-',label="$m^{\mathrm{UV}}_{\chi_2}=24.2 \,\, \mathrm{keV}$",linewidth=0.1)
plt.plot(kkplot,TkncdmIR,'g-',label="$m^{\mathrm{IR}}_{\chi_2}=15.7 \,\, \mathrm{keV}$",linewidth=0.1)
plt.plot(kkplot,Tkwdm,'b.',label="$m_{\mathrm{WDM}}=5.3\,\,\mathrm{keV}$",linewidth=0.5)
plt.title("z comparison")

plt.legend(loc = 'lower left')
fig = plt.gcf()
fig.set_size_inches(10, 6)
plt.savefig('structure_formation_transfer.pdf')

