import sys, time, os
import numpy as np
import matplotlib.pyplot as plt
from subprocess import call
from shutil import copyfile

inDir = 'images/'
outDir = inDir
image_name = 'particles'
out_anim_name = 'animation_particles'

cmd = 'ffmpeg -framerate 10 -i '
cmd += '{0}{1}_%d.png '.format( inDir, image_name )
cmd += '-pix_fmt yuv420p '
cmd += '-b 50000k '
cmd += '{0}{1}.mp4'.format( outDir, out_anim_name )
cmd += ' -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"'
os.system( cmd )
