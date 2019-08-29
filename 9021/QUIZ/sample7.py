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
# Written by Eric Martin for COMP9021


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

def nb_of_good_paths(pt_1, pt_2):
    if not grid[pt_1.y, pt_1.x] or not grid[pt_2.y, pt_2.x]:
        return 0
    if pt_1 == pt_2:
        return 1
    return nb_of_good_paths_with_last_two_directions(pt_1.x, pt_1.y, pt_2.x, pt_2.y, 'none', 'also_none')
    
def nb_of_good_paths_with_last_two_directions(x1, y1, x2, y2, penultimate_direction, last_direction):
    if x1 == x2 and y1 == y2:
        return 1
    grid[y1, x1] = 0
    nb_of_solutions = 0
    other_directions = {'N': 'ESW', 'E': 'SWN', 'S': 'WNE', 'W': 'NES'}
    directions_to_try = 'NSEW' if penultimate_direction != last_direction else other_directions[last_direction]
    for direction in directions_to_try:
        if direction == 'N' and y1 and grid[y1 - 1, x1]:
            nb_of_solutions += nb_of_good_paths_with_last_two_directions(x1, y1 - 1, x2, y2, last_direction, 'N')
        elif direction == 'S' and y1 < height - 1 and grid[y1 + 1, x1]:
            nb_of_solutions += nb_of_good_paths_with_last_two_directions(x1, y1 + 1, x2, y2, last_direction, 'S')
        elif direction == 'W' and x1 and grid[y1, x1 - 1]:
            nb_of_solutions += nb_of_good_paths_with_last_two_directions(x1 - 1, y1, x2, y2, last_direction, 'W')
        elif direction == 'E' and x1 < width - 1 and grid[y1, x1 + 1]:
            nb_of_solutions += nb_of_good_paths_with_last_two_directions(x1 + 1, y1, x2, y2, last_direction, 'E')
    grid[y1, x1] = 1
    return nb_of_solutions    
    
    
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
paths_nb = nb_of_good_paths(pt_1, pt_2)
if not paths_nb:
    print('There is no good path.')
elif paths_nb == 1:
    print('There is a unique good path.')
else:
    print('There are', paths_nb, 'good paths.')