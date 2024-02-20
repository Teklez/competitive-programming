class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sum_of_mins = 0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                idx = stack.pop()
                left = stack[-1] if stack else -1
                right = i - idx
                sum_of_mins += arr[idx]*((idx - left)*right)
            stack.append(i)
        while stack:
                idx = stack.pop()
                left = stack[-1] if stack else -1
                right = len(arr) - idx
                sum_of_mins += arr[idx]*((idx - left)*right)
        return sum_of_mins % (10**9 + 7)
