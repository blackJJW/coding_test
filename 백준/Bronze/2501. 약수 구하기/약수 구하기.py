a, b = map(int, input().split())

tmp = 1
ans = []

while True:
    if tmp > a:
        break
        
    if a % tmp == 0:
        ans.append(tmp)
        
    tmp += 1

if len(ans) < b:
    print(0)
else:
    print(ans[b-1])

    