class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0]*2*n
        j = 0
        for i in range(0, 2*n - 1, 2):
            res[i] = nums[j]
            res[i + 1] = nums[n]
            j += 1
            n += 1
        return res