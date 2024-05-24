# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
   def __init__(self):
        self.children = {}
        self.is_last = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_last = True

    def search(self, word: str) -> bool:
        res = ""
        cur = self.root
        for ch in word:
            if len(cur.children) == 1:
                res += ch
                if cur.children[ch].is_last:
                    return res
            else:
                return res

            cur = cur.children[ch]
        return res
        



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        trie = Trie()
        for word in strs:
            trie.insert(word)
        return trie.search(strs[0])
        
