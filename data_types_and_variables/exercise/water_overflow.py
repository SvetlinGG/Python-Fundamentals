number_of_lines = int(input())
capacity = 255
fill = 0

for _ in range(number_of_lines):
    liters = int(input())

    if capacity - liters >= 0:
        capacity -= liters
        fill += liters

    else:
        print("Insufficient capacity!")
        print(f'{fill}')


