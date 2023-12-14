class UndergroundSystem:

    def __init__(self):
        self.store = {}
        self.time = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.store:
            self.store[id] = [stationName, t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t - self.store[id][1]
        summ = self.time.get((self.store[id][0], stationName), [0,0])[0] + time
        count = self.time.get((self.store[id][0], stationName), [0,0])[1] + 1
        self.time[(self.store[id][0], stationName)] = [summ, count]
        del self.store[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.time[(startStation, endStation)]
        average = time[0]/time[1]
        return average
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)