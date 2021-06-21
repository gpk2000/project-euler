def count_divisors(n):
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_cnt = 0
            while n % i == 0:
                n //= i
                prime_cnt += 1

            total *= (prime_cnt + 1)
        i += 1

    if n > 1:
        total *= 2

    return total

def triangular_num(i):
    return i * (i + 1) // 2

i = 1
while True:
    N = triangular_num(i)
    if count_divisors(N) > 500:
        print(N)
        exit(0)
    i += 1
