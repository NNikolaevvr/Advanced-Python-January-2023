number_of_cars = int(input())
stored_cars = set()
for i in range(number_of_cars):
    command, key_number = input().split(", ")

    if command == "IN":
        stored_cars.add(key_number)

    elif command== 'OUT':
        stored_cars.remove(key_number)

if stored_cars:
        print(*stored_cars, sep="\n")

if not stored_cars:

    print('Parking Lot is Empty')


