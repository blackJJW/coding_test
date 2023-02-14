n = int(input())
pile = 1
cnt = 1
while n > pile :
    pile += 6 * cnt
    cnt += 1
    
print(cnt)