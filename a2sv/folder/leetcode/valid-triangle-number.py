class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] < nums[j] + nums[k]:
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count



        


        