class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = 0
        result = 0
        dictn = {}
        
        for j in range(len(answerKey)):
            dictn[answerKey[j]] = dictn.get(answerKey[j], 0) + 1
            subst = min(list(dictn.values())) if len(dictn) == 2 else 0
            while i < j and subst > k:
                dictn[answerKey[i]] -= 1
                i += 1
                subst = min(list(dictn.values())) if len(dictn) == 2 else 0
            result = max(result, j - i + 1)
        return result
        