import os
import glob

for i in range(18, 23):
    fpath_temp = "D:\\Project\\Team Project\\MoDeep\\Dataset-for-MyoGAN\\dataset\\" + str(i) + "\\*.png"
    

    fpath = fpath_temp

    for fpath in glob.glob(fpath):
        fpath_r = fpath.replace('hand-edge', 'hand')
        os.rename(fpath, fpath_r)

