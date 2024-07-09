# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            max1 = -1*heapq.heappop(stones)
            max2 = -1*heapq.heappop(stones)
            diff = abs(max2 - max1)
            if diff:
                heapq.heappush(stones, -1*diff)
        res = 0 if not stones else stones[0]
        if not res: return 0
        return res if res > 0 else -1*res



        
        



