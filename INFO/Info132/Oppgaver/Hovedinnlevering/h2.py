import re # Regex bibliotek

class Tekstanalyse:
    avsnittliste = [] # liste over normaliserte avsnitt i teksten
    ordlister = [] # liste av lister over ord som forekommer i hvert avsnitt
    ordtellinger = [] # liste av lister med ordtellinger for hvert avsnitt

    def __init__(self):
        self.tekst = "eksempeltekst.txt"

    def normaliser_tekst(self):
        "Fjerner spesialtegn fra self.tekst og konverterer til små bokstaver."
        regex_match = re.compile("[^a-æøåA-ÆØÅ0-9- \n]", re.DOTALL)
        
        with open(self.tekst) as file:
            data = file.read()
            
        data = regex_match.sub("", data)
        normal = data.lower()

        print(normal)

    def til_avsnitt(self, avsnittskille="\n\n"):
        "Deler self.tekst opp i en liste av avsnitt som lagres i self.avsnitt ."
        with open(self.tekst) as file:
            data = file.read()

        avsnitt = data.split(avsnittskille)
        print(avsnitt)
        ord_liste = self.lag_ordliste(avsnitt)
        print(ord_liste)
        

    def lag_ordliste(self, avsnittekst):
        "Lager en liste av ord som forekommer i avsnittet."
        avsnitt_list = []
        for item in avsnittekst:
            words = item.split()
            avsnitt_list.append(words)
        return avsnitt_list
        
        

    # def tell_ordforekomster(self, ordliste, avsnittekst):
    #     "Lager en liste over antall forekomster av ordene i ordliste i avsnittet."
    #     pass  

filnavn = "eksempeltekst.txt"
eksempeltekst = open(filnavn).read()
tekstanalyse = Tekstanalyse()
tekstanalyse.normaliser_tekst()
tekstanalyse.til_avsnitt()
    # def analyser_tekst(self):
    #     "Lager en ordliste og teller ordforekomster for hvert avsnitt i teksten."

    #     ordlister = []
    #     ordtellinger = []

    #     for avsnittekst in self.avsnittliste:
    #         ordliste = self.lag_ordliste(avsnittekst)
    #         ordtelling = self.tell_ordforekomster(ordliste, avsnittekst)
    #         ordlister.append(ordliste)
    #         ordtellinger.append(ordtelling)

    #     self.ordlister = ordlister
    #     self.ordtellinger = ordtellinger

    # def skriv_ut(self):
    #     "Skriver ut analyseresultatene for hvert avsnitt på skjermen."
    #     pass 

    # def lagre_til_fil(self, filnavn):
    #     "Lagrer analyseresultatene for hvert avsnitt i en fil."
    #     pass

# testkjøring
# tekstanalyse.analyser_tekst()
# tekstanalyse.skriv_ut()