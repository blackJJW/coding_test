n = int(input())
a = input()
a_list = [int(i) for i in str(a)]
tmp = 0
for i in range(n):
    tmp += a_list[i]

print(tmp)