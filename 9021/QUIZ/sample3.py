# Written by Eric Martin for COMP9021



import sys
from random import seed, randint, randrange


try:
    arg_for_seed, upper_bound, length =\
            (int(x) for x in input('Enter three integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def length_of_longest_increasing_sequence(L):
    if not L:
        return 0
    max_init_length = 1
    while max_init_length < len(L) and L[max_init_length] >= L[max_init_length - 1]:
        max_init_length += 1
    if max_init_length == len(L):
        return max_init_length
    max_length = max_init_length
    current_length = 1
    for i in range(max_init_length + 1, len(L)):
        if L[i] >= L[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
    if L[0] >= L[-1]:
        current_length += max_init_length
    if current_length > max_length:
        max_length = current_length
    return max_length

def max_int_jumping_in(L):
    max_int = 0
    for i in range(len(L)):
        not_used = [True] * len(L)
        digits = []
        j = i
        while not_used[j]:
            not_used[j] = False
            j = L[j]
            digits.append(j)
        max_int = max(max_int, int(''.join(str(x) for x in digits)))
    return max_int
        

seed(arg_for_seed)
L_1 = [randint(0, upper_bound) for _ in range(length)]
print('L_1 is:', L_1)
print('The length of the longest increasing sequence\n'
      '  of members of L_1, possibly wrapping around, is:',
      length_of_longest_increasing_sequence(L_1), end = '.\n\n'
     )
L_2 = [randrange(length) for _ in range(length)]
print('L_2 is:', L_2)
print('The maximum integer built from L_2 by jumping\n'
      '  as directed by its members, from some starting member\n'
      '  and not using any member more than once, is:',
      max_int_jumping_in(L_2)
     )

