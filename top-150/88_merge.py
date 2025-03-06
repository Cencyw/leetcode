class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #O(m+n)
        #sort nlog(n)
        #space n time n
        p1,p2,idx =m - 1,n - 1,len(nums1)-1
        #n的长度
        while  p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[idx] = nums1[p1]
                p1-=1
            else:
                nums1[idx] = nums2[p2]
                p2-=1
            idx-=1
        