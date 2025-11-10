"""
PRG550 Assignment 02 – Part B
Author: Agastya Suri
Description:
Display ASCII and Unicode mazes side-by-side using Part A's generator (a2.py)
"""

import sys
import os
import random
import a2

random.seed(42)

sys.path.append(os.path.join(os.path.dirname(__file__), "."))


LABELS = (
    [str(i) for i in range(10)] +
    [chr(c) for c in range(ord("A"), ord("Z") + 1)]
)


def label_sequence(n):
    seq = []
    i = 0
    while len(seq) < n:
        seq.append(LABELS[i % len(LABELS)])
        i += 1
    return seq


def add_row_col_numbers(maze_text):
    lines = maze_text.rstrip("\n").split("\n")
    num_rows = len(lines)
    row_labels = label_sequence(num_rows)
    line_len = max(len(line) for line in lines)
    col_labels = label_sequence(line_len)
    header = "   " + "".join(col_labels[:line_len]) + "\n"
    body = []
    for i, line in enumerate(lines):
        body.append(f"{row_labels[i]:>2} {line}")
    return header + "\n".join(body) + "\n"


def ascii_to_unicode(maze):
    grid = [list(row) for row in maze.splitlines()]
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            ch = grid[r][c]
            if ch != "+":
                continue

            up = r > 0 and grid[r - 1][c] in "|+"
            down = r < rows - 1 and grid[r + 1][c] in "|+"
            left = c > 0 and grid[r][c - 1] in "-+"
            right = c < cols - 1 and grid[r][c + 1] in "-+"

            if up and right and not down and not left:
                grid[r][c] = "└"
            elif up and left and not down and not right:
                grid[r][c] = "┘"
            elif down and right and not up and not left:
                grid[r][c] = "┌"
            elif down and left and not up and not right:
                grid[r][c] = "┐"
            elif up and down and right and not left:
                grid[r][c] = "├"
            elif up and down and left and not right:
                grid[r][c] = "┤"
            elif left and right and down and not up:
                grid[r][c] = "┬"
            elif left and right and up and not down:
                grid[r][c] = "┴"
            elif up and down and left and right:
                grid[r][c] = "┼"
            else:
                grid[r][c] = "┼"

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "-":
                grid[r][c] = "─"
            elif grid[r][c] == "|":
                grid[r][c] = "│"

    return "\n".join("".join(row) for row in grid)


def combine_side_by_side(left, right):
    left_lines = left.splitlines()
    right_lines = right.splitlines()
    max_left = max(len(line) for line in left_lines)
    combined = []
    for i in range(len(left_lines)):
        left_part = left_lines[i].ljust(max_left)
        right_part = right_lines[i] if i < len(right_lines) else ""
        combined.append(f"{left_part}    {right_part}")
    return "\n".join(combined)


def main(argv):
    if len(argv) != 3:
        print("Usage: python3 partB.py rows cols")
        return 1

    rows, cols = int(argv[1]), int(argv[2])
    ascii_maze = a2.create_maze(rows, cols)
    ascii_labelled = add_row_col_numbers(ascii_maze)
    unicode_maze = ascii_to_unicode(ascii_maze)
    unicode_labelled = add_row_col_numbers(unicode_maze)
    combined = combine_side_by_side(ascii_labelled, unicode_labelled)

    print("ASCII Maze:                     Unicode Maze:\n")
    print(combined)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
