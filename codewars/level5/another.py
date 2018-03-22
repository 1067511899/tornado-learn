import numpy as np
import numba
from time import time

LIMIT = pow(10, 8)


# You could also just use @numba.jit or @numba.jit(nopython=True)
# here and get comparable timings.
@numba.jit('void(uint8[:])', nopython=True)
def primes_util(sieve):
    ssz = sieve.shape[0]
    for j in range(ssz):
        if sieve[j]:
            new_prime = 2 * j + 3
            for k in range((2 * j + 6) * j + 3, ssz, new_prime):
                sieve[k] = False


def primes_numba(limit):
    sieve = np.ones(limit // 2, dtype=np.uint8)
    primes_util(sieve)

    return [2] + (np.nonzero(sieve)[0] * 2 + 3).tolist()


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


t1 = time()
print(t1)
primes(LIMIT)
t2 = time()
print(t2 - t1)
primes_numba(LIMIT)
t3 = time()
print(t3 - t2)
print((t2 - t1) / (t3 - t2))
