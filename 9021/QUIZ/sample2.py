# Written by Eric Martin for COMP9021


def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}

def describe_rule(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    print()
    for last_two in range(4):
        penultimate, last = last_two // 2, last_two % 2
        print('After', penultimate, 'followed by', last, end = ', ')
        print('we draw', rule[penultimate, last])


def draw_line(rule_nb, first, second, length):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).

    
    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".
    '''
    rule = rule_encoded_by(rule_nb)
    if length == 0:
        return
    if length == 1:
        print(first)
        return
    print(first, second, sep = '', end = '')
    penultimate = first
    last = second
    for i in range(length - 2):
        following = rule[penultimate, last]
        print(following, end = '')
        penultimate, last = last, following
    print()


def uniquely_produced_by_rule(line):
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    '''
    rule_nb = 0
    rule = {}
    line = [int(d) for d in line]
    for i in range(len(line) - 2):
        if rule.setdefault((line[i], line[i + 1]), line[i + 2]) != line[i + 2]:
            return -1
    if len(rule) != 4:
        return -1
    for p in range(4):
        rule_nb += 2 ** (3 - p) * rule[p // 2, p % 2]
    return rule_nb