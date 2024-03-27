#!/usr/bin/env python
# coding: utf-8

# # Assignment 12
# 
# Complete the `Matrix` class below by implementing the three member functions that perform the following matrix row operations:
# 
#  * `row_swap`: Should swap rows `i` and `j` in a matrix.
#  
#  * `row_multiply`: Should multiply row `i` by `factor`.
#  
#  * `row_combine`: Should perform the operation
#  
#     $$
#     A_i = A_i - m  A_j
#     $$
#     
#     where $A$ is a matrix and $i$ and $j$ are rows of the matrix.  $m$ is a     scalar multiplication `factor`.
#     
# The operations should perform the matrix manipulations to the `mat` class attribute *in place*, i.e. they should **not** return a new matrix.  You can assume that `mat` will always be a NumPy array.

# In[8]:


import numpy as np

class Matrix(object):
    
    def __init__(self, array):
        
        if not isinstance(array, (list, np.ndarray)):
            raise TypeError('Input matrix must be a Python list or NumPy ndarray.')
        else:
            self.mat = np.array(array, dtype=np.double)
        
    def __str__(self):
        return str(self.mat)
    
    def __call__(self):
        return self.mat

    def __getitem__(self, key):
        return self.mat[key]
    
    def __setitem__(self, key, value):
        self.mat[key] = value
    
    def row_swap(self, i, j):
        temp = self.mat[i].copy() 
        self.mat[i] = self.mat[j]
        self.mat[j] = temp
        return
    
    def row_multiply(self, i, factor):
        self.mat[i] *= factor
        return
        
    def row_combine(self, i, j, factor):
        self.mat[i] -= factor * self.mat[j]
        return

