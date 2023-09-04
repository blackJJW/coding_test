num_list = []

for i in range(5):
    tmp = int(input())
    num_list.append(tmp)
    
sum_list = sum(num_list)
num_mean = int(sum_list / 5)

sorted_list = sorted(num_list)
n = len(sorted_list)
median = (sorted_list[n//2] + sorted_list[n//2 - 1]) / 2  if n%2==0 else sorted_list[n//2]

print(num_mean)
print(median)