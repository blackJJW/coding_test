cnt = int(input())
score = input().split()
new_score_list = []

for i in range(cnt):
    score[i] = int(score[i])

max_score = max(score)

for i in score:
    new_score_list.append((i / max_score) * 100)

print(sum(new_score_list) / cnt)