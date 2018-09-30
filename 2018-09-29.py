#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original
# array except the one at i.

from __future__ import print_function

from operator import mul

TEST = [
    ([3, 2, 1], [2, 3, 6]),
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
    ([234, 829, 447], [370563, 104598, 193986]),
]


def ex02(l):
    ret = []
    for i, _ in enumerate(l):
        t = list(l)
        t.pop(i)
        ret.append(reduce(mul, t, 1))
    return ret


def test_ex02(t):
    ret = []
    for a, b in t:
        if ex02(a) == b:
            ret.append("OK")
        else:
            ret.append("failed")
    return ret


if __name__ == "__main__":
    print("Tests:", test_ex02(TEST))
