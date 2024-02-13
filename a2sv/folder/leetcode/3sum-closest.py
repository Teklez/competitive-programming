class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float(inf)
        res = 0
        for i in range(len(nums)):
            j , k = i + 1, len(nums) - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if abs(summ - target) < closest:
                    closest = abs(summ - target)
                    res = summ
                if summ > target:
                    k -= 1
                elif summ < target:
                    j += 1
                else:
                    return summ
        return res



                    

        
