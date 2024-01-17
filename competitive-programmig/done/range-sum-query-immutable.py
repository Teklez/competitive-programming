class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0]*(len(nums) + 1)
        accumulator = 0
        for i in range(1,len(nums) + 1):
            accumulator += nums[i - 1]
            self.prefixSum[i] = accumulator
        print(self.prefixSum)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right  + 1] - self.prefixSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)