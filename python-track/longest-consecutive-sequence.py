class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numbers:
                temp = num
                while temp  in numbers:
                    temp += 1
                longest = max(longest, temp - num)
        return longest 


        

        