budget = float(input())
price_kg_flour = float(input())

price_pack_eggs = price_kg_flour * 0.75
price_litter_milk = price_kg_flour * 1.25

eggs_needed = 1
milk_needed = price_litter_milk * 0.25

bread = price_kg_flour + eggs_needed * price_pack_eggs + milk_needed
breads = 0
colored_eggs = 0


# 0.25 L milk for bread
while budget >= bread:

    budget -= bread
    breads += 1
    colored_eggs += 3

    if  breads % 3 == 0:
        colored_eggs -= breads - 2
print(f'You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')



