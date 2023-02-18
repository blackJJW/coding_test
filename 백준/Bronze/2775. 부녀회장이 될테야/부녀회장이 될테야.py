t = int(input())

for _ in range(t):
    floor = int(input()) # 층
    num = int(input()) # 호
    lst_0 = [ x for x in range(1, num + 1) ] # 0 층 리스트
    for k in range(floor):
        for i in range(1, num):
            lst_0[i] += lst_0[i - 1]
    print(lst_0[-1]) # 가장 마지막 수 출력