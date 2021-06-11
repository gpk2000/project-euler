N = 1000
multiple_sum = 0

for i in range(1, N):
    if i % 3 == 0 or i % 5 == 0:
        multiple_sum += i

print(multiple_sum)
