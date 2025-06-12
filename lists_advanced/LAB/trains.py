train_wagons = int(input())
train = [0] * train_wagons
arr = []

while True:
    command = input()
    if command == 'End':
        break
    for operation in arr:
        arr.append(command)
        operation = operation.split(' ')
        if operation[0] == 'add':
            train[-1] = int(operation[1])
        if operation[0] == 'insert':
            train.pop(int(operation[1]))
            train.insert(int(operation[1]), int(operation[2]))
print(train)


