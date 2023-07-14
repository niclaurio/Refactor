from version1 import check_input, List
from math import isqrt


def get_primes_lower_n(n: int) -> List[int]:
    check_input(n)
    multiples = []
    primes = []
    sqrt = isqrt(n)
    for num in range(3, sqrt + 1, 2):
        if num not in multiples:
            multiples += list(range(num ** 2, n + 1, num * 2))
            primes += [num]
    for num in range(sqrt + 1, n + 1, 2):
        if num not in multiples:
            primes += [num]
    return primes
