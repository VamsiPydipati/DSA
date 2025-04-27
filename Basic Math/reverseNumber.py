class Solution:
    def reverseNumber(self, n):
      rev=0
      while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
      print(rev)
s=Solution()
n=int(input())
s.reverseNumber(n)