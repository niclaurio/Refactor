"""
Refactor:
    List comprehension is faster than "explicit" for loop
"""

from version1 import check_input, is_prime, List


def get_primes_lower_n(n: int) -> List[int]:
    n = check_input(n)
    return [num for num in range(2, n+1) if is_prime(num)]
