class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = senate.count("R")
        D = senate.count("D")
        senate = deque(list(senate))
        r = 0
        d = 0
        while R > 0 and D > 0:

            if senate[0] == "R":
                if d:
                    senate.popleft()
                    d -= 1
                    continue
                D -= 1
                if D == 0:return "Radiant"
                senate.append(senate.popleft())
                r += 1
            elif senate[0] == "D":
                if r:
                    senate.popleft()
                    r -= 1
                    continue
                R -= 1
                if R == 0:return "Dire"
                senate.append(senate.popleft())
                d += 1
        return "Dire" if D else  "Radiant"


