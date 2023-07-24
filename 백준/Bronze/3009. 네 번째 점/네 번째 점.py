def rec_count(list):
    for i in list:
        if list.count(i) == 1:
            return i
        else:
            continue

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

x_list = [a, c, e]
y_list = [b, d, f]

x = rec_count(x_list)
y = rec_count(y_list)

print(x, y)
