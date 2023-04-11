def get_info(**kwargs):
    info = []
    dictionary = kwargs
    for k, v in dictionary.items():

        key = k
        info.append(v)


    result = f'This is {info[0]} from {info[1]} and he is {info[2]} years old'

    return result







print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))