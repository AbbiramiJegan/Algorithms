def selection_sort(my_list):
    for i in range(len(my_list)):
        minimum = i 
        print(minimum)
        for j in range(i+1, len(my_list)):
            if my_list[minimum] > my_list[j]:
                minimum = j
        # swap
        my_list[i], my_list[minimum] = my_list[minimum], my_list[i]

my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Sorted array:", my_list)

