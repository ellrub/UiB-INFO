# Tema 2
# Oppgave 1
# Uttrykket 3+2*8/4-3 evalueres til 4.0 i henhold til PEMDAS-reglene. 
# Sett inn parenteser slik at det evalueres til 40.0 i stedet.
expression = (3+2)*8/(4-3)
# print(expression)

# Oppgave 2
# Lag et program som først ber om fornavnet ditt, så etternavnet 
# og til slutt skriver ut hvor mange bokstaver du har i navnet.

def num_letters_in_name():
    fornavn = input("Hva er fornavnet ditt? ")
    etternavn = input("Hva er etternavnet ditt? ")

    num_letters = len(fornavn) + len(etternavn)

    print(f"Det er {num_letters} bokstaver i navnet ditt")

# num_letters_in_name()
    
# Oppgave 3
# Tenk deg at du skal hente et antall personer i bil. Lag et program der du oppgir 
# hvor mange du skal hente og hvor mange passasjerer det er plass til i bilen.
# Programmet skal skrive ut hvor mange turer du må kjøre for å hente alle personene.
import math

def num_car_trips():
    num_p = int(input("Hvor mange personer skal du hente? "))
    num_p_in_car = int(input("Hvor mange passasjerer har du plass til i bilen? "))
    num_trips = math.ceil(num_p/num_p_in_car)
    print(f"Du må kjøre {num_trips} turer for å hente alle sammen")

# num_car_trips()

# Oppgave 4
# Lag et program som først leser inn et tall fra tastaturet, deretter utvider tallet 
# med et tilfeldig siffer bakerst og til slutt deler det nye tallet på det gamle.
# Skriv ut resultatet med 2 desimaler.

import random

def random_num():
    user_num = str(input("Gi meg et tall: "))
    random_num = str(random.randint(0, 9))
    combine_num = user_num + random_num
    expression = int(combine_num) / int(user_num)

    print(f"{combine_num}/{user_num} = {expression:.2f}")

random_num()