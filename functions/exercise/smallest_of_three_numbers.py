num_a = int(input())
num_b = int(input())
num_c = int(input())

def numbers(num_a, num_b, num_c):

    result = 0
    if num_a < num_b and num_a < num_c:
        result += num_a
    elif num_b < num_c and num_b < num_a:
        result += num_b
    elif num_c < num_a and num_c < num_b:
        result += num_c

    return print(result)
numbers(num_a, num_b, num_c)