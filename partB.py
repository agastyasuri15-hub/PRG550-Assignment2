import sys

def ascii_to_unicode(line_above, line, line_below):
    """Convert one ASCII maze line to a Unicode maze line."""
    result = ""
    for i, ch in enumerate(line):
        if ch == '+':
            up = (i < len(line_above) and line_above[i] in ('|', '+'))
            down = (i < len(line_below) and line_below[i] in ('|', '+'))
            left = (i > 0 and line[i - 1] in ('-', '+'))
            right = (i < len(line) - 1 and line[i + 1] in ('-', '+'))

            # Use proper Unicode box-drawing characters
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


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 partB.py <maze_file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            ascii_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Cannot open file '{filename}'")
        sys.exit(1)

    ascii_lines = [line.rstrip('\n') for line in ascii_lines]

    unicode_lines = []
    for i, line in enumerate(ascii_lines):
        line_above = ascii_lines[i - 1] if i > 0 else ""
        line_below = ascii_lines[i + 1] if i < len(ascii_lines) - 1 else ""
        unicode_lines.append(ascii_to_unicode(line_above, line, line_below))

    print("ASCII Maze:".ljust(40) + "Unicode Maze:")
    for a, u in zip(ascii_lines, unicode_lines):
        print(a.ljust(40) + "    " + u)


if __name__ == "__main__":
    main()
