# -*- coding: utf-8 -*-

""" Statistical Analysis """

__author__ = 'Zitong Lu'

import numpy as np
from neurora.stats_cal import stats_fmri

# forced

corrs = np.zeros([18, 59, 71, 59, 2], dtype=np.float)

for sub in range(18):
    subcorrs = np.loadtxt("corrs/forced/sub" + str(sub+1) + ".txt")
    subcorrs = np.reshape(subcorrs, [59, 71, 59, 2])
    corrs[sub] = subcorrs
    print(sub)

stats_results = stats_fmri(corrs, permutation=False)

stats_results = np.reshape(stats_results, [59*71*59, 2])
np.savetxt("stats/forced.txt", stats_results)

# free

corrs = np.zeros([18, 59, 71, 59, 2], dtype=np.float)

for sub in range(18):
    subcorrs = np.loadtxt("corrs/free/sub" + str(sub+1) + ".txt")
    subcorrs = np.reshape(subcorrs, [59, 71, 59, 2])
    corrs[sub] = subcorrs
    print(sub)

stats_results = stats_fmri(corrs, permutation=False)

stats_results = np.reshape(stats_results, [59*71*59, 2])
np.savetxt("stats/free.txt", stats_results)

# con

corrs = np.zeros([18, 59, 71, 59, 2], dtype=np.float)

for sub in range(18):
    subcorrs = np.loadtxt("corrs/con/sub" + str(sub+1) + ".txt")
    subcorrs = np.reshape(subcorrs, [59, 71, 59, 2])
    corrs[sub] = subcorrs
    print(sub)

stats_results = stats_fmri(corrs, permutation=False)

stats_results = np.reshape(stats_results, [59*71*59, 2])
np.savetxt("stats/con.txt", stats_results)

# seq

corrs = np.zeros([18, 59, 71, 59, 2], dtype=np.float)

for sub in range(18):
    subcorrs = np.loadtxt("corrs/seq/sub" + str(sub+1) + ".txt")
    subcorrs = np.reshape(subcorrs, [59, 71, 59, 2])
    corrs[sub] = subcorrs
    print(sub)

stats_results = stats_fmri(corrs, permutation=False)

stats_results = np.reshape(stats_results, [59*71*59, 2])
np.savetxt("stats/seq.txt", stats_results)