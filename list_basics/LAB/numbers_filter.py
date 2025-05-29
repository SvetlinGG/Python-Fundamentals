num = int(input())
arr = []
newArr = []

for _ in range(num):
    number = int(input())

    arr.append(number)
operation = input()
for i in range(len(arr)):
    if operation == 'even' and arr[i] % 2 == 0:
        newArr.append(arr[i])
    elif operation == 'odd' and arr[i] % 2 != 0:
        newArr.append(arr[i])
    elif operation == 'negative' and arr[i] < 0:
        newArr.append(arr[i])
    elif operation == 'positive' and arr[i] >= 0:
        newArr.append(arr[i])
print(newArr)



