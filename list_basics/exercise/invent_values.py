nums = input().split()
arr = []
for i in nums:
    num = int(i)
    num *= -1
    arr.append(num)
print(arr)