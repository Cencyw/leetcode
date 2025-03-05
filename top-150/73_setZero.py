class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        zero = []
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    zero.append((i,j))
        for item in zero:
            x,y = item[0],item[1]
            for i in range(n):
                matrix[x][i] = 0
            for i in range(m):
                matrix[i][y] = 0
        

        

