class Solution:
    def divisors(self, n):
      list=[]
      for i in range(1,n+1):
        if n%i==0:
          list.append(i)
      print(list)
s=Solution()
n=int(input())
s.divisors(n)