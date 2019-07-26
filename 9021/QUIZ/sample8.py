# Written by Eric Martin for COMP9021


'''
Defines Monomial and Polynomial classes.
A polynomial is built from a string that represents a polynomial,
that is, a sum or difference of monomials.
- The leading monomial can be either an integer,
  or an integer followed by x,
  or an integer followed by x\^ followed by a nonnegative integer.
- The other monomials can be either a nonnegative integer,
  or an integer followed by x,
  or an integer followed by x\^ followed by a nonnegative integer.
Spaces can be inserted anywhere in the string.
'''


import re # split() suffices though
from collections import defaultdict
from copy import deepcopy


class Polynomial:
    def __init__(self, polynomial = None):
        self.monomials = defaultdict(int)
        if not polynomial:
            return
        tokens = polynomial.split()
        if tokens[0][0] == '-':
            tokens[0] = tokens[0][1: ]
            tokens.insert(0, '-')
        else:
            tokens.insert(0, '+')
        for i in range(0, len(tokens), 2):
            if 'x' not in tokens[i + 1]:
                factor = int(tokens[i + 1])
                if factor:
                    if tokens[i] == '-':
                        factor = -factor
                    self.monomials[0] = factor
            else:
                factor, power = tokens[i + 1].split('x')
                factor = int(factor) if factor else 1
                if tokens[i] == '-':
                        factor = -factor
                if power:
                    power = power[1: ]
                power = int(power) if power else 1
                self.monomials[power] = factor
            
    def __str__(self):
        if not self.monomials:
            return '0'
        output = []
        for power in sorted(self.monomials, reverse = True):
            if output:
                if self.monomials[power] > 0:
                    output.append(' + ')
                else:
                    output.append(' - ')
            elif self.monomials[power] < 0:
                output.append('-')
            if not power or self.monomials[power] not in {-1, 1}:
                output.append(str(abs(self.monomials[power])))
            if power:
                output.append('x')
            if power > 1:
                output.append(f'^{power}')
        return ''.join(output)
                   
    def __add__(self, polynomial):
        polynomial_sum = deepcopy(self)
        for power in polynomial.monomials:
            polynomial_sum.monomials[power] += polynomial.monomials[power]
        polynomial_sum._clean()
        return polynomial_sum

    def __iadd__(self, polynomial):
        polynomial_sum = self + polynomial
        self.monomials = {factor: polynomial_sum.monomials[factor] for factor in polynomial_sum.monomials}
        return self

    def __mul__(self, polynomial):
        product_polynomial = Polynomial()
        for power_1 in self.monomials:
            for power_2 in polynomial.monomials:
                product_polynomial.monomials[power_1 + power_2] += self.monomials[power_1] *\
                                                                  polynomial.monomials[power_2]
        product_polynomial._clean()
        return product_polynomial

    def __imul__(self, polynomial):
        polynomial_prod = self * polynomial
        self.monomials = {factor: polynomial_prod.monomials[factor] for factor in polynomial_prod.monomials}
        return self

    def _clean(self):
        self.monomials = {factor: self.monomials[factor]
                                         for factor in self.monomials if self.monomials[factor]
                         }
   
