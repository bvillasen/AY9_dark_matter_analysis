import numpy as np
import pymc



def dens_model_NFW( r, data, dataError ):
  rho0_mc  = pymc.Uniform('rho0', 1e5, 1e11, value=1e8 )
  r0_mc    = pymc.Uniform('r0', 0.01, 1000., value=10  )
  @pymc.deterministic( plot=False )
  def dens_mc( r=r, rho0=rho0_mc, r0=r0_mc,  ):
    return rho0 / ( ( r/r0 ) * ( 1 + ( r/r0 ) )**2 )
  densObsrv = pymc.Normal('dens', mu=dens_mc, tau=1.0/dataError**2, value=data, observed=True)
  return locals()

def getModelResults_dens( r_data, data, densMDL,  ):
  modelResults = { 'dens':{}, 'rho0':{}, 'r0':{},     }
  modelResults['dens']['mean'] = densMDL.stats()['dens_mc']['mean']
  modelResults['dens']['min']  = densMDL.stats()['dens_mc']['quantiles'][2.5]
  modelResults['dens']['max']  = densMDL.stats()['dens_mc']['quantiles'][97.5]
  #rho0
  modelResults['rho0']['mean'] = densMDL.stats()['rho0']['mean']
  modelResults['rho0']['min']  = densMDL.stats()['rho0']['quantiles'][2.5]
  modelResults['rho0']['max']  = densMDL.stats()['rho0']['quantiles'][97.5]
  #r0
  modelResults['r0']['mean'] = densMDL.stats()['r0']['mean']
  modelResults['r0']['min']  = densMDL.stats()['r0']['quantiles'][2.5]
  modelResults['r0']['max']  = densMDL.stats()['r0']['quantiles'][97.5]
  #Error in density
  dens_mean = modelResults['dens']['mean']
  error_dens = (  dens_mean - data)/data
  error_dens_hig = np.array([[ r_data[i], error_dens[i] ] for i in range( len(error_dens)) if data[i] < dens_mean[i] ] )
  error_dens_low = np.array([[ r_data[i], error_dens[i] ] for i in range( len(error_dens)) if data[i] > dens_mean[i] ] )
  modelResults['dens']['error'] = error_dens
  modelResults['dens']['error_hig'] = error_dens_hig
  modelResults['dens']['error_low'] = error_dens_low
  return modelResults
