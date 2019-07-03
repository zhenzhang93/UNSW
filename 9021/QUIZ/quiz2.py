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
def uniquely_produced_by_rule(line):

    if (len(line) <= 2):
        return -1
    dicall = {}
    dic = {}
    for i in range(16):
        dicall[int(i)] = rule_encoded_by(i)
    for j in range(len(line) - 2):
        if ((int(line[j]), int(line[j + 1])) not in dic):
            dic[int(line[j]), int(line[j + 1])] = int(line[j + 2])
        elif (dic[int(line[j]), int(line[j + 1])] != int(line[j + 2])):
            return -1
    if (len(dic) < 4):
        return -1
    else:
        a, b, c, d = dic[(0, 0)], dic[(0, 1)], dic[(1, 0)], dic[(1, 1)]
        return(d*1+c*2+b*4+a*8)
