import sys


class Game(object):
    def __init__(self):
        self.board = [['-'for i in range(9)]for j in range(9)]
        self.ai_mov = 0
        self.max_depth = 5

    def print_board(self):    #print board
        board = self.board
        for i in range(0, 3):
            for j in range(0, 3):
                sys.stderr.write(board[3 * i][3 * j] + board[3 * i][3 * j + 1] + board[3 * i][3 * j + 2] + ' ' + board[3 * i + 1][3 * j] + board[3 * i + 1][3 * j + 1] + board[3 * i + 1][3 * j + 2] + ' ' + board[3 * i + 2][3 * j] + board[3 * i + 2][3 * j + 1] + board[3 * i + 2][3 * j + 2]+'\n')
            if i == 1 or 2:
                sys.stderr.write('             \n')

    def start(self):    #start the game
      while(True):
        sys.stderr.write('Chose first(x) or second(o)')
        chess = sys.stdin.readline().strip()
        if chess == 'X':
            chess == 'x'
        if chess == 'x':
            while(self.terminate() == 2):
                sys.stderr.write('take your move')
                move = sys.stdin.readline().strip()
                if self.board[((int(move)/10) % 10)-1][((int(move)/1) % 10)-1] != '-':
                    sys.stderr.write('not a valid move, take your move again\n')
                    move = sys.stdin.readline().strip()
                    self.pl_move(move, chess)
                    self.print_board()
                    sys.stderr.write('             \n')
                else:
                    self.pl_move(move, chess)
                    self.print_board()
                    sys.stderr.write('             \n')
                self.ai_move(self.minimax((int(move) / 1) % 10, self.rev_chess(chess), self.max_depth)[1],
                             self.rev_chess(chess))
                self.print_board()
                sys.stderr.write('             \n')
                sys.stdout.write('Ai move:' + str(self.ai_mov) + '\n')
                if self.terminate() == 1:
                    sys.stderr.write('x wins')
                    break
                if self.terminate() == -1:
                    sys.stderr.write('o wins')
                    break
                if self.terminate() == 0:
                    sys.stderr.write('tie')
                    break
        if chess == 'O':
            chess = 'o'
        if chess =='o':
            self.board[4][4] = self.rev_chess(chess)
            sys.stdout.write('Ai move:55\n')
            while(self.terminate() == 2):
                self.print_board()
                sys.stderr.write('take your move')
                move = sys.stdin.readline().strip()
                if self.board[((int(move)/10) % 10)-1][((int(move)/1) % 10)-1] != '-':
                    sys.stderr.write('not a valid move, take your move again\n')
                    move = sys.stdin.readline().strip()
                    self.pl_move(move, chess)
                    self.print_board()
                    sys.stderr.write('             \n')
                else:
                    self.pl_move(move, chess)
                    self.print_board()
                    sys.stderr.write('             \n')
                self.ai_move(self.minimax((int(move)/1) % 10, self.rev_chess(chess), self.max_depth)[1],self.rev_chess(chess))
                sys.stdout.write('Ai move:' + str(self.ai_mov) + '\n')
                if self.terminate() == 1:
                    sys.stderr.write('x wins')
                    break
                if self.terminate() == -1:
                    sys.stderr.write('o wins')
                    break
                if self.terminate() == 0:
                    sys.stderr.write('tie')
                    break

    def pl_move(self, move, chess):   #human move
        board = self.board
        x = (int(move)/10) % 10
        y = (int(move)/1) % 10
        board[x-1][y-1] = chess

    def ai_move(self, move, chess):   #ai move
        board = self.board
        if move == None:
            pass
        else:
            x = (int(move) / 10) % 10
            y = (int(move) / 1) % 10
            board[x-1][y-1] = chess

    def terminate(self):      #return if the game ends
        board = self.board
        win_combo = [board[0:3], board[3:6], board[6:9], board[0::3], board[1::3], board[2::3], board[0::4],
                     board[2:7:2]]
        all_element = []
        for i in range(0, 9):
            for j in range(0, 9):
                all_element.append(board[i][j])
            if ['x', 'x', 'x'] in [board[i][0:3], board[i][3:6], board[i][6:9], board[i][0::3], board[i][1::3], board[i][2::3], board[i][0::4],
                     board[i][2:7:2]]:
                return 1
            if ['o', 'o', 'o'] in [board[i][0:3], board[i][3:6], board[i][6:9], board[i][0::3], board[i][1::3], board[i][2::3], board[i][0::4],
                     board[i][2:7:2]]:
                return -1
            if '-' not in all_element:
                return 0
        else:
            return 2

    def rev_chess(self, chess):
        if chess == 'x':
            return 'o'
        else:
            return 'x'

    def search_move(self, num_board):     #return all available moves
        self.av_move=[]
        board = self.board
        for i in range(0,9):
            if board[num_board-1][i] == '-':
                self.av_move.append(num_board*10+(i+1))
        return self.av_move

    def evaluate(self, chess):      #return a score, to evaluate each move of minimax
        board = self.board
        score = [0]*9
        total_score = 0
        for i in range(0, 9):    #all the combination of Z_Z and ZZ_
            potent_win = [[board[i][0],board[i][1],board[i][2]],[board[i][1],board[i][2],board[i][0]],[board[i][3],board[i][4],board[i][5]]
                ,[board[i][4],board[i][5],board[i][3]],[board[i][6],board[i][7],board[i][8]],[board[i][7],board[i][8],board[i][6]],[board[i][0],board[i][3],board[i][6]]
                ,[board[i][3],board[i][6],board[i][0]],[board[i][1],board[i][4],board[i][7]],[board[i][4],board[i][7],board[i][1]],[board[i][2],board[i][5],board[i][8]]
                ,[board[i][5],board[i][8],board[i][2]],[board[i][0],board[i][4],board[i][8]],[board[i][4],board[i][8],board[i][0]],[board[i][2],board[i][4],board[i][6]]
                ,[board[i][4],board[i][6],board[i][2]],[board[i][0],board[i][2],board[i][1]],[board[i][3],board[i][5],board[i][4]],[board[i][6],board[i][8],board[i][7]]
                ,[board[i][0],board[i][6],board[i][3]],[board[i][1],board[i][7],board[i][4]],[board[i][2],board[i][8],board[i][5]],[board[i][0],board[i][8],board[i][4]]
                ,[board[i][2],board[i][6]],board[i][4]]
            for j in range(0, 24):
                if [chess, chess, '-'] == potent_win[j]:
                   score[i] += 1
                if [self.rev_chess(chess),self.rev_chess(chess),'-'] == potent_win[j]:
                   score[i] -= 1
            total_score += score[i]
        return total_score

    def minimax(self, num_board, chess, max_depth, depth=0):
        if chess =='o':
            bestscore=float('-inf')
        else:
            bestscore=float('inf')
        if self.terminate() != 2:
            if self.terminate() == 1:
                return -100, None
            elif self.terminate() == 0:
                return 0, None
            elif self.terminate() == -1:
                return 100, None
        if max_depth == depth:
            return self.evaluate(chess), None
        scores = []
        for move in self.search_move(num_board):
            self.ai_move(move, chess)
            score, _ = self.minimax((int(move)/1) % 10, self.rev_chess(chess), max_depth, depth+1)
            self.board[((int(move)/10)%10)-1][((int(move)/1)%10)-1] = '-'
            if chess == 'o':
                if score > bestscore:
                    bestscore, bestmove = score, move     #alpha beta pruning
            else:
                if score < bestscore:
                    bestscore, bestmove = score, move
        self.ai_mov = bestmove
        return bestscore, bestmove


if __name__ == '__main__':
    game1 = Game()
    game1.start()

