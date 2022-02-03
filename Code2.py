class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[None]*(2*len(nums))
        #i=0
        for i in range(0,len(nums)):
            ans[i],ans[i+len(nums)]=nums[i],nums[i]
        return ans


-----------------------------------------------------------------------------

class Solution(object):
    def getConcatenation(self, nums):
        return nums * 2
