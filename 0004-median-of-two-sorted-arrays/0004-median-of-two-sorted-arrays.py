from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        length = len(merged)

        if length % 2 == 0:
            mid1 = length // 2 - 1
            mid2 = length // 2
            median = (merged[mid1] + merged[mid2]) / 2
        else:
            mid = length // 2
            median = merged[mid]

        return median
