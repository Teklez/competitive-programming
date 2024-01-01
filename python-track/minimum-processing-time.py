class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        maxm = 0
        for i in range(len(processorTime)):
            j = i*4
            maxm = max(maxm, processorTime[i] + tasks[j])
        return maxm
        