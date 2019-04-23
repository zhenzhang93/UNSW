# Randomly fills a grid with True and False, with width, height and density
# controlled by user input, and computes the number of all "good paths" that link
# a point of coordinates (x1, y1) to a point of coordinates (x2, y2)
# (x1 and x2 are horizontal coordinates, increasing from left to right,
# y1 and y2 are vertical coordinates, increasing from top to bottom,
# both starting from 0), that is:
# - paths that go through nothing but True values in the grid
# - paths that never go through a given point in the grid more than once;
# - paths that never keep the same direction (North, South, East, West) over
#   a distance greater than 2.
#
# Written by *** and Eric Martin for COMP9021


from collections import namedtuple
import numpy as np
from random import seed, randrange
import sys

Point = namedtuple('Point', 'x y')


def display_grid():
    for row in grid:
        print('   ', ' '.join(str(int(e)) for e in row))


def valid(pt):
    return 0 <= pt.x < width and 0 <= pt.y < height


def destination_valid(x1, y1, x2, y2):
    for y in range(height):
        for x in range(width):
            if (x1 == x and y1 == y):
                if (grid[y][x] != 1):
                    return False
            if (x2 == x and y2 == y):
                if (grid[y][x] != 1):
                    return False
    return True


def nb_of_good_paths(pt_1, pt_2):
    # because the attribute can not change
    # so I just use another function with eight parameters
    pass


# need to calculate possibility of on point to its neighbour


def nb_of_good_paths_xy(x1, y1, x2, y2, right, down, left, up):
    count = 0

    grid[y1][x1] = 0

    if (x1 == x2 and y1 == y2):
        return 1
    # 0 means has visited
    # in order not to repeat

    if (right < 2):
        if (x1 + 1 < width and grid[y1][x1 + 1] == 1):
            # other direction renew to 0
            count += nb_of_good_paths_xy(x1 + 1, y1, x2, y2, right + 1, 0, 0, 0)
            grid[y1][x1 + 1] = 1

    if (down < 2):
        if (y1 + 1 < height and grid[y1 + 1][x1] == 1):
            count += nb_of_good_paths_xy(x1, y1 + 1, x2, y2, 0, down + 1, 0, 0)
            grid[y1 + 1][x1] = 1

    if (left < 2):
        if (x1 - 1 >= 0 and grid[y1][x1 - 1] == 1):
            count += nb_of_good_paths_xy(x1 - 1, y1, x2, y2, 0, 0, left + 1, 0)
            grid[y1][x1 - 1] = 1

    # after one route, return the original value
    # after couting,return to 0
    if (up < 2):
        if (y1 - 1 >= 0 and grid[y1 - 1][x1] == 1):
            """
            right = 0
            left = 0
            down = 0
            up += 1
            temp4 = up
            using this way,it can not actually record four direction,it lose other direction
            so I change it to in the function
            """
            count += nb_of_good_paths_xy(x1, y1 - 1, x2, y2, 0, 0, 0, up + 1)
            grid[y1 - 1][x1] = 1

    return count


try:
    for_seed, density, height, width = (abs(int(i)) for i in
                                        input('Enter four integers: ').split()
                                        )
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not density:
    density = 1
seed(for_seed)
grid = np.array([randrange(density) > 0
                 for _ in range(height * width)
                 ]
                ).reshape((height, width))
print('Here is the grid that has been generated:')
display_grid()
try:
    i1, j1, i2, j2 = (int(i) for i in input('Enter four integers: ').split())
    pt_1 = Point(i1, j1)
    pt_2 = Point(i2, j2)
    if not valid(pt_1) or not valid(pt_2):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
print('Will compute the number of good paths '
      f'from ({pt_1.x}, {pt_1.y}) to ({pt_2.x}, {pt_2.y})...'
      )

if (not destination_valid(pt_1.x, pt_1.y, pt_2.x, pt_2.y)):
    paths_nb = 0
else:
    paths_nb = nb_of_good_paths_xy(pt_1.x, pt_1.y, pt_2.x, pt_2.y, 0, 0, 0, 0)

if not paths_nb:
    print('There is no good path.')
elif paths_nb == 1:
    print('There is a unique good path.')
else:
    print('There are', paths_nb, 'good paths.')
