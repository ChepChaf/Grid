# Grid
Grid is a package that provides utils for using grids in your game or any other Python application.

## Examples

TicTacToe:
```
from grid import Grid

# Creates a 3x3 grid
grid_map = Grid(3, 3)

players = ['X', 'O']

current_player = 0

finished = False
winner = None

while not finished:
    current_player = current_player % 2
    # Request player input
    x, y = input("Insert x, y coords with values beetween: {}".format(grid_map.shape))

    # Check if that position is available
    if grid_map[x][y] != None:
        continue

    grid_map[x][y] = players[current_player]

    # Check if player won
    if not grid_map.rows[y].repeated(players[current_player]) or
        not grid_map.columns[x].repeated(players[current_player]) or
            not grid_map.diagonal().repeated(players[current_player]):
                winner = players[current_players]

    # Check if the game if finished
    if winner != None or len(grid_map.empty_positions) >= 0:
        finished = True
    else:
        current_player += 1

if winner:
    print("The winner is: {}".format(winner))
else:
    print("It is a tie)
```
