class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums1)
        maps = {val:key for key,val in enumerate(nums1)}
        for i in range(len(nums2)-1,-1,-1):
            num = nums2[i]
            while stack and nums2[stack[-1]] < num:
                stack.pop()
            if stack and num in nums1:
                ans[maps[num]] = nums2[stack[-1]]
            stack.append(i)
        return ans