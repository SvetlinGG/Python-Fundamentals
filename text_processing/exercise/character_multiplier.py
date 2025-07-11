
words = input().split()
total_word_1 = [ord(first) for first in words[0]]
total_word_2 = [ord(second) for second in words[1]]
sum_one = 1
sum_two = 1
if len(total_word_1) > len(total_word_2):
    dif_one = len(total_word_1) - len(total_word_2)
    for one in total_word_1[:-dif_one]:
        sum_one *= one #+ total_word_1[-dif_one]
else:
    dif_two = len(total_word_2) - len(total_word_1)
    for two in total_word_2[:-dif_two]:
        sum_two *= two #+ total_word_2[-dif_two]
total = sum_one + sum_two
print(total)

# words = input().split()
# word1 = words[0]
# word2 = words[1]
#
# ascii_1 = [ord(ch) for ch in word1]
# ascii_2 = [ord(ch) for ch in word2]
#
# min_len = min(len(word1), len(word2))
# max_len = max(len(word1), len(word2))
#
# total = 0
# for i in range(min_len):
#     total += ascii_1[i] * ascii_2[i]
#
# if len(word1) > len(word2):
#     for i in range(min_len, max_len):
#         total += ascii_1[i]
# else:
#     for i in range(min_len, max_len):
#         total += ascii_2[i]
#
# print(total)

