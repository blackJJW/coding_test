import sys
input=sys.stdin.readline

n = int(input())

num = [0] * 10001

for i in range(n):
    tmp = int(input())
    num[tmp] += 1

for j in range(10001):
    if num[j] != 0:
        for k in range(num[j]):
            print(j)
    