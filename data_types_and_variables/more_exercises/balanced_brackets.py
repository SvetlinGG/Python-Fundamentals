lines = int(input())
sum = []

for _ in range(lines):
    char = input()
    if char == '(' and char == ')':
        print('BALANCED')
    else:
        print('UNBALANCED')