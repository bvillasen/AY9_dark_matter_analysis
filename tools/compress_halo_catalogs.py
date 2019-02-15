import numpy as np

dataDir = '/home/bruno/Desktop/data/ay9/'
inputDir =  dataDir + 'halos_128/'
outputDir =  dataDir + 'halo_catalogs_128/'


base_name = 'halos'

# #Load the header
# filename = 'halos_0.0.ascii'
# f = open( inputDir + filename, 'r')
# header = f.read()
# f.close()

n_boxes = 8
n_col = 54
n_snap = 200

for n_snap in range(0,201):
  data_list = []
  print "Snap: ", n_snap
  n_halos = 0
  for n_box in range(n_boxes):
    filename = '{0}_{1}.{2}.ascii'.format( base_name, n_snap, n_box )
    if n_box == 0:
      header = ''
      f = open( inputDir + filename, 'r')
      header_raw = f.read().splitlines()[0].replace('#','')
      # header_raw = f.read().replace('#','').splitlines()[:20]
      f.close()
      # for line in header_raw:
      #   header += line + '\n'

    data = np.loadtxt( inputDir + filename )
    if len(data) == 0: continue
    n_dim = data.ndim
    if n_dim == 1: n = 1
    else:  n = len(data)
    data_new = data.reshape(n,n_col).copy()
    data_list.append( data_new )
    n_halos += n

  # n_halos = len(data_list)
  if n_halos == 0: data_snap = np.array([])
  if len( data_list) == 1: data_snap = np.array( data_list[0]). reshape(1,n_col)
  if len( data_list) > 1 : data_snap = np.concatenate(data_list, axis=0)
  print ' N halos: ', n_halos
  if n_halos > 1: data_snap = data_snap[np.argsort(data_snap[:,0])]

  filename = 'halos_{0:03}.ascii'.format(n_snap)
  np.savetxt( outputDir+filename, data_snap, header=header_raw, comments='' )
  print " Saved file: " + outputDir+filename + '\n'
