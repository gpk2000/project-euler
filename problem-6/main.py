def sum_n(n):
    return (n * (n + 1)) // 2

def sum_square_n(n):
    return (n * (n + 1) * (2*n + 1)) // 6

print(sum_n(100)**2 - sum_square_n(100))
