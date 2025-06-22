import math

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
single_apron_price = float(input())

total_flour_price = flour_price * students
total_price = (single_apron_price * math.ceil(students * 1.2)) + ( egg_price * 10 * students ) + total_flour_price
if students >=5:
    total_flour_price = flour_price * ( students - ( students / 5))

    total_price = (single_apron_price * math.ceil(students * 1.2)) + ( egg_price * 10 * students ) + total_flour_price


if total_price <= budget:
    print(f'Items purchased for {total_price:.2f}$.')
else:
    needed_money = total_price - budget
    print(f'{needed_money:.2f}$ more needed.')

# import math
#
# budget = float(input())
# students = int(input())
# price_flour = float(input())
# price_egg = float(input())
# price_apron = float(input())
# 
# # Изчисляване на броя безплатни брашна
# free_flour = students // 5
#
# # Общо брашна за плащане
# flour_total = (students - free_flour) * price_flour
#
# # Общо яйца
# egg_total = students * 10 * price_egg
#
# # Престилки с 20% повече, закръглено нагоре
# apron_total = math.ceil(students * 1.2) * price_apron
#
# # Крайна сума
# total_price = flour_total + egg_total + apron_total
#
# # Проверка спрямо бюджета
# if total_price <= budget:
#     print(f"Items purchased for {total_price:.2f}$.")
# else:
#     needed = total_price - budget
#     print(f"{needed:.2f}$ more needed.")
