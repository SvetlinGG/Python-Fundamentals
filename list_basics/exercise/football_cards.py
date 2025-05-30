game = input().split()

team_a = 11
team_b = 11

for title in game:
    letter,number = title.split('-')
    if letter == 'A':
        team_a -= 1
    elif letter == 'B':
        team_b -= 1
print(f'Team A - {team_a}; Team B - {team_b}')
if team_a < 7 or team_b < 7:
    print('Game was terminated')