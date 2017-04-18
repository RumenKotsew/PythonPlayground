def prime_sieve(n):
    # returns all primes smaller than n
    sieve = [True] * n
    sieve[:2] = [False, False]  # 0 and 1 are not primes
    primes = []
    for prime, is_prime in enumerate(sieve):
        if not is_prime:
            continue
        primes.append(prime)
        for not_prime in range(prime * prime, n, prime):
            sieve[not_prime] = False
    return primes


def sum_of_primes_generator(value):
    primes = prime_sieve(value)
    lo = 0
    hi = len(primes) - 1
    while lo <= hi:
        prime_sum = primes[lo] + primes[hi]
        if prime_sum < value:
            lo += 1
        else:
            if prime_sum == value:
                yield primes[lo], primes[hi]
            hi -= 1


def goldbach(n):
    arr = sum_of_primes_generator(n)
    res = []

    for i in arr:
        res.append(i)

    return res
