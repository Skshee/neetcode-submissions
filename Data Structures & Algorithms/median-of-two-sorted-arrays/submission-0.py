class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1 + nums2
        combined.sort()
        
        n = len(combined)

        if n % 2 == 1:
            return combined[n//2]
        else:
            return (combined[n//2] + combined[n//2 - 1])/2