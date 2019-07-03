# A polynomial object can be created from a string that represents a polynomial
# as sums or differences of monomials.
# - Monomials are ordered from highest to lowest powers.
# - All factors are strictly positive, except possibly for the leading factor
# - For nonzero powers, factors of 1 are only implicit.
# A single space surrounds + and - signs between monomials.

# Written by *** and Eric Martin for COMP9021


import re  # split() suffices though
from collections import defaultdict
from copy import deepcopy


class Polynomial:
    def __init__(self, polynomial=None):
        self.polynomial = polynomial

    def __str__(self):
        return '0' if self.polynomial == None else self.polynomial.strip()

    def __iadd__(self, other):
        return self.__add__(other)

    def __add__(self, other):
        item1 = self.become_dic().items()
        item2 = other.become_dic().items()
        len1 = len(item1)
        len2 = len(item2)
        index1 = 0
        index2 = 0
        newdic = {}
        help1 = []
        help2 = []
        for i in item1:
            help1.append([i[0], i[1]])
        for i in item2:
            help2.append([i[0], i[1]])

        while (index1 < len1 and index2 < len2):
            if (help1[index1][0] < help2[index2][0]):
                newdic[help2[index2][0]] = help2[index2][1]
                index2 += 1
            elif ((help1[index1][0] > help2[index2][0])):
                newdic[help1[index1][0]] = help1[index1][1]
                index1 += 1
            else:
                newdic[help1[index1][0]] = int(help1[index1][1]) + int(help2[index2][1])
                index1 += 1
                index2 += 1
        while (index1 < len1):
            newdic[help1[index1][0]] = help1[index1][1]
            index1 += 1
        while (index2 < len2):
            newdic[help2[index2][0]] = help2[index2][1]
            index2 += 1

        # print(newdic)
        newstr = decode_dic(newdic)
        # print(newstr)
        return Polynomial(newstr)

    def __imul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        item1 = self.become_dic().items()
        item2 = other.become_dic().items()
        newdic = defaultdict(int)
        help1 = []
        help2 = []
        for i in item1:
            help1.append([i[0], i[1]])
        for i in item2:
            help2.append([i[0], i[1]])
        #print(item1)
        #print(item2)

        for i in range(len(help1)):
            for j in range(len(help2)):
                newdic[int(help1[i][0]) + int(help2[j][0])] = newdic[int(help1[i][0]) + int(help2[j][0])] + \
                                                              int(help1[i][1]) * int(help2[j][1])

        a = sorted(newdic.items(), key=lambda x: x, reverse=True)
        # print(a)
        newstr = decode_dic(dict(a))
        return Polynomial(newstr)

    # easy one, so I add it.
    def __isub__(self, other):
        return self.__sub__(other)

    def __sub__(self, other):
        return self.__iadd__(other.__imul__(Polynomial('-1')))

    def __len__(self):
        return '0' if self.polynomial == None else len(self.polynomial)

    def deal_polynomial(self):
        newstr = []
        start = 0
        end = 0
        if (self.polynomial == None):
            return '0'
        s = self.polynomial
        while (start < len(s)):
            if (s[start] == '+' or s[start] == '-'):
                newstr.append(s[end:start])
                end = start
            start += 1

        newstr.append(s[end:])
        res = []
        for i in newstr:
            i.strip()
            if (i == ""):
                continue
            res.append(i.replace(" ", ""))
        return res

    def become_dic(self):
        res = self.deal_polynomial()
        dic = {}
        for i in res:
            temp = i.split('^')
            # the key is the power,value is value
            # 5x^3, key is 3, value is 5
            if (len(temp) == 2):
                a = temp[0].split('x')
                if (len(a[0]) == 1 and not a[0].isdigit() or len(a[0])==0):
                    dic[temp[1]] = temp[0][:-1] + '1'

                else:
                    dic[temp[1]] = temp[0][:-1]

            else:
                if str(temp).__contains__('x'):
                    if (len(temp[0][:-1]) < 2):
                        dic['1'] = temp[0][:-1] + '1'
                    else:
                        dic['1'] = temp[0][:-1]
                else:
                    dic['0'] = temp[0]
        return dic


def decode_dic(newdic):
    item = newdic.items()
    newstr = ""
    for i in item:
        if (int(i[0]) >= 2):
            if (int(i[1]) > 1):
                newstr += f'+ {int(i[1])}x^{i[0]}' + " "
            elif (int(i[1]) < -1):
                newstr += f'- {abs(int(i[1]))}x^{i[0]}' + " "
            elif (int(i[1]) == -1):
                newstr += f'- x^{abs(int(i[0]))}' + " "
            elif (int(i[1]) == 1):
                newstr += f'+ x^{int(i[0])}' + " "
        else:
            if int(i[0]) == 1:
                if int(i[1]) > 1:
                    newstr += f'+ {int(i[1])}x' + " "
                elif int(i[1]) == 1:
                    newstr += f'+ x' + " "
                elif int(i[1]) < -1:
                    newstr += f'- {abs(int(i[1]))}x' + " "
                elif int(i[1]) == -1:
                    newstr += f'+ x' + " "
            else:
                if (int(i[1]) > 0):
                    newstr += f'+ {int(i[1])}'
                elif (int(i[1]) < 0):
                    newstr += f'- {abs(int(i[1]))}'

    if (newstr == ""):
        newstr = '0'
        return newstr
    if (newstr[0] == '+'):
        return newstr[2:].strip()
    else:
        return ('-' + newstr[2:]).strip()



