"""
oldest version
"""


from typing import List


def get_primes_lower_n(n: int) -> List[int]:
	"""
	n: int
		the given input number
	returns: List[int]
		all primes number lower than given input number
	"""
	return [num for num in range(2, n + 1) if is_prime(num)]


def is_prime(num: int) -> bool:
	"""
	it checks whether the number is prime or not
	num: int
		number to check
	returns: bool
		True if the num is prime else False
	"""
	for t in range(2, num):
		if num % t == 0:
			return False
	return True
