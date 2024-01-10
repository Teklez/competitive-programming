class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # i, res = 0, len(cards) + 1
        # hash = {}
        
        # for j in range(len(cards)):
        #     hash[cards[j]] = hash.get(cards[j], 0) + 1
        #     while hash[cards[j]] == 2:
        #         res = min(res, j - i + 1)
        #         hash[cards[i]] -= 1
        #         i += 1

        # return res if res < len(cards) + 1 else -1 
        

        res, pos = 10**6+1, {}
        for i, c in enumerate(cards):
            if c in pos:
                res = min(res, i - pos[c] + 1)
            pos[c] = i
        
        return res % (10**6+1) or -1
