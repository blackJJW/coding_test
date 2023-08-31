def do_sum(n):
    return n + sum(map(int, str(n)))

N = int(input())
len_N = len(str(N))
num_list = []

for i in range(max(1, N - 9 * len_N), N):
    check_num = do_sum(i)
    if check_num == N:
        num_list.append(i)

if num_list:
    print(min(num_list))
else:
    print(0)
    
   