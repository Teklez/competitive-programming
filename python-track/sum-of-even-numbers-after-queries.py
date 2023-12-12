class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = 0
        res = {}
        c = []
        for i, v in enumerate(nums):
            if v % 2 == 0:
                summ += v
            res[i] = v
        for v, j in queries:
            print(v,j)
            after = nums[j] + v
            print(after)
            if nums[j] % 2 == 0 and after % 2 == 0:
                summ += v
            elif nums[j] % 2 == 0 and after % 2 == 1:
                summ -= nums[j]
            elif nums[j] % 2 == 1 and after % 2 == 0:
                summ += after
            nums[j] = after
            c.append(summ)
        return c
            
            



        