"""
refactor:
	for each prime number p lower than n Version2.py is going to iterate over any odd number lower than p for nothing.
	This can be avoided subtracting to all odd numbers lower than n, all the multiples of any prime numb lower than sqrt(n)
"""


from math import isqrt
from typing import List


def get_primes_lower_n(n: int) -> List[int]:
	"""
		n: int
			the given input number
		returns: List[int]
			all primes number lower than given input number
		raises:
			ValueError: the given input is an integer < 2
			TypeError: the given input is not an integer
	"""
	if not isinstance(n, int):
		raise TypeError("an integer is required")
	if n < 2:
		raise ValueError("an integer > 1 is required")
	primes = set(range(3, n + 1, 2))
	for num in range(3, isqrt(n) + 1, 2):
		if num in primes:
			primes = primes.difference(set(range(num ** 2, n + 1, num * 2)))
	return [2] + sorted(list(primes))
