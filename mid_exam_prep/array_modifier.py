array_elements = [int(num) for num in input().split(' ')]

while True:
    parts = input().split()
    command = parts[0]

    if command == 'end':
        break
    print(command)
