# -*- coding: utf-8 -*-

import numpy as np

# [0]*N 与 [[0]*N]*M 的用法

test1 = [0]*5
print test1
### result: [0, 0, 0, 0, 0]

test2 = [[0]*2]*3
print test2
### result: [[0, 0], [0, 0], [0, 0]]

test2[1][0] = 1
print test2
### result: [[1, 0], [1, 0], [1, 0]] 此处矩阵每一行都以 *3 的关系进行改变

test3 = [[0]*2]*3
test3_1 = np.array(test3)
test3_1[1][0] = 1
print test3_1
### result: [[0 0]
###          [1 0]
###          [0 0]]