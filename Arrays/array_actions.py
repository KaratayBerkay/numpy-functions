import numpy as np


a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2]
b += 1
"""
a = [2 3 3 4 5 6]
b = [2 3]
"""

a = np.array([1, 2, 3, 4])
b = a[:2].copy()
b += 1
"""
a = [1 2 3 4]
b = [2 3]
"""

A = np.ones((2, 2))
B = np.eye(2, 2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

xx = np.block([[A, B], [C, D]])
"""
    [
[ 1.  1.  1.  0.]
[ 1.  1.  0.  1.]
[ 0.  0. -3.  0.]
[ 0.  0.  0. -4.]
    ]
"""

loaded = np.loadtxt("simple.csv", delimiter=",", skiprows=1)
"""
    [
[1. 1. 1. 1.]
[2. 2. 2. 2.]
[3. 3. 3. 3.]
    ]
"""
