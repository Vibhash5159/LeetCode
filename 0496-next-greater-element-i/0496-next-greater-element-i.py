from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}

        # Build mapping for next greater elements in nums2
        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num
            stack.append(num)

        # Return results for nums1 based on mapping
        return [mapping.get(x, -1) for x in nums1]
