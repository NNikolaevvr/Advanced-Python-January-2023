first_player, second_player = input().split(", ")
first_player_needs_rest = False
second_player_needs_rest = False


matrix = []

for i in range(6):
    raw_data = [x for x in input().split()]

    matrix.append(raw_data)


while True:
    coordinates = input()
    row = int(coordinates[1])
    col = int(coordinates[4])

    position = matrix[row][col]
    if not first_player_needs_rest:

        if position == 'E':
            print(f"{first_player} found the Exit and wins the game!")
            break
        if position == 'T':
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        if position == 'W':
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_needs_rest = True

    else:
        first_player_needs_rest= False

    coordinates = input()
    if not second_player_needs_rest:

        row = int(coordinates[1])
        col = int(coordinates[4])

        position = matrix[row][col]
        if position == 'E':
            print(f"{second_player} found the Exit and wins the game!")
            break
        if position == 'T':
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        if position == 'W':
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_needs_rest = True
    else:
        second_player_needs_rest = False







