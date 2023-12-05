from max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)

s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}')
print(f'{s}의 최댓값은 {max_of(s)}') # 문자 가운데 가장 큰 문자 코드인 t를 출력
print(f'{a}의 최댓값은 {max_of(a)}') # 사전 순으로 가장 큰 문자열인 FLAC을 출력