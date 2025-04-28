class Solution:
    def bubbleSort(self, arr):
        n=len(arr)
        for i in range(n-1,0,-1):
            for j in range(0,i):
                if arr[j]>arr[j+1]:
                  arr[j+1],arr[j]=arr[j],arr[j+1]
n=int(input())
arr=list(map(int,input().split()))
s=Solution()
s.bubbleSort(arr)
print(arr)