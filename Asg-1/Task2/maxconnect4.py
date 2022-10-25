from random import randint
import sys, os
from game_rules import *

HUMAN = 'Human'
COMPUTER = 'Computer'
# TOKEN_DICT = {'Blank': 0, HUMAN: 1, COMPUTER: 2}
TOKEN_DICT = {'Blank': 0, HUMAN: 2, COMPUTER: 1}

def get_fresh_board(rows, columns):
    game_board = [[0] * columns for i in range(rows)]

    game_state = {}

    for col_idx in range(7):
        game_state[col_idx] = 0

    game_state['holes_left'] = 42
    game_state['score'] = 0

    return game_board, game_state


def display_game(game, score_dict):
    # print('--------------------\n')
    for arr in reversed(game):
        print(arr)
    print('============================')
    print(score_dict)
    print('============================')
    # print('\n--------------------\n')


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

    token = TOKEN_DICT[player]

    row_idx = game_state[chosen_col_idx]

    if row_idx <= max_row_idx:
        board[row_idx][chosen_col_idx] = token
        game_state[chosen_col_idx] += 1
        game_state['holes_left'] -= 1

        if score_tracking_connect_4(row_idx, chosen_col_idx, token, board):
            score_dict[player] += 1
    else:
        if player == 'Human':
            print('Column =', chosen_col_idx + 1, 'is filled. Choose another col.')
            human_col = human_player_turn()
            return update_board(board, game_state, 'Human', human_col, score_dict)

    return board, game_state, score_dict


def computer_player_turn(board, game_state, token_dict, max_depth_program_input):

    alpha, beta = -sys.maxsize, sys.maxsize
    hypothetical_board = [[0] * 7 for i in range(6)]

    for r in range(6):
        for c in range(7):
            hypothetical_board[r][c] = board[r][c]

    hypothetical_game_state = game_state.copy()

    best_pos, score = minmax(hypothetical_board, hypothetical_game_state, token_dict, 0, max_depth_program_input, COMPUTER, alpha,
                             beta)
    return best_pos, game_state


'''Min Max Algo implemented'''


def minmax(board, game_state, token_dict, depth, max_depth, player, alpha, beta, row_idx=None, col_idx=None):

    rows, cols = len(board), len(board[0])
    max_row_idx = rows - 1
    pos_score_arr = [0] * cols

    ''' Depth Limiting '''
    if depth == max_depth:
        # return -1, position_score(board, game_state, row_idx, col_idx, max_row_idx, token_dict, player)
        return -1, 0

    if player == COMPUTER:
        for col_idx in range(cols):
            row_idx = game_state[col_idx]
            if row_idx <= max_row_idx:
                board[row_idx][col_idx] = token_dict[COMPUTER]
                game_state[col_idx] += 1
                game_state['holes_left'] -= 1
                curr_score = position_score(board, game_state, row_idx, col_idx, max_row_idx, token_dict, player)
                pos, score = minmax(board, game_state, token_dict, depth + 1, max_depth, HUMAN, row_idx, col_idx)
                pos_score_arr[col_idx] = curr_score + score
                # pos_score_arr[col_idx] = score - curr_score

                board[row_idx][col_idx] = 0
                game_state[col_idx] -= 1
                game_state['holes_left'] += 1

                '''Performing Pruning for MAX node'''
                if pos_score_arr[col_idx] >= beta:
                    break
                elif pos_score_arr[col_idx] > alpha:
                    alpha = pos_score_arr[col_idx]

        max_score = max(pos_score_arr)
        game_state['score'] += max_score

        all_zero = True

        for i in range(len(pos_score_arr)):
            if pos_score_arr[i] != 0:
                all_zero = False

        put_pos_idx = pos_score_arr.index(max_score)

        if all_zero:
            return computer_player_turn_random(), max_score
        return put_pos_idx, max_score

    if player == HUMAN:
        for col_idx in range(cols):
            row_idx = game_state[col_idx]
            if row_idx <= max_row_idx:
                board[row_idx][col_idx] = token_dict[HUMAN]
                game_state[col_idx] += 1
                game_state['holes_left'] -= 1
                curr_score = position_score(board, game_state, row_idx, col_idx, max_row_idx, token_dict, player)
                pos, score = minmax(board, game_state, token_dict, depth + 1, max_depth, COMPUTER, row_idx, col_idx)
                pos_score_arr[col_idx] = curr_score + score
                # pos_score_arr[col_idx] = score - curr_score

                board[row_idx][col_idx] = 0
                game_state[col_idx] -= 1
                game_state['holes_left'] += 1

                '''Performing Pruning for MIN node'''
                if pos_score_arr[col_idx] <= alpha:
                    break
                elif pos_score_arr[col_idx] < beta:
                    beta = pos_score_arr[col_idx]

        min_score = min(pos_score_arr)
        game_state['score'] += min_score

        all_zero = True

        for i in range(len(pos_score_arr)):
            if pos_score_arr[i] != 0:
                all_zero = False

        put_pos_idx = pos_score_arr.index(min_score)

        if all_zero:
            return computer_player_turn_random(), min_score
        return put_pos_idx, min_score


def save_game_board(player, board):
    filename = ''
    if player == HUMAN:
        filename = 'human.txt'
    elif player == COMPUTER:
        filename = 'computer.txt'

    with open(filename, 'w') as f:
        for arr in reversed(board):
            for c in arr:
                f.write(str(c))
            f.write('\n')
        if player == HUMAN:
            f.write(str(TOKEN_DICT[COMPUTER]))
        elif player == COMPUTER:
            f.write(str(TOKEN_DICT[HUMAN]))
        f.close()


def interactive_mode(filename, next_player, depth_limit):
    print('Starting Game in Interactive Mode')
    expected_token = -1

    if os.path.exists(filename):
        input_data, next_player_number = read_input(filename)
        board, game_state = create_game_board(6, 7, input_data)

        if next_player_number == 1:
            expected_token = 1
        elif next_player_number == 2:
            expected_token = 2
        else:
            print(next_player_number, '- this number is not 1 or 2. Hence stopping program.')
            exit(0)
    else:
        print('input file not found. Starting a fresh board.')
        board, game_state = get_fresh_board(6, 7)

    if next_player == 'computer-next':
        turn = COMPUTER
    elif next_player == 'human-next':
        turn = HUMAN
    else:
        print(next_player, '- this number is not computer-next/human-next. Hence stopping program.')
        exit(0)

    if expected_token != -1:
        if turn == COMPUTER and expected_token == 1:
            TOKEN_DICT[COMPUTER] = 1
            TOKEN_DICT[HUMAN] = 2
        elif turn == COMPUTER and expected_token == 2:
            TOKEN_DICT[COMPUTER] = 2
            TOKEN_DICT[HUMAN] = 1
        elif turn == HUMAN and expected_token == 1:
            TOKEN_DICT[HUMAN] = 1
            TOKEN_DICT[COMPUTER] = 2
        elif turn == HUMAN and expected_token == 2:
            TOKEN_DICT[HUMAN] = 2
            TOKEN_DICT[COMPUTER] = 1

    score_dict = init_scores()
    display_game(board, score_dict)

    if game_state['holes_left'] == 0:
        print('Board is full')
        exit(0)

    while game_state['holes_left'] > 0:
        if turn == HUMAN:
            human_col = human_player_turn()
            # human_col = computer_player_turn_random()  # for debug purpose
            board, game_state, score_dict = update_board(board, game_state, HUMAN, human_col, score_dict)
            # display_game(board)
            save_game_board(turn, board)
            turn = COMPUTER
        if turn == COMPUTER:
            computer_col, game_state = computer_player_turn(board, game_state, TOKEN_DICT, depth_limit)
            board, game_state, score_dict = update_board(board, game_state, COMPUTER, computer_col, score_dict)
            display_game(board, score_dict)
            save_game_board(turn, board)
            turn = HUMAN

    if score_dict[HUMAN] > score_dict[COMPUTER]:
        print('YOU WIN')
    elif score_dict[HUMAN] < score_dict[COMPUTER]:
        print('YOU LOSE')
    else:
        print('DRAW')
    print('END')


def clean_data(line):
    return list(line.replace('\n', ''))


def read_input(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()

        ''' Last line says who plays next '''
        next_player_token = int(input_data.pop())

        clean_input = list(map(clean_data, input_data))
        f.close()
    return clean_input, next_player_token


def create_game_board(rows, columns, input_data):
    game_board = [[0] * columns for i in range(rows)]
    game_state = {}
    total_zeros = 0

    for col_idx in range(7):
        game_state[col_idx] = 0

    for c in range(columns):
        s = 0
        for r in range(rows - 1, -1, -1):
            data_point = int(input_data[r][c])
            if data_point != 0:
                game_board[rows - 1 - r][c] = data_point
                s += 1
            else:
                total_zeros += 1
        game_state[c] = s

    game_state['holes_left'] = total_zeros
    game_state['score'] = 0

    return game_board, game_state


def one_move_mode():
    filename = 'input3.txt'
    input_data, next_player_token = read_input(filename)
    board, game_state = create_game_board(6, 7, input_data)
    score_dict = init_scores()
    display_game(board, score_dict)

    turn = next_player_token
    p = 0
    while p < 2:
        if turn == 1:
            human_col = human_player_turn()
            # human_col = computer_player_turn_random()  # for debug purpose
            board, game_state, score_dict = update_board(board, game_state, HUMAN, human_col, score_dict)

            turn = 2
        if turn == 2:
            computer_col, game_state = computer_player_turn(board, game_state, TOKEN_DICT)
            board, game_state, score_dict = update_board(board, game_state, COMPUTER, computer_col, score_dict)
            turn = 1
        display_game(board, score_dict)
        p += 1

    if score_dict[HUMAN] > score_dict[COMPUTER]:
        print('YOU WIN')
    elif score_dict[HUMAN] < score_dict[COMPUTER]:
        print('YOU LOSE')
    else:
        print('DRAW')
    print('END')


def main():
    print('START Task 2')
    # print(sys.argv)

    mode = sys.argv[1]
    input_filename = sys.argv[2]
    next_player = sys.argv[3]
    depth_limit = int(sys.argv[4])

    print(mode, input_filename, next_player, depth_limit)

    # one_move_mode()
    interactive_mode(input_filename, next_player, depth_limit)


if __name__ == "__main__":
    main()
