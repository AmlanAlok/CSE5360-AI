import math as m

HUMAN = 'Human'
COMPUTER = 'Computer'
SCORE_LINE_OF_2_1_SIDE = 2
'''SCORE_LINE_OF_3_1_SIDE must be more than SCORE_LINE_OF_3_OPPONENT 
to choose connect 3 of yours rather than stopping 3 of the opponent'''
SCORE_LINE_OF_3_1_SIDE = 20
SCORE_CONNECT_4 = 5000
SCORE_CENTER_COL = 4

SCORE_LINE_OF_4_OPPONENT = 2000
SCORE_LINE_OF_3_OPPONENT = 15
SCORE_LINE_OF_2_OPPONENT = 2


def score_calculation(r, c, token_dict, board, score, hypothetical_game_state, player, r_limit=6, c_limit=7):

    if player == COMPUTER:
        max_player, min_player = COMPUTER, HUMAN
    if player == HUMAN:
        max_player, min_player = HUMAN, COMPUTER

    is_2, score_2 = line_of_2(r, c, token_dict[max_player], board, SCORE_LINE_OF_2_1_SIDE, hypothetical_game_state)
    is_3, score_3 = line_of_3(r, c, token_dict[max_player], board, SCORE_LINE_OF_3_1_SIDE, hypothetical_game_state)
    is_4, score_4 = connect_4(r, c, token_dict[max_player], board, SCORE_CONNECT_4)

    board[r][c] = token_dict[min_player]

    opponent_2, oppo_2 = line_of_2(r, c, token_dict[min_player], board, SCORE_LINE_OF_2_OPPONENT, hypothetical_game_state)
    opponent_3, oppo_3 = line_of_3(r, c, token_dict[min_player], board, SCORE_LINE_OF_3_OPPONENT, hypothetical_game_state)
    opponent_4, oppo_4 = connect_4(r, c, token_dict[min_player], board, SCORE_LINE_OF_4_OPPONENT)

    board[r][c] = token_dict[max_player]

    if c == m.floor(c_limit / 2) and r == 0:
        score += SCORE_CENTER_COL
    if is_2:
        score += score_2
    if is_3:
        score += score_3
    if is_4:
        score += score_4

    if oppo_2:
        score += oppo_2
    if opponent_3:
        score += oppo_3
    if opponent_4:
        score += oppo_4

    return score


def position_score(board, game_state, row_idx, chosen_col_idx, max_row_idx, token_dict, player):

    # score = game_state['score']
    score = 0
    add_score = score_calculation(row_idx, chosen_col_idx, token_dict, board, score, game_state, player)
    score += add_score
    # hypothetical_game_state['score'] = score
    return score
    # else:
    #     return -sys.maxsize


def line_of_2(r, c, token, board, score_2, hypothetical_game_state, count=0, r_limit=6, c_limit=7):
    score = 0

    h_2, h_score = horizontal_line_of_2(r, c, c_limit, token, board, score_2, hypothetical_game_state)
    v_2, v_score = vertical_line_of_2(r, c, r_limit, token, board, score_2)
    rd_2, rd_score = right_diagonal_line_of_2(r, c, r_limit, c_limit, token, board, score_2, hypothetical_game_state)
    ld_2, ld_score = left_diagonal_line_of_2(r, c, r_limit, c_limit, token, board, score_2, hypothetical_game_state)

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


def left_diagonal_line_of_2(r, c, r_limit, c_limit, token, board, score_2, hypothetical_game_state):
    count = 0
    score = 0
    i, j = r, c
    while i < r_limit and 0 <= j:
        if board[i][j] == token:
            if hypothetical_game_state[j] - 1 == i:
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
            if hypothetical_game_state[j] - 1 == i:
                count += 1
            i -= 1
            j += 1
        else:
            if board[i][j] == 0:
                score += score_2
            break

    return count == 2, score


def right_diagonal_line_of_2(r, c, r_limit, c_limit, token, board, score_2, hypothetical_game_state):
    count = 0
    score = 0
    i, j = r, c
    while i < r_limit and j < c_limit:
        if board[i][j] == token:
            if hypothetical_game_state[j] - 1 == i:
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
            if hypothetical_game_state[j] - 1 == i:
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


def horizontal_line_of_2(r, c, c_limit, token, board, score_2, hypothetical_game_state):
    count = 0
    score = 0
    i = c
    while i < c_limit:
        if board[r][i] == token:
            if hypothetical_game_state[i] - 1 == r:
                count += 1
            i += 1
        else:
            if board[r][i] == 0:
                score += score_2
            break
    j = c - 1
    while 0 <= j:
        if board[r][j] == token:
            if hypothetical_game_state[j] - 1 == r:
                count += 1
            j -= 1
        else:
            if board[r][j] == 0:
                score += score_2
            break

    return count == 2, score


def line_of_3(r, c, token, board, score_3, hypothetical_game_state, count=0, r_limit=6, c_limit=7):
    score = 0

    h_3, h_score = horizontal_line_of_3(r, c, c_limit, token, board, score_3, hypothetical_game_state)
    v_3, v_score = vertical_line_of_3(r, c, r_limit, token, board, score_3)
    rd_3, rd_score = right_diagonal_line_of_3(r, c, r_limit, c_limit, token, board, score_3, hypothetical_game_state)
    ld_3, ld_score = left_diagonal_line_of_3(r, c, r_limit, c_limit, token, board, score_3, hypothetical_game_state)

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


def left_diagonal_line_of_3(r, c, r_limit, c_limit, token, board, score_3, hypothetical_game_state):
    count = 0
    score = 0
    i, j = r, c
    while i < r_limit and 0 <= j:
        if board[i][j] == token:
            if hypothetical_game_state[j] - 1 == i:
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
            if hypothetical_game_state[j] - 1 == i:
                count += 1
            i -= 1
            j += 1
        else:
            if board[i][j] == 0:
                score += score_3
            break

    return count == 3, score


def right_diagonal_line_of_3(r, c, r_limit, c_limit, token, board, score_3, hypothetical_game_state):
    count = 0
    score = 0
    i, j = r, c
    while i < r_limit and j < c_limit:
        if board[i][j] == token:
            if hypothetical_game_state[j] - 1 == i:
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
            if hypothetical_game_state[j] - 1 == i:
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


def horizontal_line_of_3(r, c, c_limit, token, board, score_3, hypothetical_game_state):
    count = 0
    score = 0
    i = c
    while i < c_limit:
        if board[r][i] == token:
            if hypothetical_game_state[i]-1 == r:
                count += 1
            i += 1
        else:
            if board[r][i] == 0:
                score += score_3
            break
    j = c - 1
    while 0 <= j:
        if board[r][j] == token:
            if hypothetical_game_state[j] - 1 == r:
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


def connect_4(r, c, token, board, score_4, count=0, r_limit=6, c_limit=7):
    # if r < r_limit and c < c_limit and board[r][c] == token:
    #     count += 1
    #
    #     horizontal = horizontal_count(r, c, c_limit, token, board, score_4)
    #     vertical = vertical_count(r, c, r_limit, token, board, score_4)
    #     left_diag = left_diagonal(r, c, r_limit, c_limit, token, board, score_4)
    #     right_diag = right_diagonal(r, c, r_limit, c_limit, token, board, score_4)
    #
    #     return horizontal or vertical or left_diag or right_diag
    # else:
    #     return False
    score = 0
    # if r < r_limit and c < c_limit and board[r][c] == token:
    horizontal, h_score = horizontal_count(r, c, c_limit, token, board, score_4)
    vertical, v_score = vertical_count(r, c, r_limit, token, board, score_4)
    left_diag, ld_score = left_diagonal(r, c, r_limit, c_limit, token, board, score_4)
    right_diag, rd_score = right_diagonal(r, c, r_limit, c_limit, token, board, score_4)

    if horizontal:
        score += h_score
    if vertical:
        score += v_score
    if left_diag:
        score += ld_score
    if right_diag:
        score += rd_score

    if score == 0:
        return False, 0
    return True, score
    # else:
    #     return False, score


def left_diagonal(r, c, r_limit, c_limit, token, board, score_4):
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

    return count >= 4, score_4


def right_diagonal(r, c, r_limit, c_limit, token, board, score_4):
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

    return count >= 4, score_4


def vertical_count(r, c, r_limit, token, board, score_4):
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
    return count >= 4, score_4


def horizontal_count(r, c, c_limit, token, board, score_4):
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

    return count >= 4, score_4


def score_tracking_connect_4(r, c, token, board, score_4=SCORE_CONNECT_4, count=0, r_limit=6, c_limit=7):
    if r < r_limit and c < c_limit and board[r][c] == token:
        count += 1

        horizontal, h_score = horizontal_count(r, c, c_limit, token, board, score_4)
        vertical, v_score = vertical_count(r, c, r_limit, token, board, score_4)
        left_diag, ld_score = left_diagonal(r, c, r_limit, c_limit, token, board, score_4)
        right_diag, rd_score = right_diagonal(r, c, r_limit, c_limit, token, board, score_4)

        return horizontal or vertical or left_diag or right_diag
    else:
        return False
