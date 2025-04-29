class Solution:
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quickSort(arr, low, high):
        if low < high:
            pi = Solution.partition(arr, low, high)
            Solution.quickSort(arr, low, pi - 1)
            Solution.quickSort(arr, pi + 1, high)

# --- User input section ---
if __name__ == "__main__":
    arr = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    Solution.quickSort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
 