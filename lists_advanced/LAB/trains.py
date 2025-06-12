train_wagons = int(input())
train = [0, 0, 0]
arr = []

for _ in range(train_wagons):
    command = input()
    arr.append(command)
for operation in arr:
    operation = operation.split(' ')
    if operation[0] == 'add':
        train[-1] = int(operation[1])
    if operation[0] == 'insert':
        train.pop(int(operation[1]))
        train.insert(int(operation[1]), int(operation[2]))
print(train)


