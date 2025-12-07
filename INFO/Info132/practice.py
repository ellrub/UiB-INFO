# Tema 7
# Oppgave 1

friends = [
    ['Ole',99887766],['Liv',99778899],['Gro',99556644],
    ['Tom',98675601],['Eva',98987665],['Jan',88997766]
    ]

def find_tlf_num(name, tlf_list):
    for friend in tlf_list:
        if friend[0] == name:
            print(f'{friend[1]}')
            return

    print("Ukjent person")

find_tlf_num("Li", friends)

friends_dict = {
    'Ole': 99887766, 'Liv': 99778899, 'Gro': 99556644,
    'Tom': 98675601, 'Eva': 98987665, 'Jan': 88997766
}

def find_tlf_dict(name, tlf_dict):
    if name in tlf_dict:
        print(tlf_dict[name])
    else:
        print("Ukjent person")

find_tlf_dict("Jan", friends_dict)

def remove_person(person, tlf_list):