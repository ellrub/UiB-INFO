class Student():
    def __init__(self, user_name, e_mail):
        self.user_name = user_name
        self.e_mail = e_mail
        
    def output(self):
        print(f"Navn: {self.user_name}, epost: {self.e_mail}")

    def new_evaluation(self, code, evaluation, score):
        print(f"Vurderinger\n{self.user_name}, {code}\t{evaluation}, skår={score}")

        

class Emne():
    def __init__(self, code, title):
        self.code = code
        self.title = title

    def topic_code(self):
        return self.code

    def output(self):
        print(f"Emne: {self.code}: {self.title}")

    
# class Review():
#     def __init__(self):
#         pass
    

alina = Student("Alina Farschian", "afa754@student.uib.no")
alina.output()

info132 = Emne("INFO132", "Innføring i programmering")
info132.output()

alina.new_evaluation(info132, "Kjempebra emne! Jeg tar det om igjen neste høst!", 5)
alina.output()
# info132.output()

# olea = Student("Olea Haldorsen", "oha356@student.uib.no")
# olea.output()

# olea.new_evaluation(info132, "Sånn passe. DATA110 om våren dekker omtrent det samme.", 3)
# olea.output()
# info132.output()