# Written by Eric Martin for COMP9021


'''
See https://en.wikipedia.org/wiki/Deterministic_finite_automaton

We consider as alphabet a set of digits.

We accept partial transition functions (that is, there might be no transition
for a given state and symbol).

With the accepts() function, we will deal with a single accept state rather than
a set of accept states.

In the test cases below, transitions_2 is the wikipedia example
(with 'S1' and 'S2' renamed as 'state_1' and 'state_2', respectively),
so the automaton that with 'state_1' as both initial and unique accept state,
accepts words with an even number of occurrences of 0's.

'''


def describe_automaton(transitions):
    '''
    The output is produced with the print() function.
    
    >>> transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'}
    >>> describe_automaton(transitions_1)
    When in state "q0" and processing "0", automaton's state becomes "q1".
    When in state "q1" and processing "1", automaton's state becomes "q0".

    >>> transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1',\
                         ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    >>> describe_automaton(transitions_2)
    When in state "state_1" and processing "0", automaton's state becomes "state_2".
    When in state "state_1" and processing "1", automaton's state becomes "state_1".
    When in state "state_2" and processing "0", automaton's state becomes "state_1".
    When in state "state_2" and processing "1", automaton's state becomes "state_2".
    '''
    for (state, symbol) in transitions:
        print(f'When in state "{state}" and processing "{symbol}", '
              f'automaton\'s state becomes "{transitions[state, symbol]}".'
             )

def transitions_as_dict(transitions_as_list):
    '''
    transitions_as_list is a list of strings of the form 'state_1,symbol:state_2'
    where 'state_1' and 'state_2' are words and 'symbol' is one of the 10 digits.
    We assume that there is at most one 'state_2' for given 'state_1' and 'symbol'.
    
    >>> transitions_as_dict(['q0,0:q1', 'q1,1:q0'])
    {('q0', 0): 'q1', ('q1', 1): 'q0'}
    >>> transitions_as_dict(['state_1,0:state_2', 'state_1,1:state_1',\
                             'state_2,0:state_1', 'state_2,1:state_2'])
    {('state_1', 0): 'state_2', ('state_1', 1): 'state_1', \
('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    '''
    transitions = {}
    for state_1__symbol__state_2 in transitions_as_list:
        state_1__symbol, state_2 = state_1__symbol__state_2.split(':')
        state_1, symbol = state_1__symbol.split(',')
        transitions[state_1, int(symbol)] = state_2
    return transitions

def accepts(transitions, word, initial_state, accept_state):
    '''
    Starting in 'initial_state', if the automaton can process with 'transitions'
    all symbols in 'word' and eventually reach 'accept_state', then the function
    returns True; otherwise it returns False.
    
    >>> transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'} 
    >>> accepts(transitions_1, '00', 'q0', 'q1')
    False
    >>> accepts(transitions_1, '2', 'q0', 'q0')
    False
    >>> accepts(transitions_1, '0101010', 'q0', 'q0')
    False
    >>> accepts(transitions_1, '01010101', 'q0', 'q0')
    True
    >>> not accepts(transitions_1, '01', 'q0', 'q1') and\
        accepts(transitions_1, '010', 'q0', 'q1')
    True

    >>> transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1',\
                         ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    >>> accepts(transitions_2, '011', 'state_1', 'state_1')
    False
    >>> accepts(transitions_2, '001110000', 'state_1', 'state_1')
    True
    >>> accepts(transitions_2, '1011100101', 'state_1', 'state_1')
    True
    >>> accepts(transitions_2, '10111000101', 'state_1', 'state_1')
    False
    '''
    if not transitions:
        return False
    current_state = initial_state
    for symbol in word:
        symbol = int(symbol)
        if not (current_state, symbol) in transitions:
            return False
        current_state = transitions[current_state, symbol]
    return current_state == accept_state

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()