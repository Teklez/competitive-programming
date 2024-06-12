# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        if name[0] != typed[0]:return False
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if j != 0 and typed[j - 1] != typed[j]:return False

                j += 1
        if i == len(name) and len(set(typed[j - 1:])) == 1:
            return True
        return False

