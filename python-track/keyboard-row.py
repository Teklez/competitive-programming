class Solution:
    def findWords(self, words: List[str]) -> List[str]:
       row1 = "qwertyuiop"
       row2 =  "asdfghjkl"
       row3 =  "zxcvbnm"
       res = []
       
       for word in words:
           temp = word.lower()
           if temp[0] in row1:
               row = row1
           elif temp[0] in row2:
               row = row2
           else:
               row = row3
           flag = True
           for ch in temp:
                if ch not in row:
                    flag = False
                    break
           if flag:
               res.append(word)
       return res



                
        