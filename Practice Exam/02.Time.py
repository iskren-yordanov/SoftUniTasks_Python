from collections import deque

first = input().split()
second = input().split()

rows = len(first) + 1
cols = len(second) + 1

dp = []
for _ in range(rows):
    dp.append([0] * cols)

for row in range(1, rows):
    for col in range(1, cols):
    
        if first[row-1] == second[col-1]:
            # only when they matche we will increase
            dp[row][col] = dp[row-1][col-1] + 1
        else:
            dp[row][col] = max(dp[row-1][col], dp[row][col-1]) #if not matching, just move the best solution further without increase


row = rows - 1
col = cols - 1


result = deque()

while row > 0 and col > 0:
    if first[row-1] == second[col-1]:
        result.appendleft(first[row-1])
        row -=1
        col -=1

    elif dp[row-1][col] > dp[row][col-1]:
        row -=1
    
    else:
        col -=1
        
    
print(*result, sep = ' ')
print(dp[rows-1][cols-1])