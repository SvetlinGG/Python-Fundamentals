key = int(input())
letter = int(input())
sum = []

for char in range(letter):

        char = ord(input())
        sum.append(chr(char + key))
print(''.join(sum))




