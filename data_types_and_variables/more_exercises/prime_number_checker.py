prime_num = int(input())

if prime_num > 1 and all(prime_num % i != 0 for i in range(2, int(prime_num**0.5) + 1)):
    print('True')
else:
    print('False')
