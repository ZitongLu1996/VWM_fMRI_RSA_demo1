# -*- coding: utf-8 -*-

__author__ = 'Zitong Lu'

""" Calculate the similarities between model RDM and fMRI RDMs """

import numpy as np
from neurora.corr_cal_by_rdm import fmrirdms_corr

# corrs between forced_RDM and fmri RDMs

model_rdm = np.loadtxt("RDMs/forced_model.txt")

fmri_rdms = np.loadtxt("RDMs/fmri_rdms_cue.txt")
fmri_rdms = np.reshape(fmri_rdms, [18, 59, 71, 59, 6, 6])

for sub in range(18):

    subcorrs = fmrirdms_corr(model_rdm, fmri_rdms[sub])
    subcorrs = np.reshape(subcorrs, [59*71*59, 2])
    np.savetxt("corrs/forced/sub" + str(sub+1) + ".txt", subcorrs)

# corrs between free_RDM and fmri RDMs

model_rdm = np.loadtxt("RDMs/free_model.txt")

fmri_rdms = np.loadtxt("RDMs/fmri_rdms_cue.txt")
fmri_rdms = np.reshape(fmri_rdms, [18, 59, 71, 59, 6, 6])

for sub in range(18):

    subcorrs = fmrirdms_corr(model_rdm, fmri_rdms[sub])
    subcorrs = np.reshape(subcorrs, [59*71*59, 2])
    np.savetxt("corrs/free/sub" + str(sub+1) + ".txt", subcorrs)

# corrs between con_RDM and fmri RDMs

model_rdm = np.loadtxt("RDMs/con_model.txt")

fmri_rdms = np.loadtxt("RDMs/fmri_rdms_cue.txt")
fmri_rdms = np.reshape(fmri_rdms, [18, 59, 71, 59, 6, 6])

for sub in range(18):

    subcorrs = fmrirdms_corr(model_rdm, fmri_rdms[sub])
    subcorrs = np.reshape(subcorrs, [59*71*59, 2])
    np.savetxt("corrs/con/sub" + str(sub+1) + ".txt", subcorrs)

# corrs between seq_RDM and fmri RDMs

model_rdm = np.loadtxt("RDMs/seq_model.txt")

fmri_rdms = np.loadtxt("RDMs/fmri_rdms_cue.txt")
fmri_rdms = np.reshape(fmri_rdms, [18, 59, 71, 59, 6, 6])

for sub in range(18):

    subcorrs = fmrirdms_corr(model_rdm, fmri_rdms[sub])
    subcorrs = np.reshape(subcorrs, [59*71*59, 2])
    np.savetxt("corrs/seq/sub" + str(sub+1) + ".txt", subcorrs)