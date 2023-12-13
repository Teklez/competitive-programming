class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        seen = set()
        for rang in ranges:
            for i in range(left, right + 1):
                if rang[0] <= i <=rang[1]:
                    seen.add(i)
        return len(seen) == abs(right - left) + 1
            

        