class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        good = 0
        for num in nums:
            if num in hash:
                good += hash[num]
            hash[num] = hash.get(num , 0) + 1
        return good

