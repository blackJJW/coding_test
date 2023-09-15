N = int(input())

n_list = []
for i in range(N):
    age, name = map(str, input().split())
    n_list.append((int(age), name))

n_list.sort(key = lambda x : x[0])

for i in n_list:
    print(i[0], i[1])