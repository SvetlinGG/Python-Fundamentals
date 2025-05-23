number_of_lines = int(input())
result = 0

for _ in range(number_of_lines):
    line = input()
    result += ord(line)
print(f'The sum equals: {result}')