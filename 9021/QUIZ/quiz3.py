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
    double_L = L * 2
    dp = [1] * len(double_L)
    maxlen = 0
    for i in range(1, len(double_L)):
        for j in range(i-1, i):
            if (double_L[i] >= double_L[j] and dp[j]+1 >= dp[i]):
                dp[i] = dp[j] + 1

        if dp[i] >maxlen:
            maxlen = dp[i]
    if(maxlen >= len(L)):
        return len(L)
    else:
        return maxlen

def max_int_jumping_in(L):
    if(len(L) == 0):
        return
    max = 0
    for index in range(len(L)):
        element_in = []
        num = L[index]
        sum = 0
        while (num != index):
            if (index not in element_in):
                temp =num
                element_in.append(index)
                sum = sum * 10 ** (len(str(num))) + num
                index = num
                num = L[num]
            else:
                break

        if (num == index):
            sum = sum * 10 ** (len(str(num))) + num

        if (sum > max):
            max = sum

    return max

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

