class Solution:
    def isArmstrong(self, n):
      original=n
      sum=0
      z=len(str(n))
      while n>0:
        digit=n%10
        sum=sum+digit**z
        n//=10
      if sum==original:
        return True
      else:
        return False
s=Solution()
n=int(input())
s.isArmstrong(n)