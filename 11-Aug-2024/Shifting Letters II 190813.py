# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letter_to_integer = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
    't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}

        integer_to_letter = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
    10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's',
    19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'
}


        post = [0]*len(s)
        for q in shifts:
            if  q[2] == 0:
                post[q[0]] -= 1
                if q[1] + 1 < len(s):
                    post[q[1] + 1] += 1
            else:
                post[q[0]] += 1
                if q[1] + 1 < len(s):
                    post[q[1] + 1] -= 1
        summ = 0
        for i in range(len(post)):
            summ += post[i]
            post[i] = summ
        
        res = ""
        for i in range(len(s)):
            c = integer_to_letter[(letter_to_integer[s[i]] + post[i])%26]
            res += c
        return res
            






        