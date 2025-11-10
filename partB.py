"""
PRG550 Assignment 2 - Part B
Name: Agastya Suri
Date: November 2025
"""

# Step 1: open the maze text file
with open("maze.txt", "r") as file:
    maze_lines = file.readlines()

# Step 2: print maze to confirm we loaded it
for line in maze_lines:
    print(line, end="")
