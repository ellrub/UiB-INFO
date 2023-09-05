saldo = 500
rentesats = 0.01
rente = 0

def velg():
    while saldo > 0:
        user_input = input("--------------------\n1 - vis saldo\n2 - innskudd\n3 - uttak\n4 - renteoppgjør\n--------------------\n")
        if user_input == "1":
            print(f"Saldo: {saldo}")
        elif user_input == "rentesats":
            print(rentesats)
        elif user_input == "2":
            print(innskudd(innskudd))
        elif user_input == "3":
            print(uttak(uttak))
        elif user_input == "beregn rente":
            print(beregn_rente())
        elif user_input == "4":
            print(renteoppgjør())
        elif user_input == "q":
            break

def innskudd(innskudd):
    global saldo
    global rentesats
    innskudd = int(input("Hvor mye vil du sette inn?: "))
    saldo += innskudd
    if saldo > 1000000 and rentesats == 0.01:
        print("Gratulerer, du får bonusrente!")
        rentesats = 0.02
    return saldo

def uttak(uttak):
    global saldo
    global rentesats
    uttak = int(input("Hvor mye vil du ta ut?: "))
    if uttak < saldo:
        saldo -= uttak
    else:
        print("Overtrekk")
    if saldo < 1000000 and rentesats == 0.02:
        print("Du har nå ordinær rente.")
        rentesats = 0.01
    return saldo

def beregn_rente():
    global saldo
    global rentesats
    global rente
    rente = saldo * rentesats
    return rente

def renteoppgjør():
    global rente
    global saldo
    saldo += rente
    return saldo

velg()