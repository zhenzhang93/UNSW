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
# Written by Eric Martin for COMP9021


from itertools import accumulate
import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def decode_set(encoded_set):
    elements_in_decoded_set = []
    encoded_set = [int(bit) for bit in reversed(f'{encoded_set:b}')]
    for i in range(len(encoded_set) // 2 * 2 - 1, -1, -2):
        if encoded_set[i]:
            elements_in_decoded_set.append(-(i + 1) // 2)
    for i in range(0, len(encoded_set) , 2):
        if encoded_set[i]:
            elements_in_decoded_set.append(i // 2)
    return elements_in_decoded_set
    
def display_encoded_set(encoded_set):
    print('{', ', '.join(str(e) for e in decode_set(encoded_set)), '}', sep = '')
        
def code_derived_set(encoded_set):
    encoded_running_sum = 0
    running_sums = accumulate(decode_set(encoded_set))
    for e in running_sums:
        if e < 0:
            encoded_running_sum |= 1 << (-e * 2 - 1)
        else:
            encoded_running_sum |= 1 << (e * 2)
    return encoded_running_sum

print('The encoded set is: ', end = '')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end = '')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)

    