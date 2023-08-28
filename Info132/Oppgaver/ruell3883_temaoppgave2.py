# Oppgave 1.
# Lag et program som leser inn radiusen til en sirkel (hel- eller kommma-tall) fra 
# tastaturet og beregner arealet til sirkelen. Skriv ut med tre desimaler. For 
# eksempel kan dialogen se slik ut:
# Radius: 6.73

# Arealet til en sirkel med radius 6.73 er 142.292

# import math
# radius = float(input("Radius: "))
# areal = math.pi * radius**2
# print(f"Arealet til en sirkel med radius {radius} er {areal:.3f}")

# Oppgave 2.
# Lag et program der brukeren først taster inn en setning og deretter gjetter på hvor mange bokstaver 
# det er i setningen. Programmet skal skrive ut True dersom gjetningen er korrekt, False ellers.
# For eksempel kan dialogen se slik ut:
# Skriv setning: Always look on the bright side of life
# Gjett lengde: 34
# That's False!!

write_sentence = input("Skriv setning: ")
guess_length = int(input("Gjett lengde: "))

if len(write_sentence) == guess_length:
    print("That's True")
else:
    print("That's False")