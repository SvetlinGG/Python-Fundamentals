rooms = int(input())
free_chairs = 0
needed_chairs = 0

for i in range(1, rooms + 1):
    chair_str, person_str = input().split()
    chairs = len(chair_str)
    people = int(person_str)

    if chairs >= people:
        free_chairs += chairs - people
    else:
        shortage = people - chairs
        needed_chairs += shortage
        print(f"{shortage} more chairs needed in room {i}")

if needed_chairs == 0:
    print(f"Game On, {free_chairs} free chairs left")


# rooms = int(input())
# total_chairs = 0
# free_chairs = 0
# total_person = 0
# needed_chairs = 0
#
#
# for i in range(1, rooms + 1):
#
#     chair, person = input().split()
#     total_chairs += len(chair)
#     total_person += int(person)
#     if total_chairs >= total_person:
#         free_chairs = total_chairs - total_person
#     else:
#         shortage = total_person - total_chairs
#         needed_chairs += shortage
#         print(f"{shortage} more chairs needed in room {i}")
#
# if needed_chairs == 0:
#     print(f"Game On, {free_chairs} free chairs left")



