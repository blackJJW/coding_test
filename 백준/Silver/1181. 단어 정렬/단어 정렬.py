N = int(input())

word_list = []
for i in range(N):
    tmp = input()
    word_list.append(tmp)

word_list = list(set(word_list))

sort_word = []
for j in word_list:
    sort_word.append((len(j), j))

sort_word.sort()

for l, w in sort_word:
    print(w)

    