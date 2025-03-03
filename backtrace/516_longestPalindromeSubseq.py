class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # @cache
        # def dfs(i:int,j:int)->int:
        #     if i > j:
        #         return 0
        #     if i == j:
        #         return 1
        #     if s[i]==s[j]:
        #         return dfs(i+1,j-1)+2
        #     if s[i]!=s[j]:
        #         return max(dfs(i+1,j),dfs(i,j-1))
        # return dfs(0,len(s)-1)
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
