start_year = int(input())
end_year = start_year + 1000
new_year = []
for dig in range(start_year, end_year + 1):
    uniq_digit1 = int(str(dig)[0])
    uniq_digit2 = int(str(dig)[1])
    uniq_digit3 = int(str(dig)[2])
    uniq_digit4 = int(str(dig)[3])
    if uniq_digit1 != uniq_digit2 and uniq_digit1 != uniq_digit3 and uniq_digit1 != uniq_digit4:
        new_year.append(uniq_digit1)
    if uniq_digit2 != uniq_digit1 and uniq_digit2 != uniq_digit3 and uniq_digit2 != uniq_digit4:
        new_year.append(uniq_digit2)
    if uniq_digit3 != uniq_digit2 and uniq_digit3 != uniq_digit1 and uniq_digit3 != uniq_digit4:
        new_year.append(uniq_digit3)
    if uniq_digit4 != uniq_digit1 and uniq_digit4 != uniq_digit2 and uniq_digit4 != uniq_digit3:
        new_year.append(uniq_digit4)
    print(new_year)
