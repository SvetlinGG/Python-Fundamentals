number_of_lines = int(input())
capacity = 255
fill = 0

for _ in range(number_of_lines):
    liters = int(input())

    if liters <= capacity:
        fill += liters

print("Insufficient capacity!")
print(f'{fill}')


