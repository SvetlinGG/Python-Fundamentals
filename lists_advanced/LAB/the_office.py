employees = input().split(' ')
happiness_factor = int(input())
int_employees = map(int, employees)
mapping = map(lambda x: x * happiness_factor, int_employees)
arr = []
sum = 0
for i in mapping:
    arr.append(i)
for happy in arr:
    sum += happy
    average = sum / len(arr)

    if happy >= average:
        newArr = []
        newArr.append(happy)
    print(f'Score: {newArr}/{len(arr)}. Employees are not happy!"')


