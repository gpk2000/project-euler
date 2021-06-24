N = 21
ways = [[0] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 or j == 0:      ways[i][j] = 1
        else:
            ways[i][j] = ways[i - 1][j] + ways[i][j - 1] 

# we need to give the result of ways[20][20]
print(ways[20][20])
