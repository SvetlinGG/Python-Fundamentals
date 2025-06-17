prime_energy = int(input())

count_energy = 0

for _ in range(prime_energy):

    distance = int(input())

    if distance:
        prime_energy -= distance
        if prime_energy > distance:
            count_energy += distance
    