cache = dict()

def collatz_chain_len(num):
    if num == 1:
        return 1
    
    # already found the chain length
    if num in cache:
        return cache[num]

    # else now solve this problem
    if num % 2 == 0:
        cache[num] = collatz_chain_len(num//2) + 1
    else:
        cache[num] = collatz_chain_len(3*num + 1) + 1

    # return the result
    return cache[num]

iter = 1
max_chain_len = 0
max_chain_num = 0
while iter < int(1e6):
    curr_chain_len = collatz_chain_len(iter)
    
    if curr_chain_len > max_chain_len:
        max_chain_len = curr_chain_len
        max_chain_num = iter
    
    iter += 1

print(max_chain_num)
