
command = input()
result = []

while command != 'End':

    pos, task = command.split('-')
    result.append([int(pos), task])
    command = input()
print([do[1] for do in sorted(result, key=lambda x: x[0])])








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







