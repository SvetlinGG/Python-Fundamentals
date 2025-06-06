number = input()
digits = [int(d) for d in str(number)]

def sum_odd_and_even(number):

    even_sum = 0
    odd_sum = 0
    for digit in digits:
        if digit % 2 ==0:
            even_sum += digit
        else:
            odd_sum += digit
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')
sum_odd_and_even(number)