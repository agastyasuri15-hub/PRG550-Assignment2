import sys
import a2


def ascii_to_unicode(line_above, line, line_below):
    """Convert one ASCII maze line to a Unicode maze line."""
    result = ""
    for i, ch in enumerate(line):
        if ch == '+':
            up = (i < len(line_above) and line_above[i] in ('|', '+'))
            down = (i < len(line_below) and line_below[i] in ('|', '+'))
            left = (i > 0 and line[i - 1] in ('-', '+'))
            right = (i < len(line) - 1 and line[i + 1] in ('-', '+'))

            if up and down and left and right:
                result += '┼'
            elif up and down and left:
                result += '┤'
            elif up and down and right:
                result += '├'
            elif left and right and up:
                result += '┴'
            elif left and right and down:
                result += '┬'
            elif down and right:
                result += '┌'
            elif down and left:
                result += '┐'
            elif up and right:
                result += '└'
            elif up and left:
                result += '┘'
            elif left and right:
                result += '─'
            elif up and down:
                result += '│'
            elif left or right:
                result += '─'
            elif up or down:
                result += '│'
            else:
                result += '+'
        elif ch == '-':
            result += '─'
        elif ch == '|':
            result += '│'
        else:
            result += ch
    return result


def generate_labels(length):
    """Generate 0–9 then A–Z labels up to maze width."""
    labels = []
    for i in range(length):
        if i < 10:
            labels.append(str(i))
        else:
            labels.append(chr(ord('A') + i - 10))
    return " ".join(labels)


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as f:
                ascii_lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: Cannot open file '{filename}'")
            sys.exit(1)
    elif len(sys.argv) == 3:
        try:
            height = int(sys.argv[1])
            width = int(sys.argv[2])
        except ValueError:
            print("Error: Height and width must be integers.")
            sys.exit(1)
        ascii_maze = a2.create_maze(height, width)
        ascii_lines = ascii_maze.splitlines()
    else:
        print("Usage:")
        print("  python3 partB.py <maze_file>")
        print("  OR")
        print("  python3 partB.py <height> <width>")
        sys.exit(1)

    ascii_lines = [line.rstrip('\n') for line in ascii_lines]

    unicode_lines = []
    for i, line in enumerate(ascii_lines):
        line_above = ascii_lines[i - 1] if i > 0 else ""
        line_below = ascii_lines[i + 1] if i < len(ascii_lines) - 1 else ""
        unicode_lines.append(ascii_to_unicode(line_above, line, line_below))

    top_label = "   " + generate_labels(len(ascii_lines[0]))
    print("ASCII Maze:".ljust(40) + "Unicode Maze:")
    print(top_label.ljust(40) + "   " + top_label)

    for row_num, (a, u) in enumerate(zip(ascii_lines, unicode_lines)):
        if row_num < 10:
            label = f" {row_num} "
        else:
            label = f" {chr(ord('A') + row_num - 10)} "
        print(f"{label}{a}".ljust(40) + "   " + f"{label}{u}")


if __name__ == "__main__":
    main()
