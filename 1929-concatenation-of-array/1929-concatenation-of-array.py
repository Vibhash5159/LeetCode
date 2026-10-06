class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans=[]
        count=0
        while count<2:
            for i in nums:
                ans.append(i)
            count+=1
        return ans
        