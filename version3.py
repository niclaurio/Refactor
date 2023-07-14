"""
refactor:
    - every even number greater than 2 is not prime as it is divisible by 2.
    - As no integer number is the result of the product between 2 numbers greater than its square root, it the number has no
    divisor lower than its square root, the number is prime.
"""

from version1 import check_input, List
from math import isqrt


def get_primes_lower_n(n: int) -> List[int]:
    n = check_input(n)
    return [2] + [num for num in range(3, n + 1, 2) if is_prime(num)]


def is_prime(n: int) -> bool:
    for num in range(3, isqrt(n) + 1, 2):
        if not n % num:  # n % num == 0
            return False
    return True
