class Solution:
    def countDigit(self, n):
      count=0
      while n>0:
        digit=n%10
        count+=1
        n//=10
      print(count)
s=Solution()
n=int(input())
s.countDigit(n)