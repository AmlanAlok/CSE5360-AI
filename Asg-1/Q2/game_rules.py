import sys
import math as m

SCORE_LINE_OF_3_1_SIDE = 5
SCORE_CONNECT_4 = 1000
SCORE_CENTER_COL = 4


def score_calculation(r, c, token, board, score, r_limit=6, c_limit=7):
    is_3, score_3 = line_of_3(r, c, token, board)
    is_4 = connect_4(r, c, token, board)

    if c == m.floor(c_limit):
        score += SCORE_CENTER_COL
    if is_3:
        score += score_3
    if is_4:
        score += SCORE_CONNECT_4


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


def line_of_3(r, c, token, board, count=0, r_limit=6, c_limit=7):
    score = 0

    h_3, h_score = horizontal_line_of_3(r, c, c_limit, token, board)
    v_3, v_score = vertical_line_of_3(r, c, r_limit, token, board)
    rd_3, rd_score = right_diagonal_line_of_3(r, c, r_limit, c_limit, token, board)
    ld_3, ld_score = left_diagonal(r, c, r_limit, c_limit, token, board)

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


def left_diagonal(r, c, r_limit, c_limit, token, board):
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
                score += SCORE_LINE_OF_3_1_SIDE
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
                score += SCORE_LINE_OF_3_1_SIDE
            break

    return count == 3, score


def right_diagonal_line_of_3(r, c, r_limit, c_limit, token, board):
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
                score += SCORE_LINE_OF_3_1_SIDE
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
                score += SCORE_LINE_OF_3_1_SIDE
            break

    return count >= 3, score


def vertical_line_of_3(r, c, r_limit, token, board):
    count = 0
    score = 0
    i = r

    while i < r_limit:
        if board[i][c] == token:
            count += 1
            i += 1
        else:
            if board[i][c] == 0:
                score += SCORE_LINE_OF_3_1_SIDE
            break
    j = r - 1
    while 0 <= j:
        if board[j][c] == token:
            count += 1
            j -= 1
        else:
            if board[j][c] == 0:
                score += SCORE_LINE_OF_3_1_SIDE
            break
    return count == 3, score


def horizontal_line_of_3(r, c, c_limit, token, board):
    count = 0
    score = 0
    i = c
    while i < c_limit:
        if board[r][i] == token:
            count += 1
            i += 1
        else:
            if board[r][i] == 0:
                score += SCORE_LINE_OF_3_1_SIDE
            break
    j = c - 1
    while 0 <= j:
        if board[r][j] == token:
            count += 1
            j -= 1
        else:
            if board[r][j] == 0:
                score += SCORE_LINE_OF_3_1_SIDE
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
