    class Solution:
      def thirdMax(self, nums: List[int]) -> int:
        ans1=list(set(nums))
        ans1.sort()
        if len(ans1)>2:
            return ans1[-3]
        else:
            return max(ans1)
