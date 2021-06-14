def reverse(n):
    ret = 0
    while n:
        ret = ret * 10 + n % 10
        n //= 10
    return ret


def check_palindrome(n):
    rev_n = reverse(n)
    return n == rev_n


max_palin_prod = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i * j
        if check_palindrome(prod):
            max_palin_prod = max(max_palin_prod, prod)

print(max_palin_prod)
