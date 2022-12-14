UNDECIDED = -1
PLAYER = 1
DRAW = 0
AI = 2

class TicTacToeGame:
    def __init__(self):
        self.gamestate = UNDECIDED


    def is_moves_left(self, board):
        for i in range(0, 9):
            if board[i] == "":
                return True
        return False


    def check_game_score(self, receivedboard) -> int:
        boardcombinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                             [0, 3, 6], [1, 4, 7], [2, 5, 8],
                             [0, 4, 8], [2, 4, 6]]
        ooccurences = 0
        xoccurences = 0
        for combination in range(len(boardcombinations)):
            for square_index in range(len(boardcombinations[combination])):
                if receivedboard[boardcombinations[combination][square_index]] == 'X':
                    xoccurences += 1
                    if xoccurences == 3:
                        return 10

                if receivedboard[boardcombinations[combination][square_index]] == 'O':
                    ooccurences += 1
                    if ooccurences == 3:
                        return -10

            ooccurences = 0
            xoccurences = 0

        if self.is_moves_left(receivedboard) == True:
            return UNDECIDED
        return DRAW


    def make_move(self, receivedboard) -> dict:
        self.gamestate = self.check_game_score(receivedboard)

        if self.gamestate == UNDECIDED:
            pmove = self.find_best_move(receivedboard)
            if pmove in range(0, 9):
                if receivedboard[int(pmove)] == "":
                    receivedboard[int(pmove)] = 'O'

                    self.gamestate = self.check_game_score(receivedboard)
                    if self.gamestate == UNDECIDED:
                        return {"board": receivedboard,
                                "gamestatus": -1} #undecided
                    else:
                        return {"board": receivedboard,
                                "gamestatus": self.gamestate} #decided

        else:
            return {"board": receivedboard,
                    "gamestatus": self.gamestate} #undecided


    def minimax(self, board, depth, ismax, alpha, beta, position):
        if self.is_moves_left(board):
            score = self.check_game_score(board)

            if score == 10:
                return score

            if score == -10:
                return score

        if not self.is_moves_left(board):
            return 0

        if ismax:
            best = -1000

            for i in range(0, 9):
                if board[i] == "":
                    board[i] = 'X'
                    best = max(best, self.minimax(board, depth + 1, False, alpha, beta, position))
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
                    best = min(best, self.minimax(board, depth + 1, False, alpha, beta, position))
                    beta = min(beta, best)
                    board[i] = ""
                    if beta <= alpha:
                        break
            return best


    def find_best_move(self, board):
        bestval = -1000
        bestmove = -1
        alpha = -1000
        beta = 1000

        for i in range(0, 9):
            if board[i] == "":
                board[i] = 'O'
                moveval = self.minimax(board, 0, False, alpha, beta, i)
                board[i] = ""
                if moveval > bestval:
                    bestmove = i
                    bestval = moveval
                alpha = max(alpha, bestval)
                if beta <= alpha:
                    break

        return bestmove
