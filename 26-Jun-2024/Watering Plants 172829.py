# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        cap = capacity
        for i in range(len(plants)):
            if plants[i] > capacity:
                capacity = cap
                steps += 2*i
            steps += 1
            capacity -= plants[i]
        return steps

                