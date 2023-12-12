class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        i = start
        summ = 0
        while i != destination:
            summ += distance[i]
            i = (i + 1) % n

        i = start
        total = 0
        while i != destination:
            total += distance[(i - 1) % n]
            i = (i - 1) % n

        return min(summ, total)
        
        