number_list = [int(n) for n in input().split(", ")]

for n in range(1, 11):
    check_list = list()
    if len(number_list) != 0:
        [check_list.append(i) for i in number_list if i <= (n * 10)]
        [number_list.remove(o) for o in check_list]
        print(f"Group of {n * 10}'s: {check_list}")

# numbers = [ int(num) for num  in input().split(', ')]
# arr_10 = []
# arr_20 = []
# arr_30 = []
# arr_40 = []
# arr_50 = []
#
# for num in numbers:
#
#     if num <= 10:
#         arr_10.append(num)
#     elif num <= 20:
#         arr_20.append(num)
#     elif num <= 30:
#         arr_30.append(num)
#     elif num <= 40:
#         arr_40.append(num)
#     elif num <= 50:
#         arr_50.append(num)
#
# print(f"Group of {1 * 10}'s: {arr_10}")
# print(f"Group of {2 * 10}'s: {arr_20}")
# print(f"Group of {3 * 10}'s: {arr_30}")
# print(f"Group of {4 * 10}'s: {arr_40}")
# print(f"Group of {5 * 10}'s: {arr_50}")