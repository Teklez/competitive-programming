class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
         n = len(arr)
         arr = Counter(arr)
         for element, count in arr.items():
             if count > n / 4:
                 return element