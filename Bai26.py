
n = 8
board = [list("--------"),
         list("--------"),
         list("--------"),
         list("--------"),
         list("--------"),
         list("--------"),
         list("--------"),
         list("--------")
         ]
def isSafe(i, j, board):
  for c in range(len(board)):
    for r in range(len(board)):
      if board[c][r] == 'q' and i==c and j!=r:
        return False
      elif board[c][r] == 'q' and j==r and i!=c:
        return False
      elif (i+j == c+r or i-j == c-r) and board[c][r] == 'q':
        return False
  return True

count = 0

def Try(i : int):
  global count
  for j in range(0, 8):
    if isSafe(i, j, board):
        board[i][j] = "q"
        if i == 7:
          count += 1
          for x in board:
            print(x)
          print("\n", end = '')
        else:
          Try(i + 1)
        board[i][j] = '-'



def placeNQueens(n, board):
  Try(0)
  '''
  To check whether index i,j is safe to place queen call isSafe(i, j, board)
  True means it is safe, False means it is not
  '''

  return board


board = placeNQueens(n, board)
print(count)
