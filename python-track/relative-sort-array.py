class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {}
        for i in range(len(arr2)):
            order[arr2[i]] = i
        arr2 = [i for i in arr1 if i not in order]
        arr1 = [i for i in arr1 if i in order]
        
        for i in range(len(arr1) - 1):
            for j in range(len(arr1) - i - 1):
                if order[arr1[j]] > order[arr1[j + 1]]:
                    arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
        return arr1 + sorted(arr2)