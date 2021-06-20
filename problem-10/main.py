def sieve_of_eratosthenes(limit):
    prime_flag = [True] * limit
    prime_flag[0] = prime_flag[1] = False

    i = 2
    while i * i <= limit:
        if prime_flag[i]:
            for j in range(2*i, limit, i):
                prime_flag[j] = False
        i += 1

    return prime_flag

primes = sieve_of_eratosthenes(int(2e6))
primes_sum = sum(i for i, el in enumerate(primes) if el)
print(primes_sum)
