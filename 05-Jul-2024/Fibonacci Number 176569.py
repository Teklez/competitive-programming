# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        
        for i in range(n):
            t = a + b
            a = b
            b = t
            
        return a



        
