class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def myPow(x: float, n: int) -> float:
            def pow(x,n):
                n = abs(n)
                if n == 0: return 1
                if n == 1: return  x
                res = pow(x, n//2)
                res = res*res
                return res%mod  if n % 2 == 0 else x*res%mod
            return pow(x,n) if n >= 0 else 1/pow(x,n)
        count = myPow(20,n//2) if n % 2 == 0 else myPow(20, n//2)*5
        return count % mod  
