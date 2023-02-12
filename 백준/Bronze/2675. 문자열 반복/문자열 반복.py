a = int(input())
for i in range(a):
    b, c = input().split()
    txt = ''
    for i in c:
        txt += int(b) * i
    print(txt)
    