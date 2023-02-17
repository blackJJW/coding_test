import math

A, B, V = map(int, input().split())

cal = A - B
result = (V - B) / cal

print(math.ceil(result))