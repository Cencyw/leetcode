
from functools import cache


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        @cache
        def dfs(r:int,k:int)->bool:
            if k == 0:
                return s[:r] == s[:r][::-1]
            ans = False
            for l in range(k,r):
                if s[l:r] == s[l:r][::-1] and not ans:
                    ans = dfs(l,k-1)
            return ans
        return dfs(len(s),2)
if __name__=='__main__':
    s = Solution()
    ss = "acab"
    print(s.checkPartitioning(ss))
            