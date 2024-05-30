# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        equalIndexContainer = defaultdict(list)
        for i in range(len(nums)):
            equalIndexContainer[nums[i]].append(i)
        
        print(equalIndexContainer)
        for num , indexList in equalIndexContainer.items():
            tot = sum(indexList)
            preSum = 0
            for k in range(len(indexList)):
                preSum += indexList[k]
                distance = indexList[k]*(k + 1) - preSum + (tot - preSum) - indexList[k]*(len(indexList) - k - 1)
                nums[indexList[k]] = distance
               
        return nums








