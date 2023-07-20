while True:
    a = int(input())
    if a == -1:
        break
    
    tmp = []
    for i in range(1, a):
        if a % i == 0:
            tmp.append(i)
    
    if sum(tmp) == a:
        print(a, " = ", " + ".join(str(i) for i in tmp), sep="")
    else:
        print(f"{a} is NOT perfect.")