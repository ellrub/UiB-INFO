# oppgave  1

def selection_sort_one_pass(int_list):
    size = len(int_list) # list length
    minimum_index = 0

    for i in range(1, size):
        if int_list[i] < int_list[minimum_index]:
            minimum_index = i

    temp = int_list[0]
    int_list[0] = int_list[minimum_index]
    int_list[minimum_index] = temp

    return int_list

print(selection_sort_one_pass([5, 2, 3, 4, 0, 1]))


# oppgave 2
from lab3_list import liste

def filter_tuples(tuples):
    new_tuple = []
    for item in tuples:
        if item[0] + item[1] == item[2]:
            new_tuple.append(item)

    return(new_tuple)

def selection_sort(list):
    size = len(list)
    for pass_num in range(size):
        minimum_index = pass_num

        for i in range(pass_num + 1, size):
            if list[i][2] < list[minimum_index][2]:
                minimum_index = i

        temp = list[pass_num]
        list[pass_num] = list[minimum_index]
        list[minimum_index] = temp

    print(list)

# tuples = [(0,0,1), (0,1,1), (0,1,2), (1,1,2), (1,2,3)]
liste = filter_tuples(liste)
selection_sort(liste)