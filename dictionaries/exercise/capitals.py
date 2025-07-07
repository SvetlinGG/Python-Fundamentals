
countries = input().split(', ')
capitals = input().split(', ')
combined = { country: capital for country, capital in zip(countries, capitals)}

for country, capital in combined.items():
    print(f'{country} -> {capital}')