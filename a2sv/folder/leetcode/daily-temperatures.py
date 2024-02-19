class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [0]*len(temperatures)
        for i,value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                removed = stack.pop()
                answer[removed[1]] = i - removed[1]
            stack.append((value, i))
        
        return answer


                
            

        