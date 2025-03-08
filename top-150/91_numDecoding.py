
# .占位符
from functools import cache
class Solution:
    #s = "12"
    # [A,B]/[L]
    # ans = 2    
    def numDecodings(self, s: str) -> int:
        
        # +1 / +2˜˜˜
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1,n+1):
            if s[i-1] !='0': 
                dp[i] = dp[i-1]
            if i >= 2 and (s[i-2] == '1' or  s[i-2] == '2' and s[i-1] < '7'):
                dp[i] += dp[i-2]
        return dp[n]
        # n = len(s) - 1
        # @cache
        # def dfs(l : int):
        #     nonlocal ans
        #     if l > n:
        #         ans += 1
        #         return
        #     if s[l] == '0':
        #         return
        #     dfs(l+1)
        #     if l < n and (s[l] == '1' or  s[l] == '2' and s[l+1] < '7'):
        #         dfs(l+2)
        # dfs(0)
        # return ans
if __name__ == "__main__":
    s = "06"
    print(Solution().numDecodings(s))
                
            