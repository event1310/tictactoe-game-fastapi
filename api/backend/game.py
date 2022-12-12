def is_moves_left(board):
    for i in range(0, 9):
        if board[i] == "":
            return True
    return True


def check_game_state(board) -> int:
    if is_moves_left(board):
        boardcombinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                             [0, 3, 6], [1, 4, 7], [2, 5, 8],
                             [0, 4, 8], [2, 4, 6]]
        ooccurences = 0
        xoccurences = 0
        for combination in range(len(boardcombinations)):
            for square_index in range(len(boardcombinations[combination])):
                if board[boardcombinations[combination][square_index]] == 'X':
                    xoccurences += 1
                    if xoccurences == 3:
                        return 10

                if board[boardcombinations[combination][square_index]] == 'O':
                    ooccurences += 1
                    if ooccurences == 3:
                        return -10

            ooccurences = 0
            xoccurences = 0

        return -1
    else:
        return 0


def handle_game(board):
    while make_move(board)["gamestatus"] != -1:
        print("make_move called")
        return False

    return True


def make_move(board) -> dict:
    current_result = check_game_state(board)

    if current_result == -1:
        pmove = find_best_move(board)
        if pmove in range(0, 9):
            if board[int(pmove)] == "":
                board[int(pmove)] = 'O'

                current_result = check_game_state(board)
                if current_result == -1:
                    return {"board": board,
                            "gamestatus": -1} #undecided
                else:
                    return {"board": board,
                            "gamestatus": current_result} #decided

    else:
        return {"board": board,
                "gamestatus": current_result} #undecided


def minimax(board, depth, ismax, alpha, beta, position):
    if is_moves_left(board):
        score = check_game_state(board)

        if score == 10:
            return score

        if score == -10:
            return score

    if not is_moves_left(board):
        return 0

    if ismax:
        best = -1000

        for i in range(0, 9):
            if board[i] == "":
                board[i] = 'X'
                best = max(best, minimax(board, depth + 1, False, alpha, beta, position))
                alpha = max(alpha, best)
                board[i] = ""
                if beta <= alpha:
                    break
        return best

    else:
        best = 1000

        for i in range(0, 9):
            if board[i] == "":
                board[i] = 'O'
                best = min(best, minimax(board, depth + 1, False, alpha, beta, position))
                beta = min(beta, best)
                board[i] = ""
                if beta <= alpha:
                    break
        return best


def find_best_move(board):
    bestval = -1000
    bestmove = -1
    alpha = -1000
    beta = 1000

    for i in range(0, 9):
        if board[i] == "":
            board[i] = 'O'
            moveval = minimax(board, 0, False, alpha, beta, i)
            board[i] = ""
            if moveval > bestval:
                bestmove = i
                bestval = moveval
            alpha = max(alpha, bestval)
            if beta <= alpha:
                break

    return bestmove