numbers = [int(x) for x in input().split()]
average = sum(numbers) / len(numbers)
arr = []
sorted_arr = []
for num in numbers:

    if num > average:
        arr.append(num)
        sorted_arr = sorted(arr)
        if len(sorted_arr) > 4:
            break

if len(arr) == 0:
    print('No')

print(" ".join(map(str, sorted_arr[::-1])))


