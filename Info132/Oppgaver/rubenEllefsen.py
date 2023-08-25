# Oppgave 1. Lag minst to ulike programmer som skriver navnet ditt på skjermen, med for- 
# (mellom-) og etternavn på hver sin linje. (Hint: bruk forskjellige varianter av print()-funksjonen.)

#------------- Program 1 -------------#
print("Ruben\nEllefsen")

#------------- Program 2 -------------#
name = "Ruben"
lastname = "Ellefsen"

print(name)
print(lastname)

#------------- Program 3 -------------#
names = ["Ruben", "Ellefsen"]

for name in names:
    print(name)


# Oppgave 2 
    # 2a)  Lag et program som regner om et beløp fra norske kroner til Euro og Dollar. Gi svaret med to desimaler. 
    # Du kan anta en fast kronekurs, f eks dollarkurs = 11.62 og eurokurs = 10.2. Utskriften skal se slik ut:
    # "250 norske kroner tilsvarer 25.62 Euro og 29.05 Dollar"

krone = input("Antall kroner du vil gjøre om til Euro og Dollar: ")
euro_exchange = 10.20
dollar_exchange = 11.62

print(f"{krone} norske kroner tilsvarer {float(krone) / euro_exchange:.2f} Euro og {float(krone) / dollar_exchange:.2f} Dollar")

    # 2b)  Spesialtegnene € og $ kan skrives ved hjelp av tegnkoder, henholdsvis u"\N{euro sign}" og u"\N{dollar sign}".
    # Bruk disse til å lage penere utskrift som dette: 250 norske kroner tilsvarer 25.62€ og 29.05$

print(f"{krone} norske kroner tilsvarer {float(krone) / euro_exchange:.2f}\N{euro sign} og {float(krone) / dollar_exchange:.2f}\N{dollar sign}")