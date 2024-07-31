# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, maximum_fruit = 0, 0
        count = defaultdict(int)
        
        for j in range(len(fruits)):
            count[fruits[j]] += 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
                
            maximum_fruit = max(maximum_fruit, j - i + 1)

        return maximum_fruit
        