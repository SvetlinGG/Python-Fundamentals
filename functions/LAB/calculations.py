operations = input()
a = int(input())
b = int(input())

def calculation(operation, a, b):
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result =  a - b
    elif operation == 'multiply':
        result =  a * b
    elif operation == 'divide':
        result =  a / b

    return int(result)
print(calculation(operations, a, b))
