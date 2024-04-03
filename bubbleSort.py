def bubble_sort(my_list):
    n = len(my_list)
    # Perform n - 1 passes
    for i in range(n - 1):
        # Initialize flag to False for each pass
        flag = False
        # In each pass, compare each element with its adjacent element
        for j in range(n - i - 1):
            if my_list[j] > my_list[j + 1]:
                # Swap the elements
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                # Set flag to True if a swap occurs
                flag = True
        # If no swaps occur in a pass, the my_list is already sorted, so break the loop
        if not flag:
            break

my_list = [8, 8, 3, 5, 4]
bubble_sort(my_list)
print("Sorted array:", my_list)
