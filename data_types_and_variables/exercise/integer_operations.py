firs_number = int(input())
second_number = int(input())
third_number = int(input())
four_number = int(input())

sum_first_two = firs_number + second_number
result = int(sum_first_two / third_number)
final = int(result * four_number)
print(f'{final:.0f}')