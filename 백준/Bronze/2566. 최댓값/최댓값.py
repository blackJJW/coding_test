table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
tmp = 0
m_row = 0
for r in range(9):
    tmp = max(table[r])
    if max_num < tmp:
        max_num = tmp
        m_row = r
        
print(max_num)
print(m_row + 1, table[m_row].index(max_num) + 1)