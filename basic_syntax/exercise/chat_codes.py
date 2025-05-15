number_of_messages = int(input())

for _ in range(number_of_messages):

    message = int(input())

    if message == 88:
        print('Hello')
    if message == 86:
        print('How are you?')
    if message != 88 and message != 86 and message < 88 :
        print('GREAT!')
    if message > 88:
        print('Bye.')


