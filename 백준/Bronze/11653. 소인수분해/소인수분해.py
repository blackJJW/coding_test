a = int(input())

if a == 1:
    print('')
    
for i in range(2, a + 1):
    if a % i == 0:
        while a % i == 0:
            print(i)
            a = a / i
        