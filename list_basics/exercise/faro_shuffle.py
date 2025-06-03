letters = input().split()
count = int(input())
length = len(letters)
mid = int(length / 2)

for i in range(count):
    arr = []
    for p in range(0, mid):
        arr.append(letters[p])
        arr.append(letters[mid])
        mid += 1
    letters = arr
    mid = int(length / 2)
print(arr)
