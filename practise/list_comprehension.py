nums = [1, 2, 3, 4, 5]
result = [ num ** 2 for num in nums ]
print(result)
arr = []
total = [ num ** 3 for num in nums ]
total.insert(1, 25)
total.append(10)
total.pop(3)
print(total + result)
for num in total:
    if num % 2 == 0:
        arr.append(num)
print(arr)
