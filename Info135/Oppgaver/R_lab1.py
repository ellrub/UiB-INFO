# Classes
# Oppgave 1

class Person:
    def __init__(self, name):
        self.name = name

    def greets(self, person):
        print(f'{self.name}: "Hello, {person.name}!"')

alice = Person('Alice')
bob = Person('Bob')
alice.greets(bob)


# Oppgave 2

class Employee:
    def __init__(self, firstname, lastname, salary = 10000):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def get_fullname(self):
        return f'{self.firstname} {self.lastname}'

    def print_email(self):
        print(f'{self.firstname.lower()}.{self.lastname.lower()}@company.com')

    def increase_salary(self, rate):
        return self.salary * rate
    
ruben = Employee('Ruben', 'Ellefsen')

print(ruben.get_fullname())
ruben.print_email()
print(ruben.increase_salary(2))

# Binary Search
# Oppgave 1
# a)
# 1, 3 and 5

# b)

# Oppgave 2
# a), b) and c)
import math
def binary_search_big_o(my_list):
    return math.ceil(math.log(len(my_list), 2))

def simple_search_big_o(my_list):
    return len(my_list)

my_list = [x for x in range(964)]
print('Simple search big O:', simple_search_big_o(my_list))
print('Binary search big 0:', binary_search_big_o(my_list))

