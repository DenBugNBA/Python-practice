from itertools import permutations

word = input()
word_list = list(permutations(list(word)))
word_list.sort()
word_set = set(word_list)
word_list = list(word_set)
word_list.sort()

words = []
for i in word_list:
    words.append("".join(list(i)))

print(words.index(word) + 1)
