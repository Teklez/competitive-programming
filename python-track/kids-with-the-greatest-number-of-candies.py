class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = sorted(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= temp[-1]:
                candies[i] = True
            else:
                candies[i] = False
        return candies

        