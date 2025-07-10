
usernames = input().split(', ')

for username in usernames:

    if 3 <= len(username) <= 16:
        for check in username:
            if not any([check.isdigit(), check.isalpha(), check =='-', check == '_']):
                break
        else:
            print(username)
