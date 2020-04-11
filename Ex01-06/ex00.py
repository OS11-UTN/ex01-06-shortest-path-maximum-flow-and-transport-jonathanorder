
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

# Matrix treatment:
def nn2na(NN):
    idxs = np.argwhere(NN)
    NA = np.zeros([NN.shape[0], idxs.shape[0]]).astype(int)
    C = np.zeros(NA.shape[1])
    for i, arc in enumerate(idxs):
        NA[arc[0], i] = 1 # From
        NA[arc[1], i] = -1 # To

    arc_idxs = [(arc[0], arc[1]) for arc in idxs]

    return  NA, arc_idxs


