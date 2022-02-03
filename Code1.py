class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [None]*len(nums)
        i,j=0,0
        for i in range(0,len(nums)):
            ans[i]=nums[nums[i]]
            #print(ans[i])
            i=i+1
        return ans
