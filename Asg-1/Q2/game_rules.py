import sys
import math as m

HUMAN = 'Human'
COMPUTER = 'Computer'
SCORE_LINE_OF_2_1_SIDE = 2
SCORE_LINE_OF_3_1_SIDE = 5
SCORE_CONNECT_4 = 1000
SCORE_CENTER_COL = 4

SCORE_LINE_OF_3_OPPONENT = -100
SCORE_LINE_OF_2_OPPONENT = -2


def score_calculation(r, c, token_dict, board, score, r_limit=6, c_limit=7):

    is_2, score_2 = line_of_2(r, c, token_dict[COMPUTER], board, SCORE_LINE_OF_2_1_SIDE)
    is_3, score_3 = line_of_3(r, c, token_dict[COMPUTER], board, SCORE_LINE_OF_3_1_SIDE)
    is_4 = connect_4(r, c, token_dict[COMPUTER], board)

    opponent_2, oppo_2 = line_of_2(r, c, token_dict[HUMAN], board, SCORE_LINE_OF_2_OPPONENT)
    opponent_3, oppo_3 = line_of_3(r, c, token_dict[HUMAN], board, SCORE_LINE_OF_3_OPPONENT)

    if c == m.floor(c_limit):
        score += SCORE_CENTER_COL
    if is_2:
        score += score_2
    if is_3:
        score += score_3
    if is_4:
        score += SCORE_CONNECT_4

    if oppo_2:
        score -= oppo_2
    if oppo_3:
        score -= oppo_3


def position_score(board, game_state, chosen_col_idx, max_row_idx, token):
    row_idx = game_state[chosen_col_idx]

    if row_idx <= max_row_idx:
        board[row_idx][chosen_col_idx] = token
        game_state[chosen_col_idx] += 1
        game_state['holes_left'] -= 1

        score = game_state['score']

        score_calculation(row_idx, chosen_col_idx, token, board, score)
    else:
        return -sys.maxsize


def line_of_2(r, c, token, board, score_2, count=0, r_limit=6, c_limit=7):
    score = 0

    h_2, h_score = horizontal_line_of_2(r, c, c_limit, token, board, score_2)
    v_2, v_score = vertical_line_of_2(r, c, r_limit, token, board, score_2)
    rd_2, rd_score = right_diagonal_line_of_2(r, c, r_limit, c_limit, token, board, score_2)
    ld_2, ld_score = left_diagonal_line_of_2(r, c, r_limit, c_limit, token, board, score_2)

    if h_2:
        score += h_score
    if v_2:
        score += v_score
    if rd_2:
        score += rd_score
    if ld_2:
        score += ld_score

    if score == 0:
        return False, 0
    return True, score


def left_diagonal_line_of_2(r, c, r_limit, c_limit, token, board, score_2):
    count = 0
    score = 0
    i, j = r, c
    while i < r_limit and 0 <= j:
        if board[i][j] == token:
            count += 1
            i += 1
            j -= 1
        else:
            if board[i][j] == 0:
                score += score_2
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
            if board[i][j] == 0:
                score += score_2
            break

    return count == 2, score


def right_diagonal_line_of_2(r, c, r_limit, c_limit, token, board, score_2):
    count = 0
    score = 0
    i, j = r, c
    while i < r_limit and j < c_limit:
        if board[i][j] == token:
            count += 1
            i += 1
            j += 1
        else:
            if board[i][j] == 0:
                score += score_2
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
            if board[i][j] == 0:
                score += score_2
            break

    return count == 2, score


def vertical_line_of_2(r, c, r_limit, token, board, score_2):
    count = 0
    score = 0
    i = r

    while i < r_limit:
        if board[i][c] == token:
            count += 1
            i += 1
        else:
            if board[i][c] == 0:
                score += score_2
            break
    j = r - 1
    while 0 <= j:
        if board[j][c] == token:
            count += 1
            j -= 1
        else:
            if board[j][c] == 0:
                score += score_2
            break
    return count == 2, score


def horizontal_line_of_2(r, c, c_limit, token, board, score_2):
    count = 0
    score = 0
    i = c
    while i < c_limit:
        if board[r][i] == token:
            count += 1
            i += 1
        else:
            if board[r][i] == 0:
                score += score_2
            break
    j = c - 1
    while 0 <= j:
        if board[r][j] == token:
            count += 1
            j -= 1
        else:
            if board[r][j] == 0:
                score += score_2
            break

    return count == 2, score


def line_of_3(r, c, token, board, score_3, count=0, r_limit=6, c_limit=7):
    score = 0

    h_3, h_score = horizontal_line_of_3(r, c, c_limit, token, board, score_3)
    v_3, v_score = vertical_line_of_3(r, c, r_limit, token, board, score_3)
    rd_3, rd_score = right_diagonal_line_of_3(r, c, r_limit, c_limit, token, board, score_3)
    ld_3, ld_score = left_diagonal_line_of_3(r, c, r_limit, c_limit, token, board, score_3)

    if h_3:
        score += h_score
    if v_3:
        score += v_score
    if rd_3:
        score += rd_score
    if ld_3:
        score += ld_score

    if score == 0:
        return False, 0
    return True, score


def left_diagonal_line_of_3(r, c, r_limit, c_limit, token, board, score_3):
    count = 0
    score = 0
    i, j = r, c
    while i < r_limit and 0 <= j:
        if board[i][j] == token:
            count += 1
            i += 1
            j -= 1
        else:
            if board[i][j] == 0:
                score += score_3
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
            if board[i][j] == 0:
                score += score_3
            break

    return count == 3, score


def right_diagonal_line_of_3(r, c, r_limit, c_limit, token, board, score_3):
    count = 0
    score = 0
    i, j = r, c
    while i < r_limit and j < c_limit:
        if board[i][j] == token:
            count += 1
            i += 1
            j += 1
        else:
            if board[i][j] == 0:
                score += score_3
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
            if board[i][j] == 0:
                score += score_3
            break

    return count == 3, score


def vertical_line_of_3(r, c, r_limit, token, board, score_3):
    count = 0
    score = 0
    i = r

    while i < r_limit:
        if board[i][c] == token:
            count += 1
            i += 1
        else:
            if board[i][c] == 0:
                score += score_3
            break
    j = r - 1
    while 0 <= j:
        if board[j][c] == token:
            count += 1
            j -= 1
        else:
            if board[j][c] == 0:
                score += score_3
            break
    return count == 3, score


def horizontal_line_of_3(r, c, c_limit, token, board, score_3):
    count = 0
    score = 0
    i = c
    while i < c_limit:
        if board[r][i] == token:
            count += 1
            i += 1
        else:
            if board[r][i] == 0:
                score += score_3
            break
    j = c - 1
    while 0 <= j:
        if board[r][j] == token:
            count += 1
            j -= 1
        else:
            if board[r][j] == 0:
                score += score_3
            break

    return count == 3, score


'''
Checks for 4 consecutive tokens along: 
1. Horizontal    2. Vertical    3. Right Diagonal   4. left Diagonal
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
