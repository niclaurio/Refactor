"""
refactor:
    a logical deletion of primes ' multiples is faster
"""
import numpy as np
from version1 import check_input
from math import isqrt


def get_primes_lower_n(n: int):
    n = check_input(n)
    primes = np.ones(n, dtype=bool)
    primes[:2] = False
    primes[4: n + 1: 2] = False
    for i in range(3, isqrt(n), 2):
        if primes[i]:
            primes[i ** 2:n + 1:2 * i] = False
    return np.where(primes == True)


