class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)):
            if len(palindrome) % 2 == 1 and i == len(palindrome)//2:
                continue
            elif palindrome[i] != "a":
                return palindrome[0:i] +"a"+ palindrome[i+1:]
            elif i == len(palindrome) - 1:
                return palindrome[0:-1] + "b"
        
