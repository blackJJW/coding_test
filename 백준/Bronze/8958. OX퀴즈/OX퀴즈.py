cnt = int(input())
input_list = []
score_list = []

for i in range(cnt):
    input_obj = input()
    input_list.append(input_obj)

for i in range(len(input_list)):
    tmp = 0
    score = 0
    for j in range(len(input_list[i])):
        if input_list[i][j] == 'O':
            tmp += 1
            score += tmp
        else:
            tmp = 0
    score_list.append(score)

for i in score_list:
    print(i)
        