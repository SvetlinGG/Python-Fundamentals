command = input()
operation = input()


def data_types(com, operat):

    if com == 'int':
        num = int(operat)
        result = num * 2
    elif com == 'real':
        real_num = float(operat)
        result = f'{(real_num * 1.5):.2f}'
    elif com == 'string':

        result = f'${operat}$'

    print(result)
data_types(command, operation)
