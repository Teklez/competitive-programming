class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        contribution = []
        for i in range(len(weights) - 1 ):
            contribution.append(weights[i] + weights[i  + 1])

        max_score = 0
        min_score = 0
        contribution.sort()

        for i in range(k-1):
            min_score += contribution[i]
            max_score += contribution[len(contribution) - i - 1]
        return max_score - min_score
        


        