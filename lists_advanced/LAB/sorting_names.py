names = input().split(', ')
names.sort(key = len, reverse=True)
print(names)


# names = input().split(', ')
# sorted_names = sorted(names, key=lambda name: (-len(name), name))
# print(sorted_names)