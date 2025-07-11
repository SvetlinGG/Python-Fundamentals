
words = input().split()
sum = words[0] + words[1]
total_word_1 = [ord(first) for first in words[0]]
total_word_2 = [ord(second) for second in words[1]]
if len(total_word_1) > len(total_word_2):
    pass
else:
    pass
print(total_word_1[0] * total_word_2[0])