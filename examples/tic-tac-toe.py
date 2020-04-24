from grid import Grid

# Creates a 3x3 grid
grid_map = Grid(3, 3)

players = ['X', 'O']

current_player = 0

finished = False
winner = None


def check_win(arr):
    # Check if player won
    for row in arr:
        if row.repeated_count(players[current_player]) == 3:
            return players[current_player]
    return None


while not finished:
    current_player = current_player % 2

    print(grid_map)
    print("Player {} turns".format(players[current_player]))

    # Request player input
    x, y = tuple(input(
        "Insert x, y coords with values beetween {}: ".format(grid_map.shape)).strip().split(' '))
    x, y = int(x), int(y)

    # Check if that position is available
    if grid_map[x][y] != None:
        continue

    grid_map.set_value(x, y, players[current_player])

    winner = check_win(grid_map.rows) or check_win(
        grid_map.columns) or check_win(grid_map.diagonals)

    # Check if the game if finished
    if winner != None or grid_map.empty_positions() <= 0:
        finished = True
    else:
        current_player += 1

print(grid_map)

if winner:
    print("The winner is: {}".format(winner))
else:
    print("It is a tie")
