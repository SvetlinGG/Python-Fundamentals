def add_stops(stops_string: str, some_index: int, some_sub_string: str):
    if some_index in range(len(stops_string)):
        stops_string = stops_string[:some_index] + some_sub_string +  some_sub_string[index:]
    return stops_string

def remove_stop(stops_string: str, some_start_index: int, some_end_index: int):
    if some_start_index in range(len(stops_string)) and some_end_index in range(len(stops_string)):
        pass
    return stops_string


stops = [input()]
command  = input().split(':')

while command[0] != 'Travel':

    command = input().split(':')
    if command[0] == 'Add Stop':
        index, sub_string = int(command[1]), command[2]
        stops = add_stops(stops, index, sub_string)
    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        stops = remove_stop(stops, start_index, end_index)
    elif command[0] == 'Switch':
        pass
    command = input().split(':')

