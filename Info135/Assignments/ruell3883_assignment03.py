# Assignment 3
#------- Question 1 -------#
def hash_function1(key):
    m = 13
    print(key % m)

hash_function1(27) # Output 1
hash_function1(130) # Output 0

# Answer is b) 1, 0

#------- Question 2 -------#
def load_factor():
    keys = [11, 12, 14, 17, 18, 19, 20, 21, 25]
    num_slots = 11
    num_entries = len(keys)

    print(num_entries / num_slots)

load_factor() # Output 0.818

# Answer Q1: The load factor is 0.818

def hash_function2(key):
    m = 11
    print(key % m)

hash_function2(11) # Output 0
hash_function2(12) # Output 1
hash_function2(14) # Output 3
hash_function2(17) # Output 6
hash_function2(18) # Output 7
hash_function2(19) # Output 8
hash_function2(20) # Output 9
hash_function2(21) # Output 10
hash_function2(25) # Output 3 - Linear probing puts this at index 4

# Answer Q2 is D [11, 12, •, 14, 25, •, 17, 18, 19, 20, 21]
#                [ 0   1  2   3   4  5   6   7   8   9  10]

#------- Question 3 -------#

import hashlib as hl
import random

class HashClass:

    def __init__(self, id_num):
        self.id_num = id_num

    def hash_it(self):
        salt = random.randint(1, 1000)
        combine = str(salt + self.id_num)
        hash_id = hl.sha1(combine.encode()).hexdigest()
        return hash_id

    def print_it(self):
        print(self.hash_it())

my_hash = HashClass(11011999)
my_hash.print_it() # Output 59816215872da89c03ec50bb21bfb80c22053482 (Random each time)

#------- Question 4 -------#

def most_frequent_integer(list):
    dictionary = {}
    for num in list:
        if num not in dictionary:
            dictionary[num] = 0
        dictionary[num] += 1

    most_frequent_int = max(dictionary, key=dictionary.get)
    return most_frequent_int

my_list = [10, 2, 5, 2, 0, 5, 6, 8, 5, 10]
result = most_frequent_integer(my_list)
print(result) # Output 5