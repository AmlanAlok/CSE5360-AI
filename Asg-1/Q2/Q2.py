from random import randint
import sys, os

HUMAN = 'Human'
COMPUTER = 'Computer'


def get_fresh_board(rows, columns):
    game_board = [[0] * columns for i in range(rows)]

    game_state = {}

    for col_idx in range(7):
        game_state[col_idx] = 0

    game_state['holes_left'] = 42

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


def computer_player_turn():
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

        if connect_4(row_idx, chosen_col_idx, token, board):
            score_dict[player] += 1
    else:
        if player == 'Human':
            print('Column =', chosen_col_idx + 1, 'is filled. Choose another col.')
            human_col = human_player_turn()
            return update_board(board, game_state, 'Human', human_col, score_dict)
        elif player == 'Computer':
            computer_col = computer_player_turn()
            return update_board(board, game_state, 'Computer', computer_col, score_dict)

    return board, game_state, score_dict


'''
Checks for 4 consecutive tokens along:
1. Horizontal
2. Vertical
3. Right Diagonal
4. left Diagonal
'''


def connect_4(r, c, token, board, count=0, r_limit=6, c_limit=7):
    if r < r_limit and c < c_limit and board[r][c] == token:
        count += 1

        horizontal = horizontal_count(r, c, c_limit, token, board)
        vertical = vertical_count(r, c, r_limit, token, board)
        left_diag = left_diagonal(r, c, r_limit, c_limit, token, board)
        right_diag = right_diagonal(r, c, r_limit, c_limit, token, board)

        return horizontal or vertical or left_diag or right_diag
    else:
        return False


def left_diagonal(r, c, r_limit, c_limit, token, board):
    count = 0
    i, j = r, c
    while i < r_limit and 0 <= j:
        if board[i][j] == token:
            count += 1
            i += 1
            j -= 1
        else:
            break
    i, j = r, c
    i -= 1
    j += 1
    while 0 <= i and j < c_limit:
        if board[i][j] == token:
            count += 1
            i -= 1
            j += 1
        else:
            break

    return count >= 4


def right_diagonal(r, c, r_limit, c_limit, token, board):
    count = 0
    i, j = r, c
    while i < r_limit and j < c_limit:
        if board[i][j] == token:
            count += 1
            i += 1
            j += 1
        else:
            break
    i, j = r, c
    i -= 1
    j -= 1
    while 0 <= i and 0 <= j:
        if board[i][j] == token:
            count += 1
            i -= 1
            j -= 1
        else:
            break

    return count >= 4


def vertical_count(r, c, r_limit, token, board):
    count = 0
    i = r

    while i < r_limit:
        if board[i][c] == token:
            count += 1
            i += 1
        else:
            break
    j = r - 1
    while 0 <= j:
        if board[j][c] == token:
            count += 1
            j -= 1
        else:
            break
    return count >= 4


def horizontal_count(r, c, c_limit, token, board):
    count = 0
    i = c
    while i < c_limit:
        if board[r][i] == token:
            count += 1
            i += 1
        else:
            break
    j = c - 1
    while 0 <= j:
        if board[r][j] == token:
            count += 1
            j -= 1
        else:
            break

    return count >= 4


def main():
    print('Q2 --')
    board, game_state = get_fresh_board(6, 7)
    print('New Game')
    score_dict = init_scores()
    display_game(board, score_dict)

    while game_state['holes_left'] > 0:
        human_col = human_player_turn()
        board, game_state, score_dict = update_board(board, game_state, HUMAN, human_col, score_dict)
        # display_game(board)
        computer_col = computer_player_turn()
        board, game_state, score_dict = update_board(board, game_state, COMPUTER, computer_col, score_dict)
        display_game(board, score_dict)
    print('END')


if __name__ == "__main__":
    main()
