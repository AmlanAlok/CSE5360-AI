


def get_fresh_board():
    return [[0] * 7 for i in range(6)]

def display_game(game):

    for arr in game:
        print(arr)



def main():
    print('Q2 --')
    board = get_fresh_board()
    display_game(board)
    print('END')


if __name__ == "__main__":
    main()
