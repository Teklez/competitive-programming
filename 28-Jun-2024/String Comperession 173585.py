# Problem: String Comperession - https://leetcode.com/problems/string-compression/

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        j = 0

        while j < len(chars):
            count = 1
            while j + 1 < len(chars) and chars[j] == chars[j + 1]:
                count += 1
                j += 1
            chars[i] = chars[j]
            i += 1
            if count > 1:
                count = str(count)
                for k in range(len(count)):
                    chars[i] = count[k]
                    i += 1
            
            j += 1
        print(chars)
        return i

        














