prime_num = int(input())

if prime_num > 1 and prime_num % prime_num == 0 and prime_num % 1 == 0 and prime_num < 10 and prime_num % 2 != 0:
    print('True')
else:
    print('False')