class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash = {}
        longest = ""
        for i in range(len(s)):
            hash[s[i]] = i
            for j in range(i + 1, len(s)):
                hash[s[j]] = j
                flag = True
                for st in s[i:j + 1]:
                    if (st.islower() and st.upper() not in hash) or (st.isupper() and st.lower() not in hash):
                        flag = False
                if flag and len(s[i:j + 1]) > len(longest):
                    longest = s[i:j + 1]
            hash = {} 
        return longest

        
        

        
        