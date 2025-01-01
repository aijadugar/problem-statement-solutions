
grid = [[3,0,8,4],
        [2,4,5,7],
        [9,2,6,3],
        [0,3,1,0]]

n = len(grid)

row, col = [0]*n, [0]*n

for i in range(n):
    for j in range(n):
        row[i] = max(row[i], grid[i][j])
        col[j] = max(col[j], grid[i][j])
        
print(row, col)
ans = 0

for i in range(n):
    for j in range(n):
        ans += (min(row[i], col[j]) - grid[i][j])

print(ans)