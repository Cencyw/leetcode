
from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # [K:]
        n = len(s)
        @cache
        def mis_match(i: int, j: int) -> int:
            if i >= j:
                return 0
            return mis_match(i + 1, j - 1) + (0 if s[i] == s[j] else 1)
        @cache
        def dfs(r: int, kk: int) -> int:
            if kk == 0:
                return mis_match(0,r) 
            res = n
            for i in range(kk,r + 1):
                res = min(mis_match(i, r) + dfs(i - 1, kk - 1), res)
            return res

        return dfs(n - 1, k - 1)
if __name__=="__main__":
    solution = Solution()
    s = "aea"
    k = 2
    print(solution.palindromePartition(s,k))
