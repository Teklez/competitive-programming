class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        l = len(salary)
        average = (sum(salary[1:l-1]))/(l - 2)
        return average