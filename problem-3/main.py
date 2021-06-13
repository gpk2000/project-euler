def get_max_prime_factor(n):
    max_prime_factor = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            max_prime_factor = max(max_prime_factor, i)
            while n % i == 0:
                n //= i
        i += 1

    if n > 1:
        max_prime_factor = max(max_prime_factor, n)

    return max_prime_factor

N = 600851475143
print(get_max_prime_factor(N))
