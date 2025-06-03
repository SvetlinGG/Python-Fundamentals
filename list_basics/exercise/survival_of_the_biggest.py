integers = input().split()
num = int(input())
arr = []
for n in integers:

    numbers = int(n)
    arr.append(numbers)
arr.sort(reverse=True)
arr.remove(num)
print(arr)