n = int(input())
lst = []
for i in range(n):
    tmp = input()
    lst.append(tmp)
    
for i in lst:
    print(i[0] + i[-1])