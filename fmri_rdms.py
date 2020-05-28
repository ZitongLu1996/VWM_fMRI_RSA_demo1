# -*- coding: utf-8 -*-

""" Calculate the RDMs based on fMRI data """

__author__ = 'Zitong Lu'

import numpy as np
import nibabel as nib
from neurora.stuff import get_affine
from neurora.rdm_cal import fmriRDM

sample = "/Users/zitonglu/Desktop/VWM_hyt/02/con_0002.nii"

affine = get_affine(sample)

size = nib.load(sample).shape
print(size)

nx, ny, nz = size

# cue period

fmri_data = np.zeros([6, 18, nx, ny, nz])

for sub in range(18):
    file = "/Users/zitonglu/Desktop/VWM_hyt/" + str(sub + 2).zfill(2) + "/con_0002.nii"
    data = nib.load(file).get_fdata()
    fmri_data[0, sub] = data

    file = "/Users/zitonglu/Desktop/VWM_hyt/" + str(sub + 2).zfill(2) + "/con_0004.nii"
    data = nib.load(file).get_fdata()
    fmri_data[1, sub] = data

    file = "/Users/zitonglu/Desktop/VWM_hyt/" + str(sub + 2).zfill(2) + "/con_0006.nii"
    data = nib.load(file).get_fdata()
    fmri_data[2, sub] = data

    file = "/Users/zitonglu/Desktop/VWM_hyt/" + str(sub + 2).zfill(2) + "/con_0001.nii"
    data = nib.load(file).get_fdata()
    fmri_data[3, sub] = data

    file = "/Users/zitonglu/Desktop/VWM_hyt/" + str(sub + 2).zfill(2) + "/con_0003.nii"
    data = nib.load(file).get_fdata()
    fmri_data[4, sub] = data

    file = "/Users/zitonglu/Desktop/VWM_hyt/" + str(sub + 2).zfill(2) + "/con_0005.nii"
    data = nib.load(file).get_fdata()
    fmri_data[5, sub] = data

fmri_rdms = fmriRDM(fmri_data, ksize=[3, 3, 3], strides=[1, 1, 1], sub_result=1)

fmri_rdms = np.reshape(fmri_rdms, [18*(nx-2)*(ny-2)*(nz-2), 6*6])
np.savetxt("RDMs/fmri_rdms_cue.txt", fmri_rdms)