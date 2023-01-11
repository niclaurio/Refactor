"""
refactor:
  - what happens if I insert an object that is not integer?
  - What happens if I insert an integer <2?
  - even number greater than 2 they are not prime as they are all divisible by 2
  - if n = a*b & a > sqrt(n) => b < sqrt(n). If this is true,
  		if a number is not divisible by any number lower than its sqrt, then the number is prime

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
	return [2] + [num for num in range(3, n + 1, 2) if is_prime(num)]


def is_prime(num: int) -> bool:
	"""
	it checks whether the number is prime or not
	num: int
		number to check
	returns: bool
		True if the num is prime else False
	"""
	for t in range(3, isqrt(num) + 1, 2):
		if num % t == 0:
			return False
	return True
