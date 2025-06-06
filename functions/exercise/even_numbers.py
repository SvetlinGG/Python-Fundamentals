numbers = input()
digits = [int(d) for d in numbers.split()]
def even_numbers(digits):

    arr = []
    for d in digits:
        if d % 2 == 0:
            arr.append(d)
    print(arr)
even_numbers(digits)

