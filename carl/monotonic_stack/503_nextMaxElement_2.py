class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        nums.extend(nums)
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack and i < n:
                ans[i] = nums[stack[-1]]
            stack.append(i)
        return ans