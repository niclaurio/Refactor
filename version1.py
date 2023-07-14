from typing import List


def check_input(n: int) -> int:
    if isinstance(n, float):
        return int(n)
    if not isinstance(n, int):
        raise TypeError("an integer is required")
    if n <= 2:
        raise ValueError("this algorithm works only with number greater than 1")
    return n


def get_primes_lower_n(n: int) -> List[int]:
    n = check_input(n)
    primes = []
    for num in range(2, n + 1):
        is_prime_ = is_prime(num)
        if is_prime_:
            primes.append(num)
    return primes


def is_prime(n: int) -> bool:
    for num in range(2, n):
        if not n % num: # n % num == 0
            return False
    return True

