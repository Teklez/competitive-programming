class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        flips = []
        def flip(right):
            left = 0
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] != i + 1:
                for j in range(i - 1, -1, -1):
                    if arr[j] == i + 1:
                        break
                flip(j)
                flips.append(j + 1)
                flip(i)
                flips.append(i + 1)
        return flips



        