#quiz2
def rule_encoded_by(rule_nb):
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}


def draw_line(rule_nb, first, second, length):
    if (length == 0):
        return
    res = []
    res.append(first)
    res.append(second)
    rule = rule_encoded_by(rule_nb)
    for i in range(length):
        if (i <= 1):
            print(res[i], end='')
            continue

        res.append(rule[res[i - 2], res[i - 1]])
        print(res[i], end='')
    print()
