numbers = input().split()
arr = []

for i in numbers:
    num = float(i)
    arr.append(abs(num))
print(arr)