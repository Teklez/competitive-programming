class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
       minm, maxm = nums[0],nums[-1]
       right = [0]*len(nums)
       n = len(nums) - 1

       for i in range(1, len(nums) - 1):
           right[n - i] = maxm
           maxm = max(maxm, nums[n - i])

       for j in range(1, len(nums) - 1):
           if minm < nums[j] < right[j]:
               return True
           minm = min(minm, nums[j])
       return False

           

        