
notes = [0]


for _ in notes:

    command = input().split('-')

    for num, token in enumerate(command):
        filtered = list(filter(lambda num: num == num, command))
        print(' '.join(filtered))




# notes = [0] * 10
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     tokens = command.split('-')
#     priority = int(tokens[0]) - 1
#     note = tokens[1]
#     notes.pop(priority)
#     notes.insert(priority, note)
# result = [element for element in notes if element != 0]
# print(result)







