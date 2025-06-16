employees = input().split(' ')
happiness_factor = int(input())


arr = [int(e) * happiness_factor for e in employees]


average = sum(arr) / len(arr)


newArr = [e for e in arr if e >= average]


if len(newArr) >= len(arr) / 2:
    print(f"Score: {len(newArr)}/{len(arr)}. Employees are happy!")
else:
    print(f"Score: {len(newArr)}/{len(arr)}. Employees are not happy!")



