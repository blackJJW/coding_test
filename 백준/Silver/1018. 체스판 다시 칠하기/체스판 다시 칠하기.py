n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())
    
for i in range(n - 7):
    for j in range(m - 7):
        dr1 = 0
        dr2 = 0
        
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'B':
                        dr1 += 1
                    if board[k][l] != 'W':
                        dr2 += 1
                else:
                    if board[k][l] != 'W':
                        dr1 += 1
                    if board[k][l] != 'B':
                        dr2 += 1
        result.append(dr1)
        result.append(dr2)
        
print(min(result))