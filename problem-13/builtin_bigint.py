final_result = 0
with open('nums.txt', 'r') as f:
    for num in f.readlines():
        final_result += int(num)

final_result = str(final_result)
print(final_result[:10])
