class Solution:
    def GCD(self, n1, n2):
      gcd =1
      for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
          gcd=i
        return gcd
s=Solution()
n1=int(input())
n2=int(input())
s.GCD(n1,n2)
        