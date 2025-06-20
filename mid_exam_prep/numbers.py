numbers = [int(x) for x in input().split(' ')]
average = sum(numbers) / len(numbers)

above_average = [num for num in numbers if num > average]

if not above_average:
    print('No')
else:
    top_5 = sorted(above_average, reverse=True)[:5]
    print(" ".join(map(str, top_5)))




