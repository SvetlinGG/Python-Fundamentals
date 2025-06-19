array_elements = [int(num) for num in input().split(' ')]

while True:
    command, ind_1, ind_2 = input().split(' ')
    if command == 'end':
        break
    print(command)
    print(ind_1)