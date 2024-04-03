def bubble_sort(arr):
    n = len(arr)
    # Perform n - 1 passes
    for i in range(n - 1):
        # Initialize flag to False for each pass
        flag = False
        # In each pass, compare each element with its adjacent element
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set flag to True if a swap occurs
                flag = True
        # If no swaps occur in a pass, the array is already sorted, so break the loop
        if not flag:
            break

arr = [8, 8, 3, 5, 4]
bubble_sort(arr)
print("Sorted array:", arr)
