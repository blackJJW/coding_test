N = int(input())

num_list = []

for i in range(N):
    tmp = int(input())
    num_list.append(tmp)
    
num_list.sort()

for j in num_list:
    print(j)