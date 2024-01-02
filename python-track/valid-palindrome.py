class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                if i.isalpha() and i.isupper:
                    i = i.lower()
                temp += i

        i = 0
        j = len(temp) - 1
        while  i < j:
            if temp[i] != temp[j]:
                return False
            i += 1
            j -= 1
        return True
