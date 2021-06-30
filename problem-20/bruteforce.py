def getFactDigitSum(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    print(len(str(fact)))
    digSum = 0
    while fact:
        digSum += fact % 10
        fact //= 10

    return digSum

print(getFactDigitSum(10000))
