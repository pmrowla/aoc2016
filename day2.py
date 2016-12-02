#!/usr/bin/env python

from __future__ import absolute_import, division, print_function
import sys


KP1 = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]

KP2 = [
    [None, None, '1', None, None],
    [None, '2', '3', '4', None],
    ['5', '6', '7', '8', '9'],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None],
]


def get_code(keypad, x, y, lines):
    code = ''
    dimension = len(keypad)
    for line in lines:
        for move in line.strip().upper():
            if move == 'U':
                if y > 0 and keypad[y - 1][x]:
                    y -= 1
            elif move == 'D':
                if y < dimension - 1 and keypad[y + 1][x]:
                    y += 1
            elif move == 'R':
                if x < dimension - 1 and keypad[y][x + 1]:
                    x += 1
            elif move == 'L':
                if x > 0 and keypad[y][x - 1]:
                    x -= 1
            else:
                print('Unexpected move: {}'.format(move))
                continue
        digit = keypad[y][x]
        code += digit
    return code


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: {} input_file'.format(sys.argv[0]))
    f = open(sys.argv[1])
    lines = f.readlines()
    print('Code 1: {}'.format(get_code(KP1, 1, 1, lines)))
    print('Code 2: {}'.format(get_code(KP2, 0, 2, lines)))


if __name__ == '__main__':
    main()
