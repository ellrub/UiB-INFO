def dictionary():
    while True:
        with open("ordliste.txt") as file:
            search_word = input("Oppgi søkeord (avslutt med 'slutt')")
            for line in file:
                if line.startswith(search_word):
                    print(line.replace(",", " ="), end="")
                elif search_word == "slutt":
                    return False 
            continue
                
dictionary()