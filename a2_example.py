#!/usr/bin/env python3

'''
    Example:        ASCII vs. Unicode boxes in Terminal
    Written by:     Michal Heidenreich
    Last update:    February 20, 2025
    Requires:       Python 3.7+
'''

# Unicode characters with meaningful names
BOX = {
    "ulcorner": "\u250C",  # upper-left corner ┌
    "urcorner": "\u2510",  # upper-right corner ┐
    "llcorner": "\u2514",  # lower-left corner └
    "lrcorner": "\u2518",  # lower-right corner ┘
    "hline":    "\u2500",  # horizontal line ─
    "vline":    "\u2502",  # vertical line │
    "ttee":     "\u252C",  # top tee ┬
    "btee":     "\u2534",  # bottom tee ┴
    "ltee":     "\u251C",  # left tee ├
    "rtee":     "\u2524",  # right tee ┤
    "plus":     "\u253C"   # middle cross ┼
}


def print_ascii_grid():
    grid = (
        "+---+---+",
        "| A | B |",
        "+---+---+",
        "| C | D |",
        "+---+---+"
    )

    show(grid)


def print_unicode_grid():
    grid = (
        "┌───┬───┐",
        "│ A │ B │",
        "├───┼───┤",
        "│ C │ D │",
        "└───┴───┘"
    )

    show(grid)


def show(grid):
    for row in grid:
        print(row)


def print_unicode_grid_with_codes():
    print(f"{BOX['ulcorner']}{BOX['hline']*3}{BOX['ttee']}{BOX['hline']*3}{BOX['urcorner']}")
    print(f"{BOX['vline']} A {BOX['vline']} B {BOX['vline']}")
    print(f"{BOX['ltee']}{BOX['hline']*3}{BOX['plus']}{BOX['hline']*3}{BOX['rtee']}")
    print(f"{BOX['vline']} C {BOX['vline']} D {BOX['vline']}")
    print(f"{BOX['llcorner']}{BOX['hline']*3}{BOX['btee']}{BOX['hline']*3}{BOX['lrcorner']}")


if __name__ == "__main__":
    print("ASCII Grid:")
    print_ascii_grid()
    print("Unicode Grid Hardcoded:")
    print_unicode_grid()
    print("Unicode Grid Symbolic:")
    print_unicode_grid_with_codes()
