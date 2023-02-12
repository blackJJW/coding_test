s = input()
a_list = []
result = []

for i in range(97, 123):
    if chr(i) in s:
        al = chr(i)
        tmp = s.index(al)
        result.append(tmp)
    else:
        result.append(-1)

for i in result:
    print(i, end=" ")
    