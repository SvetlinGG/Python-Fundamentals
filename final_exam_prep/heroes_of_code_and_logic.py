
heroes_count = int(input())
heroes = {}

for _ in range(heroes_count):
    hero_name, hit_point, mana_point = input().split(' ')
    heroes[hero_name] = {'HP': int(hit_point), 'MP': int(mana_point)}

command = input()
while command != 'End':

    operation = command.split(' - ')
    command_type = operation[0]
    hero_name = operation[1]

    if command_type == 'Heal':
        amount = int(operation[2])
        current_hp = heroes[hero_name]['HP']
        heal_amount = min(100 - current_hp, amount)
        heroes[hero_name]['HP'] += heal_amount
        print(f'{hero_name} healed for {heal_amount} HP!')

    elif command_type == 'Recharge':
        amount = int(operation[2])
        current_mp = heroes[hero_name]['MP']
        heal_amount = min(200 - current_mp, amount)
        heroes[hero_name]['MP'] += heal_amount
        print(f'{hero_name} recharged for {heal_amount} MP!')
    elif command_type == 'TakeDamage':
        damage = int(operation[2])
        attacker = operation[3]
        current_hp = heroes[hero_name]['HP']
        current_hp -= damage
        if heroes[hero_name]['HP'] > 0:
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!')
        else:
            print(f'{hero_name} has been killed by {attacker}!')
    elif command_type == 'CastSpell':
        mp_needed = int(operation[2])
        spell_name = operation[3]
        current_mp = heroes[hero_name]['MP']
        if current_mp > mp_needed:
            mana_points_left = current_mp - mp_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {mana_points_left} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    command = input()
for hero, stats in heroes.items():
    print(f'{hero}')
    print(f'  HP: {stats["HP"]}')
    print(f'  MP: {stats["MP"]}')





