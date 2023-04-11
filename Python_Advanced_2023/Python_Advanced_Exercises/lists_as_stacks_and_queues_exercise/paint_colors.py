from collections import deque

main_colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {"purple": {'red', 'blue'}, "orange":{"red", "yellow"}, "green":{"yellow", "blue"}}
found_colors = []
color = deque(input().split())

while color:
    first_character = color.popleft()

    last_character = color.pop() if color else ""




    for i in (first_character + last_character, last_character + first_character):
        if i in main_colors:
            found_colors.append(i)
            break



    else:


        for el in (first_character[:-1], last_character[:-1]):
            if el :
                color.insert(len(color) // 2, el)


for k in set(secondary_colors.keys()).intersection(found_colors):
    if not secondary_colors[k].issubset(found_colors):
        found_colors.remove(k)

print(found_colors)