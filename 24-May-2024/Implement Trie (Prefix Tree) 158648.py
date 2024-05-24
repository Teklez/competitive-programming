# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
   def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_last = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            idx = ord(ch) - 97
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_last = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            idx = ord(ch) - 97
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        
        return True if cur.is_last else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            idx = ord(ch) - 97
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)