factNum = [1]

def multiply(x):
    # multiplies the number represented
    # as a list with x using the elementary
    # school multiplication method
    carry = 0
    for i in range(len(factNum)):
        current = carry + factNum[i] * x
        factNum[i] = current % 10
        carry = current // 10

    # if carry is left append it
    while carry:
        factNum.append(carry % 10)
        carry //= 10

N = 10000
for i in range(1, N):
    multiply(i)

digSum = sum(el for el in factNum)
print(digSum)
