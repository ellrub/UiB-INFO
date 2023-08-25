#---------------- Programmeringsoppgaver ----------------#

# Oppgave 1 (enkel). Lag et program som tegner en pil
# print("        *\n        **\n        * *\n*********  *\n        *   *\n*********  *\n        * *\n        **\n        *")

#Oppgave 2 (middels).

# 2a)  Finn feilen i de følgende programmene og bestem om det er snakk om en syntaktisk, 
# logisk eller semantisk feil, jfr avsnitt 1.10 i læreboken. (Kjør gjerne programmene i 
# IDLE for å se hvilke feilmeldinger som gis.)

# 1
# antall_studenter = 55
# antall_kvinner = 32
# kvinneandel = Antall_kvinner/antall_studenter 
# print('kvinneandelen er ', kvinneandel)

# Denne vil gi en NameError fordi Antall_kvinner ikke er definert.

# antall_studenter = 55
# antall_kvinner = 32
# kvinneandel = antall_kvinner/antall_studenter 
# print('kvinneandelen er ', kvinneandel)

# 2
# antall_studenter = 55
# antall_kvinner = 32
# kvinneandel = antall_kvinner/antall_studenter 
# print(kvinneandelen er , kvinneandel)

# Her er ikke "er" og "kvinneandelen" definert

# antall_studenter = 55
# antall_kvinner = 32
# kvinneandel = antall_kvinner/antall_studenter 
# print(f"kvinneandelen er {kvinneandel}")

# 3
antall_studenter = 55 
antall_kvinner = 32
kvinneandel = antall_kvinner/antall_studenter 
print('kvinneandelen er ', kvinneandel)

# 4
# kvinneandel = antall_kvinner/antall_studenter 
# antall_studenter = 55
# antall_kvinner = 32
# print('kvinneandelen er ', kvinneandel)

# 5
# kvinneandel = antall_kvinner=32/antall_studenter=55
# print('kvinneandelen er ', kvinneandel)

# 6
# antall_studenter = 55
# antall_kvinner = 32
# kvinneandel = antall_studenter/antall_kvinner 
# print('kvinneandelen er ', kvinneandel)