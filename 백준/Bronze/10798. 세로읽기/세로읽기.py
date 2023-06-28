table = [input() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(table[i]):
            print(table[i][j], end='')