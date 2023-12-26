class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        maxm = 0
        for i in range(1, len(flips)+1):
            maxm = max(maxm, flips[i-1])
            if maxm == i:
                count += 1
        return count


        