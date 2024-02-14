# Assignment 2
# 1
def selection_sort(selction_list):
    size = len(selction_list)
    for pass_num in range(3): # Controll the number of passes here.
        minimum_index = pass_num

        for i in range(pass_num + 1, size):
            if selction_list[i] < selction_list[minimum_index]:
                minimum_index = i

        temp = selction_list[pass_num]
        selction_list[pass_num] = selction_list[minimum_index]
        selction_list[minimum_index] = temp

    print(selction_list)

selction_list = [ 1502, 1560, 1600, 1540, 100, 1660, 1700, 2024 ]
selection_sort(selction_list)

# First pass    [ 100, 1560, 1600, 1540, 1502, 1660, 1700, 2024 ]
# Second pass   [ 100, 1502, 1600, 1540, 1560, 1660, 1700, 2024 ]
# Third Pass    [ 100, 1502, 1540, 1600, 1560, 1660, 1700, 2024 ]

# 2
def bubble_sort(bubble_list):
    size = len(bubble_list)
    for i in range(3): # Controll number of passes here.
        for j in range(0, size - i - 1):
            if bubble_list[j] > bubble_list[j + 1]:
                temp = bubble_list[j]
                bubble_list[j] = bubble_list[j + 1]
                bubble_list[j + 1] = temp

    print(bubble_list)

bubble_list = [ 400, 10, 210, 160, 70, 220, 280, 380, 180, 260, 540 ]
bubble_sort(bubble_list)

# First pass    [ 10, 210, 160, 70, 220, 280, 380, 180, 260, 400, 540 ]
# Second pass   [ 10, 160, 70, 210, 220, 280, 180, 260, 380, 400, 540 ]
# Third pass    [ 10, 70, 160, 210, 220, 180, 260, 280, 380, 400, 540 ]

# 3
def sort_and_rem_dup(list):
    sorted_list = bubble_sort(list)
    no_duplicates = remove_duplicates(sorted_list) 
    return no_duplicates
    

def bubble_sort(bubble_list):
    size = len(bubble_list)
    for i in range(size):
        for j in range(0, size - i - 1):
            if bubble_list[j] > bubble_list[j + 1]:
                temp = bubble_list[j]
                bubble_list[j] = bubble_list[j + 1]
                bubble_list[j + 1] = temp

    return bubble_list

def remove_duplicates(list):
    new_list = []
    for num in list:
        if num not in new_list:
            new_list.append(num)

    return new_list

my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]

new_list = sort_and_rem_dup(my_list)
print(new_list)

