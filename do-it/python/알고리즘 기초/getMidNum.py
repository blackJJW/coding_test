# 세 정수를 입력받아 중앙값 구하기 1

def med3(a, b, c):
    # a, b, c의 중앙값을 구하여 반환
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
        
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b
    
print("세 정수의 중앙값을 구한다.")
a = int(input("정수 a의 값을 입력 : "))
b = int(input("정수 b의 값을 입력 : "))
c = int(input("정수 c의 값을 입력 : "))

print(f"중앙값 : {med3(a, b, c)}")