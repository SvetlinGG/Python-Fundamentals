
count_electrons = int(input())
n = 1
result = []

while count_electrons > 0:
    capacity = 2 * n ** 2
    electrons = min(count_electrons, capacity)
    result.append(electrons)
    count_electrons -= electrons
    n += 1

print(result)

# count_electrons = int(input())
# electron_list = [1, 2, 3, 4]
# electron_distribution = 0
# arr = []
# newArr = []
# total = 0
# for num in electron_list:
#     electron_distribution = 2 * (num ** 2)
#     if electron_distribution > 18:
#         electron_distribution = num ** 2
#
#     arr.append(electron_distribution)
#
# for suma  in arr:
#     total += suma
#     newArr.append(suma)
#     if total == count_electrons:
#         break
#
#
# print(newArr)





