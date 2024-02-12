class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        i, maxFruit = 0, 0
        for j in range(len(fruits)):
            count[fruits[j]] += 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] ==0:
                    del count[fruits[i]]
                i += 1
            maxFruit = max(maxFruit, j - i + 1)
        return maxFruit
            

        
        