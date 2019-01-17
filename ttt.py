import sys


class Game(object):
    def __init__(self):
        self.board = ['-']*9  #initiate game board
        self.av_move = []
        self.ai_mov = 0

    def print_board(self):   #print game board
        board = self.board
        for i in range(0, 3):
            sys.stderr.write(board[3*i]+board[3*i+1]+board[3*i+2]+'\n')
        sys.stderr.write('       \n')

    def start(self):  #start the game
     while(True):
        sys.stderr.write('Chose first(x) or second(o)\n')
        chess = sys.stdin.readline().strip()
        if chess == 'X':
            chess = 'x'
        if chess == 'x':
            while True:
                sys.stderr.write('take your move\n')
                move = sys.stdin.readline().strip()
                if self.board[int(move) - 1] != '-':
                    sys.stderr.write('no a valid move, take your move again\n')    #if a valid move
                    move = sys.stdin.readline().strip()
                    self.pl_move(int(move) - 1, chess)
                    self.print_board()
                else:
                    self.pl_move(int(move)-1, chess)
                    self.print_board()
                self.ai_move(self.minimax(self.rev_chess(chess))[1], self.rev_chess(chess))
                self.print_board()
                sys.stdout.write('Ai move:' + str(self.ai_mov) + '\n')
                if self.terminate() == 1:
                    sys.stderr.write('x wins\n')
                    break
                if self.terminate() == -1:
                    sys.stderr.write('o wins\n')
                    break
                if self.terminate() == 0:
                    sys.stderr.write('tie\n')
                    break
        if chess == 'O':
            chess = 'o'
        if chess == 'o':
            while True:
                self.ai_move(self.minimax(self.rev_chess(chess))[1], self.rev_chess(chess))
                self.print_board()
                sys.stdout.write('Ai move:' + str(self.ai_mov) + '\n')
                if self.terminate() == 1:
                    sys.stderr.write('x wins\n')
                    break
                if self.terminate() == -1:
                    sys.stderr.write('o wins\n')
                    break
                if self.terminate() == 0:
                    sys.stderr.write('tie\n')
                    break
                sys.stderr.write('take your move\n')
                move = sys.stdin.readline().strip()
                if self.board[int(move)-1] != '-':
                    sys.stderr.write('not a valid move, take your move again\n')
                    move = sys.stdin.readline().strip()
                    self.pl_move(int(move) - 1, chess)
                    self.print_board()
                else:
                    self.pl_move(int(move) - 1, chess)
                    self.print_board()

    def pl_move(self, move, chess):   #human player move
        board = self.board
        if chess == 'x':
            board[move] = 'x'
        if chess == 'o':
            board[move] = 'o'

    def ai_move(self, move, chess):  #ai move
        board = self.board
        if move == None:
            pass
        else:
            board[move] = chess

    def terminate(self):        #return if the game ends
        board = self.board
        win_combo = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4],
                     board[2:7:2]]
        if ['x', 'x', 'x'] in win_combo:
            return 1
        if ['o', 'o', 'o'] in win_combo:
            return -1
        if '-' not in board:
            return 0
        else:
            return 2

    def search_move(self):  #return all available moves
        self.av_move=[]
        board = self.board
        for i in range(0,len(board)):
            if board[i] == '-':
                self.av_move.append(i)
        return self.av_move

    def rev_chess(self, chess):  #turn 'x' into 'o' or 'o' into 'x'
        if chess == 'x':
            return 'o'
        else:
            return 'x'

    def minimax(self, chess, depth=0):  #minimax function
        if chess == 'o':
            bestscore = -10
        else:
            bestscore = 10
        if self.terminate() != 2:
            if self.terminate() == 1:
                return -10 + depth, None
            elif self.terminate() == 0:
                return 0, None
            elif self.terminate() == -1:
                return 10 - depth, None
        for move in self.search_move():
            self.ai_move(move, chess)
            score, _ = self.minimax(self.rev_chess(chess), depth+1)
            self.board[move] = '-'
            if chess == 'o':
                if score > bestscore:
                    bestscore, bestmove = score, move   #alpha and beta pruning
            else:
                if score < bestscore:
                    bestscore, bestmove = score, move
        self.ai_mov = bestmove + 1
        return bestscore, bestmove


if __name__ == '__main__':
    game1 = Game()
    game1.start()

