
num = int(input())

letter_lower = 97

for i in range(letter_lower, letter_lower + num):
    for j in range(letter_lower, letter_lower + num):
        for k in range(letter_lower, letter_lower + num):
            print(f'{chr(i)}{chr(j)}{chr(k)}')


