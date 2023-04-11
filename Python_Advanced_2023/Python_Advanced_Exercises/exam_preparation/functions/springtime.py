def start_spring(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[1]))
    my_dict = {}

    for i in sorted_result:
        if i[1] not in my_dict:
            my_dict[i[1]] = []
        my_dict[i[1]].append(i[0])
    result = ''


    for k,v in my_dict.items():
        result += f'{k}:\n'
        for i in sorted(my_dict[k]):
            result += f'-{i}\n'

    return result






example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))


