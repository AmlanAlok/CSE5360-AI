from random import randint


def get_fresh_board():
    game_board = [[0] * 7 for i in range(6)]

    game_state = {}

    for col_idx in range(7):
        game_state[col_idx] = 0

    game_state['holes_left'] = 42

    return game_board, game_state


def display_game(game):
    print('--------------------\n')
    for arr in reversed(game):
        print(arr)
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



def update_board(board, game_state, player, chosen_col_idx):
    max_row_idx = 5

    if player == 'Human':
        token = 1
    if player == 'Computer':
        token = 2

    row_idx = game_state[chosen_col_idx]

    if row_idx <= max_row_idx:
        board[row_idx][chosen_col_idx] = token
        game_state[chosen_col_idx] += 1
        game_state['holes_left'] -= 1
    else:
        if player == 'Human':
            print('Column =', chosen_col_idx + 1, 'is filled. Choose another col.')
            human_col = human_player_turn()
            return update_board(board, game_state, 'Human', human_col)
        elif player == 'Computer':
            computer_col = computer_player_turn()
            return update_board(board, game_state, 'Computer', computer_col)

    return board, game_state


def main():
    print('Q2 --')
    board, game_state = get_fresh_board()
    print('New Game')
    display_game(board)

    while game_state['holes_left'] > 0:
        human_col = human_player_turn()
        board, game_state = update_board(board, game_state, 'Human', human_col)
        # display_game(board)
        computer_col = computer_player_turn()
        board, game_state = update_board(board, game_state, 'Computer', computer_col)
        display_game(board)
    print('END')


if __name__ == "__main__":
    main()
