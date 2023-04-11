def even_odd_filter(**kwargs):

    for key, values in kwargs.items():

        if key == "even":
            kwargs[key] = [num for num in values if num % 2 == 0]

        elif key == "odd":
            kwargs[key] = [num for num in values if num % 2 != 0]

    sorted_tuple = sorted(kwargs.items(), key=lambda x: -len(x[1]))
    sorted_dict = {item[0]: item[1] for item in sorted_tuple}

    return sorted_dict