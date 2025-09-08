class Student:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.assessments = []

    def add_assessment(self, subject, assessment_text, score):
        assessment = Assessment(assessment_text, score, subject, self)
        self.assessments.append(assessment)
        subject.add_assessment(assessment)

    def print_out(self):
        print(f"Navn: {self.username}, epost: {self.email}")
        if self.assessments:
            print("Vurderinger:")
        for assessment in self.assessments:
            assessment.print_out()
        print()

class Subject:
    def __init__(self, code, title):
        self.code = code
        self.title = title
        self.assessments = []
        self.avarage_score = 0

    def add_assessment(self, assessment):
        self.assessments.append(assessment)
        self.calculate_avarage_score()

    def calculate_avarage_score(self):
        total_score = sum(assessment.score for assessment in self.assessments)
        self.avarage_score = total_score / len(self.assessments)

    def print_out(self):
        print(f"Emne {self.code}: {self.title}")
        if self.assessments:
            print("Vurderinger:")
            for assessment in self.assessments:
                assessment.print_out()
            print(f"Gjennomsnittlig vurdering: {self.avarage_score}")
        print()

class Assessment:
    def __init__(self, assessment_text, score, subject, student):
        self.assessment_text = assessment_text
        self.score = score
        self.subject = subject
        self.student = student

    def print_out(self):
        print(f"{self.student.username}, {self.subject.code}:\t {self.assessment_text}, skår: {self.score}")


alina = Student("Alina Farschian", "afa754@student.uib.no")
alina.print_out()

info132 = Subject("INFO132", "Innføring i programmering")
info132.print_out()

alina.add_assessment(info132, "Kjempebra emne! Jeg tar det om igjen neste høst!", 5)
alina.print_out()
info132.print_out()

olea = Student("Olea Haldorsen", "oha356@student.uib.no")
olea.print_out()

olea.add_assessment(info132, "Sånn passe. DATA110 om våren dekker omtrent det samme.", 3)
olea.print_out()
info132.print_out()