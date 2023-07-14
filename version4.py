"""
Refactor:
    - I remove all multiples lower than n of all the primes lower than n
"""


from version1 import check_input, List
from math import isqrt


def get_primes_lower_n(n: int) -> List:
    check_input(n)
    primes = set(range(3, n+1, 2))
    for num in range(3, isqrt(n)+1, 2):
        if num in primes:
            primes = primes.difference(set(range(num ** 2, n + 1, num * 2)))
    return [2] + list(primes)
