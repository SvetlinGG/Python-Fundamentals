
words = input().split()
sum = words[0] + words[1]
total_word_1 = 0
total_word_2 = 0
total_sum = 0

for word_1 in words[0]:
    total_word_1 += ord(word_1)

for word_2 in words[1]:
    total_word_2 += ord(word_2)
total_sum = total_word_1 + total_word_2
print(total_sum)