class Solution:
    def countAndSay(self, n: int) -> str:
        def dfs(n:int)->str:
            if n == 1:
                return "1"
            s = dfs(n-1)
            ans = ""
            left = 0
            for idx,ch in enumerate(s):
                if s[left] == ch:
                    continue
                if s[left] != ch:
                    ans += str(idx - left)+str(s[left])
                    left = idx
            ans += str(len(s) - left) + str(s[left])
            return ans
        return dfs(n)
if __name__ == "__main__":
    n = 4
    s = Solution()
    print(s.countAndSay(4)) 