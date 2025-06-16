nums = [int(num) for num in input().split(', ')]

positive = []
negative = []
even = []
odd = []
for num in nums:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print('Positive: '+", ".join(str(digit) for digit in positive))
print('Negative: '+", ".join(str(digit) for digit in negative))
print('Even: '+", ".join(str(digit) for digit in even))
print('Odd: '+", ".join(str(digit) for digit in odd))