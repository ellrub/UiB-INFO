# Question 1
# c)

# Question 2
# a) Matrix 1

# Question 3
# d) Python Tuples are mutable (They are imutable)

# Question 4
# b) O(n^2)

# Question 5
# O(n^3)

# Question 6
# c) [50, 40, 30, 20]

# Question 7
# c)

# Question 8
# e)

# Question 9
# Diagram 3

# Question 10
# e) - Correct order is 2, 1, 5, 4, 3

# Question 11
def fact_func2(n):
    memo = [0] * (n + 1)
    memo[1], memo[0] = 1, 1

    for i in range(2, n + 1):
        memo[i] = i * memo[i - 1]
    return memo[n]

for n in range(1, 6):
     print(fact_func2(n))

# Question 12
# O(n log n)

# Question 13
# c) @abstractmethod

# Question 14
# a) self.next = None

# Question 15
# d)

# Question 16
import random as rand

class HashTable:
    def __init__(self, capacity, prime):
        self.__capacity = capacity
        self.__table = [None] * capacity
        self.__prime = prime
        self.__scale = rand.randint(1, 1000)

    def hash_function(self, key):
        return (key * self.__scale)\
            % self.__prime \
            % self.__capacity
    
# Question 17
# c) O(n^3)

from multiprocessing import Process

def my_function():
    pass

my_process = Process(target = my_function)

if __name__ == "__main__":
    my_process.start()
    my_process.join()