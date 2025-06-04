integers = input().split()
count = int(input())
current_count = 0
arr = []
newArr = []
for n in integers:
    numbers = int(n)
    arr.append(numbers)
for i in arr:
    if arr[i] < arr[i+1]:
        current_count += 1
        arr.pop(i)
        if current_count == count:
            break
print(arr)



