def forecast(*args):
  sunny_locations = []
  cloudy_locations = []
  rainy_locations = []

  for (location, weather) in args:
    if weather == 'Sunny':
      sunny_locations.append(location)
    elif weather == 'Cloudy':
      cloudy_locations.append(location)
    elif weather == 'Rainy':
      rainy_locations.append(location)

  sunny_locations.sort()
  cloudy_locations.sort()
  rainy_locations.sort()

  output = ''
  for location in sunny_locations:
    output += f'{location} - Sunny\n'
  for location in cloudy_locations:
    output += f'{location} - Cloudy\n'
  for location in rainy_locations:
    output += f'{location} - Rainy\n'

  return output

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
