box_of_clothes = [int(x) for x in (input()).split(" ")]
rack = 1
capacity_of_rack = int(input())
current_rack_space = capacity_of_rack
while box_of_clothes:

    cloth = box_of_clothes.pop()

    if current_rack_space - cloth >= 0:

        current_rack_space -= cloth
    else:
        rack += 1
        current_rack_space = capacity_of_rack - cloth

print(rack)
