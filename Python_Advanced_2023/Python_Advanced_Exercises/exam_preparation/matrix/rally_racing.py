size_of_the_matrix = int(input())
car_number = input()
matrix = []
car_coordinates = [0,0]
kilometers = 0
for i in range(size_of_the_matrix):
    matrix.append(input().split(" "))

while True:
    command = input()

    if command == 'End':
        matrix[car_coordinates[0]] [car_coordinates[1]] = "C"
        print(f'Racing car {car_number} DNF.')
        break

    elif command == 'up':
        car_coordinates[0] -= 1

    elif command == 'down':
        car_coordinates[0] += 1

    elif command == 'right':
        car_coordinates[1] +=1

    elif command == 'left':
        car_coordinates[1] -= 1

    if matrix[car_coordinates[0]][car_coordinates[1]] == "F":
        kilometers +=10
        matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
        print(f"Racing car {car_number} finished the stage!")
        break

    elif matrix[car_coordinates[0]][car_coordinates[1]] == "T":
        kilometers += 30
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == "T":
                    matrix[row][col] = "."
                    car_coordinates[0], car_coordinates[1] = row, col


    else:
        kilometers += 10


print(f"Distance covered {kilometers} km.")
for row in range(len(matrix)):
    print("".join(matrix[row]))













