class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min = k
        if 'B'*k in blocks:
            return 0
        for i in range(len(blocks) - k + 1):
            operation = blocks[i:i + k].count('W')
            if operation < min:
                min = operation
        return min
        