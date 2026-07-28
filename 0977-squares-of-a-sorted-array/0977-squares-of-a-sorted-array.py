class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        k=len(nums)-1
        ans=[0]*len(nums)
        while l<=r:
            if nums[l]**2>nums[r]**2:
                ans[k]=nums[l]**2
                k-=1
                l+=1
            else:
                ans[k]=nums[r]**2
                k-=1
                r-=1
        return ans