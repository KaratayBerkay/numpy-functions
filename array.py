import numpy as np
from numpy.random import default_rng


a1D = np.array([1, 2, 3, 4])
a2D = np.array([[1, 2], [3, 4]])
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
"""
Output:
[1 2 3 4]
        [
[1 2]
[3 4]
        ]
        [
    [
[1 2]
[3 4]
    ]
"""
a_bit = np.array([127, 128, 129], dtype=np.uint32)
b_bit = np.array([2, 3, 4], dtype=np.uint32)
c_bit = np.array([5, 6, 7], dtype=np.uint32)
"""
Output:
[127 128 129] 
[2 3 4]
[5 6 7]
"""

x_bit = np.diag([1, 2, 3])
y_bit = np.diag([1, 2, 3], 1)
z_bit = np.array([[1, 2], [3, 4]])
"""
Output:
            [
[1 0 0]
[0 2 0]
[0 0 3]
            ] 
            [
[0 1 0 0]
[0 0 2 0]
[0 0 0 3]
[0 0 0 0]   ]
            [
[1 2]
[3 4]
            ]
"""

at_bit = np.vander(np.linspace(0, 2, 5), 2)
bt_bit = np.vander([1, 2, 3, 4], 2)
ct_bit = np.vander((1, 2, 3, 4), 4)
"""
Output:
    [
[0.  1. ]
[0.5 1. ]
[1.  1. ]
[1.5 1. ]
[2.  1. ]
    ]
    [
[1 1] [2 1] [3 1] [4 1]
    ]
    [
[ 1  1  1  1]
[ 8  4  2  1]
[27  9  3  1]
[64 16  4  1]
    ]
"""

xx_result = np.vander(np.linspace(0, 2, 5), 2)
xy_result = np.vander([1, 2, 3, 4], 2)
xz_result = np.vander((1, 2, 3, 4), 4)
"""
        [
[0. , 1. ],
[0.5, 1. ],
[1. , 1. ],
[1.5, 1. ],
[2. , 1. ]
        ]
        [
[1, 1],
[2, 1],
[3, 1],
[4, 1]
        ]
        [
[ 1,  1,  1,  1],
[ 8,  4,  2,  1],
[27,  9,  3,  1],
[64, 16,  4,  1]
        ]
"""
xt_result = default_rng(42).random((2, 3))
yt_result = default_rng(42).random((2, 3, 2))
print(xt_result)
print(yt_result)

"""
[
[0.77395605 0.43887844 0.85859792]
[0.69736803 0.09417735 0.97562235]
] 
        [
    [
[0.77395605 0.43887844]
[0.85859792 0.69736803]
[0.09417735 0.97562235]]

[[0.7611397  0.78606431]
[0.12811363 0.45038594]
[0.37079802 0.92676499]
    ]
        ]
"""

