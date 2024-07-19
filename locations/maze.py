# locations/maze.py

import os

def load_maze(file_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'images', file_name)
    with open(file_path, 'r') as f:
        maze = f.readlines()
    return [line.rstrip() for line in maze]

def display_maze(maze, player_pos):
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if (y, x) == player_pos:
                print("P", end="")  # Display player position
            else:
                print(char, end="")
        print()

def move_player(maze, player_pos, direction):
    y, x = player_pos
    if direction == 'w' and y > 0 and maze[y - 1][x] != '@':
        y -= 1
    elif direction == 's' and y < len(maze) - 1 and maze[y + 1][x] != '@':
        y += 1
    elif direction == 'a' and x > 0 and maze[y][x - 1] != '@':
        x -= 1
    elif direction == 'd' and x < len(maze[0]) - 1 and maze[y][x + 1] != '@':
        x += 1
    return y, x

def maze(controller):
    maze = load_maze('ascii-art_2.txt')
    player_pos = (1, 1)  # Starting position

    while True:
        display_maze(maze, player_pos)
        move = input("Move (w/a/s/d): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            player_pos = move_player(maze, player_pos, move)
        else:
            print("Invalid move. Use 'w', 'a', 's', 'd' to move.")

        # Add any conditions to exit the maze
        if player_pos == (exit_y, exit_x):
            print("You've found the exit!")
            break
