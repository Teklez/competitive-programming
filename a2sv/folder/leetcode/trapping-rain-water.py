class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        trapped_water = 0
        for i in range(len(height)):
            # print(stack)
            while stack and height[stack[-1]] <= height[i]:
                cur = stack.pop()
                if stack:
                    left = stack[-1]
                    trapped_water += (min(height[left],height[i])- height[cur])*(i - left - 1) 
            stack.append(i)
        return trapped_water
            

            

        