class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        left,n = 0,len(nums)
        maps = defaultdict(int)
        for right in range(n):
            if right - left + 1 == k:
                ss = set(nums[left:right+1])
                for s in ss:
                    maps[s]+=1
            while right - left + 1 >= k:
                left+=1
        ans = [-1]
        for key in maps.keys():
            if maps[key] == 1:
                ans.append(key)
        return max(ans)