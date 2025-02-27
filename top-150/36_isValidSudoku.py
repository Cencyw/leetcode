from collections import defaultdict
from typing import List
# class Solution:
  
    # def isValidSudoku(self, board: List[List[str]]) -> bool:

        # def checkMatrix(m:int,n:int) -> bool:

            # maps = defaultdict(bool)

            # for i in range(m,m+3):

                # for j in range(n,n+3):

                    # num = board[i][j]

                    # if num >='1'and num <= '9'and maps[num]:

                        # return False

                    # maps[num] = True

            # return True

        # def checkRow(i:int)->bool:

            # maps = defaultdict(bool)

            # for j in range(0,9):

                # num = board[i][j]

                # if num >='1'and num <= '9'and maps[num]:

                    # return False

                # maps[num] = True

# 
  
            # return True

        # def checkCol(i:int)->bool:

            # maps = defaultdict(bool)

            # for j in range(0,9):

                # num = board[j][i]

                # if num >='1'and num <= '9'and maps[num]:

                    # return False

                # maps[num] = True 

            # return True 

        # for i in range(0,9,3):

            # for j in range(0,9,3):

                # if not checkMatrix(i,j):

                    # return False

        # for i in range(0,9):

            # if not checkCol(i) or not checkRow(i):

                # return False

        # return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [[False]*10 for _ in range(10)]
        row = [[False]*10 for _ in range(10)]
        matrix = [[False]*10 for _ in range(10)]
        for i in range(0,9):
            for j in range(0,9):
                c = board[i][j]
                if c == '.':
                    continue
                c = int(c)
                if col[i][c] or row[j][c] or matrix[i//3*3+j//3][c]:
                    return False
                col[i][c] = True
                row[j][c] = True
                matrix[i//3*3+j//3][c] = True
        return True

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    ss = Solution()
    print(ss.isValidSudoku(board))
    print("done")
        