
sequence_of_strings = input().split()
arr = []
for string in sequence_of_strings:
    result = string * len(string)
    arr.append(result)
print(''.join(arr))