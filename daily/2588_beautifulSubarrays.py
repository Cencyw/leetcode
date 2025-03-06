class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        #找规律，0，i，j，m
        #子数组，滑动窗口//双指针
        #dp？，i，j 10^5 no 
        #nlog(n)//log(n)//n
        ans,s = 0,0
        #j > i
        #s[j]-s[i] = k
        #s[i] = s[j] - k
        cnt = defaultdict(int)
        cnt[0] = 1
        for num in nums:
            s^=num#s[j]
            ans += cnt[s]
            cnt[s]+=1
        return ans


