initial_list = [ str(word) for word in input().split('!')]

for _ in initial_list:

    command, products = input().split()
    if command == 'Urgent':
        if products:
            continue
        initial_list[0] += products




    print(' '.join(initial_list))