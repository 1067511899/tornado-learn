from numba import autojit
from time import time

LIMIT = pow(10, 6)


def primes(limit):
    # Keep only odd numbers in sieve, mapping from index to number is
    # num = 2 * idx + 3
    # The square of the number corresponding to idx then corresponds to:
    # idx2 = 2*idx*idx + 6*idx + 3
    sieve = [True] * (limit // 2)
    prime_numbers = set([2])
    for j in range(len(sieve)):
        if sieve[j]:
            new_prime = 2 * j + 3
            prime_numbers.add(new_prime)
            for k in range((2 * j + 6) * j + 3, len(sieve), new_prime):
                sieve[k] = False
    return list(prime_numbers)


numba_primes = autojit(primes)

start = time()
numba_primes(LIMIT)
end = time()
print("Numba: Time Taken : ", end - start)

start = time()
primes(LIMIT)
end = time()
print("Python: Time Taken : ", end - start)

