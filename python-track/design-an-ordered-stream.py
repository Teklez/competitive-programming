class OrderedStream:

    def __init__(self, n: int):
        self.stream = [0]*n
        self.ptr = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        i = idKey - 1
        self.stream[i] = value
        temp = i
        if i == self.ptr:
            while i < len(self.stream) and self.stream[i] != 0:
                i += 1
            self.ptr = i
            return self.stream[temp:i]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)