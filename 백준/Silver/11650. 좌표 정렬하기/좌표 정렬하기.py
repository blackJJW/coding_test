N = int(input())

num_list = []

for i in range(N):
    x, y = map(int, input().split())
    num_list.append([x, y])

num_list.sort()

for j, k in num_list:
    print(j, k)
    