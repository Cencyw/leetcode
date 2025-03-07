class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        tmp = []
        ans = []
        def check(i):
            for num in tmp:
                if abs(num - nums[i]) == k:
                    return False
            return True
        def dfs(l):
            if tmp and l >= n:
                # ans.append(tmp.copy())
                return
            for i in range(l,n):
                if check(i):
                    tmp.append(nums[i])
                    ans.append(tmp.copy())
                    dfs(i+1)
                    tmp.pop()
        dfs(0)
        return len(ans)
