class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        s = list(map(ord,s))
        @cache
        def dfs(i:int,j:int,k:int)->int:
            if i >= j:
                return j - i + 1 
            res = max( dfs(i+1,j,k),dfs(i,j-1,k))
            d = abs(s[i] - s[j])
            d = min(d,26-d)
            if d <= k:
                res = max(res,dfs(i+1,j-1,k-d)+2)
            return res
        ans = dfs(0,n-1,k)
        dfs.cache_clear()  # 避免超出内存限制
        return ans