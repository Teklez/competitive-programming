class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                break
        print(i)
        for j in range(len(arr) - 1, 0, -1):
            if arr[j] >= arr[j - 1]:
                break

        print(j)

        if j == i and i != len(arr) - 1 and j != 0:
            return True
        return False