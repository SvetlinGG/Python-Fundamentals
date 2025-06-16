words_first_line = input().split(', ')
words_second_line = input().split(', ')
arr = []

for word_1 in words_first_line:
    for word_2 in words_second_line:
        if word_1 in word_2:
            arr.append(word_1)
            break
print(arr)