direct = [[0,1],[1,0],[0,-1],[-1,0]]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        size = m * n
        ans = []
        i,j,d = 0, -1, 0
        while len(ans) < size:
            dx,dy = direct[d]
            for _ in range(n):
                i,j = i+dx,j+dy
                ans.append(matrix[i][j])
            d = (d + 1) % 4
            n, m = m-1, n
        return ans
