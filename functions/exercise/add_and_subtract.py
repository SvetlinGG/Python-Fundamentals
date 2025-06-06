

first_num = int(input())
second_num = int(input())
third_num = int(input())
def add_and_subtract(first_num, second_num, third_num):
    def add():

        sum = first_num + second_num
        return sum

    def subtract(sum_result):

        return sum_result - third_num
    result =  subtract(add())
    print(result)


add_and_subtract(first_num, second_num, third_num)
