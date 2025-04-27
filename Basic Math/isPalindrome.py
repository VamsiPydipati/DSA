class Solution:
    def isPalindrome(self, n):
         original=n
         rev=0
         while n>0:
          digit=n%10
          rev=rev*10+digit
          n//=10
         if rev==original:
          return True
         else:
           return False
s=Solution()
n=int(input())
print(s.isPalindrome(n))