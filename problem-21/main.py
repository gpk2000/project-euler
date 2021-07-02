def D(n):
    div_sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            div_sum += i
            # if they are the same for ex n = 36, and 6 6
            if n // i != i:
                div_sum += n // i
        i += 1

    return div_sum

i = 1
amic_sum = 0
while i < 10000:
    temp = D(i)
    if i != temp and i == D(temp):
        amic_sum += i

    i += 1

print(amic_sum)
