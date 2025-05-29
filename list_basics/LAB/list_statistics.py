digit = int(input())

positive = []
negative = []
sum = 0
for _ in range(digit):
    current_num = int(input())
    if current_num >= 0:
        positive.append(current_num)
    elif current_num < 0:
        negative.append(current_num)
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
for num in negative:
    sum += num
print(f'Sum of negatives: {sum}')

