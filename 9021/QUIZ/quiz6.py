# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def newgrid():
    # translate array to a new grid
    newgrid = grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (grid[i][j] != 0):
                newgrid[i][j] = 1
    return newgrid


def size_of_largest_isosceles_triangle():
    res = []
    height = [0] * 10
    for i in range(len(newgrid)):
        for j in range(len(newgrid)):
            if newgrid[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0
        res.append(height.copy())

    width = newgrid.copy()
    for i in range(len(newgrid) - 1, -1, -1):
        for j in range(1, len(newgrid)):
            if newgrid[i][j] == 1:
                width[i][j] = width[i][j - 1] + 1
            else:
                width[i][j] = 0
    print()
    for i in range(len(res)):
        print('   ', ' '.join(str(int(width[i][j])) for j in range(len(res))))

    print()
    for i in range(len(res)):
        print('   ', ' '.join(str(int(res[i][j])) for j in range(len(res))))

    # vertical direction
    maxsize = 0
    for i in range(len(res)):
        for j in range(len(res)):
            if res[i][j] >= 9:
                if (i - 4 >= 0 and j - 4 >= 0 and res[i - 4][j - 4] >= 1 and res[i - 3][j - 3] >= 3 and res[i - 2][
                    j - 2] >= 5 and res[i - 1][j - 1] >= 7) or \
                        (i - 4 >= 0 and j + 4 < len(res) and res[i - 1][j + 1] >= 7 and res[i - 2][j + 2] >= 5 and
                         res[i - 3][j + 3] >= 3 and res[i - 4][j + 4] >= 1):
                    maxsize = 5
                    return maxsize
            if res[i][j] >= 7:
                if (i - 3 >= 0 and j - 3 >= 0 and res[i - 3][j - 3] >= 1
                    and res[i - 2][j - 2] >= 3 and res[i - 1][j - 1] >= 5) or \
                        (i - 3 >= 0 and j + 3 < len(res) and res[i - 1][j + 1] >= 5 and res[i - 2][j + 2] >= 3 and
                         res[i - 3][j + 3] >= 1):
                    maxsize = max(maxsize, 4)
            if res[i][j] >= 5:
                if (i - 2 >= 0 and j - 2 >= 0 and res[i - 2][j - 2] >= 1 and res[i - 1][j - 1] >= 3) or \
                        (j + 2 < len(res) and res[i - 1][j + 1] >= 3 and res[i - 1][j + 2] >= 1):
                    maxsize = max(maxsize, 3)

            if res[i][j] >= 3:
                if (i - 1 >= 0 and j - 1 >= 0 and res[i - 1][j - 1] > 0) or \
                        (i - 1 >= 0 and j + 1 < len(res) and res[i - 1][j + 1] > 0):
                    maxsize = max(maxsize, 2)
            if res[i][j] >= 1:
                maxsize = max(maxsize, 1)
    # horizon direction
    for i in range(len(width)):
        for j in range(len(width)):
            if width[i][j] >= 9:
                if (i - 4 >= 0 and j - 4 >= 0 and width[i - 4][j - 4] >= 1 and width[i - 3][j - 3] >= 3 and
                    width[i - 2][j - 2] >= 5 and width[i - 1][j - 1] >= 7) or \
                        (j - 4 >= 0 and i + 4 < len(width) and width[i + 1][j - 1] >= 7 and width[i + 2][j - 2] >= 5 and
                         width[i + 3][j - 3] >= 3 and width[i + 4][j - 4] >= 1):
                    maxsize = 5
                    return maxsize
            if width[i][j] >= 7:
                if ((i - 3 >= 0 and j - 3 >= 0 and width[i - 3][j - 3] >= 1) and
                    width[i - 2][j - 2] >= 3 and width[i - 1][j - 1] >= 5) or \
                        (j - 3 >= 0 and i + 3 < len(width) and width[i + 1][j - 1] >= 5 and width[i + 2][j - 2] >= 3 and
                         width[i + 3][j - 3] >= 1):
                    maxsize = max(maxsize, 4)
            if res[i][j] >= 5:
                if ((i - 2 >= 0 and j - 2 >= 0 and width[i - 2][j - 2] >= 1) and width[i - 1][j - 1] >= 3) or \
                        (j - 2 >= 0 and i + 2 < len(width) and width[i + 1][j - 1] >= 3 and width[i + 2][j - 2] >= 1):
                    maxsize = max(maxsize, 3)
            if res[i][j] >= 3:
                if (i - 1 >= 0 and j - 1 >= 0 and width[i - 1][j - 1] >= 1) or \
                        (j - 1 >= 0 and i + 1 < len(width) and width[i + 1][j - 1] >= 1):
                    maxsize = max(maxsize, 2)

            if res[i][j] >= 1:
                maxsize = max(maxsize, 1)

    return maxsize


try:
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()

newgrid = newgrid()

print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle()
      )
