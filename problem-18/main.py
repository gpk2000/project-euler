ROWS = COLS = 15

# initial matrix all filled with zeros
tri_sum = [[0 for j in range(COLS)] for i in range(ROWS)]

# read the file and fill the entries in tri_sum
with open('input', 'r') as f:
    r = 0
    for line in f.readlines():
        line = list(map(int, line.split()))
        
        for c, el in enumerate(line):
            tri_sum[r][c] = el
        r += 1

for i in range(ROWS):
    for j in range(COLS):
        if i == 0 and j == 0: continue
        if j == 0:
            tri_sum[i][j] += tri_sum[i - 1][j]
        else:
            tri_sum[i][j] += max(tri_sum[i - 1][j], tri_sum[i - 1][j - 1])

# as we can end at any position in the last
# row we need to print maximum of all those
# values
print(max(tri_sum[ROWS-1]))
