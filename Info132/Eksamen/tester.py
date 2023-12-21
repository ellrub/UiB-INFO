#71
def periode(filnavn):
    tid_list = []
    for line in open(filnavn, "r"):
        test = line.split(",")
        stasjon, nedbør, temp, vind, tid = test
        tid_list.append(tid.strip())
    
    return tid_list[0], tid_list[-1]

filnavn = "målinger.txt"
første_dato, siste_dato = periode(filnavn)
print(første_dato, siste_dato)





# 2021-01-15 06:00
#  2021-01-15 18:00