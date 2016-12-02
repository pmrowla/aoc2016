#!/usr/bin/env python

from __future__ import absolute_import, division, print_function
from builtins import input


def main():
    # 0 = N, 1 = E, 2 = S, 3 = W
    current_dir = 0
    x = 0
    y = 0
    visited = set([(0, 0)])
    repeated = False
    data = input('Input: ')
    for direction in data.split(','):
        direction = direction.strip().upper()
        turn = direction[0]
        blocks = int(direction[1:])
        if turn == 'R':
            current_dir += 1
        elif turn == 'L':
            current_dir -= 1
        else:
            print('Unexpected direction: {}'.format(turn))
            continue
        current_dir %= 4
        for i in range(blocks):
            if current_dir == 0:
                x += 1
            elif current_dir == 1:
                y += 1
            elif current_dir == 2:
                x -= 1
            else:
                y -= 1
            if not repeated and (x, y) in visited:
                print('First repeat distance: {} blocks'.format(
                    abs(x) + abs(y)))
                repeated = True
            else:
                visited.add((x, y))
    print('Distance: {} blocks'.format(abs(x) + abs(y)))


if __name__ == '__main__':
    main()
