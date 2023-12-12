class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        max_len = 0
        result = []
        for c in s:
            max_len = max(max_len, len(c))

        for i in range(max_len):
            temp = ""
            for ch in s:
                if i < len(ch):
                    temp += ch[i]
                else:
                    print(i)
                    temp += " "
            result.append(temp.rstrip())
        
        return result


        