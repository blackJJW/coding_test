import sys

n = int(sys.stdin.readline())
tmp = dict()

for i in range(n):
    name, stat = map(str, sys.stdin.readline().split())
    
    if stat == "enter":
        tmp[name] = stat
    else:
        del tmp[name]
        
tmp = sorted(tmp.keys(), reverse=True)

for j in tmp:
    print(j)