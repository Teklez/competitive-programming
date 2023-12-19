class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
            combination = set(zip(fronts, backs))
            minm = 2001
            for i in range(len(fronts)):
                if fronts[i] != backs[i]:
                    if (fronts[i], fronts[i]) not in combination:
                        minm = min(minm, fronts[i])
                    if (backs[i], backs[i]) not in combination:
                        minm = min(minm, backs[i])
            
            return minm if minm != 2001 else 0

        
