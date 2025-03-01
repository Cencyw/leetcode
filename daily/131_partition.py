class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []
        #从start开始 第 i个 逗号
        def dfs(i:int, start:int)->None:
            if i == n:
                ans.append(path.copy())
                return
            #asdas start  db i
            if i < n - 1:
                #next
                dfs(i+1,start)
            
            ss = s[start:i+1]
            if ss == ss[::-1]:
                path.append(ss)
                dfs(i+1,i+1)
                path.pop()
        dfs(0,0)
        return ans
                
            