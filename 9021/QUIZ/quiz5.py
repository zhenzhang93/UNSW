# Prompts the user for a positive integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived positive integer that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
# Written by *** and Eric Martin for COMP9021


from itertools import accumulate
import sys
from math import ceil

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def myfuc(encoded_set):
    res_set = []
    number = bin(encoded_set)[2:]
    number_s = str(number)
    length_number = len(number_s)
    for i in range(length_number):
        if (number_s[length_number - 1 - i] == '1'):
            if (i % 2 == 0):
                res_set.append(i // 2)
            else:
                res_set.append(ceil(-i // 2))
    sort_set = sorted(res_set)
    return sort_set


# POSSIBLY DEFINE OTHER FUNCTIONS
def display_encoded_set(encoded_set):
    res_set = []
    number = bin(encoded_set)[2:]
    number_s = str(number)
    length_number = len(number_s)
    for i in range(length_number):
        if (number_s[length_number - 1 - i] == '1'):
            if (i % 2 == 0):
                res_set.append(i // 2)
            else:
                res_set.append(ceil(-i // 2))
    sort_set = sorted(res_set)
    if (len(res_set) == 0):
        print({})
    else:
        for i in range(0, len(sort_set)):
            if (i == 0 and len(sort_set) > 1):
                print("{", end="")
                print(str(sort_set[i]) + ", ", end="")
            elif (i == 0 and len(sort_set) == 1):
                print("{", end="")
                print(str(sort_set[i]) + "}")
            elif (i == len(sort_set) - 1):
                print(str(sort_set[i]) + "}")
            else:
                print(str(sort_set[i]) + ", ", end="")


def code_derived_set(encoded_set):
    encoded_running_sum = 0
    final_set = []
    res_set = myfuc(encoded_set)
    for i in range(len(res_set)):
        final_set.append(sum(res_set[k] for k in range(0, i + 1)))
    decode = set(final_set)
    for i in decode:
        if i < 0:
            encoded_running_sum += 2 ** (abs(i) * 2 - 1)
        else:
            encoded_running_sum += 2 ** (i * 2)

    return encoded_running_sum


print('The encoded set is: ', end='')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end='')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)
