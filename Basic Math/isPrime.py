class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
          if n%i==0:
            return False
        return True
s=Solution()
n=int(input())
s.isPrime(n)