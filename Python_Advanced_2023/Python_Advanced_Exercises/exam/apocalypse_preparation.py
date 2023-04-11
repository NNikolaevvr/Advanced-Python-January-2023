from collections import deque

textiles = deque(int(x) for x in input().split(" "))
medicaments = deque(int(x) for x in input().split(" "))

patch = 30
bandage = 40
medkit = 100

my_dict = {'Patch': 0, 'Bandage':0, 'MedKit':0}
sorted_dict = {}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    create_healing_item = textile + medicament

    if create_healing_item == patch:
        my_dict['Patch'] += 1

    elif create_healing_item == bandage:
        my_dict['Bandage'] += 1

    elif create_healing_item == medkit:
        my_dict['MedKit'] += 1


    elif create_healing_item > medkit:

        my_dict['MedKit'] += 1
        remaining_sum = create_healing_item - medkit

        medicament1 = medicaments.pop()
        medicament1 += remaining_sum
        medicaments.append(medicament1)

    else:
        medicament += 10
        medicaments.append(medicament)



if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

else:
    if not textiles:
        print(f'Textiles are empty.')

    if not medicaments:
        print(f'Medicaments are empty.')

sorted_dict = sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))
for k, v in sorted_dict:
    if v > 0:
        print(f'{k} - {v}')


if medicaments:
    sorted_medicaments = reversed(medicaments)
    print(f"Medicaments left: {', '.join(str(x) for x in sorted_medicaments)}")

if textiles:

    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")

