def getAsciiSum(string):
    ascii_sum = 0
    for ch in string:
        ascii_sum += ord(ch) - ord('A') + 1
    return ascii_sum

with open('names.txt', 'r') as file:
    strings = [s.replace('\"', '') for s in file.readlines()[0].split(',')]
    strings.sort()
    
    total_score = 0
    for i, string in enumerate(strings):
        total_score += getAsciiSum(string) * (i+1)

print(total_score)

