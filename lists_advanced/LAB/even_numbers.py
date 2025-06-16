main_list = [int(n) for n in input().split(", ")]
even_list = list()

for n, index in enumerate(main_list):
    if index % 2 == 0:
        even_list.append(n)

print(even_list)

# numbers = input().split(', ')
# arr = []
# for number in numbers:
#
#     if int(number) % 2 == 0:
#         index = numbers.index(number)
#         arr.append(index)
# print(arr)