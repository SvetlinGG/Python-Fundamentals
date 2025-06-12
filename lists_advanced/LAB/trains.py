train_wagons = int(input())
train = [0, 0, 0]
arr = []

for _ in range(train_wagons):
    command = input()
    arr.append(command)
for operation in arr:
    operation = operation.split(' ')
    if operation[0] == 'add':
        train.append(operation[1])
print(train)


