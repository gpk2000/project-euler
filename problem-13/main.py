def adjust(numA, numB):
    if len(numA) > len(numB):
        numA, numB = numB, numA

    diff = len(numB) - len(numA)
    numA += '0' * diff

    return numA, numB


def add(numA, numB):
    # reverse them as we normally add
    # from right to left
    numA = numA[::-1]
    numB = numB[::-1]

    # modify them so that their
    # lengths are equal
    numA, numB = adjust(numA, numB)
    
    result = ''
    carry = 0
    N = len(numA)
    for i in range(N):
        curr = int(numA[i]) + int(numB[i]) + carry
        dig = curr % 10
        carry = curr // 10
        result += str(dig)

    if carry:
        result += str(carry)

    # reverse of result will be the answer
    return result[::-1]

final_result = ''

# read the numbers stored in nums.txt
with open('nums.txt', 'r') as f:
    for num in f.readlines():
        num = num.strip()
        final_result = add(final_result, num)

print(final_result[:10])
