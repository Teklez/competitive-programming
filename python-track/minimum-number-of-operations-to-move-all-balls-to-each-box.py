class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            temp = 0
            j = (i + 1) % len(boxes)
            while j != i:
                if boxes[j] == "1":
                    temp += abs(j - i)
                j = (j + 1) % len(boxes)
            res.append(temp)
        return res
        