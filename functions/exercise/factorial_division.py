import math

number_one = int(input())
number_two = int(input())


def factorial_division(one, two):
    one = math.factorial(one)
    two = math.factorial(two)
    return f"{(one / two):.2f}"


print(factorial_division(number_one, number_two))

# number_one = int(input())
# number_two = int(input())
#
# def fibonacci(num_one: int, num_two: int):
#     sum = 1
#     for i in range(num_one, 0, -1):
#         sum *= i
#     total = sum / num_two
#     print(f'{total:.2f}')
#
#
# fibonacci(number_one, number_two)