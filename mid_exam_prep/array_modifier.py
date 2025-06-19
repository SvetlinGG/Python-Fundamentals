array_elements = [int(num) for num in input().split()]

while True:
    parts = input().split()
    command = parts[0]

    if command == 'end':
        break
    if command == 'swap':
        array_elements[int(parts[1])], array_elements[int(parts[2])] = array_elements[int(parts[2])], array_elements[int(parts[1])]
    elif command == 'multiply':
        multiplication = array_elements[int(parts[1])] * array_elements[int(parts[2])]
        array_elements[int(parts[1])] = multiplication
    elif command == 'decrease':
        for i in range(len(array_elements)):
            array_elements[i] -= 1

print(", ".join(map(str, array_elements)))