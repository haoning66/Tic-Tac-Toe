Hi, I am readme.

Environment: Mac OS 10.13.6  python2.7.10 

There are three files, ttt1.py is for basic TTT, ttt2.py is for advanced TTT, ttt3.py is for super TTT.
 
Basic TTT:
First input 'x' or 'o', to decide whether you want to go first or second, then input a one-digit number to take your move, each number represents one position of the board as follows. Repeat the second step until the game ends.
1  2  3
—— —— ——
4  5  6
—— —— ——
7  8  9
—— —— ——

Advanced TTT:
You have nine 3x3 TTT boards arranged in a 3x3 grid. The goal of the game is to win a single one of the boards like in regular TTT. However there is one crucial constraint: If a player has just played at some position on some board, then the next player must play on the board in the corresponding position in the grid. For example, if a player marks the bottom right position, position 9, of any board, then the next player must mark any open space on the bottom right board (the board at position 9). The first player to play can play anywhere. If the board required by the preceding rule is full, the player can play on any board.

First input 'x' or 'o', to decide whether you want to go first or second, then input a two-digit number to take your move, the tens digit of the number indicates which board you will take, the units digit indicates which position of the board you want to take. Repeat the second step until the game ends.
 
11 12 13  21 22 23  31 32 33
—— —— ——  —— —— ——  —— —— —— 
14 15 16  24 25 26  34 35 36
—— —— ——  —— —— ——  —— —— —— 
17 18 19  27 28 29  37 38 39
—— —— ——  —— —— ——  —— —— ——

41 42 43  51 52 53  61 62 63
—— —— ——  —— —— ——  —— —— ——
44 45 46  54 55 56  64 65 66
—— —— ——  —— —— ——  —— —— ——
47 48 49  57 58 59  67 68 69
—— —— ——  —— —— ——  —— —— ——

71 72 73  81 82 83  91 92 93
—— —— ——  —— —— ——  —— —— ——
74 75 76  84 85 86  94 95 96
—— —— ——  —— —— ——  —— —— ——
77 78 79  87 88 89  97 98 99
—— —— ——  —— —— ——  —— —— ——

Super TTT:
The rule is the same with Advanced TTT. But instead of winning a single child board, you try to win 3 child boards in row horizontally, vertically, or diagonally (like TTT).

              Copyright: 2018, Haoning Hu