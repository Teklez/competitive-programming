class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        que = deque([deck.pop()])
        for i in range(len(deck)):
            que.appendleft(que.pop())
            que.appendleft(deck.pop())
        return list(que)

        


        

        