list_of_numbers = [float(x) for x in input().split(" ")]
count_numbers = []


dict = {key: list_of_numbers.count(key) for key in list_of_numbers}



for k, v in dict.items():
    print(f'{k} - {v} times')