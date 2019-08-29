#!/usr/bin/python3
# Unsing the template offered by Zac Partridge, thanks a lot


###  Question anwser:
# This AI program is implemented by using alpha-beta algorithm

# The main function is ab_pruning() function(implementing alpha-beta algorithm), which is actually a recursive function, return a int value to decide a move to play
#    the function initially set alpha = -9999 and beta = 9999, using get_available_move()function in every recursive to get the child_nodes(branches) of each node
#    after recursive, the function will compute the heuristic value of every child node and return a place where to playin depth 0
#    When more than one value of child nodes in depth 0 are the biggest, use evaluate_singleboard()function to choose the best move to play

# In this program, I design a function to change the default depth of recursive in ab_pruning() to avoid time out.
#    In early move, the function only goes to the depth of 5. Along with the increase of moves(after 15/25/40/60), the default depth is also increased by this function

# In every leaf node, the heuristic value is compute by evaluate() function. the main algorithm to compute it is that
#    checking the X number and O number in every rows, colums and diagonals in every sub_board, if almost win(2 X or 2 O in a row/colum/diagonal),
#    give a bigger heuristic value, otherwise, give a small value. add all 9 sub_boards value to compute the whole heuristic value

# Also In the recursive in ab_pruning(), this program also identify the win state. If any player wins in a recursive, return a very big or very small value(10000 or -10000)
#    depands on which player is playing

# To see the detail of every functions, please see the comments above every functions

import socket
import sys
import numpy as np
import copy

# a board cell can hold:
#   0 - Empty
#   1 - I played here
#   2 - They played here

# the boards are of size 10 because index 0 isn't used
boards = np.zeros((10, 10), dtype="int8")
curr = 0  # this is the current board to play in
move_number = 0


# This function is a support function of ab_pruning(), returning the moves(or child_nodes) that can play in every recursive
def get_available_move(current_move, current_board):
    available_list = []
    for i in range(1, 10):
        if current_board[current_move][i] == 0:
            available_list.append(i)
    return available_list


# This function is the heuristic function
# When the alpha-beta algorithm get the default depth(leaf node), using this function to compute the heuristic value
# When there are 2 X and 1 available moves in a row/colum/diagonal, give more heuristic value(3), but when 2 O and 1 available move, give more minus heuristic value(-3)
# Otherwise, every time we meet there are 1 X or O and 2 available moves in a row/colum/diagonal, heuristic value in every sub board get 1 or -1
def evaluate(current_board):
    my_value = 0
    their_value = 0
    for i in range(1, len(current_board)):
        # for row
        x = 0
        o = 0
        for j in range(1, 4):
            if current_board[i][j] == 1:
                x += 1
            elif current_board[i][j] == 2:
                o += 1
        if x == 1 and o == 0:
            my_value += 1
        elif x == 2 and o == 0:
            my_value += 3
        elif o == 1 and x == 0:
            their_value += 1
        elif o == 2 and x == 0:
            their_value += 3

        x = 0
        o = 0
        for j in range(4, 7):
            if current_board[i][j] == 1:
                x += 1
            elif current_board[i][j] == 2:
                o += 1
        if x == 1 and o == 0:
            my_value += 1
        elif x == 2 and o == 0:
            my_value += 3
        elif o == 1 and x == 0:
            their_value += 1
        elif o == 2 and x == 0:
            their_value += 3

        x = 0
        o = 0
        for j in range(7, 10):
            if current_board[i][j] == 1:
                x += 1
            elif current_board[i][j] == 2:
                o += 1
        if x == 1 and o == 0:
            my_value += 1
        elif x == 2 and o == 0:
            my_value += 3
        elif o == 1 and x == 0:
            their_value += 1
        elif o == 2 and x == 0:
            their_value += 3

        # for colum
        colum_list = [1, 4, 7]
        x = 0
        o = 0
        for j in colum_list:
            if current_board[i][j] == 1:
                x += 1
            elif current_board[i][j] == 2:
                o += 1
        if x == 1 and o == 0:
            my_value += 1
        elif x == 2 and o == 0:
            my_value += 3
        elif o == 1 and x == 0:
            their_value += 1
        elif o == 2 and x == 0:
            their_value += 3

        colum_list = [2, 5, 8]
        x = 0
        o = 0
        for j in colum_list:
            if current_board[i][j] == 1:
                x += 1
            elif current_board[i][j] == 2:
                o += 1
        if x == 1 and o == 0:
            my_value += 1
        elif x == 2 and o == 0:
            my_value += 3
        elif o == 1 and x == 0:
            their_value += 1
        elif o == 2 and x == 0:
            their_value += 3

        colum_list = [3, 6, 9]
        x = 0
        o = 0
        for j in colum_list:
            if current_board[i][j] == 1:
                x += 1
            elif current_board[i][j] == 2:
                o += 1
        if x == 1 and o == 0:
            my_value += 1
        elif x == 2 and o == 0:
            my_value += 3
        elif o == 1 and x == 0:
            their_value += 1
        elif o == 2 and x == 0:
            their_value += 3

        # for diagnoal
        colum_list = [1, 5, 9]
        x = 0
        o = 0
        for j in colum_list:
            if current_board[i][j] == 1:
                x += 1
            elif current_board[i][j] == 2:
                o += 1
        if x == 1 and o == 0:
            my_value += 1
        elif x == 2 and o == 0:
            my_value += 3
        elif o == 1 and x == 0:
            their_value += 1
        elif o == 2 and x == 0:
            their_value += 3

        colum_list = [3, 5, 7]
        x = 0
        o = 0
        for j in colum_list:
            if current_board[i][j] == 1:
                x += 1
            elif current_board[i][j] == 2:
                o += 1
        if x == 1 and o == 0:
            my_value += 1
        elif x == 2 and o == 0:
            my_value += 3
        elif o == 1 and x == 0:
            their_value += 1
        elif o == 2 and x == 0:
            their_value += 3
    final_value = my_value - their_value
    return final_value


# This function is a support function in ab_pruning() function.
# when many branches in depth 0 return same value(alpha value), using this function to choose the best one
# almost the same as evaluate() function, to see the detail, please see the comments above evaluate()
def evaluate_single(current_board, i):
    my_value = 0
    their_value = 0

    # for row
    x = 0
    o = 0
    for j in range(1, 4):
        if current_board[i][j] == 1:
            x += 1
        elif current_board[i][j] == 2:
            o += 1
    if x == 1 and o == 0:
        my_value += 1
    elif x == 2 and o == 0:
        my_value += 3
    elif o == 1 and x == 0:
        their_value += 1
    elif o == 2 and x == 0:
        their_value += 3

    x = 0
    o = 0
    for j in range(4, 7):
        if current_board[i][j] == 1:
            x += 1
        elif current_board[i][j] == 2:
            o += 1
    if x == 1 and o == 0:
        my_value += 1
    elif x == 2 and o == 0:
        my_value += 3
    elif o == 1 and x == 0:
        their_value += 1
    elif o == 2 and x == 0:
        their_value += 3

    x = 0
    o = 0
    for j in range(7, 10):
        if current_board[i][j] == 1:
            x += 1
        elif current_board[i][j] == 2:
            o += 1
    if x == 1 and o == 0:
        my_value += 1
    elif x == 2 and o == 0:
        my_value += 3
    elif o == 1 and x == 0:
        their_value += 1
    elif o == 2 and x == 0:
        their_value += 3

    # for colum
    colum_list = [1, 4, 7]
    x = 0
    o = 0
    for j in colum_list:
        if current_board[i][j] == 1:
            x += 1
        elif current_board[i][j] == 2:
            o += 1
    if x == 1 and o == 0:
        my_value += 1
    elif x == 2 and o == 0:
        my_value += 3
    elif o == 1 and x == 0:
        their_value += 1
    elif o == 2 and x == 0:
        their_value += 3

    colum_list = [2, 5, 8]
    x = 0
    o = 0
    for j in colum_list:
        if current_board[i][j] == 1:
            x += 1
        elif current_board[i][j] == 2:
            o += 1
    if x == 1 and o == 0:
        my_value += 1
    elif x == 2 and o == 0:
        my_value += 3
    elif o == 1 and x == 0:
        their_value += 1
    elif o == 2 and x == 0:
        their_value += 3

    colum_list = [3, 6, 9]
    x = 0
    o = 0
    for j in colum_list:
        if current_board[i][j] == 1:
            x += 1
        elif current_board[i][j] == 2:
            o += 1
    if x == 1 and o == 0:
        my_value += 1
    elif x == 2 and o == 0:
        my_value += 3
    elif o == 1 and x == 0:
        their_value += 1
    elif o == 2 and x == 0:
        their_value += 3

    # for diagnoal
    colum_list = [1, 5, 9]
    x = 0
    o = 0
    for j in colum_list:
        if current_board[i][j] == 1:
            x += 1
        elif current_board[i][j] == 2:
            o += 1
    if x == 1 and o == 0:
        my_value += 1
    elif x == 2 and o == 0:
        my_value += 3
    elif o == 1 and x == 0:
        their_value += 1
    elif o == 2 and x == 0:
        their_value += 3

    colum_list = [3, 5, 7]
    x = 0
    o = 0
    for j in colum_list:
        if current_board[i][j] == 1:
            x += 1
        elif current_board[i][j] == 2:
            o += 1
    if x == 1 and o == 0:
        my_value += 1
    elif x == 2 and o == 0:
        my_value += 3
    elif o == 1 and x == 0:
        their_value += 1
    elif o == 2 and x == 0:
        their_value += 3
    return my_value - their_value

# This function is the implement of alpha-beta pruning algorithm, but adds some details to make the performance better
# Beside the algorithm, this function add the identify of win-state, when win state occurs, the recursive stops,
# return a big value or small value(depands on which player is playing)
# In the depth of 0, instead of returning alpha, this function returns the place(a number) where we play next move
# when in depth 0, if many branchs return the same value(alpha value), using the heuristic function(evaluate_singleboard)
# to choose the best one
def ab_pruning(current_board, current_playing_board, player, alpha, beta, depth):
    if win_state(current_board):
        if player == 1:
            return -10000
        elif player == 2:
            return 10000
    if depth < get_max_iteration():
        templist = get_available_move(current_playing_board, current_board)
        mydic = {}
        if player == 1:
            for i in range(len(templist)):
                copyboard = copy.deepcopy(current_board)
                copyboard[current_playing_board][templist[i]] = player
                this_value = ab_pruning(copyboard, templist[i], switch_player(player), alpha, beta, depth + 1)
                alpha = max(alpha, this_value)
                mydic[templist[i]] = this_value
                # If there are any move that could lead to win, return this move
                if (alpha == 10000 or alpha == 9999) and depth == 0:
                    newdic = {}
                    for k in mydic.keys():
                        if mydic[k] == alpha:
                            newdic[k] = evaluate_single(current_board, k)
                            newdic1 = sorted(newdic.items(), key=lambda x: x[1], reverse=True)
                    return newdic1[0][0]
                if alpha >= beta:
                    return alpha
            if depth == 0:
                print('The heuristic value of every child nodes are')
                print(mydic)
                for i in mydic.keys():
                    if mydic[i] == alpha:
                        return i
            if alpha == -9999 and depth == 0:
                return templist[0]
            return alpha

        elif player == 2:
            for i in range(len(templist)):
                copyboard = copy.deepcopy(current_board)
                copyboard[current_playing_board][templist[i]] = player
                this_value = ab_pruning(copyboard, templist[i], switch_player(player), alpha, beta, depth + 1)
                beta = min(beta, this_value)
                mydic[templist[i]] = this_value
                if alpha >= beta:
                    return beta
            return beta
    else:
        return evaluate(current_board)

# This funcition is a support function of ab_pruning function
# when meeting a win state in a subrecursive, immediately return
# To identify a win state, just check whether a row, colum or diagnoal contains 3 X or 3 O
def win_state(current_board):
    for i in range(1, len(current_board)):
        # for rows
        if current_board[i][1] != 0 and current_board[i][1] == current_board[i][2] == current_board[i][3]:
            return True
        if current_board[i][4] != 0 and current_board[i][4] == current_board[i][5] == current_board[i][6]:
            return True
        if current_board[i][7] != 0 and current_board[i][7] == current_board[i][8] == current_board[i][9]:
            return True
        # for colums
        if current_board[i][1] != 0 and current_board[i][1] == current_board[i][4] == current_board[i][7]:
            return True
        if current_board[i][2] != 0 and current_board[i][2] == current_board[i][5] == current_board[i][8]:
            return True
        if current_board[i][3] != 0 and current_board[i][3] == current_board[i][6] == current_board[i][9]:
            return True
        # for diagnoal
        if current_board[i][1] != 0 and current_board[i][1] == current_board[i][5] == current_board[i][9]:
            return True
        if current_board[i][3] != 0 and current_board[i][3] == current_board[i][5] == current_board[i][7]:
            return True
    return False


# This function is a support function of ab_pruning function
# Changing the player in every recursive
def switch_player(player):
    if player == 1:
        return 2
    elif player == 2:
        return 1

# This function modifys the deep of recursive in alpha-beta pruning algorthm
# In early rounds, the recursive only go to the deep of 5
# in later rounds(after 15), the deep could be increased without timeout
def get_max_iteration():
    max_iteration = 5
    if move_number >= 15 and move_number < 25:
        return 7
    elif move_number >= 25 and move_number < 40:
        return 9
    elif move_number >= 40 and move_number < 60:
        return 11
    elif move_number >= 60:
        return 13
    return max_iteration


def play():
    global move_number
    copyboard = boards.copy()
    # initially alpha = -9999 and beta = 9999, depth = 0
    n = ab_pruning(copyboard, curr, 1, -9999, 9999, 0)
    #print('we play:  ', end='')
    #print(n)
    #print()
    place(curr, n, 1)
    move_number += 1
    return n


def place_for_iter(copyboard, playing_board, num, player):
    copyboard[playing_board][num] = player


# place a move in the global boards
def place(board, num, player):
    global curr
    curr = num
    boards[board][num] = player


# read what the server sent us and
# only parses the strings that are necessary
def parse(string):
    if "(" in string:
        command, args = string.split("(")
        args = args.split(")")[0]
        args = args.split(",")
    else:
        command, args = string, []

    if command == "second_move":
        place(int(args[0]), int(args[1]), 2)
        return play()
    elif command == "third_move":
        # place the move that was generated for us
        place(int(args[0]), int(args[1]), 1)
        # place their last move
        place(curr, int(args[2]), 2)
        return play()
    elif command == "next_move":
        place(curr, int(args[0]), 2)
        return play()
    elif command == "win":
        print("Yay!! We win!! :)")
        return -1
    elif command == "loss":
        print("We lost :(")
        return -1
    return 0


# connect to socket
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(sys.argv[2])  # Usage: ./agent.py -p (port)

    s.connect(('localhost', port))
    while True:
        text = s.recv(1024).decode()
        if not text:
            continue
        for line in text.split("\n"):
            response = parse(line)
            if response == -1:
                s.close()
                return
            elif response > 0:
                s.sendall((str(response) + "\n").encode())


if __name__ == "__main__":
    main()
