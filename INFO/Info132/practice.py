# Tema 7
# Oppgave 1

# friends = [
#     ['Ole',99887766],['Liv',99778899],['Gro',99556644],
#     ['Tom',98675601],['Eva',98987665],['Jan',88997766]
#     ]

# def find_tlf_nr(name, list):
#     for friend in list:
#         if friend[0] == name:
#             print(friend[1])
#             return
        
#     print('Ukjent person')

# find_tlf_nr("Gro", friends)

# print(friends)

# def remove_nr(person, list):
#     for friend in list:
#         if friend[0] == person:
#             list.remove(friend)
#             print(list)
#             return
        
#     print('Ukjent person')

# remove_nr("Liv", friends)

# Oppgave 2
exam = {
    'INFO100':'C', 'INFO104':'B', 'INFO116':'E',
    'INFO180':'A', 'INFO201':'F','INFO280':'C',
    'GEO101':'D', 'GEO110':'B','ADM101':'A',
    'ECON100':'B', 'ECON201':'C','GEO210':'C',
    'FAIL101':'F'
    }

def grade_frequence(exam_dict):
    grade_frequence = {}
    for course in exam_dict:
        grade = exam_dict[course]
        if grade in grade_frequence:
            grade_frequence[grade] += 1
        else:
            grade_frequence[grade] = 1
    return grade_frequence

print(grade_frequence(exam))

def grade_histogram(frequence):
    for grade in sorted(frequence):
        count = frequence[grade]
        print(f'{grade}: {"*" * count}')

grade_frequence(grade_frequence(exam))
