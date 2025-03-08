from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
      #new flowers 操作次数
      #full >= target
      #partial  min(value),value < target
      n = len(flowers)
        
      for i in range(n):
        flowers[i] = min(target,flowers[i])
      
      leftFlowers = newFlowers - (target * n - sum(flowers))
      flowers = sorted(flowers)
      ans = j = preSum = 0
      for i in range(1,n+1):
        #leftFlowers 
        leftFlowers += target - flowers[i-1] 
        if leftFlowers < 0:
            continue
        while j < i and flowers[j] * j  < preSum + leftFlowers:
            preSum += flowers[j]
            j += 1
        
        avg = (preSum + leftFlowers) // j
        ans = max(ans,avg * partial + (n-i) * full)
      return ans
if __name__ == "__main__":
  flowers = [1,3,1,1]
  newFlowers = 7
  target = 6
  full = 12
  partial = 1
  print(Solution().maximumBeauty(flowers, newFlowers, target, full, partial))
