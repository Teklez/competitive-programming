class RecentCounter:
    def __init__(self):
        self.recent = deque()
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.recent.append(t)
        k = t - 3000
        while self.recent[0] < k:
            self.recent.popleft()
        return len(self.recent)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)