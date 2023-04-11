from collections import deque

textiles = deque(int(x) for x in input().split(" "))
medicaments = [int(x) for x in input().split(" ")]


my_dictionary = {'Patch': 30, 'Bandage': 40, 'MedKit': 100}

created_healing_items_dict = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}


while textiles and medicaments:

    textile = textiles.popleft()
    medicament = medicaments.pop()

    created_healing_item = textile + medicament

    if created_healing_item == my_dictionary['Patch']:
        created_healing_items_dict['Patch'] +=1


    elif created_healing_item == my_dictionary['Bandage']:
        created_healing_items_dict['Bandage'] +=1



    elif created_healing_item == my_dictionary['MedKit']:
        created_healing_items_dict['MedKit'] +=1


    elif created_healing_item > my_dictionary['MedKit']:
        created_healing_items_dict['MedKit'] += 1
        left_sum = created_healing_item - my_dictionary['MedKit']

        medicament = medicaments.pop()
        medicament +=left_sum
        medicaments.append(medicament)
        continue

    else:
        medicament +=10

        continue

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")


sorted_dict = sorted(created_healing_items_dict.items(), key=lambda x: (-x[1], x[0]))

for i in sorted_dict:
    if i[1] > 0:
        print(f'{i[0]} - {i[1]}')


if medicaments:
    sorted_medicaments = sorted(medicaments, reverse=True)
    print(f"Medicaments left: {', '.join(str(x) for x in sorted_medicaments)}")

if textiles:

    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")

