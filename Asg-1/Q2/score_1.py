
def countScore(gameBoard):
    player1Score = 0
    player2Score = 0

    # Check horizontally
    for row in gameBoard:
        # Check player 1
        if row[0:4] == [1] * 4:
            player1Score += 1
        if row[1:5] == [1] * 4:
            player1Score += 1
        if row[2:6] == [1] * 4:
            player1Score += 1
        if row[3:7] == [1] * 4:
            player1Score += 1
        # Check player 2
        if row[0:4] == [2] * 4:
            player2Score += 1
        if row[1:5] == [2] * 4:
            player2Score += 1
        if row[2:6] == [2] * 4:
            player2Score += 1
        if row[3:7] == [2] * 4:
            player2Score += 1

    # Check vertically
    for j in range(7):
        # Check player 1
        if (gameBoard[0][j] == 1 and gameBoard[1][j] == 1 and
                gameBoard[2][j] == 1 and gameBoard[3][j] == 1):
            player1Score += 1
        if (gameBoard[1][j] == 1 and gameBoard[2][j] == 1 and
                gameBoard[3][j] == 1 and gameBoard[4][j] == 1):
            player1Score += 1
        if (gameBoard[2][j] == 1 and gameBoard[3][j] == 1 and
                gameBoard[4][j] == 1 and gameBoard[5][j] == 1):
            player1Score += 1
        # Check player 2
        if (gameBoard[0][j] == 2 and gameBoard[1][j] == 2 and
                gameBoard[2][j] == 2 and gameBoard[3][j] == 2):
            player2Score += 1
        if (gameBoard[1][j] == 2 and gameBoard[2][j] == 2 and
                gameBoard[3][j] == 2 and gameBoard[4][j] == 2):
            player2Score += 1
        if (gameBoard[2][j] == 2 and gameBoard[3][j] == 2 and
                gameBoard[4][j] == 2 and gameBoard[5][j] == 2):
            player2Score += 1

    # Check diagonally

    # Check player 1
    if (gameBoard[2][0] == 1 and gameBoard[3][1] == 1 and
            gameBoard[4][2] == 1 and gameBoard[5][3] == 1):
        player1Score += 1
    if (gameBoard[1][0] == 1 and gameBoard[2][1] == 1 and
            gameBoard[3][2] == 1 and gameBoard[4][3] == 1):
        player1Score += 1
    if (gameBoard[2][1] == 1 and gameBoard[3][2] == 1 and
            gameBoard[4][3] == 1 and gameBoard[5][4] == 1):
        player1Score += 1
    if (gameBoard[0][0] == 1 and gameBoard[1][1] == 1 and
            gameBoard[2][2] == 1 and gameBoard[3][3] == 1):
        player1Score += 1
    if (gameBoard[1][1] == 1 and gameBoard[2][2] == 1 and
            gameBoard[3][3] == 1 and gameBoard[4][4] == 1):
        player1Score += 1
    if (gameBoard[2][2] == 1 and gameBoard[3][3] == 1 and
            gameBoard[4][4] == 1 and gameBoard[5][5] == 1):
        player1Score += 1
    if (gameBoard[0][1] == 1 and gameBoard[1][2] == 1 and
            gameBoard[2][3] == 1 and gameBoard[3][4] == 1):
        player1Score += 1
    if (gameBoard[1][2] == 1 and gameBoard[2][3] == 1 and
            gameBoard[3][4] == 1 and gameBoard[4][5] == 1):
        player1Score += 1
    if (gameBoard[2][3] == 1 and gameBoard[3][4] == 1 and
            gameBoard[4][5] == 1 and gameBoard[5][6] == 1):
        player1Score += 1
    if (gameBoard[0][2] == 1 and gameBoard[1][3] == 1 and
            gameBoard[2][4] == 1 and gameBoard[3][5] == 1):
        player1Score += 1
    if (gameBoard[1][3] == 1 and gameBoard[2][4] == 1 and
            gameBoard[3][5] == 1 and gameBoard[4][6] == 1):
        player1Score += 1
    if (gameBoard[0][3] == 1 and gameBoard[1][4] == 1 and
            gameBoard[2][5] == 1 and gameBoard[3][6] == 1):
        player1Score += 1

    if (gameBoard[0][3] == 1 and gameBoard[1][2] == 1 and
            gameBoard[2][1] == 1 and gameBoard[3][0] == 1):
        player1Score += 1
    if (gameBoard[0][4] == 1 and gameBoard[1][3] == 1 and
            gameBoard[2][2] == 1 and gameBoard[3][1] == 1):
        player1Score += 1
    if (gameBoard[1][3] == 1 and gameBoard[2][2] == 1 and
            gameBoard[3][1] == 1 and gameBoard[4][0] == 1):
        player1Score += 1
    if (gameBoard[0][5] == 1 and gameBoard[1][4] == 1 and
            gameBoard[2][3] == 1 and gameBoard[3][2] == 1):
        player1Score += 1
    if (gameBoard[1][4] == 1 and gameBoard[2][3] == 1 and
            gameBoard[3][2] == 1 and gameBoard[4][1] == 1):
        player1Score += 1
    if (gameBoard[2][3] == 1 and gameBoard[3][2] == 1 and
            gameBoard[4][1] == 1 and gameBoard[5][0] == 1):
        player1Score += 1
    if (gameBoard[0][6] == 1 and gameBoard[1][5] == 1 and
            gameBoard[2][4] == 1 and gameBoard[3][3] == 1):
        player1Score += 1
    if (gameBoard[1][5] == 1 and gameBoard[2][4] == 1 and
            gameBoard[3][3] == 1 and gameBoard[4][2] == 1):
        player1Score += 1
    if (gameBoard[2][4] == 1 and gameBoard[3][3] == 1 and
            gameBoard[4][2] == 1 and gameBoard[5][1] == 1):
        player1Score += 1
    if (gameBoard[1][6] == 1 and gameBoard[2][5] == 1 and
            gameBoard[3][4] == 1 and gameBoard[4][3] == 1):
        player1Score += 1
    if (gameBoard[2][5] == 1 and gameBoard[3][4] == 1 and
            gameBoard[4][3] == 1 and gameBoard[5][2] == 1):
        player1Score += 1
    if (gameBoard[2][6] == 1 and gameBoard[3][5] == 1 and
            gameBoard[4][4] == 1 and gameBoard[5][3] == 1):
        player1Score += 1

    # Check player 2
    if (gameBoard[2][0] == 2 and gameBoard[3][1] == 2 and
            gameBoard[4][2] == 2 and gameBoard[5][3] == 2):
        player2Score += 1
    if (gameBoard[1][0] == 2 and gameBoard[2][1] == 2 and
            gameBoard[3][2] == 2 and gameBoard[4][3] == 2):
        player2Score += 1
    if (gameBoard[2][1] == 2 and gameBoard[3][2] == 2 and
            gameBoard[4][3] == 2 and gameBoard[5][4] == 2):
        player2Score += 1
    if (gameBoard[0][0] == 2 and gameBoard[1][1] == 2 and
            gameBoard[2][2] == 2 and gameBoard[3][3] == 2):
        player2Score += 1
    if (gameBoard[1][1] == 2 and gameBoard[2][2] == 2 and
            gameBoard[3][3] == 2 and gameBoard[4][4] == 2):
        player2Score += 1
    if (gameBoard[2][2] == 2 and gameBoard[3][3] == 2 and
            gameBoard[4][4] == 2 and gameBoard[5][5] == 2):
        player2Score += 1
    if (gameBoard[0][1] == 2 and gameBoard[1][2] == 2 and
            gameBoard[2][3] == 2 and gameBoard[3][4] == 2):
        player2Score += 1
    if (gameBoard[1][2] == 2 and gameBoard[2][3] == 2 and
            gameBoard[3][4] == 2 and gameBoard[4][5] == 2):
        player2Score += 1
    if (gameBoard[2][3] == 2 and gameBoard[3][4] == 2 and
            gameBoard[4][5] == 2 and gameBoard[5][6] == 2):
        player2Score += 1
    if (gameBoard[0][2] == 2 and gameBoard[1][3] == 2 and
            gameBoard[2][4] == 2 and gameBoard[3][5] == 2):
        player2Score += 1
    if (gameBoard[1][3] == 2 and gameBoard[2][4] == 2 and
            gameBoard[3][5] == 2 and gameBoard[4][6] == 2):
        player2Score += 1
    if (gameBoard[0][3] == 2 and gameBoard[1][4] == 2 and
            gameBoard[2][5] == 2 and gameBoard[3][6] == 2):
        player2Score += 1

    if (gameBoard[0][3] == 2 and gameBoard[1][2] == 2 and
            gameBoard[2][1] == 2 and gameBoard[3][0] == 2):
        player2Score += 1
    if (gameBoard[0][4] == 2 and gameBoard[1][3] == 2 and
            gameBoard[2][2] == 2 and gameBoard[3][1] == 2):
        player2Score += 1
    if (gameBoard[1][3] == 2 and gameBoard[2][2] == 2 and
            gameBoard[3][1] == 2 and gameBoard[4][0] == 2):
        player2Score += 1
    if (gameBoard[0][5] == 2 and gameBoard[1][4] == 2 and
            gameBoard[2][3] == 2 and gameBoard[3][2] == 2):
        player2Score += 1
    if (gameBoard[1][4] == 2 and gameBoard[2][3] == 2 and
            gameBoard[3][2] == 2 and gameBoard[4][1] == 2):
        player2Score += 1
    if (gameBoard[2][3] == 2 and gameBoard[3][2] == 2 and
            gameBoard[4][1] == 2 and gameBoard[5][0] == 2):
        player2Score += 1
    if (gameBoard[0][6] == 2 and gameBoard[1][5] == 2 and
            gameBoard[2][4] == 2 and gameBoard[3][3] == 2):
        player2Score += 1
    if (gameBoard[1][5] == 2 and gameBoard[2][4] == 2 and
            gameBoard[3][3] == 2 and gameBoard[4][2] == 2):
        player2Score += 1
    if (gameBoard[2][4] == 2 and gameBoard[3][3] == 2 and
            gameBoard[4][2] == 2 and gameBoard[5][1] == 2):
        player2Score += 1
    if (gameBoard[1][6] == 2 and gameBoard[2][5] == 2 and
            gameBoard[3][4] == 2 and gameBoard[4][3] == 2):
        player2Score += 1
    if (gameBoard[2][5] == 2 and gameBoard[3][4] == 2 and
            gameBoard[4][3] == 2 and gameBoard[5][2] == 2):
        player2Score += 1
    if (gameBoard[2][6] == 2 and gameBoard[3][5] == 2 and
            gameBoard[4][4] == 2 and gameBoard[5][3] == 2):
        player2Score += 1

    return player2Score - player1Score