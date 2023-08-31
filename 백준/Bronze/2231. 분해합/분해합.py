def do_sum(n):
    len_n = len(str(n))
    sum_n = 0
    if len_n == 1:
        sum_n = n + n
    else:
        sum_n = n + sum(map(int, str(n)))
    return sum_n

N = int(input())
num_list = []

len_N = len(str(N))

for i in range(1, N):
    check_num = do_sum(i)
    if check_num == N:
        num_list.append(i)
    else:
        continue
        
if len(num_list) == 0:
    print(0)
else:
    print(min(num_list))
    
   