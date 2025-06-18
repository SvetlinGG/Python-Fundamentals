rooms = int(input())
total_chairs = 0
free_chairs = 0
total_person = 0


for _ in range(rooms):

    chair, person = input().split(' ')
    total_chairs += len(chair)
    total_person += int(person)
    if total_chairs >= total_person:
        free_chairs = total_chairs - total_person
print(f'Game On, {free_chairs} free chairs left')


