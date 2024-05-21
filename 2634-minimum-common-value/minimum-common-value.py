class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        l = 0
        r = 0

        while l < n and r < m:
            if nums1[l] == nums2[r]:
                return nums1[l]
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        
        return -1
                


        
            
             
                