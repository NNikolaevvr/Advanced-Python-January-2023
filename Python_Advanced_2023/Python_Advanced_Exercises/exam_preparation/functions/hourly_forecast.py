# def forecast(*args):
#     locations = {}
#     for el in args:
#         if el[0] not in locations:
#             locations[el[0]] = el[1]
#     sorted_result = {k: v for k,v in sorted(locations.items(), key=lambda x: (x[0]))}
#     sunny = ''
#     cloudy = ''
#     rainy = ''
#     for key, value in sorted_result.items():
#         if value == 'Sunny':
#             sunny += f'{key} - {value}\n'
#         elif value == 'Cloudy':
#             cloudy += f'{key} - {value}\n'
#         elif value == 'Rainy':
#             rainy += f'{key} - {value}\n'
#
#     return sunny + cloudy + rainy
#
#
# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

def forecast(*args):
    sunny_locations = []
    cloudy_locations = []
    rainy_locations = []

    for location, weather in args:
        if weather == "Sunny":
            sunny_locations.append(location)
        elif weather == "Cloudy":
            cloudy_locations.append(location)
        elif weather == "Rainy":
            rainy_locations.append(location)

    sunny_locations = sorted(sunny_locations)
    cloudy_locations = sorted(cloudy_locations)
    rainy_locations = sorted(rainy_locations)

    result = []
    for location in sunny_locations:
        result.append(f"{location} - Sunny")
    for location in cloudy_locations:
        result.append(f"{location} - Cloudy")
    for location in rainy_locations:
        result.append(f"{location} - Rainy")

    return "\n".join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
