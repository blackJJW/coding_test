import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in M_list:
    dic[i] = 0

for j in N_list:
    if j in dic:
        dic[j] = 1

for l in dic:
    print(dic[l], end=' ')