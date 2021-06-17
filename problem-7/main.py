def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

_10001st_prime = None
cnt = 0
num = 2

while cnt < 10001:
    if is_prime(num):
        cnt += 1
        _10001st_prime = num

    num += 1

print(_10001st_prime)
