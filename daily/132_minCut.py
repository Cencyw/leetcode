from functools import cache


class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)
        #r 是 最右边的坐标
        @cache
        def dfs(r:int)->int:
            # 一致 无需分割
            if s[:r] == s[:r][::-1]:
                return 0
            #最多分割n - 1次    
            res = n - 1
            # 枚举分割点，
            for l in range(1,r):
                if s[l:r] == s[l:r][::-1]:
                    res = min(res,dfs(l)+1)
            return res
        return dfs(len(s))
if __name__ == "__main__":
    s = Solution()
    print(s.minCut("coder"))
            
        