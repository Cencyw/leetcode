class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for idx in range(n-1,-1,-1):
            while  stack and temperatures[stack[-1]] <= temperatures[idx]:
                stack.pop()
            if stack:
                ans[idx] = stack[-1] - idx
            stack.append(idx)
        return ans

# 单调栈
# 单调栈是一种特殊的栈，栈内元素保持单调性。
# 单调栈可以解决很多与序列相关的问题，例如：
# 1. 找到每个元素左边第一个比它大的元素
# 2. 找到每个元素左边第一个比它小的元素
# 3. 找到每个元素右边第一个比它大的元素
# 4. 找到每个元素右边第一个比它小的元素