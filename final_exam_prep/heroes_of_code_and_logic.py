
heroes_count = int(input())

for _ in range(heroes_count):
    hero_name, hit_point, mana_point = input().split(' ')
    hit_point = int(hit_point)
    mana_point = int(mana_point)
    print(f'{hero_name} {hit_point} {mana_point}')