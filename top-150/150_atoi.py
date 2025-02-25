class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        res,i,sign = 0,1,1
        int_max,int_min = 2**31-1,2**31
        if s[0] == '-': sign = -1
        elif s[0] != '+':i = 0
        for c in s[i:]:
            if not '0' <= c <= '9': break
            res = res * 10 + int(c)
            if res >= int_min:return int_max if sign == 1 else -int_min
        return res*sign
        