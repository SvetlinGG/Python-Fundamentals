train_wagons = int(input())
train = [0] * train_wagons
arr = []
command = input()
for operation in command:
        operation = operation.split(' ')
        print(operation)
        if operation[0] == 'add':
            train[-1] = int(operation[1])
        if operation[0] == 'insert':
            train.pop(int(operation[1]))
            train.insert(int(operation[1]), int(operation[2]))
print(train)



