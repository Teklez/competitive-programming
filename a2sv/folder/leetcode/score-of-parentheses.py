class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for k in s:
            if k == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(1,score*2)
        return score



        