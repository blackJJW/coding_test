N, X = map(int, input().split())
C = list(map(int, input().split()))
l = []
for i in range(N):
    if C[i] < X:
        l.append(str(C[i]))
        
print(" ".join(l))

