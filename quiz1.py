def describe_automaton(transitions):
    for key in transitions:
        print("When in state " + "\"{}\"".format(key[0]) + " and processing "
              + "\"{}\"".format(key[1]) + ", automaton's state becomes " + "\"{}\"".format(transitions[key]) + ".")


def transitions_as_dict(transitions_as_list):
    transitions = {}
    for element in transitions_as_list:
        a, b = element.split(',')
        num, statenow = b.split(':')
        transitions[a, int(num)] = statenow

    return transitions


def accepts(transitions, word, initial_state, accept_state):
    list_start = []
    list_end = []
    number_set = [0, 1]

    for key in transitions:
        list_start.append(key[0])
        list_end.append(transitions[key])

    for number in word:
        if int(number) not in number_set:
            return False
        elif initial_state not in list_start:
            return False
        elif accept_state not in list_end:
            return False
        else:
            tuple_state_addnum = (initial_state, int(number))
            if (tuple_state_addnum in transitions):
                initial_state = transitions[tuple_state_addnum]
            else:
                return False
    return initial_state == accept_state