import numpy as np
import pandas as pd


dataDir = '/home/bruno/Desktop/data/ay9/'
inputDir =  dataDir + 'halo_catalogs_128/'

halo_file_name =  inputDir + 'halos_200.ascii'

halos = pd.read_csv( halo_file_name, sep=' '  )

mass = halos['mvir']
