from random import randint
import sys, os
import math as m
from game_rules import *

HUMAN = 'Human'
COMPUTER = 'Computer'
TOKEN_DICT = {'Blank': 0, HUMAN: 1, COMPUTER: 2}


def get_fresh_board(rows, columns):
    game_board = [[0] * columns for i in range(rows)]

    game_state = {}

    for col_idx in range(7):
        game_state[col_idx] = 0

    game_state['holes_left'] = 42
    game_state['score'] = 0

    return game_board, game_state


def display_game(game, score_dict):
    print('--------------------\n')
    for arr in reversed(game):
        print(arr)
    print(score_dict)
    print('\n--------------------\n')


def human_player_turn():
    print('YOUR TURN')
    col = int(input('Choose column between 1 to 7: \n'))
    col_idx = col - 1
    return col_idx


def computer_player_turn_random():
    col = randint(1, 7)
    if 1 <= col <= 7:
        col_idx = col - 1
        return col_idx
    else:
        print('random number generated out of range')
        exit(0)


def init_scores():
    d = {'Human': 0, 'Computer': 0}
    return d


def update_board(board, game_state, player, chosen_col_idx, score_dict):
    max_row_idx = 5

    if player == HUMAN:
        token = 1
    if player == COMPUTER:
        token = 2

    row_idx = game_state[chosen_col_idx]

    if row_idx <= max_row_idx:
        board[row_idx][chosen_col_idx] = token
        game_state[chosen_col_idx] += 1
        game_state['holes_left'] -= 1

        if score_tracking_connect_4(row_idx, chosen_col_idx, token, board):
            score_dict[player] += 1
    else:
        # if player == 'Human':
        #     print('Column =', chosen_col_idx + 1, 'is filled. Choose another col.')
        #     human_col = human_player_turn()
        #     return update_board(board, game_state, 'Human', human_col, score_dict)
        # elif player == 'Computer':
        #     computer_col = computer_player_turn_random()
        #     return update_board(board, game_state, 'Computer', computer_col, score_dict)
        if player == 'Human':
            computer_col = computer_player_turn_random()
            return update_board(board, game_state, 'Computer', computer_col, score_dict)

    return board, game_state, score_dict


def computer_player_turn(board, game_state, token_dict):
    rows, cols = len(board), len(board[0])
    max_row_idx = rows - 1
    pos_score_arr = [None] * cols

    for col_idx in range(cols):
        score = position_score(board, game_state, col_idx, max_row_idx, token_dict)
        pos_score_arr[col_idx] = score
    print('final')
    max_score = max(pos_score_arr)
    # game_state['score'] += max_score
    put_pos_idx = pos_score_arr.index(max_score)
    return put_pos_idx


def main():
    print('Q2 --')
    board, game_state = get_fresh_board(6, 7)
    print('New Game')
    score_dict = init_scores()
    display_game(board, score_dict)

    while game_state['holes_left'] > 0:
        human_col = human_player_turn()
        # human_col = computer_player_turn_random()  # for debug purpose
        board, game_state, score_dict = update_board(board, game_state, HUMAN, human_col, score_dict)
        # display_game(board)
        computer_col = computer_player_turn(board, game_state, TOKEN_DICT)
        board, game_state, score_dict = update_board(board, game_state, COMPUTER, computer_col, score_dict)
        display_game(board, score_dict)

    if score_dict[HUMAN] > score_dict[COMPUTER]:
        print('YOU WIN')
    elif score_dict[HUMAN] < score_dict[COMPUTER]:
        print('YOU LOSE')
    else:
        print('DRAW')
    print('END')


if __name__ == "__main__":
    main()
