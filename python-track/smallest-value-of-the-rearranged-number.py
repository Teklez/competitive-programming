class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            nums = list(str(num))
            nums.sort(reverse=True)
            return -1*int(''.join(nums[:-1]))

        nums = list(str(num))
        nums.sort()
        if nums[0] == "0":
            for i in range(len(nums)):
                if nums[i] != '0':
                    nums[i], nums[0] = nums[0], nums[i]
                    break
        return int("".join(nums))


