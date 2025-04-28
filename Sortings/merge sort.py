class Solution:
    def mergeSort(self, arr, low, high):
        # Base case: If the array has one or zero elements, it's already sorted
        if low >= high:
            return

        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)   # Sort left half
        self.mergeSort(arr, mid + 1, high)  # Sort right half
        self.merge(arr, low, mid, high)  # Merge sorted halves

    def merge(self, arr, low, mid, high):
        temp = []  # Temporary array
        left = low  # Starting index of left half
        right = mid + 1  # Starting index of right half

        # Storing elements in a sorted manner in temp array
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # If elements on the left half are still left
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # If elements on the right half are still left
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Transfer sorted elements from temp array to the original array
        for i in range(len(temp)):
            arr[low + i] = temp[i]


# Driver Code
arr = [9, 4, 7, 6, 3, 1, 5]
solution = Solution()
print("Before Sorting:", *arr)
solution.mergeSort(arr, 0, len(arr) - 1)
print("After Sorting:", *arr)
