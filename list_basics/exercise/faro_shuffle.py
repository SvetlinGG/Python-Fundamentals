letters = input().split()

length = len(letters) // 2
count = int(input())
first_half = letters[:length]
second_half = letters[length:]
arr = []
arr = zip(first_half, second_half)
print(*arr)
