pro_list = []
rest_list = []

for i in range(10):
    a = int(input())
    pro_list.append(a)

for i in range(len(pro_list)):
    b = pro_list[i] % 42
    rest_list.append(b)

nw = list(set(rest_list))
print(len(nw))