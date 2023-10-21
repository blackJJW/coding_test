from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int, stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int, stdin.readline().split()))

cnt = Counter(card)

for i in range(len(test)):
    if test[i] in cnt:
        print(cnt[test[i]], end=' ')
    else:
        print(0, end=' ')
