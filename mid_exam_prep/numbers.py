numbers = [int(x) for x in input().split()]
length = len(numbers)
arr = []
suma = 0
for num in numbers:
    suma += num
    average = suma / length
    if num > average:
        arr.append(num)
    if len(arr) >= 5:
        break
    if len(arr) == 0:
        print('No')

print(" ".join(map(str, arr)))
print(average)
print(suma)
