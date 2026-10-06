class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        for i in range(2*n):
            ans.append(nums[i//2+(i%2)*n])
        return ans