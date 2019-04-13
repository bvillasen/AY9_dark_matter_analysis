# from halo import *
# from accumMass import getAccumMassProp
# from scipy.special import hyp2f1, gamma, gammainc
# from scipy.optimize import curve_fit
# from optValuesKernel import *
# from getProfiles import getProfilesAll
# from matplotlib.gridspec import GridSpec
# import seaborn
#from optVals_jeans_mcmc import *

import numpy as np
from mcmcModels import *

###############################################################
print '\nFitting by MCMC ...'
print ' Density'
nIter = 1e5  
nBurn = 1e4  
nThin = 5
nPoints = 20
saveResults = True
# 

def NFW_dens( r, rho_0, r_s ):
  return rho_0 / ( (r/r_s)*(1 + r/r_s)**2 )

r_0 = 10
r_vir = 1000

rho_0 = 2e6
r_s = 200
r_data = np.logspace( np.log10(r_0), np.log10(r_vir), nPoints )
data = NFW_dens( r_data, rho_0, r_s )
dataError = 0.02 * data

print ' Fitting NFW...'
model = dens_model_NFW( r_data, data, dataError )
densMDL = pymc.MCMC( model )
densMDL.sample( iter=nIter, burn=nBurn, thin=nThin )
modelResults = getModelResults_dens( r_data, data, densMDL )
#Extract  results from mcmcm model
r0_mean, r0_max, r0_min = modelResults['r0']['mean'], modelResults['r0']['max'], modelResults['r0']['min']
rho0_mean, rho0_max, rho0_min = modelResults['rho0']['mean'], modelResults['rho0']['max'], modelResults['rho0']['min']
# dens_mean = modelResults['dens']['mean']
# #dens_mean = NFW_dens_4( r_data, rho0_mean, r0_mean, alpha_mean, gamma_mean )
# dens_min  = modelResults['dens']['min']
# dens_max  = modelResults['dens']['max']
# rho0Str = r'$\rho={0:1.1e}$ '.format(rho0_mean)
# r0Str = r'$rs={0:.2f}$ kpc'.format(r0_mean)
# paramStr = '{0}\n{1}'.format( r0Str, rho0Str )
# dens_error = modelResults['dens']['error']
# dens_errorH = modelResults['dens']['error_hig']
# dens_errorL = modelResults['dens']['error_low']
# 

print rho0_mean
print r0_mean
