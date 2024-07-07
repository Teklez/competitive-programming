# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        part = set()
        min_part = 0

        for ch in s:
            if ch in part:
                min_part += 1
                part = set([ch])
            part.add(ch)

        if part:min_part += 1
        return min_part



        