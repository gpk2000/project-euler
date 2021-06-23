def collatz_chain_len(num):
    if num == 1:
        return 1
    
    if num % 2 == 0:
        return collatz_chain_len(num//2) + 1
    return collatz_chain_len(3*num+1)

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
