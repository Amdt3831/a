import re


similar_factor = int(input())
favorite_sentence = input().split(' ')
favorite_sentence[-1] = favorite_sentence[-1][0:-1]
supposed_word = input()
a = 0
for item in favorite_sentence:
    r = supposed_word
    if len(item)<len(supposed_word):
        s = item
        item += (len(supposed_word)-len(item))*'_'
    if len(item)>len(supposed_word):
        r += (len(item)-len(supposed_word))*'_'
    for j in range(len(r)):
        if r[j] != item[j]:
            a += 1
    if a <= similar_factor:
        print(*re.findall(r'[آ-ی]+', item))
    a = 0



