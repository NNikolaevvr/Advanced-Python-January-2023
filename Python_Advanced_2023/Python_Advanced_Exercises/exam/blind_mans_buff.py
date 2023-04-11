n, m = [int(x) for x in input().split()]
playground = [input().split() for _ in range(n)]
moves_count = 0
opponents_touched = 0

for i in range(n):
    for j in range(m):
        if playground[i][j] == "B":
            player_pos = (i, j)

while True:
    command = input()
    if command == "Finish":
        print("Game over!")
        print(f"Touched opponents: {opponents_touched} Moves made: {moves_count}")
        break
    elif command == "up":
        new_pos = (player_pos[0] - 1, player_pos[1])
    elif command == "down":
        new_pos = (player_pos[0] + 1, player_pos[1])
    elif command == "left":
        new_pos = (player_pos[0], player_pos[1] - 1)
    elif command == "right":
        new_pos = (player_pos[0], player_pos[1] + 1)

    if new_pos[0] < 0:
        new_pos = (0, new_pos[1])
    elif new_pos[0] >= n:
        new_pos = (n - 1, new_pos[1])
    if new_pos[1] < 0:
        new_pos = (new_pos[0], 0)
    elif new_pos[1] >= m:
        new_pos = (new_pos[0], m - 1)

    if playground[new_pos[0]][new_pos[1]] == "-":
        moves_count += 1
        playground[player_pos[0]][player_pos[1]] = "-"
        playground[new_pos[0]][new_pos[1]] = "B"
        player_pos = new_pos
    elif playground[new_pos[0]][new_pos[1]] == "P":
        moves_count += 1
        opponents_touched += 1
        playground[player_pos[0]][player_pos[1]] = "-"
        playground[new_pos[0]][new_pos[1]] = "B"
        player_pos = new_pos

    if opponents_touched == 3:
        print("Game over!")
        print(f"Touched opponents: {opponents_touched} Moves made: {moves_count}")
        break