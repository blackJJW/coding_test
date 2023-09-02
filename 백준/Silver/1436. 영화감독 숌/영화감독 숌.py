n = int(input())

small_number = 666
list_num = []
tmp = small_number

while True:
    if str(tmp).find(str(small_number)) != -1:
        list_num.append(tmp)

    if len(list_num) == n:
        break
    
    tmp = tmp + 1
    
print(list_num[-1])