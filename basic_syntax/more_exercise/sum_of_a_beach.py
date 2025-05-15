# text = input().lower()
#
# count = 0
# count += text.count("sand")
# count += text.count("water")
# count += text.count("fish")
# count += text.count("sun")
#
# print(count)

# budget = int(input())

total_price = 0
all_i_need = False
while True:
   command = input()
   if command == "End":
       all_i_need = True
       break
   total_price += int(command)
   if budget == total_price:
       all_i_need = True
       break

   if budget < total_price:
       print("You went in overdraft!")
       break

if all_i_need is True:
   print("You bought everything needed.")