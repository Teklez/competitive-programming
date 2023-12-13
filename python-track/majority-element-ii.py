class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        res = []
        for val, count in counts.items():
            if count > n/3:
                res.append(val)
        return res




        

        