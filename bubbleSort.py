def bubble_sort(arr):
    n = len(arr)
    # Perform n - 1 passes
    for i in range(n - 1):
        # In each pass, compare each element with its adjacent element
        for j in range(n - i - 1):  # Since Bubble Sort, moves the largest unsorted element to its correct position in each pass, after i passes, the last i 
            if arr[j] > arr[j + 1]: # elements are guaranteed to be in their correct sorted positions. Therefore, there is no need to compare them again in subsequent passes.
                # Swap the elements 
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = [8, 5, 7, 3, 2]
bubble_sort(arr)
print("Sorted array:", arr)
