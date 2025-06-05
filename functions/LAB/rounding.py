
numbers = input().split(', ')

def rounding(numbers):

    arr = []
    for num in numbers:
        num = int(num)
        arr.append(num).map(round(num, 2))



    return print(arr)

rounding(numbers)