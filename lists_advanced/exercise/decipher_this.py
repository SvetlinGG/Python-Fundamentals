
message = input().split()

words = []
for word in message:
    num, let = "", ""
    for symbol in word:
        if symbol.isdigit():
            num += symbol
        else:
            let += symbol
    if len(let) != 1:
        let = f"{let[-1]}{let[1:-1]}{let[0]}"
    words.append(f"{chr(int(num))}{let}")

print(*words, end=' ')

