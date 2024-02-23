class Solution:
    def decodeString(self, s: str) -> str:
        if '[' not in s and ']' not in s:
            return s
        found = 0
        open = -1
        for i in range(len(s)):
            if s[i] == '[':
                found += 1
                if found == 1: open = i
            elif s[i] == "]":
                found -= 1
            if s[i] == ']' and found == 0:
                added = ""
                temp = open - 2
                while temp >= 0 and s[temp] != '[':
                    if s[temp].isalpha():
                        added = s[temp] + added
                    temp -= 1
                print("added", added)
                num = ""
                o = open - 1
                while o >= 0 and s[o].isnumeric():
                    num = s[o] + num
                    o -= 1

                return  added + int(num)*self.decodeString(s[open + 1:i]) + self.decodeString(s[i + 1:])
                open = -1
            

            

        

        