a = int(input())

bag = 0
while a >= 0:
    if a % 5 == 0:
        bag += (a // 5)
        print(bag)
        break
    a -= 3
    bag += 1
else:
    print(-1)