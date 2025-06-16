

numbers = input().split(', ')
arr = []
for number in numbers:

    if int(number) % 2 == 0:
        index = numbers.index(number)
        arr.append(index)
print(arr)