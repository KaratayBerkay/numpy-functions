import numpy as np

list_a_range = np.arange(10)

third, last_two = list_a_range[2], list_a_range[-2]
"""
[0 1 2 3 4 5 6 7 8 9]
2
8
"""

list_a_range.shape = (2, 5)  # now x is 2-dimensional
"""
    [
[0 1 2 3 4]
[5 6 7 8 9]
    ]
"""

x_result, y_r = list_a_range[0], list_a_range[0][2]
"""
[0 1 2 3 4]
"""
x_rr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
rr_res = x_rr[1:7:2], x_rr[-2:10], x_rr[-3:3:-1], x_rr[5:]
"""
[1 3 5], [8 9], [7 6 5 4], [5 6 7 8 9]
"""

ll_rr = np.array([[[1], [2], [3]], [[4], [5], [6]]])
ll_rr_shape, ll_slice = ll_rr.shape, ll_rr[1:2]
"""
(2, 3, 1)
        [
    [
[4]
[5]
[6]
    ]
        ]
"""

x_re = np.array([[[1], [2], [3]], [[4], [5], [6]]])
rr_equ, rx_equ = x_re[..., 0], x_re[:, :, 0]
"""
[
    [1, 2, 3],
    [4, 5, 6]
]
[
    [1, 2, 3],
    [4, 5, 6]
]
"""
tt = np.arange(10, 1, -1)
ta = np.array([3, 3, 1, 8])
aa = tt[ta]
"""
[10  9  8  7  6  5  4  3  2]
[3 3 1 8]
[7 7 9 2]
"""

