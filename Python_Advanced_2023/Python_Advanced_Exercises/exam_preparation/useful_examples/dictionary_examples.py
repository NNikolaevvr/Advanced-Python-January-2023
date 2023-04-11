list_of_numbers = [float(x) for x in input().split(" ")]
count_numbers = []


dict = {key: list_of_numbers.count(key) for key in list_of_numbers}



for k, v in dict.items():
    print(f'{k} - {v} times')




from collections import  deque
crafted_toys = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}


toys = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}
materials = deque(int(x) for x in input().split())
magic_values = deque(int(x) for x in input().split())


while materials and magic_values:

    current_material = materials.pop()
    current_magic = magic_values.popleft()


    multiplication = current_material * current_magic

    if multiplication < 0:
        sum_values = current_material + current_magic
        materials.append(sum_values)

    elif multiplication >=0:
        if current_magic == 0 and current_material == 0:
            continue

        if multiplication == toys["Doll"]:
            crafted_toys["Doll"] += 1

        elif multiplication == toys["Wooden train"]:
            crafted_toys["Wooden train"] += 1

        elif multiplication == toys["Teddy bear"]:
            crafted_toys["Teddy bear"] += 1

        elif multiplication == toys["Bicycle"]:
            crafted_toys["Bicycle"] +=1

        elif current_material == 0:
            if current_magic >0:

                magic_values.appendleft(current_magic)

        elif current_magic == 0:
            if current_material> 0:

                materials.append(current_material)


        else:
            materials.append(current_material + 15)


if crafted_toys["Doll"] > 0 and crafted_toys["Wooden train"]> 0 or crafted_toys["Bicycle"]> 0 and crafted_toys["Teddy bear"]>0:

    print(f'The presents are crafted! Merry Christmas!')

else:
    print(f'No presents this Christmas!')



if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials][::-1])}')

if magic_values:
    print(f'Magic left: {", ".join(str(x) for x in magic_values)}')

for k,v in sorted(crafted_toys.items()):
    if v >0:
        print(f'{k}: {v}')







