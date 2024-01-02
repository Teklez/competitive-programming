class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0, len(numbers) -1
        while i < j:
            summ = numbers[i] + numbers[j]
            if summ == target:
                return [i + 1, j + 1]
            elif summ < target:
                i += 1
            else:
                j -= 1
        