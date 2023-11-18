# 세 정수를 입력받아 최댓값 구하기

print("세 정수의 최댓값을 구한다.")


# input 함수는 문자열을 반환
# 문자열을 10진수 정수형으로 변환
a = int(input("정수 a의 값을 입력 : "))
b = int(input("정수 b의 값을 입력 : "))
c = int(input("정수 c의 값을 입력 : "))

'''
다음 3줄은 순차적으로 실행
이렇게 한 문장씩 순서대로 처리되는 구조를 순차 구조(sequential structure)

조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경되는데
이러한 구조를 선택 구조(select structure)라고 한다.

'''
maximum = a # maximum에 a값을 대입
if b > maximum: maximum = b # b의 값이 maximum보다 크면, maximum에 b의 값을 대입
if c > maximum: maximum = c # c의 값이 maximum보다 크면, maximum에 c의 값을 대입

print(f"최댓값 : {maximum}")