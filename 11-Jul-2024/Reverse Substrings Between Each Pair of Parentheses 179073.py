# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i]  == ")":
                word = ""
                while True:
                    l = stack.pop()
                    if l == "(":
                        for ch in word:
                            stack.append(ch)
                        break
                    word += l
                    print(word)
            else:
                stack.append(s[i])
        return ''.join(stack)                    






        