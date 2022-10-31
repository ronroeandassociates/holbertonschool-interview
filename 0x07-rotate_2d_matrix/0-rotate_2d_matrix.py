#!/usr/bin/python3
"""
    0 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):

    matrix[:] = [list(i) for i in zip(*matrix[::-1])]
