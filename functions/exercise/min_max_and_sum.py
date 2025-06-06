numbers = input()
digits = [int(d) for d in numbers.split()]

def min_max(digits):

    arr = sorted(digits)
    print(f'The minimum number is {arr[0]}')
    print(f'The maximum number is {arr[-1]}')
    print(f'The sum number is: {sum(arr)}')

min_max(digits)