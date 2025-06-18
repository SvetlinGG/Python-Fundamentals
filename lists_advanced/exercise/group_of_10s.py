numbers = [ int(num) for num  in input().split(', ')]
arr_10 = []
arr_20 = []
arr_30 = []
arr_40 = []
arr_50 = []

for num in numbers:

    if num <= 10:
        arr_10.append(num)
    elif num <= 20:
        arr_20.append(num)
    elif num <= 30:
        arr_30.append(num)
    elif num <= 40:
        arr_40.append(num)
    else:
        arr_50.append(num)
print(f"Group of 's: {arr_10}")
print(f"Group of 's: {arr_20}")
print(f"Group of 's: {arr_30}")
print(f"Group of 's: {arr_40}")
print(f"Group of 's: {arr_50}")