n = int(input())

n_list = list(map(int, str(n)))
n_list.sort(reverse = True)

sorted_n = int(''.join(map(str, n_list)))

print(sorted_n)


