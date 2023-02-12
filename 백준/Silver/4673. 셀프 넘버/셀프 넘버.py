def make_10000():
    list_10000 = []
    for i in range(10000):
        list_10000.append(i + 1)
    
    return list_10000

def check_self_number(a):
    input_num = a
    tmp = 0
    result = 0
    input_num_list = [int(a) for a in str(input_num)]
    for i in input_num_list:
        tmp += i
    result = input_num + tmp
    
    return result

list_a = make_10000()
list_b = []

for i in list_a:
    tmp = check_self_number(i)
    list_b.append(tmp)

for i in list_a:
    if i not in list_b:
        print(i)
    else:
        continue

     