# -*- coding: utf-8 -*-

""" Create the Coding Model RDM """

__author__ = 'Zitong Lu'

import numpy as np
from neurora.rsa_plot import plot_rdm

labels = ["Free 1st", "Free 2nd", "Free 3th", "Forced 1st", "Forced 2nd", "Forced 3th"]

# condition coding model

con_rdm = np.array([[0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 1, 1],
                    [1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0]])

np.savetxt("RDMs/con_model.txt", con_rdm)
plot_rdm(con_rdm, conditions=labels)

# sequence coding model

seq_rdm = np.array([[0, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0],
                    [0, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0]])

np.savetxt("RDMs/seq_model.txt", seq_rdm)
plot_rdm(seq_rdm, conditions=labels)

# free coding model

free_rdm = np.array([[0, 0, 0, 1, 1, 1],
                     [0, 0, 0, 1, 1, 1],
                     [0, 0, 0, 1, 1, 1],
                     [1, 1, 1, 0, 1, 1],
                     [1, 1, 1, 1, 0, 1],
                     [1, 1, 1, 1, 1, 0]])

np.savetxt("RDMs/free_model.txt", free_rdm)
plot_rdm(free_rdm, conditions=labels)

# forced coding model

forced_rdm = np.array([[0, 1, 1, 1, 1, 1],
                       [1, 0, 1, 1, 1, 1],
                       [1, 1, 0, 1, 1, 1],
                       [1, 1, 1, 0, 0, 0],
                       [1, 1, 1, 0, 0, 0],
                       [1, 1, 1, 0, 0, 0]])

np.savetxt("RDMs/forced_model.txt", forced_rdm)
plot_rdm(forced_rdm, conditions=labels)