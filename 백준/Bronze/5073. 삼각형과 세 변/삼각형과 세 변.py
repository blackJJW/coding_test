while True:
    x, y, z = map(int, input().split())
    
    if x == 0 and y == 0 and z == 0:
        break
    else:
        if max(x, y, z) >= (x + y + z) - max(x, y, z):
            print("Invalid")
        else:
            if x == y == z:
                print("Equilateral")
            elif x == y or x == z or y == z:
                print("Isosceles")
            else:
                print("Scalene")
     