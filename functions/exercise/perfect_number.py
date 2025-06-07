num = int(input())
current_num = num -1

def perfect_number(num):

    arr = []
    count = 0
    for i in range(1, num):
        #print(i)
        if num % i == 0:
            arr.append(i)

    if sum(arr) == num:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")
perfect_number(num)

