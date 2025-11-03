import sys
import a2 as maze


def index_label(n):
    """Return index labels: 0–9 are numbers, 10–35 are letters A–Z."""
    if n < 10:
        return str(n)
    else:
        return chr(ord('A') + (n - 10))


if len(sys.argv) != 3:
    print("Usage: python3 assignment2.py <rows> <cols>")
    sys.exit(1)

rows = int(sys.argv[1])
cols = int(sys.argv[2])

maze_text = maze.create_maze(rows, cols)
maze_lines = maze_text.splitlines()

print("   ", end="")
for c in range(cols):
    print(index_label(c), end=" ")
print()

for r, line in enumerate(maze_lines):
    print(f"{index_label(r):>2} {line}")
