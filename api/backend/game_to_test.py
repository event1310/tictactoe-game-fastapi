import random

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
                        return 999

                if receivedboard[boardcombinations[combination][square_index]] == 'O':
                    ooccurences += 1
                    if ooccurences == 3:
                        return -999

            ooccurences = 0
            xoccurences = 0

        if self.is_moves_left(receivedboard) == True:
            return UNDECIDED
        return DRAW

    def make_move(self, receivedboard):
        self.gamestate = self.check_game_score(receivedboard)

        if self.gamestate == UNDECIDED:
            if not "O" in receivedboard:
                first_pmove_index = receivedboard.index("X")
                first_aimove_range = list(range(0, first_pmove_index)) + list(range(first_pmove_index+1, 9))
                print(first_aimove_range)
                randommove = random.choice(first_aimove_range)
                print(randommove)
                receivedboard[int(randommove)] = "O"
                print(f"{receivedboard[0:3]}")
                print(f"{receivedboard[3:6]}")
                print(f"{receivedboard[6:9]}")

            else:
                pmove = self.find_best_move(receivedboard)
                if pmove in range(0, 9):
                    if receivedboard[int(pmove)] == "":
                        receivedboard[int(pmove)] = 'O'

                        self.gamestate = self.check_game_score(receivedboard)
                        if self.gamestate == UNDECIDED:
                            print(f"{receivedboard[0:3]}")
                            print(f"{receivedboard[3:6]}")
                            print(f"{receivedboard[6:9]}")

                        else:
                            print(f"{receivedboard[0:3]}")
                            print(f"{receivedboard[3:6]}")
                            print(f"{receivedboard[6:9]}")


        else:
            print(f"{receivedboard[0:3]}")
            print(f"{receivedboard[3:6]}")
            print(f"{receivedboard[6:9]}")

    def minimax(self, board, depth, ismax, alpha, beta):
        if self.is_moves_left(board):
            score = self.check_game_score(board)

            if score == 999:
                return score

            if score == -999:
                return score

        if not self.is_moves_left(board):
            return self.check_game_score(board)

        if ismax:
            best = -100000

            for i in range(0, 9):
                if board[i] == "":
                    board[i] = 'X'
                    #print(self.minimax(board, depth + 1, True, alpha, beta))
                    best = max(best, self.minimax(board, depth, True, alpha, beta))
                    alpha = max(alpha, best)
                    board[i] = ""
                    if beta <= alpha:
                        break
            return best

        else:
            best = 100000

            for i in range(0, 9):
                if board[i] == "":
                    board[i] = 'O'
                    print(f"{self.minimax(board, depth, False, alpha, beta)}")
                    print(board[0:3])
                    print(board[3:6])
                    print(board[6:9])
                    best = min(best, self.minimax(board, depth, False, alpha, beta))
                    beta = min(beta, best)
                    board[i] = ""
                    if beta <= alpha:
                        break
            return best

    def find_best_move(self, board):
        bestval = -100000
        bestmove = -1
        alpha = -100000
        beta = 100000

        for i in range(0, 9):
            if board[i] == "":
                board[i] = 'O'
                moveval = self.minimax(board, 0, False, alpha, beta)
                board[i] = ""
                if moveval > bestval:
                    bestmove = i
                    bestval = moveval
                alpha = max(alpha, bestval)
                if beta <= alpha:
                    break

        return bestmove

testgame = TicTacToeGame()
testboard = ['X', 'O', '',
             'X', 'O', 'X',
             '', '', '']
testgame.make_move(testboard)