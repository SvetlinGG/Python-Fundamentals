num = int(input())

for i in range(0, num):
    for j in range(0, num):
        for k in range(0, num):
            print(chr(num + i) + chr(num + j) + chr(num + k))