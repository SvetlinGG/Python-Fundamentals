lines = int(input())
sum = []

for _ in range(1, lines + 1):
    char = input()
    if '(' in char or ')' in char:
        sum.append(char)

if '(' in sum and ')' in sum:
    print('BALANCED')
elif '(' in sum:
    print('UNBALANCED')
