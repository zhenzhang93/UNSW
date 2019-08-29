# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def size_of_largest_isosceles_triangle():
    max_size = 0
    for i in range(10):
        for j in range(10):
            if not grid[i][j]:
                continue
            for direction in {'N', 'S', 'W', 'E'}:
                max_size = max(max_size,
                               size_of_largest_anchored_isosceles_triangle(i, j, direction)
                              )
    return max_size

def size_of_largest_anchored_isosceles_triangle(i, j, direction):
    size = 1
    if direction == 'N':
        while i + size < 10 and j - size >= 0 and j + size < 10:
            for n in range(j - size, j + size + 1):
                if not grid[i + size][n]:
                    return size
            size += 1
        return size
    if direction == 'S':
        while i - size >= 0 and j - size >= 0 and j + size < 10:
            for n in range(j - size, j + size + 1):
                if not grid[i - size][n]:
                    return size
            size += 1
        return size
    if direction == 'W':
        while j + size < 10 and i - size >= 0 and i + size < 10:
            for n in range(i - size, i + size + 1):
                if not grid[n][j + size]:
                    return size
            size += 1
        return size
    if direction == 'E':
        while j - size >= 0 and i - size >= 0 and i + size < 10:
            for n in range(i - size, i + size + 1):
                if not grid[n][j - size]:
                    return size
            size += 1
        return size

try:
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle()
     )