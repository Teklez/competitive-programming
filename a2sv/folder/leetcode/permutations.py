class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(perms):
            nonlocal n
            if len(perms) == n:
                print(perms)
                res.append(perms[:])
                return
            remain = perms[-1] if perms else 0
            r_num = nums[:remain] +  nums[remain:] if perms else nums
            # print(r_num)
            for j in range(len(r_num)):
                if r_num[j] in perms:
                    continue
                perms.append(r_num[j])
                backtrack(perms)
                perms.pop()
        backtrack([])
        return res


