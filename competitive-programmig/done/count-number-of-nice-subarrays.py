class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count = 0
        i = 0
        res1 = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                count += 1
            while count > k:
                if nums[i] % 2 == 1:
                    count -= 1
                i += 1
            res1  += j - i + 1


        count = 0
        i = 0
        res2 = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                count += 1
            while count > k - 1:
                if nums[i] % 2 == 1:
                    count -= 1
                i += 1
            res2  += j - i + 1
        return res1 - res2

            



                