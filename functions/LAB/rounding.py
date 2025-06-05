
numbers = input().split()

def rounding(numbers):

    rounded = [round(float(n)) for n in numbers]
    return print(f'{rounded}')

rounding(numbers)