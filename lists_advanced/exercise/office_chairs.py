rooms = int(input())
positive = 0
negative = 0

for _ in range(rooms):
    info = input().split(' ')
    for chair, person in enumerate(info):
        if chair > int(person):
            positive += 1
print(positive)

