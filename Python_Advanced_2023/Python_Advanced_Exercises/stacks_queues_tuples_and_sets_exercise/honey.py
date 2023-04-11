from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
all_nectar = 0
collected_nectar = 0

symbols = deque(x for x in input().split())

while working_bees and nectar:
    bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar > bee:
        if symbols[0] == "+":
            calculation = current_nectar + bee
            all_nectar += abs(calculation)
            symbols.popleft()

        elif symbols[0] == "-":
            calculation = bee - current_nectar
            all_nectar += abs(calculation)
            symbols.popleft()

        elif symbols[0] == "*":
            calculation = bee * current_nectar
            all_nectar += abs(calculation)
            symbols.popleft()

        elif symbols[0] == "/":
            calculation = bee / current_nectar
            all_nectar += abs(calculation)
            symbols.popleft()

    elif current_nectar < bee:
        collected_nectar += current_nectar
        working_bees.appendleft(bee)

print(f'Total honey made: {all_nectar}')

if working_bees:

    print(f'Bees left: {", ".join(str(x) for x in working_bees)}')

if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')
