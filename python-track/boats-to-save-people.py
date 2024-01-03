class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        max_boat = len(people)
        while j > i:
            if people[i] + people[j] <= limit:
                max_boat -= 1
                i += 1
                j -= 1
            else:
                j -= 1
        
        return max_boat
        