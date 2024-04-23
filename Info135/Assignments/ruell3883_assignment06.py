# Assignment 6
# ---------- Question 1 ---------- #
# The right order is A B D G H E I C F J, which means that a) is the right answer.

# -------------------------------- #

# ---------- Question 2 ---------- #
class Quizgift:
    def __init__(self, points, time, time_limit):
        self.points = points
        self.time = time
        self.time_limit = time_limit
        self.grid = [[0 for _ in range(time_limit + 1)] for _ in range(len(points) + 1)]
        self.items = []
    
    def compute_result(self):
        for i in range(1, len(self.points) + 1):
            for t in range(1, self.time_limit + 1):
                if self.time[i - 1] <= t:
                    self.grid[i][t] = max(self.points[i - 1] +
                                     self.grid[i - 1][t - self.time[i - 1]],
                                     self.grid[i - 1][t])
                else:
                    self.grid[i][t] = self.grid[i - 1][t]

        t = self.time_limit
        n = len(self.points)
        for i in range(n, 0, -1):
            if self.grid[i][t] != self.grid[i - 1][t]:
                self.items.append(self.points[i - 1])
                t -= self.points[i - 1]

        return self.grid[n][self.time_limit], self.items
        

    def print_result(self):
        total_points, _ = self. compute_result()
        gift = 'watch' if total_points <= 250 else 'smartphone' if total_points <= 750 else 'laptop'
        print(f'Total points: {total_points}\nGift: {gift}')

points = [120, 200, 150, 350, 100, 90]
time = [15, 20, 40, 50, 20, 10]
time_limit = 100

quiz_gift = Quizgift(points, time, time_limit)
quiz_gift.print_result()

# -------------------------------- #

# ---------- Question 3 ---------- #
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def compute_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def compute_area(self):
        area = self.side * self.side
        print(area)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        area = math.pi * self.radius * self.radius
        print(round(area, 2))

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def compute_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        print(area)

my_square = Square(2)
my_circle = Circle(2) 
my_triangle = Triangle(5, 4, 3)

print('Area of square:', end=' ') 
my_square.compute_area() 
print('Area of circle:', end=' ') 
my_circle.compute_area() 
print('Area of triangle:', end=' ') 
my_triangle.compute_area()

# -------------------------------- #

# ---------- Question 4 ---------- #
class House:
    count = 0

    def __init__(self, owner, condition, price):
        self.owner = owner
        self.condition = condition
        self.price = price
        self.cost = 0
        self.sold = False
        House.count += 1

    def sell(self, new_owner):
        self.owner = new_owner
        self.sold = True
        profit = self.price - self.cost
        print(f'House sold! Profit: {profit}')

    def change_price(self, new_price):
        if self.sold:
            print('House has been sold!')
        else:
            self.price = new_price

    def renovate(self, expense, new_condition):
        self.cost += expense
        self.condition = new_condition
        print('House renovated!')

    def print_info(self):
        print(f'Owner: {self.owner}, Condition: {self.condition}, Price: {self.price} [$]')

house1 = House('John', 'Good', 100000)
house2 = House('Sara', 'Bad', 250000)
house1.print_info()
house2.print_info()

house1.renovate(50000, 'Great')
house1.sell('Leo')
house1.print_info()

print(f'Total number of houses: {House.count}')

# -------------------------------- #