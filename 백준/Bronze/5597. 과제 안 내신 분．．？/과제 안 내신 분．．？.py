list = []
ans = []
for i in range(28):
    a = int(input())
    list.append(a)

for i in range(30):
    if (i + 1) in list:
        continue
    else:
        ans.append(int(i + 1))
print(ans[0])
print(ans[1])