#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k. For example, given [10, 15, 3, 7] and k of 17, return
# true since 10 + 7 is 17.

from __future__ import print_function

TEST = [
    (True, 17, [10, 15, 3, 7]),
    (True, 3, [9, 8, 3, 12, 1, 19, 2]),
    (True, 81, [80, 5, 4, 3, 22, 1]),
    (False, 12, [1, 2, 3, 4, 5, 6]),
    (False, 12, [12, 13, 14, 15, 16]),
    (False, 12, [3, 7, 8, 2, 24, 36]),
]


def ex01(k, ns):
    s = set()
    for n in ns:
        if k - n in s:
            return True
        s.add(n)
    return False


def test_ex01(t):
    ret = []
    for i, k, ns in t:
        if i == ex01(k, ns):
            ret.append("OK")
        else:
            ret.append("failed")
    return ret


if __name__ == "__main__":
    print("Tests:", str(test_ex01(TEST)))
