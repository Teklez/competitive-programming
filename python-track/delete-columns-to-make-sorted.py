class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        strs = list(zip(*strs))
        for sub in strs:
            for i in range(len(sub) - 1):
                if sub[i] > sub[i + 1]:
                    count += 1
                    break
        return count
        