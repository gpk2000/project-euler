def fast_power(a, b):
    # calculates a^b in O(log n) time
    res = 1
    while b:
        if b & 1:
            res *= a
        a *= a
        b >>= 1

    return res


def digit_sum(num):
    res = 0
    while num:
        res += num % 10
        num //= 10
    return res


N = 1000
pow2 = fast_power(2, N)
dig_sum = digit_sum(pow2)

print(dig_sum)
