class MyCircularQueue:
    def __init__(self, k: int):
        self.que = []
        self.capacity = k
    def enQueue(self, value: int) -> bool:
        if len(self.que) == self.capacity:
            return False
        else:
            self.que.append(value)
            return True
        
    def deQueue(self) -> bool:
        if self.que:
            p = self.que.pop(0)
            return True
        else:
            return False
    def Front(self) -> int:
        return self.que[0] if self.que else -1
    def Rear(self) -> int:
        return self.que[-1] if self.que else - 1
    def isEmpty(self) -> bool:
        return len(self.que) == 0
    def isFull(self) -> bool:
        return len(self.que) == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()