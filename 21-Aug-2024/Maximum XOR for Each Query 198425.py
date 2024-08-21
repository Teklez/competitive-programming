# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        total_xor = 0

        for num in nums:
            total_xor ^= num
        
        ans = []
        for i in range(len(nums)):
            j = 0   
            k = 0
            while j < maximumBit:
                if not (1<<j) & total_xor:
                    k |= 1<<j
                j+= 1
            ans.append(k)
            total_xor ^= nums.pop()
        return ans





