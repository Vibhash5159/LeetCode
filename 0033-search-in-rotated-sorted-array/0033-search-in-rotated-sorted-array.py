

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
        # only return -1 after checking all elements
        return -1
