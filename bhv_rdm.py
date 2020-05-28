# -*- coding: utf-8 -*-

""" Calculate the RDM based on behavior data """

__author__ = 'Zitong Lu'

import numpy as np
import scipy.io as sio
from neurora.rdm_cal import bhvRDM
from neurora.rsa_plot import plot_rdm_withvalue, plot_rdm

labels = ["Free 1st", "Free 2nd", "Free 3th", "Forced 1st", "Forced 2nd", "Forced 3th"]

# sd RDM

sd_free = sio.loadmat("/Users/zitonglu/Desktop/VWM_hyt/sd.mat")["s_free"]
sd_forced = sio.loadmat("/Users/zitonglu/Desktop/VWM_hyt/sd.mat")["s_forced"]
sd = np.zeros([19, 6])
sd[:, :3] = sd_free
sd[:, 3:] = sd_forced

sd = np.transpose(sd, (1, 0))
sd_rdm = bhvRDM(sd, data_opt=0)
plot_rdm_withvalue(sd_rdm, conditions=labels)
plot_rdm(sd_rdm, conditions=labels)
np.savetxt("RDMs/sd_rdm.txt", sd_rdm)

# rt RDM

rt_free = sio.loadmat("/Users/zitonglu/Desktop/VWM_hyt/RT.mat")["rt1_free"]
rt_forced = sio.loadmat("/Users/zitonglu/Desktop/VWM_hyt/RT.mat")["rt1_forced"]
rt = np.zeros([19, 6])
rt[:, :3] = rt_free
rt[:, 3:] = rt_forced

rt = np.transpose(rt, (1, 0))
rt_rdm = bhvRDM(rt, data_opt=0)
plot_rdm_withvalue(rt_rdm, conditions=labels)
plot_rdm(rt_rdm, conditions=labels)
np.savetxt("RDMs/rt_rdm.txt", rt_rdm)
