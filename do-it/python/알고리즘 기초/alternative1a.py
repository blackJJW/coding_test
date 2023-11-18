# + 와 -를 번갈아 출력하기 1

print("+와 -를 번갈아 출력")

n = int(input("몇 개를 출력 : "))

'''
카운터 변수 i를 0에서 n-1까지 1씩 증가
만약 i를 1부터 n까지 1씩 증가시키고 싶다면 range() 함수로
전달하는 값과 for문의 print() 함수 호출 순서를 바꿔야 한다.
'''

for i in range(1, n + 1):
    if i % 2: # 홀수
        print('+', end='') 
        
    else: # 짝수
        print('-', end='')         
print()