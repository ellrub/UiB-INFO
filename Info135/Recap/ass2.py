#Oppgvae 1
# [ 100, 1502, 1540, 1600, 1560, 1660, 1700, 2024 ]

# Oppgave 2
# [ 10, 70, 160, 210, 220, 180, 260, 280, 380, 400, 540 ]

# Oppgave 3
def sort_and_rem_dup(list):
    sorted_list = bubble_sort(list)
    no_duplicates = remove_duplicates(sorted_list)
    return no_duplicates

def bubble_sort(list):
    size = len(list)
    for i in range(size):
        for j in range(0, size - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list
    
def remove_duplicates(list):
    new_list = []
    for num in list:
        if num not in new_list:
            new_list.append(num)

    return new_list

my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]
new_list = sort_and_rem_dup(my_list)
print(new_list)