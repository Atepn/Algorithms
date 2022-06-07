def is_prime_number(N):
    """implements a prime number test by using sieve of Eratosthenes. returns a bool"""
    if N < 2:
        return False
    nlist = [True]*(N+1)
    # nlist[0] = nlist[1] = False
    for i in range(2, N+1):
        if nlist[i]:
            for j in range(2*i, N+1, i):
                nlist[j] = False
    return nlist[N]
print(is_prime_number(11))