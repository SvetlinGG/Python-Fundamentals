num = int(input())
factor = int(input())
arr = []

for i in range(num, (num*factor) + 1, num):
    arr.append(i)
print(arr)