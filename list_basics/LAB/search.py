num = int(input())
word = input()
arr = []
newArr = []

for _ in range(num):
    sentence = input()
    arr.append(sentence)
    if word in sentence:
        newArr.append(sentence)
print(arr)
print(newArr)

