from collections import deque

milligrams_of_coffeine = deque([int(x) for x in input().split(", ")])
numbers_of_energy_drinks = deque([int(x) for x in input().split(", ")])
initial_caffeine = 0
limit_per_day = 300
while milligrams_of_coffeine and numbers_of_energy_drinks:
    milligram = milligrams_of_coffeine.pop()
    energy_drink = numbers_of_energy_drinks.popleft()

    sum_of_caffeine = milligram * energy_drink

    if sum_of_caffeine <= limit_per_day:
        initial_caffeine += sum_of_caffeine
        limit_per_day -= sum_of_caffeine

    elif sum_of_caffeine > limit_per_day:
        numbers_of_energy_drinks.append(energy_drink)

        initial_caffeine -=30
        if initial_caffeine <0:
            initial_caffeine = 0
        limit_per_day +=30
        if limit_per_day > 300:
            limit_per_day = 300



if numbers_of_energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in numbers_of_energy_drinks)}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {initial_caffeine } mg caffeine.')




