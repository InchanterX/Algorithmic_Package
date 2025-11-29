def factorial(n: int) -> int:
    '''
    A fast solution to count factorial by finding prime numbers among the sequence from 0 to n
    using Eratosthenes's sieve and following math formula
    '''

    # base cases
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2

    # Eratosthenes's sieve
    primes = [n for n in range(0, n+1)]
    i = 2
    while i*i <= n:
        if primes[i] != 0:
            j = i*i
            while j <= n:
                primes[j] = 0
                j += i
        i += 1
    primes = [prime for prime in primes if prime >= 2]

    # powers count
    total = 1
    for prime in primes:
        power = 0
        copy = prime
        while copy <= n:
            power += n//copy
            copy *= prime
        total *= pow(prime, power)
    return total


def factorial_recursive(n: int) -> int:
    '''
    A simple but extremely slow solution of counting factorial using recursion
    '''
    # base cases
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    # recursive call of function
    return n*factorial_recursive(n-1)
