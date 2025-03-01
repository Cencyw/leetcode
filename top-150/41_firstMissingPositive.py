from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ##hash
        n = len(nums)
        for num in nums:
            while 0 < num <= n and nums[num-1] != num:
                nums[num-1],num =  num,nums[num-1]
        for idx,num in enumerate(nums):
            if  idx != num - 1:
                return idx + 1
        return len(nums) + 1
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     for a in nums: #遍历每个座位，记当前坐着a号乘客
    #         while 0<a<=len(nums) and a!=nums[a-1]:  #乘客a是正票但坐错了! 其座位被 ta=nums[a-1]占了
    #             nums[a-1], a = a, nums[a - 1]  # a和ta两人互换则a对号入座。此后ta相当于新的a，去找自己的座位（循环执行）
    #     for i in range(len(nums)):
    #         if i+1!=nums[i]:return i+1  #找到首个没有对号入座的nums[i]!=i+1
    #     return len(nums)+1  #满座，返回N+1

if __name__ == "__main__":
    nums = [3,4,-1,1]
    s = Solution()
    print(s.firstMissingPositive(nums))