class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache
        def maxScore(start,end, first):
            if start >= end:
                return 0
            if not first:
                p1 = maxScore(start + 1, end, False) + nums[start]
                p2 = maxScore(start, end - 1, False) + nums[end]
                if p1 > p2:
                    start += 1
                else:
                    end -= 1
            score1 = maxScore(start + 1, end, False) + nums[start]
            score2 = maxScore(start, end - 1, False) + nums[end]
            return max(score1, score2)
        if len(nums) == 1:
            return True
        score = maxScore(0, len(nums) - 1, True)
        minPass = math.ceil(sum(nums)/2)
        return score >= minPass
            



        
            

        

        
        